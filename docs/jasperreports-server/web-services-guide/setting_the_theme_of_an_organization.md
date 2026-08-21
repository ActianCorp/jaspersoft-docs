---
title: Setting the Theme of an Organization
description: "A theme determines how the JasperReports Server interface appears to users. Administrator can create and set different themes for each organization. To set a theme through web services, use the PUT..."
---

# 1.0.1 Setting the Theme of an Organization

A theme determines how the JasperReports Server interface appears to users. Administrator can create and set different themes for each organization. To set a theme through web services, use the PUT method of the REST v2/organizations service to modify the corresponding property of the desired organization.

For example:

PUT http://localhost:8080/jasperserver-pro/rest_v2/organizations/Audit

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;theme&quot;</span><span class="fu">:</span><span class="st">&quot;jasper_dark&quot;</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

For more information about themes, see the JasperReports® Server Administrator Guide.
