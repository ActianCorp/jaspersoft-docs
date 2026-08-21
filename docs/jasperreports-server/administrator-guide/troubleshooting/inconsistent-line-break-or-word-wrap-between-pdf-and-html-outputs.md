---
title: Inconsistent Line Break Between PDF and HTML Outputs
description: "When a user adds a font extension, runs the report and exports it to PDF, at times it is observed that the PDF and HTML outputs don't display text with the same line breaks."
---

# Inconsistent Line Break Between PDF and HTML Outputs

When a user adds a font extension, runs the report and exports it to PDF, at times it is observed that the PDF and HTML outputs don't display text with the same line breaks.

To ensure consistent text display in PDF exports and HTML report preview, it's recommended to use font extensions for all text. This is because the system assumes the same font is available during both report generation and PDF creation.

<table>
<thead>
<tr>
<th colspan="3"><p>Inconsistent Line Break Between PDF and HTML Outputs</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>WEB-INF/classes/jasperreports.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><code>net.sf.jasperreports.export.pdf.use.saved.line.breaks</code></td>
<td colspan="2"><p>Use the line breaks computed during report generation. Set the value to <code>true</code> to activate the fix.</p></td>
</tr>
</tbody>
</table>
