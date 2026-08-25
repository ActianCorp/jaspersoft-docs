---
title: Building JasperReports Server Source Code
description: This document describes how to build from a command-line shell in Linux or Windows. It does not address the process of building within an IDE (Integrated Development Environment) such as Eclipse or...
---

# Building JasperReports Server Source Code

!!! note

    This document describes how to build from a command-line shell in Linux or Windows. It does not address the process of building within an IDE (Integrated Development Environment) such as Eclipse or IntelliJ.

## Introduction to Buildomatic Source Build Scripts

The JasperReports Server source code comes with a set of configuration and build scripts based on Apache Ant known as the buildomatic scripts. You will find these scripts in the following directory:

\<js-src\>/jasperserver/buildomatic

The buildomatic scripts automate most aspects of configuring, building, and deploying the source code. Apache Ant is bundled into the source code distribution to simplify the setup.

## Downloading and Unpacking JasperReports Server Source Code

### Downloading the Source Archive

Download the source code package zip for the commercial version of JasperReports Server from [Jaspersoft Technical Support](https://www.jaspersoft.com/support) . The download package is

`js-jrs``_10.1.0`

\_src.zip.

For access to the site, contact technical support or your sales representative.

### Unpacking the Source Archive

Unpack the

`js-jrs``_10.1.0`

\_src.zip file to a directory location, such as `C:\` or `/home/<user>`. The resulting location is referred to as `<js-src>` in this document.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p>Windows:</p></td>
<td><p>&lt;js-src&gt; example is <span>C:\</span></p>
<p>JasperReports-Server-10.1.0</p>
-src</td>
</tr>
<tr>
<td><p>Linux:</p></td>
<td><p>&lt;js-src&gt; example is <span>/home/&lt;user&gt;/</span></p>
<p>JasperReports-Server-10.1.0</p>
-src</td>
</tr>
</tbody>
</table>

!!! note

    The source build may use paths that exceed the 260-character limit on Windows. To extract the package, **Enable NTFS long paths** (Windows 10 only) or use a third-party file archiver such as 7-Zip.

### Source Code Package Structure

After you have unpacked the zip file, the folder directory has the following structure:

| Directory or file | Description |
|----|----|
| `<js-src>/apache-ant` | Bundled version of Apache Ant build tool |
| `<js-src>/jasperserver` | JasperReports Server open source code for core functionality |
| `<js-src>/jasperserver-pro` | JasperReports Server source code for commercial functionality |
| `<js-src>/jasperserver-repo` | Dependent jar files (not readily available publicly) |
| `<js-src>/jasperserver-ui` | JasperReports Server source code for UI |

!!! note

    The repo-path variable can be set to point to the location of the `js-jrs_`

    `js-jrs``_10.1.0`

    \_repo.zip / `./repository` directory.

## Check Apache Ant

The Apache Ant tool is bundled (pre-integrated) into the source code distribution package. So you do not need to download or install Ant to run the buildomatic scripts. For example:

`cd <js-src>/jasperserver/buildomatic`

`js-ant help` or

`../js-ant help` (Linux)

If you do not use the bundled version of Apache Ant, we recommend using the 1.10.latest version.

## Configuring the Buildomatic Properties

The buildomatic scripts are found at the following location:

`<js-src>/jasperserver/buildomatic`

Use the buildomatic scripts to build the source code and configure settings for a supported application server and database. The file for configuring these settings is default_master.properties. The source distribution includes a properties file for each type of database. Add your specific settings to this file and rename it to:

default_master.properties

!!! note

    When specifying paths with Apache Ant and Java in Windows, a single forward slash (/) normally works the same as “escaped” double backlashes (\\).

### PostgreSQL

1.  Go to the buildomatic directory in the source distribution:

    ``` bash
    cd <js-src>/jasperserver/buildomatic
    ```

2.  Copy the PostgreSQL specific file to the current directory and change its name to<br>
    default_master.properties as shown below:

    |  |  |
    |----|----|
    | Windows: | `copy sample_conf\postgresql_master.properties default_master.properties` |
    | Linux: | `cp sample_conf/postgresql_master.properties default_master.properties` |

3.  Edit the new default_master.properties file and set the following properties for your local environment:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th><p>Property</p></th>
    <th><p>Examples</p></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p><code>appServerType</code></p></td>
    <td><div class="language-properties highlight"><pre><code><span class="na">appServerType</span><span class="o">=</span><span class="s">tomcat [jboss-eap-8, wildfly, skipAppServerCheck]</span></code></pre></div></td>
    </tr>
    <tr>
    <td><p><code>appServerDir</code></p></td>
    <td>appServerDir = C:\\Program Files\\Apache Software Foundation\\Tomcat 11.0 appServerDir = /home/&lt;user&gt;/apache-tomcat-11.0</td>
    </tr>
    <tr>
    <td><p><code>dbHost</code></p></td>
    <td>dbHost=localhost</td>
    </tr>
    <tr>
    <td><p><code>dbUsername</code></p></td>
    <td>dbUsername=postgres</td>
    </tr>
    <tr>
    <td><p><code>dbPassword</code></p></td>
    <td>dbPassword=postgres</td>
    </tr>
    <tr>
    <td><p><code>maven</code></p></td>
    <td><p>maven = C:\\apache-maven-3.9\\bin\\mvn.cmd</p>
    <p>maven = /home/&lt;user&gt;/apache-maven-3.9/bin/mvn</p></td>
    </tr>
    <tr>
    <td><p><code>js-path</code></p></td>
    <td><p>js-path = C:\\</p>
    <p>JasperReports-Server-10.1.0</p>
    -src\\jasperserver
    <p>js-path = /home/&lt;user&gt;/</p>
    <p>JasperReports-Server-10.1.0</p>
    -src/jasperserver</td>
    </tr>
    <tr>
    <td><p><code>js-pro-path</code></p></td>
    <td><p>js-pro-path = C:\\</p>
    <p>JasperReports-Server-10.1.0</p>
    -src\\jasperserver-pro
    <p>js-pro-path = /home/&lt;user&gt;/</p>
    <p>JasperReports-Server-10.1.0</p>
    -src/jasperserver-projs-pro-path =</td>
    </tr>
    <tr>
    <td><p><code>maven.build.type</code></p></td>
    <td><p><code>maven.build.type=repo</code></p></td>
    </tr>
    <tr>
    <td><p><code>repo-path</code></p></td>
    <td><p>repo-path = C:\\</p>
    <p>JasperReports-Server-10.1.0</p>
    \\jasperserver-repo
    <p>repo-path = /home/&lt;user&gt;/</p>
    <p>JasperReports-Server-10.1.0</p>
    -src/jasperserver-repo</td>
    </tr>
    <tr>
    <td><code>chrome.path</code></td>
    <td><p>chrome.path = C:/Program Files (x86)/Google/Chrome/Application/chrome.exe</p>
    <p>chrome.path = /usr/bin/google-chrome</p></td>
    </tr>
    </tbody>
    </table>

### MySQL

1.  Go to the buildomatic directory in the source distribution:

    ``` bash
    cd <js-src>/jasperserver/buildomatic
    ```

2.  Copy the MySQL specific file to the current directory and change its name to `default_master.properties`:

    |  |  |
    |----|----|
    | Windows: | `copy sample_conf\mysql_master.properties default_master.properties` |
    | Linux: | `cp sample_conf/mysql_master.properties default_master.properties` |

3.  Edit the new `default_master.properties` file and set the following properties to your local environment:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th><p>Property</p></th>
    <th><p>Examples</p></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p><code>appServerType</code></p></td>
    <td><div class="language-properties highlight"><pre><code><span class="na">appServerType</span><span class="o">=</span><span class="s">tomcat [jboss-eap-8, wildfly, skipAppServerCheck]</span></code></pre></div></td>
    </tr>
    <tr>
    <td><p><code>appServerDir</code></p></td>
    <td>appServerDir = C:\\Program Files\\Apache Software Foundation\\Tomcat 11.0 appServerDir = /home/&lt;user&gt;/apache-tomcat-11.0</td>
    </tr>
    <tr>
    <td><p><code>dbHost</code></p></td>
    <td><code>dbHost = localhost</code></td>
    </tr>
    <tr>
    <td><p><code>dbUsername</code></p></td>
    <td><code>dbUsername = root</code></td>
    </tr>
    <tr>
    <td><p><code>dbPassword</code></p></td>
    <td><code>dbPassword = password</code></td>
    </tr>
    <tr>
    <td><code>maven</code></td>
    <td><p>maven = C:\\apache-maven-3.9\\bin\\mvn.cmd</p>
    <p>maven = /home/&lt;user&gt;/apache-3.9/bin/mvn</p></td>
    </tr>
    <tr>
    <td><p><code>js-path</code></p></td>
    <td><p>js-path = C:\\</p>
    <p>JasperReports-Server-10.1.0</p>
    -src\\jasperserver
    <p>js-path = /home/&lt;user&gt;/</p>
    <p>JasperReports-Server-10.1.0</p>
    -src/jasperserver</td>
    </tr>
    <tr>
    <td><p><code>js-pro-path</code></p></td>
    <td><p>js-pro-path = C:\\</p>
    <p>JasperReports-Server-10.1.0</p>
    -src\\jasperserver-pro
    <p>js-pro-path = /home/&lt;user&gt;/</p>
    <p>JasperReports-Server-10.1.0</p>
    -src/jasperserver-pro</td>
    </tr>
    <tr>
    <td><p><code>maven.build.type</code></p></td>
    <td><p><code>maven.build.type=repo</code></p></td>
    </tr>
    <tr>
    <td><p><code>repo-path</code></p></td>
    <td><p>repo-path = C:\\</p>
    <p>JasperReports-Server-10.1.0</p>
    -src\\jasperserver-repo
    <p>repo-path = /home/&lt;user&gt;/</p>
    <p>JasperReports-Server-10.1.0</p>
    -src/jasperserver-repo</td>
    </tr>
    <tr>
    <td><code>chrome.path</code></td>
    <td><p>chrome.path = C:/Program Files (x86)/Google/Chrome/Application/chrome.exe</p>
    <p>chrome.path = /usr/bin/google-chrome</p></td>
    </tr>
    </tbody>
    </table>

### Additional Databases

For `default_master.properties` configurations for other databases, please see [Source Build Setup for Other Databases](setup_for_other_databases.md).

## Build Source Code

Now that you have set up your `default_master.properties` file, you can build the source code.

To build JasperReports Server

1.  Set up the `default_master.properties` file for your environment (as described above).
2.  Start the database server.
3.  Stop the application server.
4.  Run the commands shown below:

After running each Ant target in Commands for Building JasperReports Server, look for the message BUILD SUCCESSFUL.

| Commands | Description |
|----|----|
| `cd <js-src>/jasperserver/buildomatic` |  |
| `js-ant clean-config` | (Optional) Clears the `buildomatic/build_conf/default` directory. |
| `js-ant gen-config` | (Optional) Rebuilds the `buildomatic/build_conf/default` directory. |
| `js-ant add-jdbc-driver` | Used for loading the databases |
| `js-ant build-pro` | Builds the commercial source code |
| `js-ant create-load-js-db-``pro`` ` | (Optional) Creates and loads the `jasperserver` database, imports core bootstrap data |
| `js-ant deploy-webapp-``pro`` ` | (Optional) Deploys the `jasperserver` `-pro` war file to the application server |
| `js-ant deploy-jrws` | (Optional) Deploys only JasperReports Web Studio apps in the configured app path in `default_master.properties`. |

Commands for Building JasperReports Server

!!! note

    Installing JasperReports Server automatically generates encryption keys that reside on the file system. These keys are stored in a dedicated Jaspersoft keystore. Make sure that this keystore is properly secured and backed up, as described in the JasperReports Server Security Guide.

## Set Java Options

JasperReports Server needs Java memory options that are larger than the standard defaults. For information about additional Java options, see [Setting Java JVM Options](java_options_and_jrs_license.md).

### Set Increased JAVA_OPTS Settings

JasperReports Server needs greater heap settings for all functionality to operate. For testing your deployed JasperServer, set your JAVA_OPTS to the same default values described in the JasperReports Server Installation Guide. The following shows the minimum recommended settings; you may need to increase these according to your usage.

<table>
<thead>
<tr>
<th colspan="2"><p>JVM Options on Linux and Mac OSX (64 bit)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Options for all app servers</p></td>
<td><p>export JAVA_OPTS="$JAVA_OPTS -Xms2048m -Xmx4096m -Xss2m"</p></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th colspan="2"><p>JVM Options on Windows (64 bit)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Options for all app servers</p></td>
<td><p>set JAVA_OPTS=%JAVA_OPTS% -Xms2048m -Xmx4096m -Xss2m</p></td>
</tr>
</tbody>
</table>

Add these settings to your application server startup script:

|                |                                |                      |
|----------------|--------------------------------|----------------------|
| Apache Tomcat: | `<tomcat>/bin/setclasspath.sh` | (`.bat` for Windows) |
| JBoss:         | `<jboss>/bin/standalone.conf`  | (`.bat` for Windows) |

For details on setting Java memory options, please see [Setting Java JVM Options](java_options_and_jrs_license.md).

## Put jaspersoft.jrs.license in Place

JasperReports Server Commercial edition requires a license to run. An evaluation license is provided in the source code zip download package. You can use this evaluation license to get started and then replace it with one you request [Jaspersoft Technical Support](https://www.jaspersoft.com/support) or from your sales representative.

JasperReports Server looks for the license file in the home directory of the user running the application server, so copy the license to that location. You will find the license in the root of the source package:

`<js-src>/jaspersoft.jrs.license`

For more information on license configuration, please see [Configuring the JasperReports Server License File](java_options_and_jrs_license.md).

Copy `jaspersoft.jrs.license` to the appropriate folder listed in the table below.

<table>
<caption><p>License Locations</p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Operating System</p></th>
<th> </th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Linux</p></td>
<td><p><code>/opt/home/jasperserver</code> (name of the user who starts the Tomcat and mostly its jasperserver user)</p>
<p>or <code>$USER_HOME</code></p></td>
</tr>
<tr>
<td><p>Mac OSX</p></td>
<td><p>/Users/user/</p></td>
</tr>
<tr>
<td><p>Windows 7 using the bundled Tomcat</p></td>
<td><p>C:\Users\user</p></td>
</tr>
<tr>
<td><p>Windows 7 using an existing Tomcat Windows service</p></td>
<td><p>C:\</p></td>
</tr>
</tbody>
</table>

## Starting JasperReports Server

You can now start your application server. Your database should already be running.

## Logging into JasperReports Server

You can now log into JasperReports Server through a web browser:

Enter the login URL with the default port number:

`http://localhost:8080/``jasperserver`` ``-pro`` `

Log into JasperReports Server as superuser or jasperadmin:

User ID: `superuser    `Password: `superuser`

User ID: `jasperadmin `  Password: `jasperadmin`

If you are unable to log in or have other problems, see [Troubleshooting](troubleshooting.md), or the JasperReports Server Installation Guide.

## JasperReports Server Log Files

If you encounter any startup or runtime errors, you can check the application server log files. For Apache Tomcat, you will find the log file here:

`<tomcat>/logs/catalina.out`

Also check the `jasperserver.log` file. You can increase the debug output level by editing the `log4j.properties` file.

The JasperReports Server runtime log is here:

`<tomcat>/webapps//WEB-INF/logs/jasperserver.log`

The `log4j.properties` file is here:

`<tomcat>/webapps//WEB-INF/log4j.properties`
