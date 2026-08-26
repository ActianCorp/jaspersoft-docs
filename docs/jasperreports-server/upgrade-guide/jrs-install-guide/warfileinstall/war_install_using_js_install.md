---
title: Installing the WAR File Using js-install Scripts
description: "Follow this procedure to install JasperReports Server using the WAR file distribution. The js-install shell scripts, supported on Windows, Linux, and Mac, do most of the work for you."
---

# Installing the WAR File Using js-install Scripts

Follow this procedure to install JasperReports Server using the WAR file distribution. The js-install shell scripts, supported on Windows, Linux, and Mac, do most of the work for you.

Prerequisites for installing the WAR file

1.  Install a supported version of the Java Development Kit (JDK). See the TIBCO Jaspersoft Supported Platforms Datasheet document on the [Documentation section](http://community.jaspersoft.com/documentation) of the Jaspersoft Community website for a list.
2.  Create and set the `JAVA_HOME` system environment variable to point to the Java JDK location.
3.  Locate or install one of the following application servers. See the Jaspersoft Platform Support Guide for supported versions:

-   Apache Tomcat

    -   JBoss EAP or Wildfly (additional steps may be required for JBoss EAP or Wildfly. Please see [Additional Steps for Using JBoss EAP, JBoss Web Server or Wildfly](../../../installation-guide/warfileinstall/additional_steps_for_using_db2_and_j.md) ).

        1.  Locate or install the

            PostgreSQL, MySQL, Oracle, SQL Server, or DB2

            database. If you use DB2, follow the steps in [Additional Steps for Using DB2 and js-install Scripts](../../../installation-guide/warfileinstall/additional_steps_for_using_db2_and_j.md).

        !!! note

            The target database can be on a remote server. The application server should reside on the local machine.

        For an optional pre-install validation test, run `js-install`` .bat/sh test`. See [js-install Script Test Mode](../../../installation-guide/warfileinstall/war_troubleshooting_jrs.md) for more information.

        To install the WAR file using js-install scripts

        The scripts are intended for the bash shell.

        !!! note

            If installing to non-Linux Unix platforms such as IBM AIX, FreeBSD, or Solaris, the bash shell is required for using the js-install scripts.

        1.  Extract all files from

            `js-jrs``_10.1.0`

            \_bin.zip. Choose a destination, such as:

    -   On Windows: `C:\Jaspersoft`

    -   On Linux: `/home/<user>`

    -   On Mac: `/Users/<user>`

        The directory, `on Linux_bin`, appears in the file location you choose.

        1.  Copy the `<dbType>_master.properties` file for your database from `sample_conf` and paste it to `buildomatic`:

    -   Copy from: `<js-install>/buildomatic/sample_conf/`

    -   Paste to: `<js-install>/buildomatic`

For example, if your database is PostgreSQL, copy `postgresql_master.properties` to `<js-install>/buildomatic`.

1.  Rename the file that you copied to `default_master.properties`.

2.  Edit the `default_master.properties` file to add the settings for your database and application server. Sample Values for the default_master.properties File lists sample property values for each supported database.

    <table>
    <caption><p>Sample Values for the default_master.properties File</p></caption>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th><p>Database</p></th>
    <th><p>Sample Property Values</p></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>PostgreSQL</p></td>
    <td><div class="language-properties highlight"><pre><code><span class="w"> </span><span class="na">appServerType</span><span class="o">=</span><span class="s">tomcat [jboss-eap-8, wildfly, skipAppServerCheck]</span>
<span class="w">        </span>
<span class="na">appServerDir</span><span class="o">=</span><span class="s">c:</span><span class="se">\\</span><span class="s">Program Files</span><span class="se">\\</span><span class="s">Apache Software Foundation</span><span class="se">\\</span><span class="s">Tomcat 11.0</span>
<span class="w">    </span><span class="na">dbHost</span><span class="o">=</span><span class="s">localhost</span>
<span class="w">    </span><span class="na">dbUsername</span><span class="o">=</span><span class="s">postgres</span>
<span class="w">    </span><span class="na">dbPassword</span><span class="o">=</span><span class="s">postgres</span></code></pre></div></td>
    </tr>
    <tr>
    <td><p>MySQL</p></td>
    <td><div class="language-properties highlight"><pre><code><span class="na">appServerType</span><span class="o">=</span><span class="s">tomcat [jboss-eap-8, wildfly, skipAppServerCheck]</span>
<span class="w">        </span>
<span class="na">appServerDir</span><span class="o">=</span><span class="s">c:</span><span class="se">\\</span><span class="s">Program Files</span><span class="se">\\</span><span class="s">Apache Software Foundation</span><span class="se">\\</span><span class="s">Tomcat 11.0</span>
<span class="w">    </span><span class="na">dbUsername</span><span class="o">=</span><span class="s">root</span>
<span class="w">    </span><span class="na">dbPassword</span><span class="o">=</span><span class="s">password</span>
<span class="w">    </span><span class="na">dbHost</span><span class="o">=</span><span class="s">localhost</span></code></pre></div></td>
    </tr>
    <tr>
    <td><p>Standard Oracle options</p></td>
    <td><div class="language-properties highlight"><pre><code><span class="na">appServerType</span><span class="o">=</span><span class="s">tomcat [jboss-eap-8, wildfly, skipAppServerCheck]</span>
<span class="w">        </span>
<span class="na">appServerDir</span><span class="o">=</span><span class="s">c:</span><span class="se">\\</span><span class="s">Program Files</span><span class="se">\\</span><span class="s">Apache Software Foundation</span><span class="se">\\</span><span class="s">Tomcat 11.0</span>
<span class="w">    </span><span class="na">dbUsername</span><span class="o">=</span><span class="s">jasperserver</span>
<span class="w">    </span><span class="na">dbPassword</span><span class="o">=</span><span class="s">password</span>
<span class="w">    </span><span class="na">sysUsername</span><span class="o">=</span><span class="s">system</span>
<span class="w">    </span><span class="na">sysPassword</span><span class="o">=</span><span class="s">password        </span>
<span class="w">    </span><span class="na">dbHost</span><span class="o">=</span><span class="s">hostname</span>
<span class="w">    </span><span class="na">dbVersion</span><span class="o">=</span><span class="s">oracleDbVersion (for example, 12, 19c, 21c, 23ai, 26ai and so on)</span></code></pre></div></td>
    </tr>
    <tr>
    <td>Additional options for Oracle CDB with common users</td>
    <td><p>If you are using Oracle CDB and you want to use a common Jaspersoft user, then use the settings for Oracle with the following changes:</p>
    <div class="language-properties highlight"><pre><code><span class="na">dbUsername</span><span class="o">=</span><span class="s">c##jasperserver</span>
<span class="w">    </span><span class="na">sid</span><span class="o">=</span><span class="s">orclcdb</span></code></pre></div>
    <p>If you are using sample databases:</p>
    <div class="language-properties highlight"><pre><code><span class="na">foodmart.dbUsername</span><span class="o">=</span><span class="s">c##foodmart</span>
<span class="w">    </span><span class="na">sugarcrm.dbUsername</span><span class="o">=</span><span class="s">c##sugarcrm</span></code></pre></div></td>
    </tr>
    <tr>
    <td><p>DB2</p></td>
    <td><div class="language-properties highlight"><pre><code><span class="w"> </span><span class="na">appServerType</span><span class="o">=</span><span class="s">tomcat [jboss-eap-8, wildfly, skipAppServerCheck]</span>
<span class="w">        </span>
<span class="na">appServerDir</span><span class="o">=</span><span class="s">c:</span><span class="se">\\</span><span class="s">Program Files</span><span class="se">\\</span><span class="s">Apache Software Foundation</span><span class="se">\\</span><span class="s">Tomcat 11.0</span>
<span class="w">    </span><span class="na">dbUsername</span><span class="o">=</span><span class="s">db2inst1</span>
<span class="w">    </span><span class="na">dbPassword</span><span class="o">=</span><span class="s">password</span>
<span class="w">    </span><span class="na">dbHost</span><span class="o">=</span><span class="s">localhost</span></code></pre></div>
    <p>If you use DB2, follow the steps in <a href="../../../installation-guide/warfileinstall/additional_steps_for_using_db2_and_j.md">Additional Steps for Using DB2 and js-install Scripts</a></p></td>
    </tr>
    <tr>
    <td><p>SQL Server</p></td>
    <td><div class="language-properties highlight"><pre><code><span class="na">appServerType</span><span class="o">=</span><span class="s">tomcat [jboss-eap-8, wildfly, skipAppServerCheck]</span>
<span class="w">        </span>
<span class="na">appServerDir</span><span class="o">=</span><span class="s">c:</span><span class="se">\\</span><span class="s">Program Files</span><span class="se">\\</span><span class="s">Apache Software Foundation</span><span class="se">\\</span><span class="s">Tomcat 11.0</span>
<span class="w">    </span><span class="na">dbUsername</span><span class="o">=</span><span class="s">sa</span>
<span class="w">    </span><span class="na">dbPassword</span><span class="o">=</span><span class="s">sa</span>
<span class="w">    </span>
<span class="na">dbHost</span><span class="o">=</span><span class="s">localhost</span></code></pre></div></td>
    </tr>
    <tr>
    <td>Additional options for all databases</td>
    <td><p>(Optional) <code>jrws.deploy.webapps=true</code></p>
    <p>(Optional) <code>jrws.repo.url=http://localhost:8080/repo</code></p>
    <p>(Optional) <code>jrws.jrio.url=http://localhost:8080/jrio</code></p>
    <p>By default, JasperReports Web Studio applications are installed into the same application server as JasperReports Server, as configured in the <code>appServerDir</code> property.</p>
    <p>If you do not want to deploy the JasperReports Web Studio applications, set</p>
    <p><code>jrws.deploy.webapps=false</code>.</p>
    <p>In that case the integrated JasperReports Web Studio stops working.</p>
    <p>From JasperReports Server, you can still view the <strong>Open in Editor</strong> option. This option must be disabled from the context menu.</p>
    <p>For steps on how to disable the <strong>Open in Editor</strong> option, refer to the JasperReports Server <em>Administrator Guide</em>.</p>
    <p>If you have already deployed JasperReports Web Studio on another server you can skip deploying it with JasperReports Server and just point to that remote applications by setting:</p>
    <p><code>jrws.deploy.webapps=false</code></p>
    <p><code>jrws.repo.url=http://&lt;jasper-reports-webstudio-host&gt;:8080/repo</code></p>
    <p><code>jrws.jrio.url=http://&lt;jasper-reports-webstudio-host&gt;:8080/jrio</code></p></td>
    </tr>
    </tbody>
    </table>

    For the Split installation, configure the additional settings in the `default_master.properties` file as described in [Additional Buildomatic Configuration for Split Installation Upgrade](../introduction/installation_types.md).

    !!! note

        When the property `appServerType` is set to `skipAppServerCheck`, buildomatic skips any application server validation.

        Backslashes in paths must be doubled in properties files, for example:<br>
        appServerDir=C:\\\\Apache Software Foundation\\\\Tomcat 11.0.

        <span id="Oracle_dbUsername"></span>The `dbUsername` must be the same as the Oracle user name. In addition, buildomatic does with the “sys as sysdba” syntax.

        For Oracle without CDB with common users, do not use the `c##jasperserver dbUsername`. Use the standard `jasperserver dbUsername` instead.

    !!! note

        On Linux, if Tomcat is installed using apt-get, yum, or rpm, see [Tomcat Installed Using apt-get/yum](../../../installation-guide/troubleshooting/application_server_related_problems.md).

3.  In case DB2, SQL Server or Oracle databases are used you must install the required JDBC driver. For steps to install, see [Installing Database Vendor JDBC Drivers](../../../installation-guide/additional/jdbc-driver.md).

4.  Run the `js-install` script:

    1.  Start your database server.

    2.  Stop your application server.

    3.  Open Command Prompt as Administrator on Windows or open a terminal window on Linux and Mac OSX.

    4.  Run the `js-install` script for the version and files that you want, as shown in the following table:

        <table>
        <colgroup>
        <col style="width: 50%" />
        <col style="width: 50%" />
        </colgroup>
        <thead>
        <tr>
        <th><p>Commands</p></th>
        <th><p>Description</p></th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td><p><code>cd &lt;js-install&gt;/buildomatic</code></p></td>
        <td></td>
        </tr>
        <tr>
        <td><p><code>js-install</code><code> .bat </code>(Windows)</p>
        <p><code>./</code><code>js-install</code><code> .sh </code>(Linux and Mac OSX)</p></td>
        <td><p>Installs JasperReports Server and JasperReports Web Studio, sample data, and sample databases (foodmart and sugarcrm)</p></td>
        </tr>
        <tr>
        <td><p><code>js-install</code><code> .bat minimal </code>(Windows)</p>
        <p><code>./</code><code>js-install</code><code> .sh minimal </code>(Linux and Mac OSX)</p></td>
        <td><p>Installs JasperReports Server and JasperReports Web Studio, but not the sample data and sample databases</p></td>
        </tr>
        </tbody>
        </table>

        If you encounter errors during the `js-install` script execution, see [Error Running js-install Scripts (.bat/sh)](../../../installation-guide/warfileinstall/war_troubleshooting_jrs.md).

5.  Set Java JVM Options (required), as described in [Setting JVM Options for Application Servers](../../../installation-guide/additional/setting_jvm_options_for_application_.md).

6.  Set up the license (required) as described in [Setting Up the JasperReports Server License](../../../installation-guide/additional/setting_up_the_jasperreports_server_.md).

!!! note

    To view the output log, look in: `<js-install>/buildomatic/logs/``js-install`` -<date>.log`

!!! note

    Installing JasperReports Server automatically generates encryption keys that reside on the file system. These keys are stored in a dedicated Jaspersoft keystore. Make sure that this keystore is properly secured and backed up, as described in the JasperReports Server Security Guide.

# Installing Chrome/Chromium

You need to install and configure Chrome/Chromium to export the reports and dashboards to PDF and other output formats.

For information about configuring Chrome/Chromium in JasperReports Server, see the *JasperReports Server Administrator Guide*.
