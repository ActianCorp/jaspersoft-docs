---
title: "Coming from Jaspersoft Studio"
description: "Jaspersoft Desktop designs the same reports as Jaspersoft Studio: the same JRXML, the same JasperReports engine, the same elements, data adapters and JasperReports Server. Your reports open as they..."
---

# Coming from Jaspersoft Studio

Jaspersoft Desktop designs the same reports as Jaspersoft Studio: the same JRXML, the same
JasperReports engine, the same elements, data adapters and JasperReports Server. Your reports open
as they are. This page says what carries over, what works differently, and what is not there yet.

## Your projects

**A Studio project is a folder: open it.** On the home screen, **Open folder…** and choose the
project's folder. Its reports, data adapters, images, subreports and style templates are in the
explorer, where they were; nothing is imported or converted. See
[Working with workspaces](workspaces.md).

**The libraries of the project's build path** (JDBC drivers, scriptlets, font extensions, custom
components) go in **Settings › Libraries** of the workspace (see
[Workspace settings](workspace-settings.md)), which the reports of the workspace then find, in the
designer and in the preview.

**Data adapters are files with the extension `.jrdax`.** A data adapter file of Studio has the same
content in an `.xml` file: rename it to `.jrdax` and it opens, tests and runs here. A data adapter
kept in Studio's own Repository Explorer rather than in the project is not a file yet: save it to a
file from Studio first.

**A report names its data adapter** with the **Data Adapter** of its **Dataset** tab, a path in the
workspace. Studio can also remember the adapter of a report in a way of its own, which Jaspersoft
Desktop does not read: if a report opens without data, choose its data adapter there, once, and
save it.

**JasperReports Server**: connect from the home screen, **Connect to JasperReports Server…**. There
is no wizard to publish a report: the server's repository is the workspace, and you edit its
reports in place. See [Working with JasperReports Server](jasperreports-server.md).

## JRXML 6 and JRXML 7

Jaspersoft Desktop opens reports in both formats: the format of JasperReports 6 (and of Jaspersoft
Studio 6), and the format of JasperReports 7.

**A report is saved in the format it was read in.** The switch **Use JasperReports 7 Format**, in
the report's **Properties** (click an empty area of the page, so that nothing is selected), shows
which, and changes it:

- **off**: the report is saved as JRXML 6, which Jaspersoft Studio 6 and applications on
    JasperReports 6 read;
- **on**: the report is saved as JRXML 7. JasperReports 6 and Jaspersoft Studio 6 cannot read it
    any more.

New reports are made in the JasperReports 7 format. Keep a report in format 6 for as long as an
application or a colleague on JasperReports 6 uses it.

## Compiling

Jaspersoft Desktop compiles reports with the latest version of JasperReports, the one it includes,
in the preview and with **Compile the report to a .jasper file next to the .jrxml** (see
[Getting the .jasper file](concepts.md#getting-the-jasper-file)). There is no setting yet to
compile `.jasper` files for an older version: a `.jasper` made here is for JasperReports 7.

An application still on JasperReports 6 keeps its reports in JRXML 6 (the switch off) and compiles
them itself, with its own version of JasperReports, or uses `.jasper` files compiled by Jaspersoft
Studio 6.

## The palette: community and Pro elements

The **Palette** has the elements of JasperReports, which every application using JasperReports can
run:

- **Text Field**, **Static Text**, **Image**, **Rectangle**, **Ellipse**, **Line**, **Frame**,
    **Break**, **Generic**;
- **Table**, **List**, **Crosstab**, **Subreport**, **Chart** (the JFreeChart charts);
- the barcodes, and the **Composite** elements: page numbers, dates, percentages.

It also has the **Pro** components:

- **Highcharts** (the HTML5 charts), **HTML** (the HTML component), **CVC** (the custom
    visualization component), **Map**;
- the Fusion components: **Fusion Chart**, **Fusion Map**, **Fusion Widgets**;
- **AdHoc**, the Ad Hoc component.

Jaspersoft Desktop designs and previews them all. An application that runs a report using a Pro
component needs **JasperReports Pro**, the commercial library, and its license; JasperReports
Server runs them in its commercial editions.

## Not there yet

- **Custom data adapters and custom data sources.** The kinds of data are the ones of the list in
    [Working with data adapters](data-adapters.md). A data source type of your own, added to
    Jaspersoft Studio by a jar, is not among them yet: a report using one opens, but its data cannot
    be read here.
- **A designer for style templates (`.jrtx`).** A style template can be used by a report as it is,
    and edited by hand: it opens in the text editor, and the styles it holds are applied in the
    designer and in the preview. There is no page yet to design them visually: see
    [The file types of the workspace](workspaces.md#file-types).
- **A wizard for font extensions.** Make them by hand: see
    [Fonts and PDF](fonts-and-pdf.md#making-a-font-extension).
- **A visual tool to tag elements for accessible PDF** (PDF tags, a JasperReports Pro feature).
    The tags can still be set by hand, as properties of the elements.
- **Compiling for older versions of JasperReports**, see above.
- **A wizard to publish to JasperReports Server**: work on the server's repository directly.

## New here

- **The AI assistant**, beside the report, which reads and changes it with you; and an MCP server
    for Claude, ChatGPT and the other assistants. See [Designing reports with AI](ai-assistant.md)
    and [Working with the AI assistant](tutorial-ai.md).
- **A local history** of every report: the versions you saved and those you did not, restored with
    a click. Jaspersoft Desktop never saves for you, and keeps your work as you go.
- **The Samples workspace** and its **sample database**, ready on the first start, with the
    tutorials of this guide. See [The sample database](sample-database.md).
- **Custom visualization components** that the assistant writes and builds. See
    [Custom visualization components](custom-visualization-components.md).

## Keys

**⌘** on macOS is **Ctrl** on Windows and Linux.

| Keys | Does |
| --- | --- |
| **⌘S** | Save |
| **⌘Z**, **⌘Y** (or **⌘⇧Z**) | Undo, redo |
| **⌘A** | Select every element of the page |
| **Delete**, **Backspace** | Delete what is selected |
| Arrows, **Shift** + arrows | Move what is selected |
| **⌘⇧P** | Preview |
