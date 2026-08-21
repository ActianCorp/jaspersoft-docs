---
title: Configuring Report Thumbnails
description: The JasperReports Server REST API has the ability to generate and export thumbnail images (small preview images) of reports and dashboards. The JasperMobile apps for Android and iOS use this feature...
---

# Configuring Report Thumbnails

The JasperReports Server REST API has the ability to generate and export thumbnail images (small preview images) of reports and dashboards. The JasperMobile apps for Android and iOS use this feature to display small tiles with the report or dashboard image.

For more information about the REST API, see the JasperReports Server REST API Reference.

By default, report thumbnails are not active. If you use the JasperMobile apps with your server, you should turn on the report thumbnails:

<table>
<thead>
<tr>
<th colspan="2"><p>Report Thumbnails</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="2"><p><code>.../WEB-INF/js.spring.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>property.reportThumbnailServiceEnabled=false</code></p></td>
<td><p>When this property is set to <code>true</code>, JasperReports Server generates and sends report thumbnails in response to REST API requests. When it is set to <code>false</code>, report thumbnails are not generated. The default is false.</p></td>
</tr>
</tbody>
</table>
