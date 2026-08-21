---
title: Configuring 404 Error Message
description: The show404Details flag controls the level of detail provided in REST API 404 (Page Not Found) error responses. This setting helps to prevent the exposure of potentially sensitive information in...
---

# Configuring 404 Error Message

The `show404Details` flag controls the level of detail provided in REST API 404 (Page Not Found) error responses. This setting helps to prevent the exposure of potentially sensitive information in error messages.

By default, detailed 404 error messages are active. If you wish to prevent REST API responses from showing detailed 404 messages, you should disable this flag:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>404 Error Message</p></th>
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
<td><p><code>show404Details</code></p></td>
<td><p>When this property is set to <code>true</code>, REST API 404 responses have special characters escaped in strings using HTML character references (entities), and the response include detailed information. When it is set to <code>false</code>, the response is a general message, such as<code> {"message":"Page Not Found","errorCode":"resource.not.found"}</code>, to avoid displaying potentially sensitive information.</p>
<p>The default is <code>true</code>.</p></td>
</tr>
</tbody>
</table>
