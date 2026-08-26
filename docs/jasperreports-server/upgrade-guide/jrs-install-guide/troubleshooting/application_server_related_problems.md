---
title: Application Server-related Problems
description: "These steps might solve problems related to the release of memory or to container tag pooling:"
---

# Application Server-related Problems

## Memory Issues Running Under Tomcat

These steps might solve problems related to the release of memory or to container tag pooling:

1.  Set the following parameter in the global `$CATALINA_BASE/conf/web.xml`:

    `enablepooling = false`

2.  Restart Tomcat.

## Java Out of Memory Error

If you encounter a Java out of memory error, try increasing your Java heap size setting. See [Setting JVM Options for Application Servers](../../../installation-guide/additional/setting_jvm_options_for_application_.md). As a minimum, add `-Xms2048m -Xmx4096m` to your `JAVA_OPTS` setting. You may need to increase this setting according to your usage.

This Java option is set within the application server, so you must restart your application server.

## Configuration File Locations

You find JasperReports Server configuration properties specific to your application server in the following files.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p>Tomcat:</p></td>
<td><p><code>&lt;tomcat&gt;/webapps/</code><code>jasperserver</code><code> </code><code>-pro</code><code> /META-INF/context.xml</code></p>
<p><code>&lt;tomcat&gt;/webapps/</code><code>jasperserver</code><code> </code><code>-pro</code><code> /WEB-INF/classes/hibernate.properties</code></p>
<p><code>&lt;tomcat&gt;/apache-tomcat/webapps/</code><code>jasperserver</code><code> </code><code>-pro</code><code> /WEB-INF/web.xml</code>  (JNDI config)</p>
<p><code>&lt;tomcat&gt;/apache-tomcat/config/Catalina/localhost/</code><code>jasperserver</code><code> </code><code>-pro</code><code> .xml </code> (delete: see below)</p></td>
</tr>
<tr>
<td><p>JBoss:</p></td>
<td><p><code>&lt;jboss&gt;/standalone/deployments/</code><code>jasperserver</code><code> </code><code>-pro</code><code> .war/WEB-INF/js-jboss7-ds.xml</code></p>
<p><code>&lt;jboss&gt;/standalone/deployments/</code><code>jasperserver</code><code> </code><code>-pro</code><code> .war/WEB-INF/classes/hibernate.properties</code></p>
<p><code>&lt;jboss&gt;/standalone/deployments/</code><code>jasperserver</code><code> </code><code>-pro</code><code> .war/WEB-INF/web.xml</code></p>
<p><code>&lt;jboss&gt;/standalone/deployments/</code><code>jasperserver</code><code> </code><code>-pro</code><code> .war/WEB-INF/jboss-web.xml</code></p></td>
</tr>
</tbody>
</table>

## Tomcat Installed Using apt-get/yum

### Setting CATALINA_HOME

If you are installing JasperReports Server to an instance of Tomcat that was installed using a package manager like apt-get, yum, or rpm, you can use the `CATALINA_HOME` and `CATALINA_BASE` properties found in your `default_master.properties` file.

Go to the section of the `default_master.properties` that looks like this:

``` bash
# Tomcat app server root dir
appServerDir = C:\\Program Files\\Apache Software Foundation\\Tomcat 11.0
# appServerDir = /home/devuser/apache-tomcat-11.0
# if linux package managed tomcat instance, set two properties below
# CATALINA_HOME = /usr/share/tomcat9
# CATALINA_BASE = /var/lib/tomcat9
```

And change which lines are commented so it looks like this:

``` bash
# Tomcat app server root dir
# appServerDir = C:\\Program Files\\Apache Software Foundation\\Tomcat 11.0
# appServerDir = /home/devuser/apache-tomcat-11.0
# if linux package managed tomcat instance, set two properties below
CATALINA_HOME = /usr/share/tomcat9
CATALINA_BASE = /var/lib/tomcat9
```

Note that you must set both `CATALINA_HOME` and `CATALINA_BASE`.

### Database Driver Location

After installing JasperReports Server, make sure that there is a copy of the database driver file in the `/usr/share/tomcat9/webapps/jasperserver``-pro`` /WEB-INF/lib` directory. If it is not there, copy the driver to this location. For example, for PostgreSQL, you can copy the driver from the<br>
`<js-install>/buildomatic/conf_source/db/postgresql/jdbc directory`.

## JBoss Modifications

### JBoss 7.2.0 Startup JDBC Version Error

The installation with JBoss EAP 7.2.0 may fail with the following error: "Detected Elasticsearch JDBC jar but cannot retrieve its version." In this case, you can remove the JAR file from the JasperReports Server WAR file so that the installation and startup can proceed.

1.  Edit the WAR file with the following command on Linux:

    `zip -d jasperserver-pro.war WEB-INF/lib/x-pack-sql-jdbc-7.6.0.jar`

    You can verify that the JAR file has been removed with the following Linux command:

    `jar -tf jasperserver-pro.war | grep x-pack*`

2.  Stop the JBoss app server.

3.  Delete the jasperserver-pro.war objects in the &lt;jboss-eap-7.2&gt;/standalone/deployments directory.

4.  Switch to the JRS buildomatic directory and redeploy the JRS war file:

    `./js-ant deploy-webapp-pro`

5.  Restart the JBoss app server.

### JBoss 7 Startup Timeout Error

JBoss 7 has a default startup time period. If your JBoss 7 takes longer than 60 seconds to start or deploy, you may receive the following error:

`“(DeploymentScanner-threads - 1) Did not receive a response to the deployment operation within the allowed timeout period [60 seconds]. Check the server configuration file and the server logs to find more about the status of the deployment”.`

To fix this, you need to increase your `deployment-timeout` setting as follows:

1.  Change to the JBoss standalone configuration directory.

    `cd <jboss>/standalone/configuration`

2.  Open the `standalone.xml` file.

3.  Look for the `<subsystem xmlns=`"`urn:jboss:domain:deployment-scanner:1.1`"`>` element, for example:

    `<subsystem xmlns="urn:jboss:domain:deployment-scanner:1.1">`

    `<deployment-scanner path="deployments" relative-to="jboss.server.base.dir" scan-interval="5000"/>`

    `</subsystem>`

4.  Edit this to add or set the attribute `deployment-timeout` to the preferred time in seconds, for example:

    `<subsystem xmlns="urn:jboss:domain:deployment-scanner:1.1">`

    `<deployment-scanner path="deployments" relative-to="jboss.server.base.dir" scan-interval="5000" `deployment-timeout=`"`600`"/>`

    `</subsystem>`

5.  Save the file.

On server restart, your system has the specified time to start up.

### Using a Non-default JBoss Profile

When you set up the installation in the `JasperReports-server-pro-8.0.0-bin\buildomatic` folder, the `build_conf` folder will not be created. It is created when you run the `js-install` script. If JBoss is your application server and you are using a profile other than the default, then you need to set the `jboss7.profile` property before running the `js-install` script in [Installing the WAR File Using js-install Scripts](../../../installation-guide/warfileinstall/war_install_using_js_install.md):

1.  Open the file `jasperreports-server-pro-8.0.0-bin/buildomatic/conf_source/templates/app.srv.properties`.
2.  Change the profile name as follows:<br>
    `jboss 7 profile`<br>
    `jboss7.profile = <profile name>`

### Using JBoss with Non-Latin Characters

If JBoss is your application server and your organization is created with non-Latin characters, then you need to edit the `standalone.xml` configuration file.

1.  Edit `<jboss-home>/standalone/configuration/standalone.xml`
2.  Add a new `<system-properties>` tag after the `<extensions>` tag, as shown in the following example.<br>

``` xml
<extensions>
......
</extensions>
<system-properties>
<property name="org.apache.catalina.connector.URI_ENCODING" value="UTF-8"/>
<property name="org.apache.catalina.connector.USE_BODY_ENCODING_FOR_QUERY_STRING" valuee="true"/>
</system-properties>
```

### Maximum Post Size in Wildfly

If you are upgrading or importing on some versions of Wildfly and your repository or other import file is large, the import may fail and the connection may be reset. In this case, you may need to set `max-post-size`. To do this, open the file `<wildfly-home>standalone/configuration/standalone.xml` and add or change the `max-post-size` attribute of the `http-listener` property, for example:

``` xml
<http-listener name="default" socket-binding="http" max-header-size="974247881"
     max-post-size="974247881"/>
```

## WebSphere Modifications

### Page Not Found Error on Login

You may see this error during a WebSphere installation when a user attempts to log into JasperReports Server. After typing in a correct user ID and password, the user sees an error page: `Page cannot be found, HTTP 404`

Some WebSphere versions or fix packs have modified code that processes web server filters incorrectly. Components with the `/*` URL pattern get affected by this. JasperReports Server uses the Spring framework for authentication and it is mapped using a filter chain with the `/*` URL pattern. You need to set a special property that WebSphere provides to solve this problem.

To solve the Page Not Found Error on Login

1.  Login into the WebSphere Administrative Console.

2.  Navigate to **Application Servers &gt; &lt;server&gt; &gt; Web Container Settings &gt; Web Container &gt; Custom Properties**.

3.  Create a new property with the following attributes:

    `name: com.ibm.ws.webcontainer.invokefilterscompatibility`

    `value: true`

4.  Save the master configuration.

5.  Restart the WebSphere server.

## WebLogic Modifications

### Schema Validation Error

You may see an error like the following on some WebLogic installations:

`<Critical> <WebLogicServer> <BEA-000362> <Server failed. Reason: [Management:141245]Schema Validation Error in /u01/app/oracle/WLS/user_projects/domains/x2o_uat_01/config/config.xml`

This may be caused by the configuration of the `<stuck-thread-max-time>` element in the designated configuration file. In this case, removing `stuck-thread-max-time` may resolve the error.

## Disabling User Session Persistence in Application Servers

JasperReports Server stores non-serializable data in its user sessions, which can cause errors after restarting your application server:

`Exception loading sessions from persistent storage`

`Cause: java.io.NotSerializableException ...`

The errors appear in the JasperReports Server log when users log in after the application server has been restarted. Users do not see the errors, and they have no impact on JasperReports Server operations.

Because JasperReports Server user sessions are not persistent, you can configure your application server to disable persistence and avoid the error. For example, in Apache Tomcat, edit the file `<tomcat>/conf/context.xml` and locate the following lines.

``` text
<!-- Uncomment this to disable session persistence across Tomcat restarts -->
    <!--
    <Manager pathname="" />
    -->
```

Remove the comment markers from lines 2 and 4 above, then restart Apache-Tomcat activate the change. For other application servers, refer to the product documentation.
