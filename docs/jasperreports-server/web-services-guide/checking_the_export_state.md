---
title: Checking the Export State
description: "After receiving the export ID, you can check the state of the export operation."
---

# Checking the Export State

After receiving the export ID, you can check the state of the export operation.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/export</span>/&lt;export-id&gt;/<span>state</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Returns a JSON object that gives the current state of the export operation.</p></td>
<td><p>404 Not Found – When the specified export ID is not found.</p></td>
</tr>
</tbody>
</table>

The body of the response contains the current state of the export operation:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>{
  phase: &quot;inprogress&quot;,
  message: &quot;Progress...&quot;
}</code></pre></div></td>
<td><div class="language-text highlight"><pre><code>{
  phase: &quot;ready&quot;,
  message: &quot;Ready!&quot;
}</code></pre></div></td>
<td><div class="language-text highlight"><pre><code>{
  phase: &quot;failure&quot;,
  message: &quot;Not enough space on
            disk&quot;
}</code></pre></div></td>
</tr>
</tbody>
</table>
