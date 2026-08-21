---
title: Login Service
description: "When making a login request, the user ID and password can be pass as URL arguments or as content in the request body:"
---

# Login Service

When making a login request, the user ID and password can be pass as URL arguments or as content in the request body:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>POST</p>
<p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/login</span>/</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/login</span>?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>j_username</p></td>
<td><p>Text</p></td>
<td colspan="2"><p>The user ID. In commercial editions of the server that implement multiple organizations, the argument must specify the organization ID or alias in the following format: j_username%7Corganization_id (%7C is the | character).</p></td>
</tr>
<tr>
<td><p>j_password?</p></td>
<td><p>Text</p></td>
<td colspan="2"><p>The user’s password. If the server has login encryption enabled, the password must be encrypted as explained in <a href="login_encryption.md">Login Encryption</a>. The argument is optional but authentication will fail without the password.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/x-www-form-urlencoded</p></td>
<td colspan="2"><p>j_username=&lt;userID&gt;[%7C&lt;organization_id&gt;]&amp;j_password=&lt;password&gt;</p>
<p>Example: j_username=jasperadmin&amp;j_password=jasperadmin</p>
<p>or j_username=jasperadmin%7Corganization_1&amp;j_password=jasperadmin</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Session ID in cookie (POST only), empty body.</p></td>
<td><p>401 Unauthorized – Empty body.</p>
<p>302 – License expired or otherwise not valid.</p></td>
</tr>
</tbody>
</table>

The login service has several uses:

- POST method – Applications should use the POST method, because it returns the session cookie to use in future requests.
- GET method – Developers can test the login service and the user credentials from a browser, which uses the GET method.
- Credentials in arguments – When testing the login service in a browser, credentials are passed as arguments in the URL:

http://\<host\>:\<port\>/jasperserver\[-pro\]/rest/login?j_username=\<userID\>\[%7C\<organization_id\>\]<br>
&j_password=\<password\>

- Credentials in content – When using the POST method, credentials can either be sent in the URL arguments as shown above, or sent in the content of the request, as shown in the second example below.

The following example shows the HTTP request and response when testing the login service in a browser. In this case, the user credentials are passed as arguments and the browser sends a GET request. Because the GET request is meant only for testing, it does not return a cookie with the session ID.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>GET /jasperserver/rest/login?j_username=jasperadmin&amp;j_password=jasperadmin HTTP/1.1
Host: localhost:8080
User-Agent: Mozilla/5.0 (Windows NT 6.0; rv:5.0) Gecko/20100101 Firefox/5.0
Connection: keep-alive</code></pre></td>
</tr>
<tr>
<td><pre class="text"><code>HTTP/1.1 200 OK
Server: Apache-Coyote/1.1
Pragma: No-cache
Cache-Control: no-cache
Expires: Wed, 31 Dec 1969 16:00:00 PST
Content-Length: 0
Date: Fri, 19 Aug 2011 00:52:48 GMT</code></pre></td>
</tr>
</tbody>
</table>

The following example shows the content of a POST request where the credentials are passed in the content.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>POST /jasperserver/rest/login HTTP/1.1
User-Agent: Jakarta Commons-HttpClient/3.1
Host: localhost:8080
Content-Length: 45
Content-Type: application/x-www-form-urlencoded
j_username=jasperadmin&amp;j_password=jasperadmin</code></pre></td>
</tr>
<tr>
<td><pre class="text"><code>HTTP/1.1 200 OK
Server: Apache-Coyote/1.1
Set-Cookie: JSESSIONID=52E79BCEE51381DF32637EC69AD698AE; Path=/jasperserver
Content-Length: 0
Date: Fri, 19 Aug 2011 01:52:48 GMT</code></pre></td>
</tr>
</tbody>
</table>

For optimal performance, the session ID from the cookie should be used to keep the session open. To do this, include the cookie in future requests to the other RESTful services. For example, given the response to the POST request above, future requests to the repository services should include the following line in the header:

`Cookie: $Version=0; JSESSIONID=52E79BCEE51381DF32637EC69AD698AE; $Path=/jasperserver`

However, maintaining a session with cookies is not mandatory, and your application can use any combination of session cookie, HTTP Basic Authentication, or both.
