---
title: "Exposing Diagnostics Through Jaspersoft's JMX Agent"
description: "By default, the diagnostic feature is configured to allow access to the diagnostic data through a remote management console that supports JMX. This allows you to integrate JasperReports Server..."
---

# Exposing Diagnostics Through Jaspersoft's JMX Agent

By default, the diagnostic feature is configured to allow access to the diagnostic data through a remote management console that supports JMX. This allows you to integrate JasperReports Server diagnostics with your overall IT management strategy. Alternatively, the Java Development Kit provides the jConsole tool that uses JMX and can be used to monitor your server remotely. All of these management consoles access the JMX agent provided with JasperReports Server, and access is secured by the same users, passwords, and roles used by the server's web interface.

## Connecting to the JMX Agent

The JMX server component is now disabled by default, and only the Internal Diagnostic Report and Diagnostic DataSource are available. If you still require real-time diagnostics provided by the JMX Server, you can re-enable the server through the following steps:

1.  Edit `applicationContext-diagnostic.xml`.

2.  Find string `BEGIN Embedded JasperServer JMX Server`.

3.  Uncomment beans up to the word `END (beans jMXAuthenticator, jMXregistry, jasperJMXServerConnector, jasperJMXServer)`.

4.  Comment out the bean that goes after END. The updated XML snippet should look like this:

    ``` text
    <!-- BEGIN Embedded JasperServer JMX Server -->
    <bean id="jMXAuthenticator" class="com.jaspersoft.jasperserver.api.logging.diagnostic.jmx.JmxSecurityAuthenticator">
    <property name="authenticationManager" ref="authenticationManager"/>
    <property name="allowedRoles" ref="${bean.diagnosticAllowedRoles}"/>
    </bean>
    <bean id="jMXregistry" class="org.springframework.remoting.rmi.RmiRegistryFactoryBean">
    <property name="port" value="${diagnostic.port}"/>
    </bean>
    <bean id="jasperJMXServerConnector" class="org.springframework.jmx.support.ConnectorServerFactoryBean" lazy-init="false">
    <property name="server" ref="jasperJMXServer"/>
    <property name="objectName" value="connector:name=rmi"/>
    <property name="serviceUrl" value="service:jmx:rmi:///jndi/rmi://${diagnostic.rmiHost}:${diagnostic.port}/${diagnostic.name}"/>
    <property name="environmentMap">
    <map>
    <entry key="jmx.remote.authenticator" value-ref="jMXAuthenticator"/>
    </map>
    </property>
    </bean>
    <bean id="jasperJMXServer" class="org.springframework.jmx.support.MBeanServerFactoryBean" depends-on="jMXregistry">
    <property name="locateExistingServerIfPossible" value="${diagnostic.usePlatformJMXServer}"/>
    </bean>
    <!-- END -->
    <!--Comment this bean declaration out if Embedded JasperServer JMX Server is enabled-->
    <!--<bean id="jasperJMXServer" class="org.springframework.jmx.support.MBeanServerFactoryBean" >
    <property name="locateExistingServerIfPossible" value="${diagnostic.usePlatformJMXServer}"/>
    </bean>-->
    ```

5.  Start the server.

To connect your management console to the JasperReports Server's JMX agent, initiate a new connection from your console and specify the following connection string:

```
service:jmx:rmi://localhost/jndi/rmi://<host>:<port>/<connectionName>
```

where:

- `<host>` is the computer where JasperReports Server is running
- `<port>` is the JMX port, by default `10990`
- `<connectionName>` is the name of the JMX agent, by default `jasperserver`

Therefore, the default connection string is:

```
service:jmx:rmi://localhost/jndi/rmi://<host>:10992/jasperserver
```

!!! note

    If you have a firewall implemented on the computer hosting JasperReports Server, you'll need to open the JMX port (10992 by default) before connecting.

When prompted to enter a username and password, give a user with the following roles:

|                      |                                                      |
|----------------------|------------------------------------------------------|
| Commercial editions: | ROLE_SUPERUSER, thus by default the `superuser` user |

The following sections explain how to modify the default connection values for:

- The connection name
- The JMX port
- The required roles

## Configuring the Port and Connection Name

The connection name is the name registered for the JMX agent with the remote method invocation (RMI) service. If you have more than one JasperReports Server instance in a single app server, you need to change the registered connection name for all but the first one.

There are times you may want to change the port from default (10992) to another port, for example, if another service is configured to use the default port. For example, change the port if you have JasperReports Server running in a second app server on the same computer.

To change the port or connection name, edit one of following files:

- In the WAR file distribution before installation: `<js-install>/buildomatic/default_master.properties`
- In the installed WAR file before starting the server: `.../WEB-INF/js.diagnostic.properties`

Find the following lines and edit the values to the port number and connection name you want:

```
diagnostic.jmx.port = 10992
diagnostic.jmx.name = jasperserver
```

## Configuring Roles for JMX Connections

If you want to allow other users to establish the JMX connection from a remote management console, configure JasperReports Server to allow other roles:

- For commercial editions, edit the `.../WEB-INF/applicationContext-diagnostic-pro.xml` file and modify the following setting:

```
<util:list id="diagnosticAllowedRolesPro">
    <value>ROLE_SUPERUSER</value>
</util:list>
```

You can change the existing role or add additional lines containing alternate `<value>ROLE_name</value>`.

## Disabling Remote Connections to the JMX Agent

By default, remote connections to the JMX Agent are enabled and configured as described in Connecting to the JMX Agent.

To disable remote connections, edit the `.../WEB-INF/applicationContext-diagnostic.xml` file and make the following changes:

- Comment out the entire `jMXAuthenticator` bean.
- Comment out the entire `jMXregistry` bean.
- Comment out the entire `jasperJMXServerConnector` bean.
- Comment out or remove the property `depends-on="jMXregistry"` in the `jasperJMXServer` bean.

To comment out a section of this XML file, surround it with `<!--` and `-->` tags.

## Alternative Connection Through App Server JMX Service

Most app servers also have a JMX agent, and if configured properly, they can discover the JasperReports Server JMX agent and expose the diagnostic information. However, this connection has some significant security implications:

- When the app server discovers and connects to the JMX agent, it has full access to the diagnostic information.
- If the app server's JMX agent is configured for remote access, the remote manager also has access to the JasperReports Server JMX agent without needing to provide the JasperReports Server username and password. In other words, by trusting the app server to access the diagnostic information, you're also allowing anyone the app server trusts to connect.
- The connection between the two JMX agents is reciprocal. If remote access is still enabled on the JasperReports Server JMX agent, a remote manager who connects to it also sees the contents of the app server JMX agent. In other words, the app server JMX agent is also trusting anyone who we trust to connect to our JMX agent (with our username and password).

To connect automatically to the app server's JMX agent, assuming one is available, edit the `default_master.properties` file before you deploy the JasperReports Server web app, and add the following line:

```
diagnostic.jmx.usePlatformServer = true
```

If the app server is Apache Tomcat for example, a local JMX connection named Catalina appears to anyone accessing the JasperReports Server JMX agent.
