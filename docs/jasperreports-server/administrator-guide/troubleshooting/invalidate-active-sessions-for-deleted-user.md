---
title: Invalidate Active Session for Deleted User
description: "When a user logged into two browser tabs is deleted in one of the tabs and tries to perform any action in the other tab, the user is logged out of the system. This is because all the active sessions..."
---

# Invalidate Active Session for Deleted User

When a user logged into two browser tabs is deleted in one of the tabs and tries to perform any action in the other tab, the user is logged out of the system. This is because all the active sessions for the deleted user are invalidated.

<table>
<thead>
<tr>
<th colspan="3"><p>Invalidate Active Session for Deleted User</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>jasperserver/buildomatic/conf_source/templates/js.config.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><code>user.exists.check.enabled</code></td>
<td colspan="2"><p>Enables the filter to check if the request is from a deleted user, and stop active sessions, if any. By default, the value is <code>true</code>.</p></td>
</tr>
<tr>
<td><code>user.exists.check.interval</code></td>
<td colspan="2">Determines the time interval, in milliseconds, after which a check is performed to see if the user exists. By default, the value is <code>60000</code>.</td>
</tr>
</tbody>
</table>
