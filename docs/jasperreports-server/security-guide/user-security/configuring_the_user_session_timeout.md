---
title: Configuring the User Session Timeout
description: "After a period of inactivity, JasperReports Server displays a pop-up notice that the user's session is about to timeout. This gives the user a chance to continue without being logged out."
---

# Configuring the User Session Timeout

After a period of inactivity, JasperReports Server displays a pop-up notice that the user's session is about to timeout. This gives the user a chance to continue without being logged out.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>User Session Timeout</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/web.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>&lt;session-config&gt;</code><br />
<code> &lt;session-timeout&gt;</code></p></td>
<td><p><code>20</code> &lt;default&gt;</p></td>
<td><p>Set the number of minutes that a user session can remain idle before an automatic log out. Setting to 0 (zero) prevents session timeouts.</p></td>
</tr>
</tbody>
</table>

Note that the session timeout also applies to how long a session remains in memory after a web service call finishes. If another web service call with the same credentials occurs within the timeout period, the server reuses the same session. If the timeout is too short for this case, you may have performance issues caused by a high load of web service calls.

If the timeout is too long, a session may stay active for a long time (even indefinitely with a timeout of 0). The risk of allowing long sessions is that the in-memory session is not updated with any role changes until the user logs out manually (ending the session) and logs in again (creating a session).
