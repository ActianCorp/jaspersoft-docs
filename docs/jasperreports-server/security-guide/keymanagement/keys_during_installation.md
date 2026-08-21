---
title: Managing Keys During Installation
description: "As of JasperReports Server 7.5, the use of keys in a single keystore has been standardized, and all the necessary files and configuration settings are created and initialized during the installation."
---

# Managing Keys During Installation

As of JasperReports Server 7.5, the use of keys in a single keystore has been standardized, and all the necessary files and configuration settings are created and initialized during the installation.

The following files are created during installation, where \$USER is the user who installed the server:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Filename</th>
<th>Default<br />
Location</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>.jrsks</code></td>
<td>$USER/home</td>
<td>The encrypted keystore file containing the actual keys. Only the user who performs the installation can access and modify this file using the keytool utility.</td>
</tr>
</tbody>
<tbody>
<tr>
<td><code>.jrsksp</code></td>
<td>$USER/home</td>
<td>The keystore properties file that defines the keys in the keystore. This file is encoded so that it does not appear in plain text, and permissions are set so that only the user who performs the installation can modify it.</td>
</tr>
</tbody>
<tbody>
<tr>
<td><code>keystore.init</code><br />
<code>.properties</code></td>
<td>buildomatic and<br />
WEB-INF/classes</td>
<td><p>Contains the path to the keystore files above, so that JasperReports Server and its app server can use them. This file should always point to the same keystore that was created at installation. This file is copied in two locations so that when other system users (for example tomcatuser) run the buildomatic commands, they can detect the existing keystore and not create a new one.</p>
<p>If this file is missing and the buildomatic scripts do not detect the keystore, they prompt the user to create a new one. If a new keystore is created twice for a server, the scripts may overwrite database passwords and the server will no longer be able to access its internal database. Be sure to never create more than one keystore for the server.</p></td>
</tr>
</tbody>
</table>

The server uses different cryptographic keys for the following tasks:

- Encrypting user passwords and secure files in the internal database.
- Encrypting and decrypting passwords in import and export catalogs. The server may also import keys to decrypt catalogs from other servers.
- Encrypting passwords and sensitive data that appear in configuration files.
- Encrypting log contents in log collector output and diagnostic data.
- Encrypting HTTP parameters with a static key (now deprecated).

## Keys During Upgrade

Because key management was introduced recently in JasperReports Server, upgrade procedures must also deal with upgrading keys so they are unified in the keystore. For more details, see the JasperReports Server Upgrade Guide.

One important detail is that the keys and keystore are associated with the user that originally installed the server. Therefore, you must do the following for the upgrade to recover your encrypted repository contents:

- Back up your original keystore by copying the `.jrsks` and `.jrsksp` files to a safe location. Remember that these files contain sensitive keys for your data, so they must always be transmitted and stored securely.
- Run the upgrade script as the same user that was originally used to install the server. Then the keystore is available to the script in the user's home directory.
- Alternatively, copy the `.jrsks` and `.jrsksp` files to the home directory of the user that runs the upgrade script.

When the server's original keystore is available to the user running the upgrade script, the keys it contains are copied and preserved in the new keystore (`.jrsks`) with the aliases `deprecatedPasswordEncSecret` and `deprecatedImportExportEncSecret`.

When the upgrade script does not detect any keystore in the user's home directory, the script prompts you to create a new keystore. DO NOT create a new keystore if you wish to recover the contents of your old server through the upgrade process. If you create a new keystore during the upgrade procedure, you need to recover your server's repository data (all users and all reports) from a backup in a separate import. You will also need a backup of your old keystore to import the old keys. You need both backups to have been created and saved previously, they are not created by the upgrade process. In general, if the upgrade script prompts you to create a new keystore, it is recommended to quit the script and rerun it as a user with access to the original keystore, as describe above.

## Making Backups

During installation, the keys in the keystore are used to protect sensitive data by encrypting configuration files and the server’s internal repository database. Once the server is installed, the keys are used during normal operation to encrypt or decrypt information as needed. For example, when anyone logs into the server, their password is encrypted with the corresponding key and compared to the encrypted password stored in their user profile. Or when importing a report from an export catalog, the catalog must be decrypted to access the contents.

Without the keystore files, the specific files created with random keys during the installation, your instance of the server cannot function and all the information it contains becomes inaccessible. This is why having backups of the keystore files must be a part of your larger backup and recovery plans for your data. Businesses usually have IT policies for making backups, and the keystore files for your JasperReports Server instance should be included in your policies and procedures.

Backups of the keystore files are digital copies of the files stored in a secure location, usually determined by your IT policies. Use the following guidelines when creating and implementing your keystore backup policies:

- Copy both the `.jrsks` and `.jrsksp` files together, keeping the `.jrsksp` file encoded as it is.
- The keystore files should be copied only by the system user who installed the server.
- Restrict access to the backup keystore files as you would the originals on production servers. This includes digital access security for online backups and physical security for offline backups. The files are literally the keys to the application and should be guarded as such.
- If you need to restore from the backups, the system user who installed the server should copy the files to their home directory (\$USER/\$HOME). This is the location where the server expects to find them at run-time.
