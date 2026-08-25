---
title: Configuring User Password Options
description: "The user password options determine whether passwords can be remembered by the browser, whether users can change their own passwords, and whether password changes are mandatory or optional."
---

# Configuring User Password Options

The user password options determine whether passwords can be remembered by the browser, whether users can change their own passwords, and whether password changes are mandatory or optional.

!!! note

    By default, passwords are stored in an encrypted format in the server’s private database. For information about changing the way passwords are encrypted, see [Encrypting User Passwords.](encrypting_user_passwords.md)

## Configuring Password Memory

As a general security policy, sensitive passwords should not be stored in browsers. Many browsers have a "remember passwords" feature that stores a user's passwords. Most browsers do not protect passwords with a master password by default. JasperReports Server can send the property `autocomplete="off"` to indicate that its users’ passwords should not be stored or filled in automatically. This helps to ensure that your users do not store their passwords. Actual behavior depends on the browser settings and how the browser responds to the `autocomplete="off"` property.

Login encryption described in [Encrypting User Session Login](encrypting_user_session_login.md) is not compatible with password memory in the browser. Independent of the auto-complete setting, the JavaScript that implements the login encryption clears the password field before submitting the page. As a result, most browsers will not prompt to remember the password when login encryption is enabled, even if the user has password memory enabled in the browser.

!!! warning

    When `autoCompleteLoginForm=true`, as in the default installation, you should ensure that all of your users have a master password in their browser.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Password Memory in the Browser</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/jasperserver-servlet.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>autoCompleteLoginForm</code></p></td>
<td><p><code>true</code> &lt;default&gt;<br />
<code>false</code></p></td>
<td><p>When false, the server sets <code>autocomplete="off"</code> on the login page and browsers will not fill in or prompt to save Jaspersoft passwords. When true, the autocomplete property is not sent at all, and browser behavior depends on user settings.</p></td>
</tr>
</tbody>
</table>

## Enabling Password Expiration

If your security policies require users to change their passwords at regular intervals, you can enable password expiration. This way JasperReports Server prompts users to change their passwords at your set interval. Users with expired passwords cannot log in without changing their passwords. This option is disabled by default, meaning passwords do not expire and users are never prompted.

When you enable this option, the server automatically enables the **Change Password** link on the Login page, even if `allowUserPasswordChange` is set to false.

!!! warning

    If your users are externally authenticated, for example with LDAP, do not enable this option.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Password Administration Option</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/jasperserver-servlet.xml</code> (controls the Login page)</p>
<p><code>.../WEB-INF/applicationContext-security-web.xml</code> (controls web services)</p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>passwordExpirationInDays</code></p></td>
<td><p><code>0</code> &lt;default&gt;<br />
&lt;any other value&gt;</p></td>
<td><p>Set the value to any positive, non-zero value to specify the number of days after which a password expires.</p></td>
</tr>
</tbody>
</table>

## Allowing Users to Change their Passwords

With this configuration the Change Password link on the Login page is enabled. By default, this option is turned off, and an administrator must define user passwords initially or reset a forgotten password. Enabling the password expiration option (described in the previous section) automatically enables users to change their passwords.

!!! warning

    If your users are externally authenticated, for example with LDAP, do not enable this option.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Password Administration Option</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>js.spring.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>allowUserPasswordChange</code></p></td>
<td><p><code>false</code> &lt;default&gt;<br />
<code>true</code></p></td>
<td><p>Set the value to <code>true</code> to enable the <strong>Change Password</strong> link. Any other value disables it.</p></td>
</tr>
</tbody>
</table>

## Enforcing Password Patterns

If you allow or force users to change their passwords, you can enforce patterns for valid strong passwords, by requiring a minimum length and a mix of uppercase, lowercase, and numbers. The default pattern accepts any password of any length, including an empty password.

!!! warning

    If your users are externally authenticated, for example with LDAP, do not enable this option.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Password Administration Option</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>allowedPasswordPattern</code></p></td>
<td><p><code>userAuthority</code><br />
<code>Service</code></p></td>
<td><p>A regular expression that matches valid passwords. The default pattern <code>^.*$</code> matches any password. Change the regular expression to enforce patterns such as:</p>
<ul>
<li>Minimum and maximum password length</li>
<li>Both uppercase and lowercase characters</li>
<li>At least one number or special character</li>
</ul>
<p>Be sure that your pattern allows whitespace and international characters if needed by your users.</p></td>
</tr>
</tbody>
</table>

When you enforce a password pattern, you should set the following message to inform users why their password was rejected. Be sure to set the message in all your locales.

<table>
<thead>
<tr>
<th colspan="3"><p>Password Administration Option</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/bundles/jsexceptions_messages[_locale].properties</code></p></td>
</tr>
<tr>
<td colspan="2"><p>Property</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td colspan="2"><p><code>exception.remote.weak.password</code></p></td>
<td><p>A message is displayed to users when password pattern matching fails.</p></td>
</tr>
</tbody>
</table>

## Password History Validation

The password history validation feature enhances account security and ensures compliance with industry standards (for example, PCI DSS, NIST, ISO/IEC 27001) by preventing users from reusing previous credentials.

By default, the feature is disabled (for backward compatibility). Administrators must explicitly enable it and define the number of previous passwords to retain via the application property file.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Password Administration Option</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>js.spring.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>password.history.enabled</code></p></td>
<td><p><code>false</code>&lt;default&gt;<br />
<code>true</code></p></td>
<td><p>Set the value to <code>true</code> to enable the password history.</p></td>
</tr>
<tr>
<td><code>password.history.count</code></td>
<td><p><code>7</code> &lt;default&gt;</p>
<p><code>N</code></p></td>
<td>Set the value to define the number of previous passwords to retain.</td>
</tr>
</tbody>
</table>

!!! note

    - The password history validation only applies to internal authenticated users, not external ones using LDAP. The rule is enforced during both self-service resets on the Login page and admin resets via the Manage \> Users menu, but it doesn't trigger during regular logins, data imports, or other non-change events.

    - Once it's turned on, the system blocks users from picking their current password or any of their last `N` passwords, depending on what you set for `password.history.count`. If you change this number, the new limit takes effect on the next password update, checking against the most recent entries in the log.

    - If you delete a user, their entire password history is automatically wiped out.

    - When you export users, their password history is not exported.

If you enable password history validation, the rejection messages must be updated across all your active locales so users know why their new password wasn't accepted.

<table>
<thead>
<tr>
<th colspan="2"><p>Password Administration Option</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="2"><p><code>.../WEB-INF/bundles/jasperserver_messages[_locale].properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>jsp.passwordError.passwordHistoryViolation</code></p></td>
<td><p>Set the error message for when a user tries to change their password to a recently used one.</p></td>
</tr>
<tr>
<td><code>jsp.passwordError.passwordHistoryViolation.admin</code></td>
<td>Set the error message displayed to administrators when they try to reset a user's password to a recently used one.</td>
</tr>
</tbody>
</table>

### JIUserPasswordHistory Table

The `JIUserPasswordHistory` table handles password reuse protection. It links right to the main `JIUser `table and keeps a running history of a user's old, encrypted password hashes and timestamps. When an administrator enables a password history limit (for example, preventing the reuse of the last 7 passwords), the server checks this table during a password reset to ensure the new password does not match any previously stored hashes.

## Limiting Failed Login Attempts

To prevent brute-force attacks against user and administrator accounts, JasperReports Server locks an account after a configurable number of failed login attempts. JasperReports Server records failed login attempts and administrators may configure a set limit after which the account is disabled. An administrator must enable the account before it can be used again. The setting (enabled by default) is set for 10 attempts, but can be disabled, or configured to reduce or increase the number of attempts. Refer to the JasperReports Server Administrator Guide for more information on how to enable a locked user account.

The following bean definition is available in the `applicationContext-security.xml` for the class `LoginLockoutConfig`.

```
<bean id="loginLockoutConfig" class="com.jaspersoft.jasperserver.api.common.configuration.LoginLockoutConfig">
<property name="allowedNumberOfLoginAttempts" value="10"></property>
</bean>
```

The property `allowedNumberOfLoginAttempts` is used to configure the value. The default value is set as `10`.

To disable the feature, set the value to 0. Afterwards, the user has no limit to the number of times they can attempt to log into an account.

### JIUser and JExternalUserLoginEvents Tables

A new column has been added to the `JIUser` table named `numberOfFailedLoginAttempts`.

A new table `JIExternalUserLoginEvents` is added. This table is used to track valid or invalid login attempts by external and non-existing users. The property `userLoginAttemptsThreshold` is responsible for the maximum number of rows/records allowed in the table, exceeding this number removes the oldest records from that table to keep the records count under the threshold.

The `JIUser` and `JIExternalUserLoginEvents` tables are used to disable a user if the Number of Failed Attempts to login is reached. If the feature is enabled, then when a user enters an invalid password, the user sees a message that states the number of login attempts still available. If the user enters a valid password, before the counter reaches 0, then the counter gets reset back to 10. If the user exceeds the 10 counter (or whatever the administrator has set this value to (10 is the default), then the user is locked out of their account and will need to have their administrator to unlock/enable the account.

You can leave the default cleanup of 1 hour or you can change it.

The following steps, as an example, describe how to change the threshold to 2 and cron time to 20 minutes:

1.  Edit the `applicationContext.xml` file.
2.  Search for '`<bean id="externalUserLoginAttemptsCleanUpService">`'
3.  Change "`<property name="userLoginAttemptsThreshold" value="100"/>`" to "`<property name="userLoginAttemptsThreshold" value="2"/>`".
4.  Search for `<task:scheduled-tasks scheduler="externalUserCleanupScheduler">`.
5.  Change "`<task:scheduled ref="externalUserLoginAttemptsCleanUpService" method="clearAllData" cron="0 0 /1 * * *" />`" to "`<task:scheduled ref="externalUserLoginAttemptsCleanUpService" method="clearAllData" cron="0 */20 * * *" />`".

!!! note

    The cron job runs every 20 minutes. Adjust this value if needed.

6.  Restart Tomcat.

**Limitations**

LDAP users can log into JasperReports Server with or without specifying an organization_id, for example, "`user_1|organization/password`" and "`user_1/password`". Internally, such users are treated as the same user, which means that locking out "`user_1|organization/password`" will also lock out "`user_1/password`". This can be a problem when you have some internally defined users with the same name in the root level organization. To avoid such situations, stick to the following rules:

- If possible, avoid creating users in the root organization with a user id that can match an external user id.
- External LDAP users should enter their organization ids along with user id and password.
