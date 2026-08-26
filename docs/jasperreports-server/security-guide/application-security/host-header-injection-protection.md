---
title: Host Header Injection Protection
description: An HTTP Host header attack is a type of web vulnerability where an attacker can manipulate the HTTP Host header of a web request to trick a server into responding to a request that was not intended...
---

# Host Header Injection Protection

An HTTP Host header attack is a type of web vulnerability where an attacker can manipulate the HTTP Host header of a web request to trick a server into responding to a request that was not intended for that server. This can lead to a variety of security issues, including domain hijacking, cache poisoning, and server-side request forgery.

To enable JasperReports Server to filter requests matched by the Host header, edit the following configuration file: `applicationContext-security-web.xml`.

1.  Using a text editor, open the `applicationContext-security-web.xml` file (found in &lt;js-install&gt;\\apache-tomcat\\webapps\\jasperserver-pro\\WEB-INF).

2.  Locate `<bean id="authenticationAuthorizationFilterChainProxy" class="org.springframework.security.web.FilterChainProxy">`.

3.  Add allowedHostnames into the firewall:

    ``` xml
    <property name="firewall">
    <bean class="org.springframework.security.web.firewall.StrictHttpFirewall">
    <property name="allowUrlEncodedSlash" value="true"/>
    <property name="allowSemicolon" value="true"/>
    <property name="allowUrlEncodedPercent" value="true"/>
    <property name="allowBackSlash" value="true"/>
    <property name="allowedHostnames">
    <value>#{ T(java.util.function.Predicate).isEqual("allowed.hostname.com").or(T(java.util.function.Predicate).isEqual("localhost")) }</value>
    </property>
    </bean>
    </property>
    ```

4.  Save the file and restart the server.

!!! note

    In this example, we allow requests coming with HOST header == allowed.hostname.com or == localhost. To add more hosts, you can add chained "or(T(java.util.function.Predicate).isEqual("YOURHOST"))", if only one host is needed, "or...." should be removed.
