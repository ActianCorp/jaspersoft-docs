---
title: Hiding Stack Trace Messages
description: "By default, JasperReports Server displays stack traces in certain error messages. Stack traces reveal some information about the application, and security experts recommend that an application not..."
---

# Hiding Stack Trace Messages

By default, JasperReports Server displays stack traces in certain error messages. Stack traces reveal some information about the application, and security experts recommend that an application not displays them.

The following setting determines what error messages are displayed:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Hiding Stack Trace Messages</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-security.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>outputControlMap</code></p></td>
<td><p><code>exceptionOutput</code><br />
<code>Manager</code></p></td>
<td><p>Set the roles in the list for each of the three levels of error details. Only users who have a given role sees that level of detail. See sample below.</p></td>
</tr>
<tr>
<td><code>outputControlMapForContexts</code></td>
<td><code>exceptionOutput Manager</code></td>
<td><p>This property overrides the existing <code>outputControlMap </code>property of <code>exceptionOutputManager</code> in <code>/jasperserver-pro/rest_ v2/contexts</code> flow. See sample below.</p></td>
</tr>
</tbody>
</table>

Error messages contain three parts: an ID, the stack trace, and a message. You can control which of these error message parts are displayed to users based on roles.

For example, for regular users not to see stack traces, but to see error messages, remove `ROLE_USER` from the `ERROR_UID` list and add it into `MESSAGE` list, resulting in the following configuration:

```
<bean name="exceptionOutputManager" class="com.jaspersoft.jasperserver.api.common.error.handling.ExceptionOutputManagerImpl">
            <property name="outputControlMap">
                <map>
                    <entry key="ERROR_UID">
                        <list>
                            <!--<value>ROLE_USER</value>-->
                        </list>
                    </entry>
                    <entry key="STACKTRACE">
                        <list>
                            <value>ROLE_SUPERUSER</value>
                        </list>
                    </entry>
                    <entry key="MESSAGE">
                        <list>
                            <value>ROLE_USER</value>
                            <value>ROLE_SUPERUSER</value>
                        </list>
                    </entry>
                </map>
            </property>
        </bean>
    </beans>
<beans profile="engine">
        <util:map id="outputControlMapForContexts">
            <entry key="ERROR_UID">
                <list>
                    <value>ROLE_USER</value>
                </list>
            </entry>
            <entry key="STACKTRACE">
                 <list>
                 <value>ROLE_SUPERUSER</value>
              </list>
          </entry>
          <entry key="MESSAGE">
              <list>
                  <value>ROLE_SUPERUSER</value>
                  <value>ROLE_ADMINISTRATOR</value>
              </list>
          </entry>
      </util:map>
</beans>
```

Access to the error messages shown in Domain Designer when executing SQL Queries can be configured separately from error messages that user can get in other places. As another example removing `ROLE_ADMINISTRATOR` from `MESSAGE` list and adding into `ERROR_UID` list will hide error messages returned by SQL in Domains, resulting in the following configuration:

```
<beans profile="engine">
        <util:map id="outputControlMapForContexts">
            <entry key="ERROR_UID">
                <list>
                    <value>ROLE_USER</value>
                    <value>ROLE_ADMINISTRATOR</value>
                </list>
            </entry>
            <entry key="STACKTRACE">
                 <list>
                 <value>ROLE_SUPERUSER</value>
              </list>
          </entry>
          <entry key="MESSAGE">
              <list>
                  <value>ROLE_SUPERUSER</value>
                  <!--<value>ROLE_ADMINISTRATOR</value>-->
              </list>
          </entry>
      </util:map>
</beans>
```

When configuring error messages, keep in mind the following:

- We recommend the configuration shown above, so that users see a descriptive error message.
- You can turn off any or all error message parts, however, when both `STACKTRACE` and `MESSAGE` are not displayed to a user, a generic message is output instead. The generic message text is defined as follows:

<table>
<thead>
<tr>
<th colspan="3"><p>Generic Error Message</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/bundles/jasperserver_messages*.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Value</p></td>
</tr>
<tr>
<td><p><code>generic.error.message</code></p></td>
<td colspan="2"><p>By default, <code>There was an error on the server. Try again or contact site administrators.</code> is displayed. If you modify this message, you must update the translation in all language files of the bundle.</p></td>
</tr>
</tbody>
</table>

- If you remove both `STACKTRACE` and `MESSAGE` for a given role, we recommend adding back `ERROR_UID` for that role. That way, the user will see the generic message and an ID that can be sent to administrators and correlated with events in the log file.

If you update any of the error message configuration or bundles, restart your application server or redeploy the JasperReports Server web app.
