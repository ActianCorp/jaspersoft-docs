---
title: Source Build Setup for Other Databases
description: "You can use the example settings below for Oracle, SQL Server, and DB2."
---

# Source Build Setup for Other Databases

You can use the example settings below for Oracle, SQL Server, and DB2.

## Get Your JDBC Driver

You can choose to use the provided JDBC driver or download a native JDBC Driver.

## Download a JDBC Driver

You can download a JDBC driver appropriate for your database. In this case, additional configurations are required. You can download a JDBC driver from one of these vendor sites:

- <http://www.oracle.com/technetwork/indexes/downloads> (Oracle)
- <https://www.microsoft.com/en-us/download/details.aspx?id=56615> (SQL Server)
- <http://www-01.ibm.com/software/data/db2/linux-unix-windows/downloads.html> (DB2)

Copy the downloaded JDBC jar to the following location:

- `<js-src>/buildomatic/conf_source/db/<dbType>/jdbc`

For example, for SQL Server the driver would go here:

- `<js-src>/buildomatic/conf_source/db/sqlserver/jdbc`

## Set Up Your Database

### Oracle

1.  Go to the buildomatic directory in the source distribution:

    `cd <js-src>/jasperserver/buildomatic`

2.  Copy the Oracle specific file to the current directory and change its name to `default_master.properties`:
    |  |  |
    |----|----|
    | Windows: | `copy sample_conf\oracle_master.properties default_master.properties` |
    | Linux: | `cp sample_conf/oracle_master.properties default_master.properties` |

3.  Open the new `default_master.properties` file for editing.

4.  Set the following properties for your local environment:
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
    <td><pre class="properties"><code>appServerType=tomcat [jboss-eap-8, wildfly, skipAppServerCheck]</code></pre></td>
    </tr>
    <tr>
    <td><p><code>appServerDir</code></p></td>
    <td><p>appServerDir = C:\\Program Files\\Apache Software Foundation\\Tomcat 10.0</p>
    <p>appServerDir = /home/&lt;user&gt;/apache-tomcat-10.0</p></td>
    </tr>
    <tr>
    <td><p><code>sysUsername</code></p></td>
    <td>sysUsername=system</td>
    </tr>
    <tr>
    <td><p><code>sysPassword</code></p></td>
    <td>sysPassword=password</td>
    </tr>
    <tr>
    <td><p><code>dbUsername</code></p></td>
    <td>dbUsername=jasperserver</td>
    </tr>
    <tr>
    <td><p><code>dbPassword</code></p></td>
    <td>dbPassword=password</td>
    </tr>
    <tr>
    <td><p><code>dbHost</code></p></td>
    <td><code>dbHost=localhost</code></td>
    </tr>
    <tr>
    <td><code>maven</code></td>
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
    -src/jasperserver-pro</td>
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

5.  Save the default_master.properties file.

### SQL Server

1.  Go to the buildomatic directory in the source distribution:

    `cd <js-src>/jasperserver/buildomatic`

2.  Copy the SQL Server specific file to the current directory and change its name to `default_master.properties`:
    |  |  |
    |----|----|
    | Windows: | `copy sample_conf\sqlserver_master.properties default_master.properties` |
    | Linux: | `cp sample_conf/sqlserver_master.properties default_master.properties` |

3.  Edit the new `default_master.properties` file and set the following properties for your local environment:
    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th><p>Property</p></th>
    <th>Examples</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p><code>appServerType</code></p></td>
    <td><pre class="properties"><code>appServerType=tomcat [jboss-eap-8, wildfly, skipAppServerCheck]</code></pre></td>
    </tr>
    <tr>
    <td><p><code>appServerDir</code></p></td>
    <td>appServerDir = C:\\Program Files\\Apache Software Foundation\\Tomcat 10.0appServerDir = /home/&lt;user&gt;/apache-tomcat-10.0</td>
    </tr>
    <tr>
    <td><p><code>dbUsername</code></p></td>
    <td><code>dbUsername=sa</code></td>
    </tr>
    <tr>
    <td><p><code>dbPassword</code></p></td>
    <td><code>dbPassword=sa</code></td>
    </tr>
    <tr>
    <td><p><code>dbHost</code></p></td>
    <td><code>dbHost=localhost</code></td>
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
    <td><p><code>repo-path</code></p></td>
    <td><p>repo-path = C:\\</p>
    <p>JasperReports-Server-10.1.0</p>
    -src\jasperserver-repo
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

4.  Save the default_master.properties file.

### DB2

1.  Go to the buildomatic directory in the source distribution:

    `cd <js-src>/jasperserver/buildomatic`

2.  Copy the DB2 specific file to the current directory and change its name to `default_master.properties`:
    |  |  |
    |----|----|
    | Windows: | `copy sample_conf\db2_master.properties default_master.properties` |
    | Linux: | `cp sample_conf/db2_master.properties ./default_master.properties` |

3.  Edit the new `default_master.properties` file and set the following properties for your local environment:
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
    <td><pre class="properties"><code>appServerType=tomcat [jboss-eap-8, wildfly, skipAppServerCheck]</code></pre></td>
    </tr>
    <tr>
    <td><p><code>appServerDir</code></p></td>
    <td>appServerDir = C:\\Program Files\\Apache Software Foundation\\Tomcat 10.0appServerDir = /home/&lt;user&gt;/apache-tomcat-10.0</td>
    </tr>
    <tr>
    <td><p><code>dbUsername</code></p></td>
    <td><code>dbUsername=db2admin</code></td>
    </tr>
    <tr>
    <td><p><code>dbPassword</code></p></td>
    <td><code>dbPassword=password</code></td>
    </tr>
    <tr>
    <td><p><code>dbHost</code></p></td>
    <td><p><code>dbHost=localhost</code></p></td>
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

4.  Add the following additional properties, setting the correct values for your installation. For example:

    ``` properties
    db2.driverType=4
    db2.fullyMaterializeLobData=true
    db2.fullyMaterializeInputStreams=true
    db2.progressiveStreaming=2
    db2.progressiveLocators=2
    dbPort=50000
    js.dbName=JSPRSRVR
    sugarcrm.dbName=SUGARCRM
    foodmart.dbName=FOODMART
    ```

5.  Save the default_master.properties file.

!!! note

    For DB2, the database must be created manually, because it is not possible to use a JDBC call to automatically create a database on DB2.
