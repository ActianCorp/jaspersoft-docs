---
title: Invalidating Active Sessions for Deleted User
description: "After an administrator deletes a user, JasperReports Server automatically ends the active session. The system ends the user session when the user is deleted."
---

# Invalidating Active Sessions for Deleted User

After an administrator deletes a user, JasperReports Server automatically ends the active session. The system ends the user session when the user is deleted.

To handle session invalidation for such users, a custom filter `DeletedUserProcessingClusterFilter` , is implemented. This filter checks if the user exists, and based on the result, the session is either continued or invalidated. This filter is triggered only when the `user.exists.check.enabled` property is set to `true`.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Invalidate Active Session</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>js.config.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><code>user.exists.check.interval</code></td>
<td><code>60000</code> &lt;default&gt;</td>
<td>Set the time interval, in milliseconds, to check if the user exists.</td>
</tr>
<tr>
<td><p><code>user.exists.check.enabled</code><br />
</p></td>
<td><p><code>true</code> or</p>
<p><code>false</code></p></td>
<td><p>Based on the value provided in <code>user.exists.check.interval</code>, checks if the user is active or has been deleted by the admin.</p>
<ul>
<li><p>If set to <code>true</code>, the filter checks if the user is deleted and the user sessions are invalidated.</p></li>
<li><p>If set to <code>false</code>, the filter is ignored.</p></li>
</ul></td>
</tr>
</tbody>
</table>
