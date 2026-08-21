---
title: Error When Opening Ad Hoc View With Bundles
description: "When you are logged in as a superuser and you attempt to open the Ad Hoc View with bundles, Can't find bundle error is shown. Ideally the Ad Hoc View should open without any errors."
---

# Error When Opening Ad Hoc View With Bundles

When you are logged in as a superuser and you attempt to open the Ad Hoc View with bundles, **Can't find bundle** error is shown. Ideally the Ad Hoc View should open without any errors.

To fix this issue, the cache must be cleared before loading resource bundle.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Clearing the Cache Before Loading Resource Bundle</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/js.config.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><code>adhoc.bundleCache.resetIfMissing</code></p></td>
<td colspan="2"><p>To clear the bundle cache if a resource cannot be found. By default, it is set to <code>false</code></p>
<p>If a resource cannot be found, set <code>adhoc.bundleCache.resetIfMissing=true</code></p></td>
</tr>
<tr>
<td><code>adhoc.bundleCache.forceClear</code></td>
<td colspan="2"><p>To clear the bundle cache. By default, it is set to <code>true</code>.</p>
<p>To clear the bundle cache, set <code>adhoc.bundleCache.forceClear=true</code>.</p></td>
</tr>
</tbody>
</table>
