---
title: Configuring CSRF Protection
description: Cross-Site Request Forgery (CSRF) enables an attacker to either gain information or perform actions while a user is logged into JasperReports Server. The user may be logged in another window or tab...
---

# Configuring CSRF Protection

Cross-Site Request Forgery (CSRF) enables an attacker to either gain information or perform actions while a user is logged into JasperReports Server. The user may be logged in another window or tab of the same browser. This is called session riding. For example, a server administrator logged into JasperReports Server is tricked into opening a malicious website that invisibly uses the browser session to create a user with administrator permissions. The attacker can then use it to access the system later.

JasperReports Server uses the latest release of [CSRFGuard](https://www.owasp.org/index.php/Category:OWASP_CSRFGuard_Project) from OWASP (Open Web Application Security Project). CSRFGuard verifies that every POST, PUT, and DELETE request submits a valid token previously obtained from the server. This includes every request submitted via forms or AJAX. When a malicious request arrives without the proper token, the server does not reply and logs an error for administrators to analyze later.

Tokens are sent in HTTP headers or parameters, and the entire exchange is invisible to users. Tokens have the following syntax:

`OWASP_CSRFTOKEN: K8E9-L4NZ-58H6-Z4P2-ZG75-KKBW-U53Z-ZL6X`

!!! warning

    In the default configuration of the server, CSRF protection is active. We recommend leaving this setting unchanged.

    However, to fully implement CSRF and secure your server, you must configure the domain whitelist as explained in the next section.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>CSRF Protection</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/csrf/jrs.csrfguard.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>org.owasp.csrfguard.Enabled</code></p></td>
<td><p><code>true</code> &lt;default&gt;<br />
<code>false</code></p></td>
<td><p>Turns CSRF protection on or off. By default, CSRF protection is enabled. Setting this value to false disables the CSRF filter and allows any request regardless of tokens.</p></td>
</tr>
</tbody>
</table>

!!! note

    This configuration file contains many settings that are preconfigured for JasperReports Server. We do not recommend changing any other settings. In particular, the two `configOverlay` properties are unreliable and not supported.

After updating the `jrs.csrfguard.properties` file, you must restart JasperReports Server for the new values to take effect.

## Setting the Cross-Domain Whitelist

!!! warning

    In all cases, even if you do not use Visualize.js, you must configure the whitelist. Never use a server in production with the default whitelist.

Applications that use the embedded Visualize.js library typically access JasperReports Server from a different domain. For this reason, CSRF protection includes a whitelist of domains that you specifically allow to access the server. Initially, all your Visualize.js applications can access the server, but you should configure the whitelist so that only your domains have access. Then, any Visualize.js request from an unknown domain fails with HTTP error 401, and the server logs a CSRF warning.

The domain whitelist is implemented through attributes named `domainWhitelist` at the user, organization, or server-level. You may specify different values at each level. The values are defined according to the attribute hierarchy. In addition, the `domainWhitelist` attribute is defined with administrator permissions, implying that organization admins can set their own values. The attributes are set through the server UI or through the REST API. For more information on how to define attributes and how their values are determined by hierarchy, refer to the JasperReports Server Administrator Guide.

There are four cases listed in the table below. Choose the one suited to your use of Visualize.js.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Cross-Domain Whitelist</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration Location</p></td>
</tr>
<tr>
<td colspan="3"><p>The attribute <code>domainWhitelist</code> is defined at the server level. In addition to setting any alternate values at the organization or user levels, for security, always set the server level as described below:</p>
<ul>
<li>Server level: as system admin (<code>superuser</code>), select <strong><strong>Manage</strong> &gt; <strong>Server Settings</strong></strong> then <strong>Server Attributes</strong>.</li>
<li>Organization or user level: as any administrator, select <strong><strong>Manage</strong> &gt; <strong>Organizations</strong></strong> or <strong><strong>Manage</strong> &gt; <strong>Users</strong></strong>, then select the organization or user, click <strong>Edit</strong> in the right-hand panel, and select the <strong>Attributes</strong> tab.</li>
</ul></td>
</tr>
<tr>
<td><p>Attribute</p></td>
<td><p>Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>domainWhitelist</code> at server level</p></td>
<td><p>&lt;blank&gt;<br />
</p></td>
<td><p>Explicitly set the whitelist to blank (attribute defined with an empty value) if:</p>
<ul>
<li><p>you do not have any Visualize.js-enabled web applications, OR</p></li>
<li><p>you have Visualize.js-enabled web applications that access your server from the <code>same</code> domain as the server</p></li>
</ul></td>
</tr>
<tr>
<td><p><code>domainWhitelist</code> at server level</p></td>
<td><p><code>example.com</code></p>
<p>(See below)</p></td>
<td><p>If you have Visualize.js-enabled web applications that access your server from a <code>different</code> domain, then specify an expression that matches the domain name. For the syntax of this expression, see below.</p></td>
</tr>
<tr>
<td><p><code>domainWhitelist</code> at server level</p>
<p><code>domainWhitelist</code> at org1 level</p>
<p><code>domainWhitelist</code> at user2 level</p>
<p>...</p></td>
<td><p>&lt;blank&gt;</p>
<p><code>example1.com</code></p>
<p><code>example2.com</code></p>
<p>...</p>
<p>(See below)</p></td>
<td><p>If your organizations or users have Visualize.js applications on specific domains, you could use the hierarchy of attributes to set the whitelist according to each organization's or each user's individual domain. In this case, make sure that the whitelist at the server level is defined as blank. For the syntax of this expression, see below.</p></td>
</tr>
<tr>
<td><code>domainWhitelist1</code>
<p><code>domainWhitelist2</code></p></td>
<td><p>&lt;regexp&gt;</p>
<p>&lt;regexp&gt;</p></td>
<td>If you want to add more than one regular expression to the whitelist, define these additional attributes at the same level as <code>domainWhitelist</code>. If you need further attributes, you can specify them in the <code>additionalWhitelistAttributes</code> property of the <code>crossDomainFilter</code> bean in the file <code>.../WEB-INF/applicationContext.xml</code>.</td>
</tr>
</tbody>
</table>

The actual value of the attribute is a simplified expression that the server converts into the full regular expression. The value must include the protocol (http), any sub-domains that you use, and the port as well. The value can contain `*` and `.` which the server translates into the proper form as `.*` and `\.`. The server also adds `^` and `$` to the ends of the expression. For example, a typical value for this attribute would be:

`http://*.myexample.com:80\d0` which is translated to `^http://.*\.myexample\.com:80\d0$`

This matches the following domains that you might use:

http://bi3.myexample.com:8080 and http://bi3.myexample.com:8090

http://bi4.myexample.com:8080 and http://bi4.myexample.com:8090

But does not match the following:

http://myexample.com:8080 or http://bi3.myexample.com:8081

If you wish to write your own complete regular expression, surround it with `^` and `$`, and it will be used as-is by the server.

Remember that if you add Visualize.js applications that run on different domains, or change the domains where they run, then you must update the whitelist attributes accordingly. Visualize.js applications on domains that are not whitelisted do not work.

!!! warning

    Do not delete the `domainWhitelist` property from the server level. That removes the whitelist, but on upgrading the server, the attribute is restored with a less secure default value. When the attribute is defined, even with an empty value, it remains during any server upgrade.

## Sending REST Requests from a Browser

If you use the REST API to access JasperReports Server from within an application, this does not trigger a CSRF warning because the application is separate from any access through the browser. However, some browser plug-ins can be used to send REST API requests. Using these to send POST, PUT, or DELETE requests trigger a CSRF warning and fail. GET requests from a browser REST client are safe and do not fail the CSRF check.

To allow REST API requests through a browser, configure your browser REST client to include the following header in every request:

`X-REMOTE-DOMAIN: 1`

## CSRF Browser Compatibility

Only browsers are susceptible to CSRF. Hence, the CSRF protection mechanism detects browsers based on the user-agent string embedded in the request. For performance reasons, the current configuration only filters for Mozilla and Opera user-agents. They cover more than 99% of the browsers in use, such as Chrome, Firefox, Internet Explorer, and Safari.

If your users have browsers with user-agents other than Mozilla, they will not be protected against CSRF by default.

!!! note

    All browsers officially supported by JasperReports Server are protected against CSRF. The following instructions are provided for testing purposes only.

To enable CSRF protection for these browsers, you can add the corresponding user-agent to the CSRF filter:

1.  Find the name of the user-agent for the given browser. If you cannot find the user-agent, many are listed on the following website:

<http://www.useragentstring.com/pages/Browserlist/>

1.  Open the file `.../WEB-INF/applicationContext.xml` for editing.
2.  Locate the `csrfGuardFilter` bean and its `protectedUserAgentRegexs` property. Each list value is a regular expression that is matched against every request's user-agent value in its entirety.
3.  Add a regular expression to the `protectedUserAgentRegexs` property list that matches the user-agent string from your desired browser.
4.  Restart JasperReports Server.
