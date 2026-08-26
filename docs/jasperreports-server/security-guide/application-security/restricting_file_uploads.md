---
title: Restricting File Uploads
description: "Several dialogs in JasperReports Server prompt the user to upload a file to the server. For performance and security reasons, you may want to restrict file uploads by name and size."
---

# Restricting File Uploads

Several dialogs in JasperReports Server prompt the user to upload a file to the server. For performance and security reasons, you may want to restrict file uploads by name and size.

The following setting is the global file upload limit for the entire server. Any single upload that exceeds this limit triggers an error and a stack trace message. It is intended to be an absolute maximum to prevent a worse out-of-memory error that affects the entire server.

<table>
<thead>
<tr>
<th colspan="3"><p>Global File Size Upload Limit</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>…/WEB-INF/js.config.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>file.upload.max.size</code></p></td>
<td><p><code>-1</code> &lt;default&gt;</p></td>
<td><p>Maximum size in bytes allowed for any file upload. The default value, -1, means that there is no limit to the file size, and a large enough file could cause an out-of-memory error in the JVM. Some file uploads such as importing through the UI are necessarily large and must be considered. Set this value larger than your largest expected import and smaller than your available memory.</p></td>
</tr>
</tbody>
</table>

The following settings apply to most file upload dialogs in the UI, such as uploading a JRXML or a JAR file to create a JasperReport in the repository. These settings in the `fileResourceValidator` bean restrict the file size and the filename pattern.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>File Upload Restrictions</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>…/WEB-INF/flows/fileResourceBeans.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>maxFileSize</code></p></td>
<td><p><code>-1</code> &lt;default&gt;</p></td>
<td><p>The maximum size in bytes allowed for a file uploaded through most UI dialogs. If an upload exceeds this limit, the server displays a helpful error message. The default value, -1, means that there is no limit to the file size, and an upload could reach the global limit if set, or an out-of-memory error. Usually, the files required in resources are smaller, and a limit of 10 MB is reasonable.</p></td>
</tr>
<tr>
<td><code>fileNameRegexp</code></td>
<td><code>^.+$</code> &lt;default&gt;</td>
<td>A regular expression that matches allowed file names. The default expression matches all filenames of one or more characters. A more restrictive expression such as [a-zA-Z0-9]{1,200}\.[a-zA-Z0-9]{1,10} would limit uploads to alpha-numeric names with an extension.</td>
</tr>
<tr>
<td><code>fileName</code><br />
<code>ValidationMessageKey</code></td>
<td><code>&lt;null/&gt;</code> &lt;default&gt;</td>
<td><p>The name of a Java property key whose value is a custom message to display when the uploaded filename does not match <code>fileNameRegexp</code>. For example, you could add the following line to WEB-INF/js.config.properties:</p>
<p><code>my.filename.validation=The name of the uploaded filename must contain only alphanumeric characters and have a valid extension.</code></p></td>
</tr>
</tbody>
</table>

The following setting restricts the extension of the uploaded file for the sub flows, when adding files to a composite resource like reports, for example, **Add Resource &gt; JasperReport**. The upload dialog searches for files with the given extensions only.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>File Upload Extensions</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>&lt;jasperserver-pro-war&gt;/scripts/resource.locate.js</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Value</p></td>
</tr>
<tr>
<td><p><code>ALLOWED_FILE_</code><br />
<code>RESOURCE_EXTENSIONS</code></p></td>
<td colspan="2"><p>By default, the following extensions are allowed:</p>
<p><code>"css", "ttf", "jpg", "jpeg", "gif", "bmp", "png", "jar", "jrxml", "properties", "jrtx", "xml", "agxml", "docx", "doc", "ppt", "pptx", "xls", "xlsx", "ods", "odt", "odp", "pdf", "rtf", "html"</code></p>
<p>Add or remove extensions to change the file type restrictions.</p></td>
</tr>
</tbody>
</table>

The following setting restricts the extension of the uploaded file for adding individual files to the repository (for example, **Add Resource &gt; File &gt; JRXML**). The upload dialog browses only for files with the extensions that are mapped to resource types.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>File Upload Extensions</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>&lt;jasperserver-pro-war&gt;/scripts/resource.add.files.js</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Value</p></td>
</tr>
<tr>
<td><p><code>typeToExtMap</code></p></td>
<td colspan="2"><p>This property specifies the mapping of resource types to the file extensions.</p>
<p>For example: <code>'img': ['jpg', 'jpeg', 'gif', 'bmp', 'png']</code></p>
<p>Add or remove extensions to change the file type restrictions.</p></td>
</tr>
</tbody>
</table>
