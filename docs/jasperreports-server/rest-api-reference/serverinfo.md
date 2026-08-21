---
title: The serverInfo Service
description: The restv2/serverInfo service returns the same information as the About JasperReports Server link in the user interface.
---

# The serverInfo Service

The rest_v2/serverInfo service returns the same information as the **About JasperReports Server** link in the user interface.

Use the following methods to verify the server information, such as version number and supported features for compatibility with your REST client application. Your application should also use the date and date-time patterns to interpret all date or date-time strings it receives from the server and to format all date and date-time strings it sends to the server.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td>GET</td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/serverInfo</span></span></p></td>
</tr>
<tr>
<td colspan="4">Options</td>
</tr>
<tr>
<td colspan="4"><span>accept: application/xml</span>
<p><span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="2">Return Value on Success</td>
<td colspan="2">Typical Return Values on Failure</td>
</tr>
<tr>
<td colspan="2">200 OK: Body described below.</td>
<td colspan="2">This request should always succeed when the server is running.</td>
</tr>
</tbody>
</table>

The server returns a structure containing the information in the requested format, XML, or JSON:

```
<serverInfo>
  <build>20141121_1750</build>
  <dateFormatPattern>yyyy-MM-dd</dateFormatPattern>
  <datetimeFormatPattern>yyyy-MM-dd'T'HH:mm:ss</datetimeFormatPattern>
  <edition>PRO</edition>
  <editionName>Enterprise</editionName>
  <features>Fusion AHD EXP DB AUD ANA MT </features>
  <licenseType>Commercial</licenseType>
  <version>6.0.0</version>
</serverInfo>

{
  "dateFormatPattern": "yyyy-MM-dd",
  "datetimeFormatPattern": "yyyy-MM-dd'T'HH:mm:ss",
  "version": "6.0.0",
  "edition": "PRO",
  "editionName": "Enterprise",
  "licenseType": "Commercial",
  "build": "20150527_1942",
  "features": "Fusion AHD EXP DB AUD ANA MT "
}
```

You can access each value separately with the following URLs. Note that some information does not apply to community editions of the server. The response is the raw value, XML, or JSON are not accepted formats.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td>GET</td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/serverInfo/version</span></span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/serverInfo/edition</span></span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/serverInfo/editionName</span></span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/serverInfo/build</span></span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/serverInfo/licenseType</span></span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/serverInfo/features</span></span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/serverInfo/dateFormatPattern</span></span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/serverInfo/datetimeFormatPattern</span></span></p></td>
</tr>
<tr>
<td colspan="2">Return Value on Success</td>
<td colspan="2">Typical Return Values on Failure</td>
</tr>
<tr>
<td colspan="2"><p>200 OK: The requested value.</p></td>
<td colspan="2"><p>These requests should always succeed when the server is running.</p></td>
</tr>
</tbody>
</table>
