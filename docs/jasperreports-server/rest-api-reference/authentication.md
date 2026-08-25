---
title: Authentication Methods
description: This chapter demonstrates several ways for REST client applications to authenticate with JasperReports Server. Choose an authentication method that matches the usage patterns and needs of your REST...
---

# Authentication Methods

This chapter demonstrates several ways for REST client applications to authenticate with JasperReports Server. Choose an authentication method that matches the usage patterns and needs of your REST client application.

This chapter includes the following sections:

- Overview of REST Authentication
- HTTP Basic Authentication
- Argument-based Authentication
- The login Service
- Login Encryption (Deprecated)
- Logout

## Overview of REST Authentication

When using the REST API, the client application must provide a valid user ID and password to JasperReports Server. The REST services support two types of authentication:

- Stateless authentication - Your client sends user credentials with every API request. This is the traditional RESTful behavior and fully supported by JasperReports Server. Clients may send credentials using HTTP Basic Authentication, where the user ID and password are sent in the header with every request, or argument-based authentication, where the user ID and password are included in URL arguments.
- User session management - Your client performs a login operation first, and then sends a session cookie with every API request. As with a user interface, your client performs a log out operation when done. Use of the login and log out services is optional, but it can improve performance under heavy user loads.

Normally, RESTful implementations do not rely on the persistent user sessions, such as the login service and user sessions stored on the server. However, the JasperReports Server architecture automatically creates user sessions internally, and the login method takes advantage of this. There are several use cases for either type of authentication.

- If your client makes sporadic requests, for example running a report every hour, it is easier to use basic authentication and send the credentials with each request. See 1.1, “HTTP Basic Authentication,” on page 1.
- If a username or password contains UTF-8 characters, it may be corrupted by basic authentication and the service will always return an error. In this case, you can send the username and password in URL arguments with each request. See 1.1, “Argument-based Authentication,” on page 1.
- If your client applications perform many requests in a short time, you can avoid the overhead of stateless authentication by using the login service once and passing the session ID cookie instead with each request. For more information, see 1.1, “The login Service,” on page 1.
- However, sessions are kept for 20 minutes by default, so if your client makes a request every 15 minutes with the same credentials, the corresponding session is kept in memory indefinitely. This can be a problem if you have many different clients running large reports, because some report output is stored in the user session, and they can fill up the available memory. In this case, you should use the log out call to make sure the memory is freed. For more information, see 1.1, “Logout,” on page 1.

As with logging in from the web UI, you can send a user-specific locale and time zone during REST API authentication. To specify a locale and timezone, choose from the following possibilities:

- Use locale and time zone arguments on any REST API to specify the language and time in the response, for example to localize a report. It is also possible for the same user to make several requests with different locales or time zones. Once you specify a locale or time zone for a given user, the server sets a cookie so that it applies to all requests. See 1.1, “Argument-based Authentication,” on page 1.
- When doing many requests with the same locale and time zone, you can also specify the locale and time zone arguments with the login service. The language and time will be set with a cookie for all future requests. See 1.1, “The login Service,” on page 1.
- If you never specify any locale or time zone arguments, the default locale and default time zone on the server will be used for all operations.

In the case of external authentication, how you perform REST authentication depends on the type of mechanism:

- If your server is configured with an external authentication that requires a username and password, such as LDAP, then you can use any authentication method that submits those values: HTTP basic authentication, argument-based authentication, or the login service with credentials in arguments or the request body. However, repeatedly verifying external credentials might cause performance issue, in which case you should use the login service and the session cookie it returns.
- If your server is configured with SSO (Single Sign-On), use the updated v2 login service to send the token. For more information, see 1.1, “The login Service,” on page 1.
- If your server is configured with Pre-Authentication, specify the `pp` argument in every API request, as shown in 1.1, “Argument-based Authentication,” on page 1.

None of these authentication methods provide privacy, meaning that passwords are sent in plain text or easily reversed encodings. Jaspersoft recommends that you configure your server and clients to use HTTPS to provide end-to-end privacy and security. Alternatively, JasperReports Server has a login encryption feature that hides passwords. If this feature is enabled on your server, you must encrypt your passwords before sending them in REST requests. For more information, see 1.1, “Login Encyrption,” on page 1.

## HTTP Basic Authentication

HTTP basic authentication is stateless, meaning that your client application must supply a valid user and password in every API request. The user ID and password are concatenated with a colon (`:`) and Base64-encoded in the HTTP request header. Usually, your client library does this for you. For example, the default organization admin’s credentials are `jasperadmin:jasperadmin`, which is encoded as follows:

`Authorization: Basic amFzcGVyYWRtaW46amFzcGVyYWRtaW4=`

The REST API services accept the same accounts and credentials as the JasperReports Server user interface.

- In commercial editions where there is only one organization, such as in the JasperReports Server default installation, you should specify the user ID without any qualifiers, for example `jasperadmin`.
- In commercial deployments with multiple organizations, the organization ID or organization alias must be appended to the user ID, for example `jasperadmin|organization_1` or `jasperadmin|org2`. When the organization ID or alias is added to an argument in the URL, you should use the encoded form: `jasperadmin%7Corganization_1`

When your server implements external authentication, such as using LDAP, you can submit the username and password with basic HTTP authentication as well.

If log in encryption is enabled in your server, then you must encrypt the password before base64-encoding it with the username. For more information about encryption, see 1.1, “Login Encryption,” on page 1.

## Argument-based Authentication

Some UTF-8 characters in usernames and passwords are not properly handled by the encoding in HTTP basic authentication, and such requests will return an error. To get around this, all services of the REST API accept arguments for the username and password in the URL. This method also works when your server is configured to check username and passwords with external authentication, for example using LDAP. All services also recognize the `pp` argument that you use when your server is configured for pre-authentication.

Use the following arguments as an alternate method to send user credentials in a stateless manner with each API request:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th>Method</th>
<th colspan="3">URL</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>any</p></td>
<td colspan="3"><p><span>http[s]://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/&lt;service/and/path&gt;</span>[?&lt;arguments&gt;]</span></p></td>
</tr>
<tr>
<td>Argument</td>
<td>Type/Value</td>
<td colspan="2">Description</td>
</tr>
<tr>
<td><p><span>j_username</span></p></td>
<td><p>Text</p></td>
<td colspan="2"><p>The user ID. In commercial editions of the server that implement multiple organizations, the argument must specify the organization ID or alias in the following format: <span>userID%7CorgID</span> (<span>%7C</span> is the encoding for the | character).</p></td>
</tr>
<tr>
<td><p><span>j_password</span></p></td>
<td><p>Text</p></td>
<td colspan="2"><p>The user’s password. The argument is optional but authentication fails without the password. If the server has login encryption enabled, the password must be encrypted as explained in <span>1.1, “Login Encryption,” on page 1</span>.</p></td>
</tr>
<tr>
<td><span>pp</span></td>
<td>Text</td>
<td colspan="2"><p>The token for your pre-authentication mechanism. The default parameter name for a pre authentication token is <code>pp</code>. This parameter name can be changed in the configuration file <span>.../WEB-INF/applicationContext-externalAuth-preAuth.xml</span>.</p></td>
</tr>
<tr>
<td><span>userLocale</span></td>
<td>Java locale string</td>
<td colspan="2">An optional argument to set the locale for this user. The locale can affect both server strings such as messages and report content if localized by Domains. The server sets a cookie with this value so that it is used in every subsequent request until changed. If this argument is never specified for a given user, the server's default locale is used. Specify a Java locale string such as <code>fr</code> (French) or <code>de</code> (German).</td>
</tr>
<tr>
<td><span>userTime</span><br />
<span>zone</span></td>
<td>Java time zone</td>
<td colspan="2">An optional argument to set the time zone for this user. The server sets a cookie with this value so that it is used in every subsequent request until changed. If this argument is never specified for a given user, the server's default time zone is used. The time zone names are those supported by <code>java.time.ZoneID</code>, which are defined in the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">tz database</a>.</td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>The normal response for the requested operation.</p></td>
<td><p>401 Unauthorized - Login failed or j_username or j_password was missing, body of response is empty.</p>
<p>403 Forbidden - License expired or otherwise not valid.</p></td>
</tr>
</tbody>
</table>

For example, the following request returns all repository resources in the Public folder that the sample user `joeuser` has permission to read:

``` text
http[s]://<host>:<port>/jasperserver[-pro]/rest_v2/resources/Public?j_username=joeuser%7Corganization_1&j_password=<password>
```

When using pre-authentication on the server, specify only the pp argument, for example (%3D is the encoding for =, and %7C for \|):

``` text
http[s]://<host>:<port>/jasperserver[-pro]/rest_v2/resources/Public?pp=u%3Djoeuser
%7Cr%3DUSER,SALES%7Co%3DHeadquarters%7Cpa1%3DUSA%7Cpa2%3DLosAngeles
```

Even if you implement HTTPS, you should be aware that plain-text passwords in URLs may appear in your app server's logs, and you should protect such log files. To prevent this security issue, change your logging rules or implement login encryption as described in 1.1, “Login Encryption,” on page 1.

## The login Service

The login service allows your client to send user credentials to the server, verify the credentials, and receive a session cookie. By explicitly creating and maintaining a user session, your client can manage the user session and optimize the resources it uses. For more information, see 1.1, “Overview of REST Authentication,” on page 1.

As of JasperReports Server 8.2, reports executions and Input Controls are no longer session dependent. The new behavior is as follows:

1.  The user logs in as *joeuser\|organization_1*; the user gets a session ID (JSESSIONID in cookies).
2.  That user runs a report; report results are stored in the cache.
3.  The user does not log out; the session is still alive.
4.  From another browser or other client, the user logs in as the same user *joeuser\|organization_1*; the user gets a different session ID.
5.  If a user with a different session ID tries to access report results from the cache from step 2, the user will be able to get those results because now the service is session independent, it passes through the standard security layer (superuser, tenant admins, users); and if the user has the same name\|tenant or tenant admin, the user will be able to access it.

In case at step 3, if the user logs out, then the associated cache is cleared; furthermore, the user at step 5 cannot see the results.

As of JasperReports Server 7.1, the REST v1 login service (rest/login) was deprecated and removed from the API. It is replaced with the similar REST v2 login service (rest_v2/login). This section documents the use of the new rest_v2/login API.

The rest_v2/login service allows REST clients to submit authentication credentials in several ways and receive a server cookie that can be used to identify the user session in subsequent API operations. The supported authentication methods are:

- Login with the username and password in the URL arguments.
- Login with username and password in the request body.
- Login with a ticket for servers configured for Single Sign-On (SSO).

When external authentication such as LDAP is configured in the server, clients are still required to submit the username and password in one of the first two methods above.

Sending passwords in plain text is strongly discouraged, therefore Jaspersoft recommends that you configure your server and clients to use HTTPS, or that you use the login encryption feature. For more information, see 1.1, “Login Encyrption,” on page 1.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th>Method</th>
<th colspan="3">URL</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>POST</p>
<p>GET (config.)</p></td>
<td colspan="3"><p><span>http[s]://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/login</span>[?&lt;arguments&gt;]</span></p>
<p><span>http[s]://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/login</span>?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>j_username</span></p></td>
<td><p>Text</p></td>
<td colspan="2"><p>The user ID. In commercial editions of the server that implement multiple organizations, the argument must specify the organization ID or alias in the following format: <span>j_username%7CorgID</span> (<span>%7C</span> is the encoding for the | character).</p></td>
</tr>
<tr>
<td><p><span>j_password</span></p></td>
<td><p>Text</p></td>
<td colspan="2"><p>The user’s password. The argument is optional but authentication fails without the password. If the server has login encryption enabled, the password must be encrypted as explained in <span>1.1, “Login Encryption,” on page 1</span>.</p></td>
</tr>
<tr>
<td><p><span>ticket</span></p></td>
<td><p>Text</p></td>
<td colspan="2"><p>The user's ticket for your SSO mechanism, when enabled. This argument is not valid when j_username and j_password are specified. For example:</p>
<p>ticket=ST-40-CZeUUnGPxEqgScNbxh9l-sso-cas.example.com</p>
<p>The default parameter name for an SSO authentication token is <code>ticket</code>. This parameter name can be changed in the configuration file <span>WEB-INF/applicationContext-externalAuth-&lt;sso&gt;.xml</span>.</p></td>
</tr>
<tr>
<td><span>userLocale</span></td>
<td>Java locale string</td>
<td colspan="2">An optional argument to set the locale for this user session. The locale can affect both server strings such as messages and report content if localized by Domains. The server sets a cookie with this value so that it is used in every subsequent request until changed. When omitted, the server's default locale is used during this session. Specify a Java locale string such as <code>fr</code> (French) or <code>de</code> (German).</td>
</tr>
<tr>
<td><span>userTime</span><br />
<span>zone</span></td>
<td>Java time zone</td>
<td colspan="2">An optional argument to set the time zone for this user. The server sets a cookie with this value so that it is used in every subsequent request until changed. When omitted, the server's default time zone is used during this session. The time zone names are those supported by <code>java.time.ZoneID</code>, which are defined in the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">tz database</a>.</td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/x-www-form-urlencoded</span></p></td>
<td colspan="2"><p><span>j_username=&lt;userID&gt;[%7C&lt;organizationID&gt;]&amp;j_password=&lt;password&gt;</span></p>
<p>Example: <span>j_username=jasperadmin&amp;j_password=jasperadmin</span></p>
<p>or <span>j_username=jasperadmin%7Corganization_1&amp;j_password=jasperadmin</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - Session ID in cookie, body of response is empty.</p></td>
<td><p>400 Bad Request - Missing j_username or j_password.</p>
<p>401 Unauthorized - Login failed, body of response is empty.</p>
<p>403 Forbidden - License expired or otherwise not valid.</p></td>
</tr>
</tbody>
</table>

Because browsers submit URLs with the GET method, you can test the login service and test credentials by submitting requests from a web browser. With developer tools in your browser, you can see the server's response, and when successful, the session cookie it contains. Credentials must be passed as arguments in the URL, as shown in the following example:

``` text
http[s]://<host>:<port>/jasperserver[-pro]/rest_v2/login?j_username=<userID>[%7C<orgID>]&
j_password=<password>
```

Client applications typically use the POST method, and they gather the session cookie from the response to use in future requests. Credentials can be sent either in the URL arguments, as shown above, or in the content of the request, as shown in the following example:

``` text
POST /jasperserver/rest_v2/login HTTP/1.1
User-Agent: Jakarta Commons-HttpClient/3.1
Host: localhost:8080
Content-Length: 45
Content-Type: application/x-www-form-urlencoded
j_username=jasperadmin%7Corganization_1&j_password=jasperadmin
```

When the login is successful, the server sends the "200 OK" response containing a cookie for the session ID of the now-logged-in user:

``` text
HTTP/1.1 200 OK
Server: Apache-Coyote/1.1
Set-Cookie: JSESSIONID=52E79BCEE51381DF32637EC69AD698AE; Path=/jasperserver
Content-Length: 0
Date: Fri, 3 Aug 2018 01:52:48 GMT
```

For optimal performance, the session ID from the cookie should be used to keep the session open. Usually, your REST library will automatically include the cookie in future requests to the other RESTful services. For example, given the response to the POST request above, future requests to the repository services should include the following line in the header:

``` yaml
Cookie: $Version=0; JSESSIONID=52E79BCEE51381DF32637EC69AD698AE; $Path=/jasperserver
```

By default, the session timeout on the server is 20 minutes of inactivity. Beyond that time, requests using the session cookie fails due to lack of authentication. Your client will need to authenticate again using any of the methods described in this chapter.

Maintaining a session with cookies is not mandatory, and your application can use any combination of session cookie, stateless authentication, or both. However, if you use the session ID, it is good practice to close the session as described in 1.1, “Logout,” on page 1. Closing the session frees up any associated resources in memory.

## Login Encryption (Deprecated)

As of release 7.5, the HTTP parameter encryption described in this section is deprecated. This feature is no longer supported because the Javascript libraries it uses are no longer supported. Jaspersoft recommends using TLS (Transport Level Security) to implement HTTPS and secure communication between your users and the server.

JasperReports Server supports the ability to encrypt plain-text passwords over non-secure HTTP. Encryption does not make passwords more secure, it only prevents them from being readable to humans. For more information about security and how to enable login encryption, see the JasperReports Server Security Guide.

When login encryption is enabled, passwords in both HTTP Basic Authentication and using the login service must be encrypted by the client. Login encryption has two modes:

- Static key encryption – The server only uses one key that never changes. The client only needs to encrypt the password once and can use it for every REST service request.
- Dynamic key encryption – The server changes the encryption key for every request. The client must request the new key and re-encrypt the password before every request using HTTP Basic Authentication including the login service.

The GetEncryptionKey service does not take any arguments or content input.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th>Method</th>
<th colspan="3">URL</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>GetEncryptionKey</span></span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Body contains a JSON representation of public key:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;maxdigits&quot;</span><span class="fu">:</span><span class="st">&quot;131&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;e&quot;</span><span class="fu">:</span><span class="st">&quot;10001&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;n&quot;</span><span class="fu">:</span><span class="st">&quot;9f8a2dc4baa260a5835fa33ef94c...&quot;</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
<td><p>200 OK – Body contains {Error: Key generation is off}</p></td>
</tr>
</tbody>
</table>

After using this service to obtain the server’s public key, your client must encrypt the user's password with the public key using the Bouncy Castle library and the RSA/NONE/NoPadding algorithm. Then your client can send the encrypted password in simple authentication or using the login service.

## Logout

While REST calls are often stateless, JasperReports Server uses a session to hold some information such as generated reports. The session and its report data take up space in memory and it's good practice to explicitly close the session when it is no longer needed. This allows the server to free up and reuse resources much faster.

To close a session and free its resources, invoke the logout page. The request must include the JSESSIONID cookie, which your REST client libraries should do automatically.

<table>
<thead>
<tr>
<th>Method</th>
<th colspan="3">URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>GET</td>
<td colspan="3"><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/logout.html</span></td>
</tr>
<tr>
<td colspan="4">Header</td>
</tr>
<tr>
<td colspan="4"><span>Cookie: $Version=0; JSESSIONID=52E79BCEE51381DF32637EC69AD698AE; $Path=/jasperserver</span></td>
</tr>
</tbody>
</table>
