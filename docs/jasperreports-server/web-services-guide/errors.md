---
title: Errors
description: "When the repository web service returns a code other than 0, an error has occurred during the server execution. The exact error is described in the message field of the operation result."
---

# 1.1 Errors

When the repository web service returns a code other than 0, an error has occurred during the server execution. The exact error is described in the message field of the operation result.

If the problem is environmental, such as an incorrect service URL, an incorrect user name or password, network errors, or an unavailable service, a web services error is retuned.

!!! note

    In deployments with multiple organizations, the organization ID must be included in the user name in the format `username|organization_ID`. When there is only one organization exists in JasperReports Server, such as in the default installation, specify the user name alone.

The following shows an Axis connection refused error:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>AxisFault
faultCode: {http://schemas.xmlsoap.org/soap/envelope/}Server.userException
faultSubcode:
faultString: java.net.ConnectException: Connection refused: connect
faultActor:
faultNode:
faultDetail:
{http://xml.apache.org/axis/}stackTrace:java.net.ConnectException: Connection refused: connect
at java.net.PlainSocketImpl.socketConnect(Native Method)
at java.net.PlainSocketImpl.doConnect(PlainSocketImpl.java:333)
at java.net.PlainSocketImpl.connectToAddress(PlainSocketImpl.java:195)
at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:182)
at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:366)</code></pre></td>
</tr>
</tbody>
</table>

The following shows an Axis user name/password error:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>AxisFault
faultCode: {http://xml.apache.org/axis/}HTTP
faultSubcode:
faultString: (401)Bad credentials
faultActor:
faultNode:
faultDetail:
:return code: 401</code></pre></td>
</tr>
<tr>
<td><pre class="text"><code>&amp;lt;html&amp;gt;&amp;lt;head&amp;gt;&amp;lt;title&amp;gt;Apache Tomcat/5.5.16 - Error re
port&amp;lt;/title&amp;gt;&amp;lt;style&amp;gt;&amp;lt;!--H1 {font-family:Tahoma,Arial,sans-serif;co
lor:white;background-color:#525D76;font-size:22px;} H2 {font-family:Tahoma,Arial
,sans-serif;color:white;background-color:#525D76;font-size:16px;} H3 {font-famil
y:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:14px;}
BODY {font-family:Tahoma,Arial,sans-serif;color:black;background-color:white;} B
{font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;} P {
font-family:Tahoma,Arial,sans-serif;background:white;color:black;font-size:12px;
}A {color : black;}A.name {color : black;}HR {color : #525D76;}--&amp;gt;&amp;lt;/style&amp;
gt; &amp;lt;/head&amp;gt;&amp;lt;body&amp;gt;&amp;lt;h1&amp;gt;HTTP Status 401 - Bad credentials&amp;lt;/h1&amp;
gt;&amp;lt;HR size=&amp;quot;1&amp;quot; noshade=&amp;quot;noshade&amp;quot;&amp;gt;&amp;lt;p&amp;gt;&amp;lt;b&amp;gt;ty
pe&amp;lt;/b&amp;gt; Status report&amp;lt;/p&amp;gt;&amp;lt;p&amp;gt;&amp;lt;b&amp;gt;message&amp;lt;/b&amp;gt; &amp;lt;u&amp;gt
;Bad credentials&amp;lt;/u&amp;gt;&amp;lt;/p&amp;gt;&amp;lt;p&amp;gt;&amp;lt;b&amp;gt;description&amp;lt;/b&amp;gt; &amp;lt;
u&amp;gt;This request requires HTTP authentication (Bad credentials).&amp;lt;/u&amp;gt;&amp;lt;/
p&amp;gt;&amp;lt;HR size=&amp;quot;1&amp;quot; noshade=&amp;quot;noshade&amp;quot;&amp;gt;&amp;lt;h3&amp;gt;Apache T
omcat/5.5.16&amp;lt;/h3&amp;gt;&amp;lt;/body&amp;gt;&amp;lt;/html&amp;gt;
{http://xml.apache.org/axis/}HttpErrorCode:401</code></pre></td>
</tr>
<tr>
<td><pre class="text"><code>(401)Bad credentials
at org.apache.axis.transport.http.HTTPSender.readFromSocket(HTTPSender.java:744)
at org.apache.axis.transport.http.HTTPSender.invoke(HTTPSender.java:144)
at org.apache.axis.strategies.InvocationStrategy.visit(InvocationStrategy.java:32)
at org.apache.axis.SimpleChain.doVisiting(SimpleChain.java:118)
at org.apache.axis.SimpleChain.invoke(SimpleChain.java:83)
at org.apache.axis.client.AxisClient.invoke(AxisClient.java:165)</code></pre></td>
</tr>
</tbody>
</table>
