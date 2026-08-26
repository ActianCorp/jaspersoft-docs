---
title: Migrating External Authentication Sample Files
description: "If you have implemented external authentication using one of the sample-applicationContext-&lt;customName&gt;.xml files in the &lt;js‑install&gt;/samples/externalAuth-sample-config directory, do the..."
---

# Appendix 1 Migrating External Authentication Sample Files

If you have implemented external authentication using one of the sample-applicationContext-&lt;customName&gt;.xml files in the &lt;js‑install&gt;/samples/externalAuth-sample-config directory, do the following to migrate your changes to another version of JasperReports Server:

1.  Before upgrading, back up your applicationContext-&lt;customName&gt;.xml file (for example, applicationContext-externalAuth-LDAP.xml), located in the &lt;js-install-OLD&gt;/WEB-INF directory of your previous version of JasperReports Server.

2.  Update your server installation to the new version of JasperReports Server, as described in the JasperReports Server Upgrade Guide. These instructions refer to the installation directory as &lt;js‑install-NEW&gt;.

3.  In the new installation, locate the sample file that corresponds to the file you implemented previously. For example, if you implemented applicationContext-externalAuth-LDAP.xml, locate &lt;js‑install-NEW&gt;/samples/externalAuth-sample-config/sample-applicationContext-externalAuth-LDAP.xml.

4.  Rename the NEW JasperReports Server sample file to remove the sample- prefix. For example, rename sample-applicationContext-externalAuth-LDAP.xml to applicationContext-externalAuth-LDAP.xml.

5.  Configure the properties in the new sample file to match the properties in your existing sample file. To do this:

    1.  Locate each bean you modified in the previous version.

    2.  Find the same bean in the JasperReports Server NEW sample.

    3.  Copy or re-enter the properties you need for your server, taking care not to copy over class names or class packages.

        !!! warning

            Although the bean names are usually the same in the JasperReports Server sample files, the name and package of the class in bean definitions may have changed. Make sure not to overwrite the new names with the old ones.

    4.  Save the NEW JasperReports Server sample file.

    5.  Place the modified file in the &lt;js-install-NEW&gt;/WEB-INF directory.
