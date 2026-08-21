---
title: Custom URLs Not Loading in Dashboards
description: Dashboards allow you to specify frames that contain web pages loaded from custom URLs specified when designing the dashboard. These URLs can even include parameters from input controls. If the URL...
---

# Custom URLs Not Loading in Dashboards

Dashboards allow you to specify frames that contain web pages loaded from custom URLs specified when designing the dashboard. These URLs can even include parameters from input controls. If the URL takes too long to load, JasperReports Server will display an error message instead of the content.

If you expect the custom URL to take longer than 10 seconds, you can change the default timeout as follows:

<table>
<thead>
<tr>
<th colspan="3"><p>Configuring the Dashboard URL Loading Timeout</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../scripts/dashboard.designer.js</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><code>CUSTOM_URL_IFRAME_TIMEOUT</code></p></td>
<td colspan="2"><p>Time in milliseconds that the server will allow a custom URL to load in a dashboard before displaying an error. The setting takes effect immediately when the file is saved, there is no need to restart the server.</p></td>
</tr>
</tbody>
</table>
