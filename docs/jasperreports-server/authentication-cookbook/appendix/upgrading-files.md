---
title: Migrating External Authentication Sample Files
description: "If you have implemented external authentication using one of the sample-applicationContext-<customName>.xml files in the <js‑install>/samples/externalAuth-sample-config directory, do the following to..."
---

# Appendix 1 Migrating External Authentication Sample Files

If you have implemented external authentication using one of the sample-applicationContext-\<customName\>.xml files in the \<js‑install\>/samples/externalAuth-sample-config directory, do the following to migrate your changes to another version of JasperReports Server:

1.  Before upgrading, back up your applicationContext-\<customName\>.xml file (for example, applicationContext-externalAuth-LDAP.xml), located in the \<js-install-OLD\>/WEB-INF directory of your previous version of JasperReports Server.

2.  Update your server installation to the new version of JasperReports Server, as described in the JasperReports Server Upgrade Guide. These instructions refer to the installation directory as \<js‑install-NEW\>.

3.  In the new installation, locate the sample file that corresponds to the file you implemented previously. For example, if you implemented applicationContext-externalAuth-LDAP.xml, locate \<js‑install-NEW\>/samples/externalAuth-sample-config/sample-applicationContext-externalAuth-LDAP.xml.

4.  Rename the NEW JasperReports Server sample file to remove the sample- prefix. For example, rename sample-applicationContext-externalAuth-LDAP.xml to applicationContext-externalAuth-LDAP.xml.

5.  Configure the properties in the new sample file to match the properties in your existing sample file. To do this:

    1.  Locate each bean you modified in the previous version.
    2.  Find the same bean in the JasperReports Server NEW sample.
    3.  Copy or re-enter the properties you need for your server, taking care not to copy over class names or class packages.

    !!! warning

        Although the bean names are usually the same in the JasperReports Server sample files, the name and package of the class in bean definitions may have changed. Make sure not to overwrite the new names with the old ones.

6.  Save the NEW JasperReports Server sample file.

7.  Place the modified file in the \<js-install-NEW\>/WEB-INF directory.
