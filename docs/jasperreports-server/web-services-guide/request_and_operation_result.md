---
title: Request and Operation Result
description: "The repository web services operation takes a single input parameter of type String. This XML document represents the request. The following shows its DTD:"
---

# 1.1 Request and Operation Result

The repository web services operation takes a single input parameter of type `String`. This XML document represents the request. The following shows its DTD:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>&lt;!ELEMENT request (argument*, resourceDescriptor?)&gt;
&lt;!ATTLIST request
  operationName (get | list | put | runReport) &quot;list&quot;
  locale #IMPLIED
&gt;
&lt;!ELEMENT argument (#PCDATA)&gt;
&lt;!ATTLIST argument
  name CDATA #REQUIRED
&gt;</code></pre></td>
</tr>
</tbody>
</table>

A request is a very simple document that contains:

- The operation to execute (`list`, `get`, `put`, `delete`, or `runReport`).
- A set of optional arguments. Each argument is a pair of a key and a value that is used to achieve very particular results; arguments are only used rarely.
- A resource descriptor.

The operation name is redundant, since the operation to execute is intrinsic in the invoked service. However, including the name can clarify the request document.

The services act on a single resource at time. The resource that is the subject of the request is described by a `resourceDescriptor`.

To get error messages in a particular locale supported by the server, specify the locale code with the `locale` attribute. Locale codes are in the form `<language code>[_<country>[_<variant>]`. Valid examples include `en_US`, `it_IT`, `fr_FR`, `de_DE`,` ja_JP`, and `es_ES`. For a list of Java-compliant locales, refer to Sun’s Java web site.

The following sample request lists the repository root:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span><span class="fu">?&gt;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">request</span> <span class="ot">operationName=</span><span class="st">&quot;list&quot;</span> <span class="ot">locale=</span><span class="st">&quot;en&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;folder&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/&quot;</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;null&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">request</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

Executing a service produces the `operationResult` in the form of a new XML document.

The DTD is very simple:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>&lt;!ELEMENT operationResult (code, message?, resourceDescriptor*)&gt;
&lt;!ATTLIST operationResult
  version NMTOKEN #REQUIRED
&gt;
&lt;!ELEMENT code (#PCDATA)&gt;
&lt;!ELEMENT message (#PCDATA)&gt;</code></pre></td>
</tr>
</tbody>
</table>

The operation result contains a return code, an optional return message, and zero or more resource descriptors. A return code other than 0 indicates an error, which is normally described in the message tag.

The operation result always includes the `version` attribute: it can be used to detect the server version. For example, you can list the repository root and read the version set by the server in the response. In this case, we aren’t interested in the root folder’s content. We just want the version information from the response object itself.

The operation result of such a request is:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">operationResult</span> <span class="ot">version=</span><span class="st">&quot;1.2.1&quot;</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">returnCode</span>&gt;0&lt;/<span class="kw">returnCode</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  ...</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  several resource descriptors...</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  ...</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">operationResult</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
