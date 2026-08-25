---
title: Configuring JasperReports Server to Offer a Locale
description: "After creating a locale, you must configure JasperReports Server to offer it to your users, along with any new time zones."
---

# Configuring JasperReports Server to Offer a Locale

After creating a locale, you must configure JasperReports Server to offer it to your users, along with any new time zones.

The tasks in this section require you to edit these files:

| File Name | Location | Purpose of Edits |
|----|----|----|
| `applicationContext-security.xml` | `WEB-INF` | Specifying additional locales |
| `applicationContext.xml` | `WEB-INF` | Specifying additional time zones |

## Specifying Additional Locales

By default, JasperReports Server appears in the locale selected in the end user's browser. The `Login` page allows users to specify the locale they want to use. The list of available locales is defined in `applicationContext-security.xml`. Edit this file to add a new locale.

To add a new locale

1.  Edit the `applicationContext-security.xml` file and locate the bean named `userLocalesList`. For example:

    ``` xml
    <bean id="userLocalesList"
            class="com.jaspersoft.jasperserver.war.common.LocalesListImpl">
        <property name="locales">
            <list>
                <value type="java.util.Locale">en</value>
                <value type="java.util.Locale">fr</value>
                <value type="java.util.Locale">it</value>
                <value type="java.util.Locale">de</value>
                <value type="java.util.Locale">ro</value>
                <value type="java.util.Locale">ja</value>
                <value type="java.util.Locale">zh_TW</value>
            </list>
        </property>
    </bean>
    ```

2.  Add the new locale to the end of the list. For example, add the following line for Dutch (Java's nl_NL locale):

    ``` xml
                <value type="java.util.Locale">nl_NL/value>
    ```

3.  Save the file.

4.  Restart JasperReports Server, and log into the web application to test your translation. Reviewing the translated strings in context can help you improve your word choices.

For a list of Java-compliant locales, please refer to the Java documentation.

## Specifying Additional Time Zones

By default, JasperReports Server assumes the user's time zone is that of the JasperReports Server host. The `Login` page allows users to choose a different time zone. The available list is defined in `applicationContext.xml` file.

To add a time zone

1.  Open the `applicationContext.xml` file and locate the `userTimeZonesList` bean. For example:

    ``` xml
    <bean id="userTimeZonesList"
            class="com.jaspersoft.jasperserver.war.common.JdkTimeZonesList">
        <property name="timeZonesIds">
            <list>
                <value>America/Los_Angeles</value>
                <value>America/Denver</value>
                <value>America/Chicago</value>
                <value>America/New_York</value>
                <value>Europe/London</value>
                <value>Europe/Berlin</value>
                <value>Europe/Bucharest</value>
            </list>
        </property>
    </bean>
    ```

2.  Add the new time zone to the bottom of the list. Specify each time zone as the standard Java time zone values so that JasperReports Server adjusts for daylight savings time when appropriate. For example, add the following line for Tokyo:

    ``` xml
    <value>Asia/Tokyo</value>
    ```

3.  Save the file.

4.  Restart JasperReports Server.

For more information about Java-complaint time zones, please refer to the Java documentation.

## Setting a Default Time Zone

If you want JasperReports Server to use a time zone other than the host computer's, you can set a specific time zone in Java. It becomes the default time zone for all users, but they can still select a different time zone when they log in.

To set a default time zone, set the `user.timezone` property in the JVM as shown in the tables below. Locate the file containing JVM settings for your platform and application server. The value for the property must be a Java-compliant time zone, for example, `Europe/Bucharest`.

You must restart your application server for this setting to take effect. The time zone is set for all applications in your application server, including JasperReports Server.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th colspan="4"><p>JVM Settings for Default Time Zone</p></th>
</tr>
<tr>
<th><p>Operating System</p></th>
<th><p>App Server</p></th>
<th><p>File</p></th>
<th><p>Setting</p></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2"><p>Windows</p></td>
<td><p>Tomcat</p></td>
<td><p><code>&lt;apache-tomcat&gt;\bin\setenv.bat</code></p></td>
<td rowspan="2"><p>Add this line of code:</p>
<p><code>set JAVA_OPTS=%JAVA_OPTS%</code><br />
<code>-Duser.timezone=&lt;timezone&gt;</code><br />
</p></td>
</tr>
<tr>
<td><p>JBoss</p></td>
<td><p><code>&lt;jboss&gt;\bin\standalone.conf.bat</code></p></td>
</tr>
<tr>
<td rowspan="2"><p>Linux</p></td>
<td><p>Tomcat</p></td>
<td><p><code>&lt;apache-tomcat&gt;/bin/setenv.sh</code></p></td>
<td rowspan="2"><p>Add this line of code:</p>
<p><code>export JAVA_OPTS="$JAVA_OPTS</code><br />
<code>-Duser.timezone=&lt;timezone&gt;"</code><br />
</p></td>
</tr>
<tr>
<td><p>JBoss</p></td>
<td><p><code>&lt;jboss&gt;/bin/standalone.conf</code></p></td>
</tr>
</tbody>
</table>
