---
title: Import and Export Catalogs
description: "The output of the export command and the input to the import command is called a catalog. It's a set of folders and files that comprise the server's internal database, including organizations, users,..."
---

# Import and Export Catalogs

The output of the export command and the input to the import command is called a catalog. It's a set of folders and files that comprise the server's internal database, including organizations, users, roles, scheduled jobs, and repository resources such as reports and associated files. When you don't need the entire database, you can specify options to export only the contents you need, for example one role and its users.

Within a catalog, user passwords are encrypted so that they are not visible outside the server. For more details, see The Import-Export Encryption Keys below.

The catalog is usually exported as a single zip file (compressed archive) containing all the files and folders. However, the content of the catalog is not intended for external access. Objects in the database, such as users, roles, and folders are described in XML files, and repository resources are stored in various private formats consisting of data files and subfolders. The XML syntax of the catalog files is not publicly defined, and the data files aren't meant to be accessed.

To access and interact with the server's internal objects, use the REST v2 API. This web service has well defined datatypes and resource descriptors in XML or JSON formats and a complete set of methods for reading and writing objects on the server. For more information, see the JasperReports Server REST API Reference.

!!! warning

    While user passwords and data source passwords are encrypted in export catalogs, you should still take appropriate measures to secure the catalog file from unauthorized access. Catalog files may contain sensitive metadata such as user names, database URLs, and customer information (in the form of organizations). Catalog files may also contain data in the form of report output such as the PDF of an executive report.

# Dependencies During Import and Export

The resources in the repository often have dependencies on other resources, for example a report that relies on images, input datatypes, and a data source. When exporting a resource, you have the option of including all of its dependencies, even if they are stored in folders that were not selected in the repository. Importing a catalog that contains such dependencies will re-create the same folder structure in the target repository. Once imported, you can move and redefine the dependencies of these resources.

However, when exporting individual organizations, there are three scenarios that create broken dependencies:

- An organization admin exports a resource with dependencies that he does not have permission to access.

- The export from an organization includes a resource with a dependency in a parent organization. For reasons of consistency, even the system admin (`superuser`) can't export a dependency in a parent organization if the parent organization is not explicitly selected for export.

- Unchecking the **Include dependencies** check box when exporting from the repository in the Web UI.

In these cases, you will see an error to inform you that the dependency cannot be exported. If you choose to proceed with the export, it will contain a broken dependency that may block it from being imported.

To avoid dependencies between organizations, you can place shared resources in the Public folder and set permissions to restrict access and visibility. Dependent resources in the Public folders should be visible to organization admins, but not to regular organization users.

# The Import-Export Encryption Keys

As of JasperReports Server 7.5, the management of the encryption keys used during import and export has been automated. These encryption keys are used by the server to encrypt user passwords so they are not revealed in export catalogs.

In previous versions of the server, the import-export key had to be configured manually outside the server. Beginning with version 7.5, the server creates and manages its import-export key internally, and also includes UI and REST options for specifying keys during import and export operations. However, there are still cases when you may need to manage keys on the server and specify keys during import-export operations.

The following table summarizes the use of keys when importing catalogs into the current version of the server:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Origin of Export Catalog</th>
<th>Guidelines for Importing into 10.1</th>
</tr>
</thead>
<tbody>
<tr>
<td>Prior to version 7.5<br />
With default key</td>
<td>The current version of the server handles previous export catalogs created with legacy keys, and even older catalogs that did not use encryption. When importing through the UI, specify the Legacy key, and when importing through the command line, specify the <code>deprecatedImportExportEncSecret</code>.</td>
</tr>
<tr>
<td>Prior to version 7.5<br />
With custom import-export keys</td>
<td><p>The custom keys are not known to your server, so in order to import these catalogs, you will need to share the custom key with the importing server. There are two ways to specify custom keys:</p>
<ol>
<li><p>For one-time or occasional imports, you can enter the key's hex value into the UI or the import command-line, or store it in the repository for repeated use.</p></li>
<li><p>For continual use, you should import the key to server's keystore with the command-line import command. Then the key is available by it's alias either through the UI or the command-line when importing a catalog.</p></li>
</ol></td>
</tr>
<tr>
<td>Version 7.5 and later<br />
From the same server</td>
<td>When you import a catalog back into the same server, the server uses the same key for export and import and thus can read its own export catalog. When importing through the UI, specify the Server key, and when importing through the command-line, the key is detected automatically. This is also true after upgrading the server, as long as the catalog was exported from version 7.5 or later and the server's keystore was preserved during the upgrade. For more information about the keystore and catalogs during upgrade, see the <span>JasperReports Server Upgrade Guide</span>.</td>
</tr>
<tr>
<td>Version 7.5 and later<br />
From a different server</td>
<td><p>Because each server has unique randomly-generate keys, the keys of the export server are not known to your server. However, unlike the custom key scenario above, you do not have direct access to the server's keys. Before you can move export catalogs between servers, such as test and production servers, you will need to generate and share a key between the servers:</p>
<ol>
<li><p>Generate a key during the export operation on the first server.</p></li>
<li><p>Import the new key into the second server's keystore with the command-line import command.</p></li>
<li><p>Import the catalog into the second server and specify the custom key either through the UI or the command-line.</p>
<p>If you also import the key back into the originating server, both servers will share the same key. Then if you specify this custom key during import and export, catalogs can be exported from either sever and imported into the other one.</p></li>
</ol></td>
</tr>
</tbody>
</table>

In addition to the default import and export operations, this guide documents the following:

- Importing catalogs from older servers with legacy or custom keys.
- Exporting catalogs with a specific key.

For operations to set up and manipulate keys, see the JasperReports Server Security Guide:

- Specifying custom keys during import and export operations.

- Importing keys used by other servers.

- Exporting keys for use in other servers.

- Sharing custom keys between multiple servers.
