#!/usr/bin/env python3
"""flare2md — MadCap Flare (XHTML) -> Markdown conversion engine.

Per topic the pipeline is:

  1. Parse the Flare XHTML (MadCap namespace), tolerant of legacy entities.
  2. Inline <MadCap:snippetBlock/snippetText> recursively.
  3. Drop content excluded by the build target's condition expression.
  4. Resolve <MadCap:variable> against target overrides, then variable sets.
  5. Rewrite Flare's presentational idioms into semantic markup:
       div.note / autonum "Note:"      -> Material admonition
       p.Bullet + autonum "*"          -> real <ul> list
       ol MadCap:continue              -> <ol start="n">
       span.Code                       -> <code>
       span.UI / .uicontrol            -> <strong>
       table.TableStyle-Figure         -> plain figure + italic caption
  6. Convert xrefs/unresolvedLinks to anchors; strip index keywords and any
     residual MadCap attributes.
  7. Hand the cleaned <body> to pandoc -> GitHub-Flavored Markdown, with
     admonition bodies converted in the same pandoc call and re-inserted as
     `!!! note` blocks (Material admonitions carry markdown, raw HTML doesn't).
  8. Rewrite image srcs into the guide's assets/ dir and .htm links -> .md.
  9. Prepend YAML front matter (title + description).

Editorial cleanup (legacy TIBCO branding, figure numbering) is out of scope and
reported instead of guessed at.
"""
from __future__ import annotations

import html
import re
import shutil
import subprocess
from datetime import date
from pathlib import Path
from urllib.parse import quote, unquote

from lxml import etree

MC_NS = "http://www.madcapsoftware.com/Schemas/MadCap.xsd"
MC = "{%s}" % MC_NS

TOPIC_SUFFIXES = (".htm", ".html")

# Fallback condition tokens for projects whose target carries no expression.
#
# ExcludeFromHelp is deliberately not here. It means "leave this out of the
# in-product Help", not "do not publish": of the HTML5 targets in these sources
# 22 include it and only 17 exclude it, and treating it as unpublishable hid
# pages the portal shows (the Domains guide's introduction). Guides whose target
# really does exclude it are covered by `target.exclude`.
DROP_CONDITION_TOKENS = (
    "donotpublish",
    "excludefrombuilds",
    "donotimport",
    "printonly",
    "draft",
    "deprecated",
    "deleted",
    "hidden",
    "confidential",
    "comment",
    "community",
)

# Flare variable definitions that are placeholders in the shared project; they
# are only meaningful once a target overrides them.
PLACEHOLDER_VALUES = {
    "product-name®",
    "productVersion-variable",
    "productID-variable",
    "release-date",
    "xxxx-yyyy",
    "yyyy",
    "book-name",
}

# autonum label -> Material admonition type
ADMONITION_TYPES = {
    # autonum labels (colon already stripped) and Flare note classes
    "note": "note",
    "notes": "note",
    "tip": "tip",
    "tips": "tip",
    "notetip": "tip",
    "important": "info",
    "noteimportant": "info",
    "warning": "warning",
    "notewarning": "warning",
    "caution": "warning",
    "notecaution": "warning",
    "danger": "danger",
    "example": "example",
    "best practice": "tip",
    "restriction": "warning",
    "noterestriction": "warning",
    "before you begin": "info",
}

# Titles that are not the admonition type itself and should be shown as given.
ADMONITION_TITLES = {
    "important": "Important",
    "noteimportant": "Important",
    "caution": "Caution",
    "notecaution": "Caution",
    "restriction": "Restriction",
    "noterestriction": "Restriction",
    "before you begin": "Before you begin",
}

SPLIT_TOKEN = "@@FLARE2MD-SPLIT@@"
ADM_TOKEN = "@@FLARE2MD-ADM-%d@@"
# `[ \t]*`, not `\s*`: `\s` would swallow the preceding blank lines and make
# the captured indent look like a nested block.
ADM_TOKEN_RE = re.compile(r"^([ \t]*)@@FLARE2MD-ADM-(\d+)@@[ \t]*$", re.M)


# --------------------------------------------------------------------------- #
# Parsing
# --------------------------------------------------------------------------- #
def parse_flare(path: Path, warn=None) -> etree._Element:
    """Parse a Flare .htm/.flsnp/.fltoc file, tolerant of named entities."""
    data = path.read_bytes()
    if data.startswith(b"\xef\xbb\xbf"):
        data = data[3:]
    parser = etree.XMLParser(recover=True, resolve_entities=False, huge_tree=True)
    try:
        return etree.fromstring(data, parser=parser)
    except etree.XMLSyntaxError as exc:
        if warn:
            warn("parse error %s: %s" % (path, exc))
        text = data.decode("utf-8", "replace")
        text = re.sub(r"&(?!amp;|lt;|gt;|quot;|apos;|#)", "&amp;", text)
        return etree.fromstring(text.encode("utf-8"), parser=parser)


def body_of(root: etree._Element) -> etree._Element:
    for tag in ("body", "{http://www.w3.org/1999/xhtml}body"):
        b = root.find(tag)
        if b is not None:
            return b
    return root


# --------------------------------------------------------------------------- #
# Build target: variables + conditions
# --------------------------------------------------------------------------- #
class Target:
    """The subset of a Flare .fltar that changes rendered output."""

    def __init__(self, overrides=None, include=None, exclude=None, toc=None):
        self.overrides = overrides or {}
        self.include = include or set()
        self.exclude = exclude or set()
        self.toc = toc


def _parse_condition_expression(expr: str):
    """'include[A or B], exclude[C or D]' -> ({A,B}, {C,D}), lowercased."""
    include, exclude = set(), set()
    for kind, body in re.findall(r"(include|exclude)\[([^\]]*)\]", expr or ""):
        tokens = {t.strip().lower() for t in re.split(r"\bor\b", body) if t.strip()}
        (include if kind == "include" else exclude).update(tokens)
    return include, exclude


def load_target(path: Path, warn=None) -> Target:
    root = parse_flare(path, warn)
    overrides = {}
    for var in root.iter("Variable"):
        name = (var.get("Name") or "").strip()
        if not name:
            continue
        value = (var.text or "").strip()
        # "set/name" in targets, "set.name" in topics.
        overrides[name.replace("/", ".")] = value
    include, exclude = _parse_condition_expression(
        root.get("ConditionTagExpression") or ""
    )
    return Target(overrides, include, exclude, root.get("MasterToc"))


def synthetic_target(guide_condition: str, all_guide_conditions, warn=None) -> Target:
    """Condition set for guides whose project ships no dedicated HTML target.

    Mirrors what the real HTML targets do: publish the commercial (Pro) screen
    variant of this guide, and exclude every sibling guide's content marker.
    """
    prefix = "jasperguideconditions-forhtml."
    include = {
        "default.screenonly",
        "globalconditions.ctxjavascript",
        "jasperconditions.pro",
        prefix + guide_condition.lower(),
    }
    exclude = {
        "default.printonly",
        "globalconditions.autominitoc",
        "globalconditions.confidential",
        "globalconditions.donotimport",
        "globalconditions.draftwatermark",
        "globalconditions.excludefrombuilds",
        "globalconditions.hiddentext",
        "jasperconditions.community",
        "jasperconditions.donotpublish",
    }
    for token in all_guide_conditions:
        if token.lower() != guide_condition.lower():
            exclude.add(prefix + token.lower())
    return Target({}, include, exclude, None)


def load_variables(project_dirs, warn=None) -> dict:
    """{'set.name': value, 'name': value} from every .flvar in the projects.

    Earlier projects win, and obvious placeholder definitions are skipped so a
    target override or a real project-level value is used instead.
    """
    variables = {}
    for proj in project_dirs:
        vs_dir = proj / "Project" / "VariableSets"
        if not vs_dir.is_dir():
            continue
        for flvar in sorted(vs_dir.glob("*.flvar")):
            setname = flvar.stem
            root = parse_flare(flvar, warn)
            for var in root.iter("Variable"):
                name = var.get("Name")
                if not name:
                    continue
                value = var.get("EvaluatedDefinition")
                if value is None:
                    value = "".join(var.itertext())
                value = (value or "").strip()
                if var.get("Type") == "DateTime":
                    # Flare stores a format string and evaluates it at build
                    # time (CopyrightYear is literally "yyyy").
                    value = _format_datetime(value)
                if not value or value in PLACEHOLDER_VALUES:
                    continue
                for key in ("%s.%s" % (setname, name), name):
                    variables.setdefault(key, value)
    return variables


DATETIME_TOKENS = (
    ("yyyy", "%Y"),
    ("MMMM", "%B"),
    ("MMM", "%b"),
    ("MM", "%m"),
    ("dd", "%d"),
)


def _format_datetime(spec: str) -> str:
    """Render a Flare DateTime variable's format string for the build date."""
    if not spec or "yyyy" not in spec and "MM" not in spec and "dd" not in spec:
        return spec
    today = date.today()
    out = spec
    for token, directive in DATETIME_TOKENS:
        if token in out:
            out = out.replace(token, today.strftime(directive))
    return out


# --------------------------------------------------------------------------- #
# Tree transforms
# --------------------------------------------------------------------------- #
def inline_snippets(elem, base_dir: Path, warn, depth: int = 0, fallbacks=()) -> None:
    if depth > 12:
        warn("snippet recursion too deep under %s" % base_dir)
        return
    for node in list(elem.iter("%ssnippetBlock" % MC, "%ssnippetText" % MC)):
        src = node.get("src")
        parent = node.getparent()
        if parent is None:
            continue
        if not src:
            parent.remove(node)
            continue
        snippet_path = (base_dir / unquote(src).replace("\\", "/")).resolve()
        if not snippet_path.is_file():
            # Some projects reference the shared snippet library by a path that
            # only exists in the shared project; look there before giving up.
            for root in fallbacks:
                candidate = root / snippet_path.name
                if candidate.is_file():
                    snippet_path = candidate
                    warn("snippet taken from shared project: %s" % src)
                    break
        if not snippet_path.is_file():
            warn("missing snippet: %s (from %s)" % (src, base_dir))
            _drop_keeping_tail(node)
            continue
        sbody = body_of(parse_flare(snippet_path, warn))
        inline_snippets(sbody, snippet_path.parent, warn, depth + 1, fallbacks)
        idx = list(parent).index(node)
        children = list(sbody)
        for child in reversed(children):
            parent.insert(idx, child)
        if node.tail:
            if children:
                children[-1].tail = (children[-1].tail or "") + node.tail
            elif idx > 0:
                prev = parent[idx - 1]
                prev.tail = (prev.tail or "") + node.tail
            else:
                parent.text = (parent.text or "") + node.tail
        parent.remove(node)


def condition_excluded(value: str, target: Target) -> bool:
    """Whether a `conditions` value hides its element from this target.

    Flare reads the comma-separated list as the set of tags on the element, and
    exclusion wins: one excluded tag hides the element whatever else it carries.

    Used for topic content, for TOC entries (whose attribute has no MadCap
    prefix) and for deciding which links to follow, so all three agree on what
    the target publishes.
    """
    for tok in (t.strip().lower() for t in (value or "").split(",")):
        if not tok:
            continue
        if tok in target.exclude:
            return True
        if tok in target.include:
            continue
        if any(bad in tok for bad in DROP_CONDITION_TOKENS):
            # Unknown to this target, but unpublishable by convention.
            return True
    return False


def apply_conditions(elem, target: Target) -> None:
    """Drop elements excluded by the target's condition expression."""
    for node in list(elem.iter()):
        cond = node.get("%sconditions" % MC)
        if cond and condition_excluded(cond, target) and node.getparent() is not None:
            _drop_keeping_tail(node)


def resolve_variables(elem, variables: dict, overrides: dict, warn) -> None:
    for node in list(elem.iter("%svariable" % MC)):
        name = node.get("name", "")
        value = _lookup_variable(name, variables, overrides)
        if value is None:
            warn("unresolved variable: %s" % name)
            value = ""
        _replace_with_text(node, value)


# A few topics reference variables that no project defines. Where an obvious
# equivalent exists, use it rather than rendering an empty gap in a sentence.
VARIABLE_ALIASES = {
    "productnameforreleasenote": "productName",
    "softwareversion": "productVersion",
}


def _lookup_variable(name, variables, overrides):
    keys = [name]
    if "." in name:
        keys.append(name.split(".", 1)[1])
    keys.append(name.split(".")[-1])
    for key in keys:
        if key in overrides and overrides[key]:
            return overrides[key]
    for key in keys:
        if key in variables:
            return variables[key]
    alias = VARIABLE_ALIASES.get(name.split(".")[-1].lower())
    if alias:
        return _lookup_variable(alias, variables, overrides)
    return None


VAR_SYNTAX_RE = re.compile(r"\[%=\s*([A-Za-z0-9_.\-]+)\s*%\]")


def resolve_variable_syntax(elem, variables, overrides, warn) -> None:
    """Resolve `[%=set.var%]` written inline, including inside attributes.

    Flare only expands the `<MadCap:variable>` element in body text; the same
    variables appear in raw `[%=...%]` form in href/src attributes and in some
    hand-edited topics, where they would otherwise leak into the output.
    """
    def sub(value):
        def repl(match):
            name = match.group(1)
            if name.lower().startswith("system."):
                return ""
            resolved = _lookup_variable(name, variables, overrides)
            if resolved is None:
                warn("unresolved inline variable: %s" % name)
                return ""
            return resolved
        return VAR_SYNTAX_RE.sub(repl, value)

    for node in elem.iter():
        if not isinstance(node.tag, str):
            continue
        if node.text and "[%=" in node.text:
            node.text = sub(node.text)
        if node.tail and "[%=" in node.tail:
            node.tail = sub(node.tail)
        for key, value in list(node.attrib.items()):
            if "[%=" in value:
                node.set(key, sub(value))


def apply_brand(elem, replacements) -> None:
    """Rename the owning company in visible text.

    Text only — never attributes. A URL like `www.cloud.com/legal` still points
    at the previous owner's site and rewriting it would break the link, so
    those are reported rather than guessed at.
    """
    if not replacements:
        return
    for node in elem.iter():
        if not isinstance(node.tag, str):
            continue
        for attr in ("text", "tail"):
            value = getattr(node, attr)
            if not value:
                continue
            for old, new in replacements.items():
                if old in value:
                    value = value.replace(old, new)
            setattr(node, attr, value)


def drop_draft_content(elem) -> None:
    """Remove reviewer scaffolding: draft comments and <draft> autonum blocks."""
    for node in list(elem.iter()):
        if not isinstance(node.tag, str):
            continue
        cls = (node.get("class") or "").split()
        autonum = (node.get("%sautonum" % MC) or "").lower()
        if ("draft-comment" in cls or "self-note" in cls
                or "draft" in autonum or "self note" in autonum
                or "&lt;draft&gt;" in autonum):
            if node.getparent() is not None:
                node.getparent().remove(node)


# ---- admonitions ---------------------------------------------------------- #
def _autonum_label(raw: str) -> str:
    text = html.unescape(raw or "")
    text = re.sub(r"<[^>]+>", "", text)
    return text.replace(" ", " ").strip()


def admonition_type(node) -> str | None:
    """Material admonition type for a Flare note/warning block, else None."""
    classes = {c.lower() for c in (node.get("class") or "").split()}
    label = _autonum_label(node.get("%sautonum" % MC)).rstrip(":").strip().lower()
    if label in ADMONITION_TYPES:
        return ADMONITION_TYPES[label]
    for cls in classes:
        if cls in ADMONITION_TYPES:
            return ADMONITION_TYPES[cls]
    return None


BULLET_CLASS_RE = re.compile(r"^(bullet|cell_bullet)(_(\d+))?$")
NUMBER_CLASS_RE = re.compile(
    r"^(numbered|step)(_?first|_alpha|_alpha_?first|_\d+)?$", re.I
)


def _list_level(node, pattern):
    """(level, is_first) for a Flare pseudo-list paragraph, else None.

    Flare encodes list depth in the class name (Bullet, Bullet_2, Bullet_3) and
    restarts numbering with a *_First class rather than with real list markup.
    The `_alpha` variants are the lettered sub-steps of the step above them, so
    they belong one level down — treating them as top-level would break the
    outer sequence in two.
    """
    for cls in (node.get("class") or "").split():
        match = pattern.match(cls.lower())
        if not match:
            continue
        suffix = (match.group(2) or "").lower()
        level = 1
        if suffix and suffix[1:].isdigit():
            level = int(suffix[1:])
        elif "alpha" in suffix:
            level = 2
        return level, suffix.endswith("first")
    return None


def bulletize(elem) -> None:
    """Turn runs of `<p class="Bullet[_n]">` into real <ul> lists.

    The bullet glyph comes either from an autonum attribute or from the
    stylesheet, so a Bullet paragraph with no autonum is still a list item —
    several hundred of them are written that way.
    """
    def is_bullet(node):
        autonum = node.get("%sautonum" % MC)
        return autonum is None or "•" in _autonum_label(autonum)

    _listify(elem, BULLET_CLASS_RE, "ul", is_bullet)


LITERAL_BULLET_RE = re.compile(r"^\s*[•▪‣◦]\s*")


def literal_bullets(elem) -> None:
    """Paragraphs that start with a typed-in bullet character.

    A few topics were hand-authored with the bullet in the text rather than as
    a list or an autonum, so they arrive as ordinary paragraphs.
    """
    def is_bullet(node):
        return bool(node.text and LITERAL_BULLET_RE.match(node.text))

    for parent in list(elem.iter()):
        if not isinstance(parent.tag, str) or parent.tag in ("ul", "ol"):
            continue
        run = []
        for child in list(parent):
            if child.tag == "p" and not child.get("class") and is_bullet(child):
                child.text = LITERAL_BULLET_RE.sub("", child.text)
                run.append((child, 1))
                continue
            if run:
                _wrap_run_in_list(parent, run, "ul")
            run = []
        if run:
            _wrap_run_in_list(parent, run, "ul")


def numberize(elem) -> None:
    """Turn runs of `<p class="Numbered[_First]" autonum="1.">` into <ol> lists.

    Flare numbers these paragraphs itself, so left alone they render as body
    text starting with a literal "1." that no longer renumbers.
    """
    def is_numbered(node):
        autonum = node.get("%sautonum" % MC)
        if autonum is None:
            return True  # numbering supplied by the stylesheet
        label = _autonum_label(autonum)
        return bool(re.match(r"^([0-9]+|[a-z])[.)]?$", label.strip()))

    _listify(elem, NUMBER_CLASS_RE, "ol", is_numbered)


def _listify(elem, class_re, list_tag, matches, passes: int = 3) -> None:
    # Flare nests pseudo-list paragraphs inside one another (`<p class="Bullet">`
    # containing more of the same). Each pass turns one level into a real list
    # and exposes the next level as children of the new <li>.
    for _ in range(passes):
        _listify_once(elem, class_re, list_tag, matches)


def _listify_once(elem, class_re, list_tag, matches) -> None:
    """Turn one parent's pseudo-list paragraphs into real nested lists.

    A Flare pseudo-list is a *stream*: paragraphs carrying a level in their
    class name, with the figures, tables and code samples that belong to a step
    sitting between it and the next one. So the stream is walked in order and
    interrupting content is held back — if the stream resumes, that content
    belongs to the item it followed and moves inside it, at whatever depth that
    item was; if the stream has ended, it stays where it is.

    Doing it in one walk is what keeps a sub-step a sub-step: promoting the
    resumed items to the top level (which building a fresh list per run does)
    renumbered lettered sub-steps as main steps.
    """
    for parent in list(elem.iter()):
        if not isinstance(parent.tag, str) or parent.tag in ("ul", "ol"):
            continue

        root = None       # the list being built
        stack = []        # [(level, list element)] for the open nesting
        last_item = None  # where held-back content goes
        pending = []      # interrupting nodes since the last item

        for child in list(parent):
            info = None
            if child.tag == "p" and matches(child):
                info = _list_level(child, class_re)

            if info is None:
                if root is not None:
                    if (isinstance(child.tag, str)
                            and (re.fullmatch(r"h[1-6]", child.tag)
                                 or child.tag in ("ol", "ul"))):
                        root, stack, last_item, pending = None, [], None, []
                    else:
                        pending.append(child)
                continue

            level, is_first = info
            if root is None or (is_first and level == 1):
                root = etree.Element(list_tag)
                parent.insert(list(parent).index(child), root)
                stack = [(1, root)]
                last_item, pending = None, []
            elif pending and last_item is not None:
                for node in pending:
                    parent.remove(node)
                    last_item.append(node)
            pending = []

            # A run that begins deeper than the list it joins still hangs off
            # the item above it, so clamp rather than invent parents.
            level = max(1, min(level, stack[-1][0] + 1))
            # Some sequences open on a sub-step, with no step above it to hang
            # from; those sit at the level of the list they start.
            if level > stack[-1][0] and not stack[-1][1].findall("li"):
                level = stack[-1][0]
            while len(stack) > 1 and stack[-1][0] > level:
                stack.pop()
            if level > stack[-1][0]:
                host = stack[-1][1]
                items = host.findall("li")
                anchor = items[-1] if items else etree.SubElement(host, "li")
                stack.append((level, etree.SubElement(anchor, list_tag)))

            item = etree.SubElement(stack[-1][1], "li")
            item.text = child.text
            for kid in list(child):
                item.append(kid)
            parent.remove(child)
            last_item = item


def _wrap_run_in_list(parent, run, list_tag="ul", start=None) -> int:
    """Build a (possibly nested) list from consecutive pseudo-list paragraphs.

    Returns the number of top-level items, so a caller can continue the
    numbering of a sequence that something else interrupted.
    """
    root = etree.Element(list_tag)
    if start and list_tag == "ol":
        root.set("start", str(start))
    idx = list(parent).index(run[0][0])
    # A run that only contains Bullet_2 items has no level-1 parent in the
    # source; shift it up rather than inventing an empty bullet to nest under.
    base = min(level for _node, level in run) - 1
    if base:
        run = [(node, level - base) for node, level in run]
    stack = [(1, root)]
    for node, level in run:
        while len(stack) > 1 and stack[-1][0] > level:
            stack.pop()
        if level > stack[-1][0]:
            host = stack[-1][1]
            items = host.findall("li")
            anchor = items[-1] if items else etree.SubElement(host, "li")
            nested = etree.SubElement(anchor, list_tag)
            stack.append((level, nested))
        li = etree.SubElement(stack[-1][1], "li")
        li.text = node.text
        for kid in list(node):
            li.append(kid)
        parent.remove(node)
    parent.insert(idx, root)
    return len(root.findall("li"))


BLOCK_TAGS = frozenset({
    "p", "div", "table", "ul", "ol", "pre", "blockquote",
    "h1", "h2", "h3", "h4", "h5", "h6",
})


def _paragraphize(li) -> None:
    """Wrap a list item's inline content in a <p>.

    A block appended to an item whose text is bare produces a tight list item,
    and pandoc then writes the block on the line straight after the text — where
    a table is read as more sentence, not as a table. Wrapping the text first
    makes the item loose, so the block keeps its own blank line.
    """
    inline = []
    for child in list(li):
        if child.tag in BLOCK_TAGS:
            break
        inline.append(child)
    if not (li.text and li.text.strip()) and not inline:
        return
    para = etree.Element("p")
    para.text = li.text
    li.text = None
    for child in inline:
        li.remove(child)
        para.append(child)
    li.insert(0, para)


def absorb_orphan_sublists(elem) -> None:
    """Fold an item that holds nothing but a sub-list into the item before it.

    Flare's lettered sub-steps continue after a code sample or a table, and the
    resumed run has no step of its own to hang from — which renders as a bare
    "2." whose only content is "1. …". The sub-steps belong to the step that
    introduced them.
    """
    for parent in list(elem.iter("ol")):
        items = parent.findall("li")
        for position, li in enumerate(items):
            if position == 0 or li.text and li.text.strip():
                continue
            children = [c for c in li if isinstance(c.tag, str)]
            if len(children) != 1 or children[0].tag not in ("ol", "ul"):
                continue
            sublist = children[0]
            previous = items[position - 1]
            host = None
            for candidate in previous:
                if candidate.tag == sublist.tag:
                    host = candidate
            if host is None:
                previous.append(sublist)
            else:
                for item in list(sublist):
                    host.append(item)
            if li.getparent() is not None:
                parent.remove(li)


def loosen_list_items(elem) -> None:
    """Give every list item that holds a block its own paragraph first.

    Flare puts tables, code and sub-lists straight after the step text inside
    the same <li>. pandoc then writes a tight item, with the block on the line
    after the text and no blank line between them — and a pipe table read as a
    continuation of that sentence renders as literal `| … |` text. Wrapping the
    text makes the item loose, which keeps the block a block.
    """
    for li in elem.iter("li"):
        if any(isinstance(c.tag, str) and c.tag in BLOCK_TAGS for c in li):
            _paragraphize(li)


def merge_interrupted_lists(elem) -> None:
    """Rejoin a numbered sequence that content in the middle split in two.

    Flare writes steps as paragraphs numbered by a CSS counter, so a table or a
    figure belonging to one step sits between it and the next — and the counter
    keeps going. `start="n"` cannot express that here, because Python-Markdown
    ignores a list's starting number and always renders 1, 2, 3. So the split is
    healed instead: the interrupting nodes move inside the step they belong to
    and the two lists become one, which is both what the source shows and what
    markdown can represent.
    """
    for parent in list(elem.iter()):
        if not isinstance(parent.tag, str):
            continue
        children = list(parent)
        index = 0
        while index < len(children):
            first = children[index]
            if first.tag not in ("ol", "ul"):
                index += 1
                continue
            # Collect what follows, up to a continuation of the same list type.
            between, cursor = [], index + 1
            while cursor < len(children) and children[cursor].tag != first.tag:
                between.append(children[cursor])
                cursor += 1
            if cursor >= len(children):
                # No matching list after this one; keep looking from the next
                # child rather than abandoning the rest of this parent.
                index += 1
                continue
            second = children[cursor]
            continues = second.get("start") or (
                (second.get("%scontinue" % MC) or "").lower() == "true"
            )
            headings = any(
                isinstance(n.tag, str) and re.fullmatch(r"h[1-6]", n.tag)
                for n in between
            )
            items = first.findall("li")
            if not continues or headings or not items:
                # Step forward by one, not to `cursor`: the scan for a matching
                # list can pass over other list pairs — a bulleted list early in
                # the page would otherwise hide every numbered sequence after it.
                index += 1
                continue

            host = items[-1]
            _paragraphize(host)
            for node in between:
                parent.remove(node)
                host.append(node)
            for item in list(second):
                first.append(item)
            second_tail = second.tail
            parent.remove(second)
            first.attrib.pop("start", None)
            if second_tail:
                first.tail = (first.tail or "") + second_tail
            children = list(parent)


def merge_adjacent_lists(elem) -> None:
    """Join sibling lists that the source split for no visible reason.

    Flare topics frequently contain a run of single-item <ul> elements which a
    browser renders as one continuous list. Markdown cannot express two
    touching lists, so pandoc separates them with an HTML comment and the page
    ends up as a stack of one-item lists with gaps between them.

    Ordered lists are only merged when the next one is explicitly marked
    `MadCap:continue`, because otherwise Flare restarts the numbering.
    """
    for parent in list(elem.iter()):
        if not isinstance(parent.tag, str):
            continue
        child = None
        for node in list(parent):
            if child is not None and node.tag == child.tag and node.tag in ("ul", "ol"):
                separated_by_text = bool(child.tail and child.tail.strip())
                continues = (node.get("%scontinue" % MC) or "").lower() == "true"
                if not separated_by_text and (node.tag == "ul" or continues):
                    for item in list(node):
                        child.append(item)
                    child.tail = node.tail
                    parent.remove(node)
                    continue
            child = node if node.tag in ("ul", "ol") else None


def continue_ordered_lists(elem) -> None:
    """`<ol MadCap:continue="true">` restarts at 1 in markdown; set `start`."""
    for parent in list(elem.iter()):
        if not isinstance(parent.tag, str):
            continue
        count = 0
        for child in list(parent):
            if child.tag != "ol":
                continue
            if (child.get("%scontinue" % MC) or "").lower() == "true" and count:
                child.set("start", str(count + 1))
                count += len(child.findall("li"))
            else:
                count = len(child.findall("li"))


def semantic_inlines(elem) -> None:
    """span.Code -> <code>, span.UI/.uicontrol -> <strong>."""
    for node in list(elem.iter("span")):
        classes = {c.lower() for c in (node.get("class") or "").split()}
        if classes & {"code", "codeinline", "userinput", "filepath"}:
            node.tag = "code"
            node.attrib.pop("class", None)
            # <code> must hold text only; flatten any nested markup, turning a
            # <br> into the space it renders as (the source breaks long code
            # spans for layout).
            for br in node.iter("br"):
                br.tail = " " + (br.tail or "")
            text = "".join(node.itertext())
            for kid in list(node):
                node.remove(kid)
            node.text = text
        elif classes & {"ui", "uicontrol", "menucascade", "wintitle"}:
            node.tag = "strong"
            node.attrib.pop("class", None)


LANG_PATTERNS = (
    ("html", re.compile(r"^\s*<(!--|!DOCTYPE|html|head|body|div|script|select|table|p|span|a)\b", re.I)),
    ("xml", re.compile(r"^\s*<(\?xml|[a-zA-Z])")),
    ("json", re.compile(r"^\s*[\[{]\s*[\"\[{]")),
    ("sql", re.compile(r"^\s*(SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP|GRANT)\b", re.I)),
    ("java", re.compile(r"\b(public|private|protected)\s+(class|static|void)\b")),
    ("javascript", re.compile(r"\b(function\s*\(|var\s+\w+\s*=|=>|require\()")),
    ("properties", re.compile(r"^[\w.]+\s*=\s*\S")),
    ("yaml", re.compile(r"^\s*[\w.-]+:\s")),
    ("bash", re.compile(r"^\s*(\$|#|sudo |cd |cp |mv |ls |java |mvn |npm |js-|\./)")),
)


def guess_language(code: str) -> str:
    """Best-effort language for a Flare <pre> block.

    Flare records no language, so this only has to be good enough to enable
    highlighting where it clearly helps and stay out of the way otherwise.
    """
    text = code.strip()
    if not text:
        return "text"
    for lang, pattern in LANG_PATTERNS:
        if pattern.search(text):
            return lang
    return "text"


def fence_code_blocks(elem) -> None:
    """Normalize <pre> into fenced code blocks with a language hint.

    Two reasons not to leave pandoc's indented code blocks alone: fenced blocks
    get the theme's copy button and highlighting, and bracketed text inside an
    indented block is otherwise read as a markdown link reference.
    """
    for pre in list(elem.iter("pre")):
        parent = pre.getparent()
        if parent is None:
            continue
        # Flare often emits one <pre> per line; merge the run back together.
        lines = ["".join(pre.itertext())]
        sibling = pre.getnext()
        while sibling is not None and sibling.tag == "pre" and not (pre.tail or "").strip():
            lines.append("".join(sibling.itertext()))
            nxt = sibling.getnext()
            parent.remove(sibling)
            sibling = nxt if nxt is not None and nxt.tag == "pre" else None
        code_text = "\n".join(line.rstrip() for line in lines).strip("\n")
        for child in list(pre):
            pre.remove(child)
        pre.text = None
        # Drop Flare's styling classes: pandoc reads the first class on <pre>
        # as the code language, so "Indent" would become the language name.
        for attr in list(pre.attrib):
            del pre.attrib[attr]
        code = etree.SubElement(pre, "code")
        code.set("class", "language-%s" % guess_language(code_text))
        code.text = code_text


# Callout icons Flare puts in the first cell of a note table, and the Material
# admonition each one means.
ICON_KINDS = (
    ("warning", "warning"),
    ("caution", "warning"),
    ("important", "info"),
    ("restrict", "warning"),
    ("tip", "tip"),
    ("note", "note"),
    ("pro-only", "info"),
    ("proonly", "info"),
    ("premium", "info"),
)


def _icon_kind(cell):
    """The admonition type implied by the icon in a callout's icon cell."""
    for img in cell.iter("img"):
        name = Path(unquote(img.get("src") or "")).name.lower()
        for token, kind in ICON_KINDS:
            if token in name:
                return kind
    return None


def normalize_tables(elem) -> None:
    """Split Flare's multi-section tables into one table per section.

    The REST API reference builds a single <table> from a run of
    <thead>/<tbody> pairs ("Method | URL", then "Options", then "Return Value
    on Success | Typical Return Values on Failure"), each with its own column
    count expressed through colspans. pandoc reads the column count once, from
    the top of the table, and silently truncates every row that has more cells
    than that — which dropped the whole right-hand column of the later
    sections. Each section becomes its own table, so no row is over-wide.
    """
    for table in list(elem.iter("table")):
        # <col> declares the column count, but Flare's colspans routinely imply
        # more columns than there are <col> elements. pandoc believes the <col>
        # count and truncates every wider row, losing whole columns of
        # reference data, so let it infer the width from the rows instead.
        for col in list(table.findall("col")) + list(table.findall("colgroup")):
            table.remove(col)

        sections = [c for c in table if c.tag in ("thead", "tbody", "tfoot")]
        if len(sections) < 3:
            continue
        groups, current = [], []
        for section in sections:
            rows = section.findall("tr")
            if not rows:
                continue
            if section.tag == "thead" and current:
                groups.append(current)
                current = []
            current.extend(rows)
        if current:
            groups.append(current)
        if len(groups) < 2:
            continue

        parent = table.getparent()
        if parent is None:
            continue
        index = list(parent).index(table)
        new_tables = []
        for rows in groups:
            new_table = etree.Element("table")
            _fill_table(new_table, rows)
            new_tables.append(new_table)
        for new_table in reversed(new_tables):
            parent.insert(index, new_table)
        if table.tail and new_tables:
            new_tables[-1].tail = table.tail
        parent.remove(table)


def _fill_table(table, rows) -> None:
    """Populate a table from a run of rows, with consistent column widths."""
    widest = max(len(row.findall("td")) + len(row.findall("th")) for row in rows)
    head_rows = []
    body_rows = list(rows)
    if body_rows and body_rows[0].find("th") is not None:
        head_rows = [body_rows.pop(0)]
    if head_rows:
        head = etree.SubElement(table, "thead")
        for row in head_rows:
            head.append(_clean_row(row, widest))
    body = etree.SubElement(table, "tbody")
    for row in body_rows:
        body.append(_clean_row(row, widest))


def _clean_row(row, widest):
    """Drop colspans that only existed to span the old table's other sections."""
    cells = row.findall("td") + row.findall("th")
    if len(cells) == widest:
        for cell in cells:
            cell.attrib.pop("colspan", None)
    elif len(cells) == 1 and widest > 1:
        cells[0].set("colspan", str(widest))
    return row


def note_tables_to_admonitions(elem) -> None:
    """Rewrite Flare's note tables as blocks the admonition pass recognizes.

    Flare renders callouts as tables styled with Note.css, in two shapes: a
    single cell, or an icon cell plus a text cell. Left as tables they render as
    a one-row grid with a bitmap "Note" icon in it.
    """
    for table in list(elem.iter("table")):
        cells = _note_table_cells(table)
        if cells is None:
            continue
        # A single-cell table is only a callout if it is styled as one; an
        # icon-plus-text table is one whatever the style is named, and several
        # projects use the generic table style for exactly that. The icon says
        # which kind of callout it is.
        kind = _icon_column_kind(table)
        if kind is None:
            if "Note" not in (table.get("class") or ""):
                continue
            kind = "note"
        div = etree.Element("div")
        div.set("class", kind if kind != "info" else "noteImportant")
        if kind == "note":
            div.set("%sautonum" % MC, "Note: ")
        for cell in cells:
            if cell.text and cell.text.strip():
                para = etree.SubElement(div, "p")
                para.text = cell.text
            for kid in list(cell):
                div.append(kid)
        div.tail = table.tail
        table.getparent().replace(table, div)


def _note_table_cells(table):
    """The content cells of a note table, or None if it is a real table."""
    rows = table.findall(".//tr")
    if not rows:
        return None
    content = []
    for row in rows:
        cells = row.findall("td")
        if len(cells) == 1:
            content.append(cells[0])
        elif len(cells) == 2 and _is_icon_cell(cells[0]):
            content.append(cells[1])
        else:
            return None  # a genuine multi-column table that reuses the style
    return content


def _icon_column_kind(table):
    """Callout type if every row is `icon cell + text cell`, else None."""
    rows = table.findall(".//tr")
    if not rows:
        return None
    kinds = set()
    for row in rows:
        cells = row.findall("td")
        if len(cells) != 2 or not _is_icon_cell(cells[0]):
            return None
        kind = _icon_kind(cells[0])
        if kind is None:
            return None
        kinds.add(kind)
    # Mixed icons in one table: fall back to the most cautious type.
    if "warning" in kinds:
        return "warning"
    return kinds.pop() if len(kinds) == 1 else "note"


def _is_icon_cell(cell) -> bool:
    """True for the narrow cell that only holds Flare's note icon."""
    if "".join(cell.itertext()).strip():
        return False
    return cell.find(".//img") is not None


def unwrap_figure_tables(elem) -> None:
    """Flare wraps figures in single-cell tables; keep the image and caption."""
    for table in list(elem.iter("table")):
        classes = (table.get("class") or "")
        if "Figure" not in classes:
            continue
        rows = table.findall(".//tr")
        cells = table.findall(".//td")
        if rows and any(len(r.findall("td")) > 1 for r in rows):
            continue  # a real multi-column table that merely uses the style
        parent = table.getparent()
        if parent is None:
            continue
        idx = list(parent).index(table)
        moved = []
        for cell in cells:
            if cell.text and cell.text.strip():
                p = etree.Element("p")
                p.text = cell.text
                moved.append(p)
            moved.extend(list(cell))
        for node in reversed(moved):
            parent.insert(idx, node)
        if table.tail:
            if moved:
                moved[-1].tail = (moved[-1].tail or "") + table.tail
            else:
                parent.text = (parent.text or "") + table.tail
        parent.remove(table)


def handle_autonum(elem) -> None:
    """Flatten remaining autonum labels (Figure N:, Table N:) into bold text."""
    for node in list(elem.iter()):
        raw = node.get("%sautonum" % MC)
        if raw is None:
            continue
        label = _autonum_label(raw)
        node.attrib.pop("%sautonum" % MC, None)
        if node.tag in ("ol", "ul") or not label:
            continue
        if label.lower().startswith(("procedure", "chapter")) or label in (":", "•"):
            continue
        if label.lower().startswith(("figure", "table")):
            # Italicise the whole caption, not just the "Figure 1:" label.
            wrapper = etree.Element("em")
            wrapper.text = label.rstrip() + " " + (node.text or "")
            for kid in list(node):
                wrapper.append(kid)
            node.text = None
            node.append(wrapper)
        else:
            strong = etree.Element("strong")
            strong.text = label.rstrip() + " "
            strong.tail = node.text
            node.text = None
            node.insert(0, strong)


def handle_links(elem) -> None:
    for node in list(elem.iter("%sxref" % MC)):
        node.tag = "a"
        _strip_mc_attrs(node)
    for tag in ("%sunresolvedLink" % MC, "%sconditionalText" % MC, "%sannotation" % MC):
        for node in list(elem.iter(tag)):
            node.tag = "span"
            _strip_mc_attrs(node)


FOOTNOTE_CLASS = "jsd-footnote"


def mark_footnotes(elem) -> None:
    """Give each Flare footnote a superscript marker, numbered per page.

    `<MadCap:footnote>` holds only the note text; Flare's HTML output puts a
    superscript number where the element sits and shows the note after it. With
    the element merely unwrapped by `strip_madcap`, the note ran straight into
    the sentence before it — "CompatibleOther commercially supported or
    community OpenJDK-based Java 17..." on the Platform Support guide's JVM
    page, which is how it reached the reviewers.

    Written as inline HTML rather than markdown footnote syntax: 19 of the 20
    footnotes in these sources sit in a table cell, those tables stay raw HTML,
    and Python-Markdown does not read `[^1]` inside an HTML block. The element
    is renamed rather than rebuilt so a link or emphasis inside the note
    survives.
    """
    for index, node in enumerate(list(elem.iter("%sfootnote" % MC)), start=1):
        parent = node.getparent()
        if parent is None:
            continue
        # The number goes in a span wrapping the <sup>, not on the <sup>
        # itself: pandoc's superscript carries no attributes, so a class there
        # is dropped when the surrounding table is written back as raw HTML,
        # while a span keeps its own. The tail space separates the marker from
        # the note even with no stylesheet.
        marker = etree.Element("span")
        marker.set("class", FOOTNOTE_CLASS + "-ref")
        sup = etree.SubElement(marker, "sup")
        sup.text = str(index)
        marker.tail = " "
        parent.insert(parent.index(node), marker)
        # A footnote holding paragraphs cannot be a span: pandoc hoists block
        # content out of one and leaves the span empty, which is how the
        # Application Servers note lost its two system-requirement paragraphs.
        block = any(isinstance(c.tag, str) and c.tag in BLOCK_TAGS for c in node)
        node.tag = "div" if block else "span"
        node.set("class", FOOTNOTE_CLASS)
        if node.text:
            node.text = node.text.lstrip()


def strip_madcap(elem) -> None:
    for node in list(elem.iter("%skeyword" % MC, "%sindexEntry" % MC)):
        _drop_keeping_tail(node)
    for node in list(elem.iter()):
        if isinstance(node.tag, str) and node.tag.startswith(MC):
            _unwrap(node)
    for node in elem.iter():
        _strip_mc_attrs(node)


CRUFT_ATTRS = ("style", "width", "height", "cellpadding", "cellspacing", "border",
               "align", "valign", "bgcolor")


def strip_presentation(elem) -> None:
    """Drop Flare's styling hooks.

    Every remaining class points at a Flare stylesheet that does not exist on
    this site, and any attribute pandoc does not understand forces the element
    to stay raw HTML instead of becoming markdown — so a classed <a> would ship
    as an HTML anchor rather than a link.
    """
    for node in elem.iter():
        if not isinstance(node.tag, str):
            continue
        for attr in CRUFT_ATTRS:
            node.attrib.pop(attr, None)
        # Keep the language hint that fence_code_blocks added; it is what makes
        # pandoc emit a fenced block instead of an indented one, and the
        # footnote classes, which are this site's own and carry the styling that
        # tells a footnote apart from the sentence it hangs off.
        klass = node.get("class") or ""
        if not (klass.startswith("language-") or klass.startswith(FOOTNOTE_CLASS)):
            node.attrib.pop("class", None)
        if node.tag == "a":
            for attr in ("target", "rel", "alt"):
                node.attrib.pop(attr, None)


def promote_headings(elem) -> None:
    """Shift headings so each page starts at h1.

    Flare topics are chapters of a book, so their top heading is often h2/h3.
    A standalone web page wants exactly one h1, and Material builds the in-page
    table of contents from the relative heading levels.
    """
    levels = [
        int(node.tag[1])
        for node in elem.iter()
        if isinstance(node.tag, str) and re.fullmatch(r"h[1-6]", node.tag)
    ]
    if not levels:
        return
    shift = min(levels) - 1
    if shift <= 0:
        return
    for node in elem.iter():
        if isinstance(node.tag, str) and re.fullmatch(r"h[1-6]", node.tag):
            node.tag = "h%d" % max(1, int(node.tag[1]) - shift)


def flatten_headings(elem) -> None:
    """Headings become plain text: Flare wraps them in presentational spans,
    and inline HTML inside a heading breaks the generated in-page TOC."""
    for level in ("h1", "h2", "h3", "h4", "h5", "h6"):
        for h in elem.iter(level):
            text = re.sub(r"\s+", " ", "".join(h.itertext())).strip()
            for child in list(h):
                h.remove(child)
            h.text = text


def drop_empty_anchors(elem) -> None:
    for node in list(elem.iter("span", "a")):
        has_id = node.get("id") or node.get("name")
        empty = not (node.text and node.text.strip()) and len(node) == 0
        if has_id and empty:
            _unwrap(node)


def slug_relpath(relpath: str) -> str:
    """Hyphenate spaces per path segment, for clean URLs. Applied identically
    to output paths and hrefs so intra-guide links stay valid."""
    out = []
    for seg in relpath.split("/"):
        out.append(seg if seg in ("", ".", "..") else seg.replace(" ", "-"))
    return "/".join(out)


def rewrite_tree_links(elem, topic_rel: Path, resolver, warn) -> None:
    """Point every topic link at its converted page, via `resolver`.

    `resolver(topic_rel, href_path)` returns the site-relative markdown link to
    use, or None when the target is not published; unresolvable links keep their
    text but lose the href, so no page links into a 404.
    """
    for a in elem.iter("a"):
        href = (a.get("href") or "").strip().replace("\\", "/")
        if not href:
            continue
        a.set("href", href)
        if href.startswith(("http://", "https://", "mailto:", "ftp://")):
            continue
        # Flare bookmarks were removed with the empty anchors, so in-page
        # fragments no longer resolve; keep the text, drop the dead link.
        if href.startswith("#"):
            a.attrib.pop("href", None)
            continue
        path = unquote(href.split("#", 1)[0])
        if not path:
            a.attrib.pop("href", None)
            continue
        if not path.lower().endswith(TOPIC_SUFFIXES):
            continue  # handled by copy_linked_files
        link = resolver(topic_rel, path)
        if link is None:
            warn("unresolved link: %s (from %s)" % (href, topic_rel))
            a.attrib.pop("href", None)
        else:
            a.set("href", link)


def _normalize(path: Path):
    """Collapse '..' without touching the filesystem; None if it escapes root."""
    parts = []
    for part in path.parts:
        if part == "..":
            if not parts:
                return None
            parts.pop()
        elif part not in (".", ""):
            parts.append(part)
    return Path(*parts) if parts else None


def _relative_to(target: Path, base: Path) -> str:
    t, b = target.parts, base.parts
    i = 0
    while i < len(t) - 1 and i < len(b) and t[i] == b[i]:
        i += 1
    up = [".."] * (len(b) - i)
    return "/".join(up + list(t[i:])) or target.name


IMAGE_SUFFIXES = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".bmp", ".ico", ".webp")


def image_index(content_root: Path):
    """filename -> {absolute paths}, to repair image refs with a wrong depth."""
    index = {}
    for path in content_root.rglob("*"):
        if path.suffix.lower() in IMAGE_SUFFIXES and path.is_file():
            index.setdefault(path.name.lower(), set()).add(path)
    return index


def rewrite_tree_images(elem, topic_dir: Path, assets_dir: Path, assets_rel: str,
                        warn, index=None) -> None:
    assets_dir.mkdir(parents=True, exist_ok=True)
    for img in elem.iter("img"):
        src = (img.get("src") or "").strip().replace("\\", "/")
        if not src or src.startswith(("http://", "https://", "data:")):
            continue
        img.set("src", src)
        resolved = (topic_dir / unquote(src)).resolve()
        if not resolved.is_file() and index is not None:
            # Same wrong-relative-depth defect the links have; repair it when
            # the filename is unambiguous inside the project.
            matches = index.get(resolved.name.lower(), set())
            if len(matches) == 1:
                resolved = next(iter(matches))
                warn("repaired image by filename: %s (topic %s)" % (src, topic_dir))
        name = resolved.name
        if resolved.is_file():
            dest = assets_dir / name
            if not dest.exists():
                shutil.copy2(resolved, dest)
        else:
            warn("missing image: %s (topic %s)" % (src, topic_dir))
        img.set("src", "%s/%s" % (assets_rel, quote(name)))
        if not img.get("alt"):
            img.set("alt", re.sub(r"[-_]+", " ", Path(name).stem))


# --------------------------------------------------------------------------- #
# Small tree helpers
# --------------------------------------------------------------------------- #
def _drop_keeping_tail(node) -> None:
    parent = node.getparent()
    if parent is None:
        return
    if node.tail:
        prev = node.getprevious()
        if prev is not None:
            prev.tail = (prev.tail or "") + node.tail
        else:
            parent.text = (parent.text or "") + node.tail
    parent.remove(node)


def _replace_with_text(node, text: str) -> None:
    parent = node.getparent()
    if parent is None:
        return
    combined = text + (node.tail or "")
    prev = node.getprevious()
    if prev is not None:
        prev.tail = (prev.tail or "") + combined
    else:
        parent.text = (parent.text or "") + combined
    parent.remove(node)


def _unwrap(node) -> None:
    parent = node.getparent()
    if parent is None:
        return
    idx = list(parent).index(node)
    text = node.text or ""
    if idx > 0:
        parent[idx - 1].tail = (parent[idx - 1].tail or "") + text
    else:
        parent.text = (parent.text or "") + text
    for child in reversed(list(node)):
        parent.insert(idx, child)
    if node.tail:
        prev = node.getprevious()
        if prev is not None:
            prev.tail = (prev.tail or "") + node.tail
        else:
            parent.text = (parent.text or "") + node.tail
    parent.remove(node)


def _strip_mc_attrs(node) -> None:
    for attr in list(node.attrib):
        if attr.startswith(MC):
            del node.attrib[attr]


# --------------------------------------------------------------------------- #
# Serialization + pandoc
# --------------------------------------------------------------------------- #
NS_DECL_RE = re.compile(r'\s*xmlns:[a-zA-Z]+="[^"]*"')


def inner_html(body) -> str:
    parts = []
    if body.text:
        parts.append(html.escape(body.text))
    for child in body:
        parts.append(etree.tostring(child, encoding="unicode", method="html"))
    return "".join(parts)


# The markdown dialect pandoc writes.
#
# Not `gfm`: pandoc indents a nested bullet list by two spaces there, and
# Python-Markdown (what Zensical parses with) only recognizes a nested list at
# four — so every sub-bullet in the source came out as a top-level bullet.
# pandoc's own `markdown` has `four_space_rule`, which indents every level of
# list content to a multiple of four.
#
# The rest of the flavour pulls that dialect back to what Python-Markdown can
# read: pipe tables only (its `tables` extension does not know pandoc's simple,
# multiline or grid tables), and off go the constructs it would render as
# literal text — fenced divs, bracketed spans, fancy/example list markers,
# raw attributes, inline notes, citations, line blocks. `-smart` keeps
# quotes and dashes as authored, and `-implicit_figures`,
# `-header_attributes`, `-inline_code_attributes`, `-link_attributes` and
# `-fenced_code_attributes` keep images, headings, code and links plain: this
# dialect can express an element's leftover HTML attributes as a trailing
# `{...}` block, which Python-Markdown prints verbatim (a Flare
# `<code href="…">` came out as `` `url`{href="url"} ``). With them off,
# pandoc falls back to raw HTML for an attributed link exactly as gfm did.
# `-table_captions` for the same reason: a Flare table caption became a
# `: Caption` line, which renders as literal text; without it the caption
# stays the plain paragraph the source has, and `-table_attributes` keeps a
# Flare table style class off the table.
#
# `-all_symbols_escapable-tex_math_dollars` fixes an escaping mismatch that
# gfm had too: pandoc wrote `\\<` and `\\$`, and Python-Markdown only consumes
# a backslash before its own special characters, so 617 pages showed the
# backslash ("dollar signs (\\$)"). Without those two, `<` comes out as an
# entity and `$` unescaped, and both render as authored.
PANDOC_TO = (
    "markdown"
    "+four_space_rule"
    "+pipe_tables"
    "-simple_tables-multiline_tables-grid_tables"
    "-fancy_lists-example_lists"
    "-fenced_divs-bracketed_spans-native_divs-native_spans"
    "-raw_attribute-inline_notes-citations-definition_lists-line_blocks"
    "-smart-implicit_figures-header_attributes"
    "-inline_code_attributes-link_attributes-fenced_code_attributes"
    "-table_captions-table_attributes"
    "-all_symbols_escapable-tex_math_dollars"
)


def pandoc(chunks):
    """Convert several HTML fragments in one pandoc run; returns markdown list.

    Namespace declarations are stripped first. lxml keeps `xmlns:MadCap` on a
    serialized subtree even after the MadCap attributes are gone, and pandoc
    then treats `<pre xmlns:…><code class="language-js">` as an element it does
    not recognize: the fence comes out with no language, so the code is never
    highlighted. That silently affected most code blocks on the site.
    """
    chunks = [NS_DECL_RE.sub("", chunk) for chunk in chunks]
    joined = ("<p>%s</p>" % SPLIT_TOKEN).join(chunks)
    proc = subprocess.run(
        ["pandoc", "-f", "html", "-t", PANDOC_TO, "--wrap=none"],
        input=joined.encode("utf-8"),
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.decode("utf-8", "replace"))
    out = proc.stdout.decode("utf-8")
    parts = out.split(SPLIT_TOKEN)
    if len(parts) != len(chunks):
        raise RuntimeError("pandoc split mismatch: %d vs %d" % (len(parts), len(chunks)))
    return [p.strip("\n") for p in parts]


VOID_KEEP = {"img", "br", "hr", "input", "iframe", "video", "source", "object"}
EMPTY_PRUNE = ("p", "li", "ul", "ol", "div", "span", "strong", "em", "b", "i")


def drop_empty_blocks(elem) -> None:
    """Remove blocks left empty after condition filtering.

    A list whose items were all excluded from this target would otherwise
    render as a run of bare bullets.
    """
    for _ in range(4):
        removed = False
        for node in list(elem.iter(*EMPTY_PRUNE)):
            parent = node.getparent()
            if parent is None or parent is elem and node.tag == "div":
                pass
            if parent is None:
                continue
            if "".join(node.itertext()).strip():
                continue
            if any(d.tag in VOID_KEEP for d in node.iter() if isinstance(d.tag, str)):
                continue
            _drop_keeping_tail(node)
            removed = True
        if not removed:
            break


def collapse_nested_admonitions(elem) -> None:
    """Flare sometimes marks both the note wrapper and its paragraph as a note;
    keep the outer block so the label survives, and demote the inner one."""
    for node in list(elem.iter()):
        if not isinstance(node.tag, str) or not admonition_type(node):
            continue
        for child in list(node):
            if isinstance(child.tag, str) and admonition_type(child):
                child.attrib.pop("%sautonum" % MC, None)
                classes = [c for c in (child.get("class") or "").split()
                           if c.lower() not in ADMONITION_TYPES]
                if classes:
                    child.set("class", " ".join(classes))
                else:
                    child.attrib.pop("class", None)


def unwrap_plain_divs(elem) -> None:
    """Unwrap divs that carry no meaning, before the list passes run.

    Flare wraps arbitrary runs of content in divs, and a step sequence can have
    its first step inside one while the rest are outside it. The paragraphs are
    then in different parents, so neither the numbering nor the rejoining of an
    interrupted list can see the whole sequence. Callout divs are left alone —
    the admonition pass still needs them.
    """
    for node in list(elem.iter("div")):
        if node.getparent() is None or admonition_type(node):
            continue
        _unwrap(node)


def unwrap_divs(elem) -> None:
    """Flatten leftover Flare wrapper divs (conditional blocks, layout shells).

    Run only after admonitions have been extracted: by then a div carries no
    meaning that markdown cannot express, and keeping it would emit raw HTML
    that blocks markdown processing of its contents.
    """
    for node in list(elem.iter("div")):
        if node.getparent() is not None:
            _unwrap(node)


def extract_admonitions(body):
    """Replace admonition blocks with tokens, innermost first.

    Returns [(type, title, inner_html)] indexed by the token number.
    """
    found = []
    while True:
        candidates = [
            n for n in body.iter()
            if isinstance(n.tag, str) and n.tag in ("div", "p") and admonition_type(n)
        ]
        # innermost first, so nested notes are already tokenized when the
        # enclosing note is extracted
        innermost = None
        for node in candidates:
            if not any(
                admonition_type(d) for d in node.iterdescendants()
                if isinstance(d.tag, str)
            ):
                innermost = node
                break
        if innermost is None:
            break
        kind = admonition_type(innermost)
        label = _autonum_label(innermost.get("%sautonum" % MC)).rstrip(":").strip()
        key = label.lower() or next(
            (c.lower() for c in (innermost.get("class") or "").split()
             if c.lower() in ADMONITION_TYPES), "")
        label = ADMONITION_TITLES.get(key, label)
        innermost.attrib.pop("%sautonum" % MC, None)
        # Clean the extracted subtree now: its HTML is snapshotted here, so the
        # later document-wide cleanup passes would never see it.
        handle_autonum(innermost)
        strip_madcap(innermost)
        strip_presentation(innermost)
        idx = len(found)
        found.append((kind, label, inner_html(innermost)))
        token = etree.Element("p")
        token.text = ADM_TOKEN % idx
        token.tail = innermost.tail
        parent = innermost.getparent()
        parent.replace(innermost, token)
    return found


def admonition_html(idx, bodies, indent: str = "") -> str:
    """An admonition as raw HTML, for places markdown syntax cannot reach.

    Inside a bullet list item pandoc indents continuation lines by two spaces,
    but Python-Markdown only recognizes a nested block at a multiple of four —
    so `!!! note` there would render as literal text. The theme styles the
    HTML form identically, and Zensical still rewrites the `.md` links inside
    it, so nothing is lost.
    """
    kind, label, _body_md, body_html = bodies[idx]
    body_html = re.sub(
        r"<p>@@FLARE2MD-ADM-(\d+)@@</p>",
        lambda m: admonition_html(int(m.group(1)), bodies),
        body_html,
    )
    title = label or kind.title()
    block = (
        '<div class="admonition %s">\n'
        '<p class="admonition-title">%s</p>\n'
        "%s\n"
        "</div>"
    ) % (kind, title, body_html)
    if not indent:
        return block
    return "\n".join(indent + line for line in block.splitlines())


def expand_admonitions(md: str, bodies, indent: str = "") -> str:
    """Substitute admonition tokens with Material `!!! type` blocks."""

    def repl(match):
        lead, idx = match.group(1), int(match.group(2))
        kind, label, body_md, _body_html = bodies[idx]
        # Only a multiple-of-four indent is inside a block markdown can nest;
        # anything else is a bullet list item, which needs the HTML form.
        if len(lead) % 4:
            return "\n" + admonition_html(idx, bodies, lead) + "\n"
        body_md = expand_admonitions(body_md, bodies)
        title = ' "%s"' % label if label and label.lower() != kind else ""
        lines = ["%s!!! %s%s" % (lead, kind, title), ""]
        for line in body_md.splitlines():
            lines.append("%s    %s" % (lead, line) if line.strip() else "")
        lines.append("")
        return "\n".join(lines)

    prev = None
    while prev != md:
        prev = md
        md = ADM_TOKEN_RE.sub(repl, md)

    # A token inside a raw HTML block (a note nested in a real table) cannot
    # become a block-level admonition; inline it rather than leak the token.
    def inline(match):
        kind, label, body_md, _body_html = bodies[int(match.group(1))]
        text = " ".join(
            line.strip() for line in expand_admonitions(body_md, bodies).splitlines()
            if line.strip() and not line.strip().startswith("!!!")
        )
        return "**%s** %s" % (label or kind.title(), text)

    return re.sub(r"@@FLARE2MD-ADM-(\d+)@@", inline, md)


EMPTY_ATTR_RE = re.compile(r"[ \t]*\{\s*\}")

# Code that ends up inside a table stays raw HTML — markdown fences cannot live
# in an HTML block — so pandoc leaves it as <pre class="lang"><code>…</code></pre>
# and the highlighter never sees it. These blocks are common in the install and
# upgrade guides (property files, SQL, shell), so they are highlighted here with
# the same Pygments the site uses, wrapped in the markup the theme styles.
RAW_PRE_RE = re.compile(
    r'<pre(?:\s+class="(?P<lang>[^"]*)")?[^>]*>\s*<code[^>]*>(?P<code>.*?)</code>\s*</pre>',
    re.S,
)


# Only these names are handed to Pygments. An unknown name sends it looking
# through plugin lexers, and a broken plugin in the environment
# (actian-pygments-lexers points at a `custom_lexers` module that will not
# import) raises from deep inside that search. Flare's styling classes land in
# the same attribute as real languages, so the gate matters.
HIGHLIGHT_LANGS = frozenset({
    "bash", "html", "ini", "java", "javascript", "json", "properties",
    "python", "shell", "sql", "text", "xml", "yaml",
})


def highlight_raw_code(md: str) -> str:
    """Syntax-highlight raw <pre><code> blocks left in the markdown."""
    try:
        from pygments import highlight
        from pygments.formatters import HtmlFormatter
        from pygments.lexers import get_lexer_by_name
        from pygments.util import ClassNotFound
    except ImportError:  # pragma: no cover - Pygments ships with Zensical
        return md

    def repl(match):
        lang = (match.group("lang") or "text").strip().lower() or "text"
        if lang not in HIGHLIGHT_LANGS:
            return match.group(0)
        code = html.unescape(match.group("code"))
        try:
            lexer = get_lexer_by_name(lang, stripnl=False)
        except ClassNotFound:
            return match.group(0)
        except Exception:
            # Pygments imports every registered plugin lexer while resolving a
            # name, so a broken third-party plugin in the environment would
            # otherwise fail the whole page. Leave the block unhighlighted.
            return match.group(0)
        # `nowrap` keeps only the token spans, so the surrounding markup matches
        # what the theme produces for fenced blocks.
        formatter = HtmlFormatter(nowrap=True)
        tokens = highlight(code, lexer, formatter).rstrip("\n")
        return (
            '<div class="language-%s highlight"><pre><code>%s</code></pre></div>'
            % (lang, tokens)
        )

    return RAW_PRE_RE.sub(repl, md)


# pandoc writes a GFM hard line break as a trailing backslash, which
# Python-Markdown renders as a literal "\" on the page.
HARD_BREAK_RE = re.compile(r"(?<!\\)\\$", re.M)


def clean_markdown(md: str) -> str:
    md = highlight_raw_code(md)
    md = HARD_BREAK_RE.sub("<br>", md)
    md = NS_DECL_RE.sub("", md)
    md = EMPTY_ATTR_RE.sub("", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = "\n".join(line.rstrip() for line in md.splitlines())
    return md.strip() + "\n"


def first_heading(body) -> str:
    for level in ("h1", "h2", "h3"):
        el = body.find(".//%s" % level)
        if el is not None:
            txt = "".join(el.itertext()).strip()
            if txt:
                return re.sub(r"\s+", " ", txt)
    return ""


def description_of(md: str, limit: int = 200) -> str:
    """First real sentence of the page, for the meta description."""
    for block in md.split("\n\n"):
        block = block.strip()
        if not block or block.startswith(("#", "!!!", "|", "<", "-", "*", ">", "```", "!")):
            continue
        text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", block)
        text = re.sub(r"[*_`]", "", text).replace("\n", " ")
        # Drop markdown escaping and brackets: the description is plain text in
        # the front matter, and a stray "[...]" reads as a link reference.
        text = re.sub(r"\\(.)", r"\1", text)
        text = text.replace("[", "").replace("]", "")
        text = re.sub(r"\s+", " ", text).strip()
        if len(text) < 25:
            continue
        if len(text) > limit:
            cut = text[:limit].rsplit(" ", 1)[0]
            return cut + "..."
        return text
    return ""


def yaml_scalar(s: str) -> str:
    if s == "" or re.search(r'[:#\[\]{}",&*?|<>=!%@`\'\\]', s) or s != s.strip():
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def copy_linked_files(elem, topic_dir: Path, files_dir: Path, files_rel: str, warn) -> None:
    """Copy non-topic link targets (PDF/ZIP/JAR samples) into the assets tree."""
    for a in elem.iter("a"):
        href = (a.get("href") or "").strip().replace("\\", "/")
        if not href or href.startswith(("http://", "https://", "mailto:", "#", "ftp://")):
            continue
        a.set("href", href)
        path = unquote(href.split("#", 1)[0])
        if not path or path.lower().endswith(TOPIC_SUFFIXES):
            continue
        resolved = (topic_dir / path).resolve()
        if not resolved.is_file():
            warn("missing linked file: %s (topic %s)" % (href, topic_dir))
            a.attrib.pop("href", None)
            continue
        files_dir.mkdir(parents=True, exist_ok=True)
        dest = files_dir / resolved.name
        if not dest.exists():
            shutil.copy2(resolved, dest)
        a.set("href", "%s/%s" % (files_rel, quote(resolved.name)))
