---
title: Setting the Temporary Upload Directory
description: "When you create a resource by uploading a large file, the server stores the file in a temporary location while receiving and processing it. Uploaded files may be huge and cause errors if the local..."
---

# 1.0.1 Setting the Temporary Upload Directory

When you create a resource by uploading a large file, the server stores the file in a temporary location while receiving and processing it. Uploaded files may be huge and cause errors if the local disk is limited or full. If you are having issues when creating resources with large files, set the following property to a directory location with sufficient capacity.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Temporary Upload Directory for Web Services</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p>…\WEB-INF\applicationContext-webservices.xml</p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>attachmentsTempFolder</code></p></td>
<td><p><code>managementServiceImpl</code><br />
</p></td>
<td><p>Change this property to an absolute path such as /tmp/jasperserver/axis_attachments or a relative path such as {java.io.tmpdir}/jasperserver/axis_attachments.</p></td>
</tr>
</tbody>
</table>
