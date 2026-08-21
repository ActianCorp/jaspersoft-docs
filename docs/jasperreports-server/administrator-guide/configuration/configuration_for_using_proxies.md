---
title: Configuration for Using Proxies
description: "JasperReports Server exposes some URLs to itself through the UI and when using the scheduler to send emails. When using a proxy, those URLs must be rewritten so that they expose the proxy URL, not..."
---

# Configuration for Using Proxies

JasperReports Server exposes some URLs to itself through the UI and when using the scheduler to send emails. When using a proxy, those URLs must be rewritten so that they expose the proxy URL, not actual URL of the server instance. This can be done on the proxy or using JasperReports Server settings.

Configure your proxy or load balancer to set X-Forwarded-\* headers (X-Forwarded-For, X-Forwarded-Proto, X-Forwarded-Host, X-Forwarded-Port). For the configuration details, refer to the documentation of the proxy or load balancer that you use.

If you are using multiple proxies, X-Forwarded-\* headers on all intermediate proxies should be set to the address of the proxy receiving requests from the user's UI.

!!! note

    When using a proxy, make sure that the proxy is set up to allow special symbols in URLs. In Apache httpd, this option is called `AllowEncodedSlashes On`. See the documentation for your application server for more information.

Change the following setting so that JasperReports Server exposes the proxy URL for scheduled reports.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>Configuration for Using Proxies for Scheduled Reports</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="2"><p><code>.../WEB-INF/js.quartz.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>report.scheduler.web.deployment.uri</code></p></td>
<td><p>This is the base URL used by the scheduler to generate links to reports in emails. Set this property to the full URL, including application name, that you expose through your proxy.</p>
<p>For example:</p>
<pre class="text"><code>http://bi.example.com/jasperserver</code></pre>
<p>Specify <code>http</code> or <code>https</code> in your URL.</p></td>
</tr>
</tbody>
</table>
