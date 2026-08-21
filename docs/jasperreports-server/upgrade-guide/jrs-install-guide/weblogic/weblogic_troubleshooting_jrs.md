---
title: Troubleshooting Your JasperReports Server Configuration
description: "If you have problems running the buildomatic scripts that set up the database, set up the database manually. For more information, see Setting JVM Options for Application Servers."
---

# Troubleshooting Your JasperReports Server Configuration

If you have problems running the buildomatic scripts that set up the database, set up the database manually. For more information, see [Setting JVM Options for Application Servers](../../../installation-guide/additional/setting_jvm_options_for_application_.md).

## Startup Problems

Problems starting a new JasperReports Server instance are usually errors in the database or application server configuration files. To resolve these errors, see [Troubleshooting](../../../installation-guide/troubleshooting/troubleshooting.md).

## Error Running Report

If you have trouble running reports in your new JasperReports Server instance, see [Error Running a Report](../../../installation-guide/troubleshooting/database_related_problems.md).

## Managing Keystore Files

When you install JasperReports Server recent version on a machine in addition to versions 7.2.x and 7.5.x, the new installation or one of the previous instances may not function properly. This is caused by permissions on the keystore files needing to be different in recent releases, and differences in file contents. This issue affects only version 7.2.x and higher. Earlier versions are not affected. To resolve this issue, you need to change the `.ksp` path.

To change the .ksp path for deploying JasperReports Server war file

!!! note

    Before making the changes, you must back up the `.jrsksp` and `.jrsks` files to a secure location. And make sure all backups are readable only by admin users.

1.  Decode the `.jrsksp` file using Base64 Table 1 of RFC 2045, url unsafe, and padded. For example:<br>
    **Linux:** `cat.jrsksp | openssl base64 -d > <temp_file>`<br>
    **Windows**: `certutil -decode .jrsksp temp.jrsksp`
2.  Edit the `.jrsksp` file and add the `ksPath` property with the path to the `.jrsks` file in the current folder, for example:<br>
    **Linux:**` ksPath=~/jrs800/.jrsks/`<br>
    **Windows**: `ksPath=$HOME\\jrs800\\.jrsks`
3.  Encrypt the `temp.jrsksp` file back to `.jrsksp`.
4.  Re-encode the `.jrsksp` file with the same Base64 settings, for example:

- **Linux:** `base64 .jrsksp > ./temp.jrsksp`<br>
  `mv temp.jrsksp .jrsksp`

  <div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>mv is not required, but you should make sure that the original .jrsksp file does not exist (backed up). The command for this is: <code>base64 /path/to/file &gt; .jrsksp</code>. <br>For example: <code>./temp.jrsksp &gt; .jrsksp</code></p>
  </div>

- **Windows:** `certutil a- encode temp.jrsksp tmp.b64 && findstr /v /c:tmp.b64 .jrsksp`<br>

1.  Locate the `buildomatic/keystore.init.properties` server configuration file and edit it to modify the ks and ksp properties:<br>
    **Linux:** `ks=~/jrs800/` `ksp=~/jrs800/`<br>
    **Windows:** `ks=$HOME\\jrs800\\` `ksp=$HOME\\jrs800\\`
2.  Use the modified `buildomatic/keystore.init.properties` file to overwrite the same file in the following locations (depending on the release):<br>
    <br>
    `buildomatic/conf_source/iePro/keystore.init.properties`<br>
    `buildomatic/build_conf/default/webapp/WEB-INF/classes/keystore.init.properties`<br>
    `apache-tomcat/webapps/jasperserver-pro/WEB-INF/classes/keystore.init.properties`
3.  Restart the service.
