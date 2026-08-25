---
title: Deleting Attributes
description: "The DELETE method of the attributes service removes attributes from the specified entity (a user, an organization, or the server-level). When attributes are removed, both the name and the value of..."
---

# 1.0.1 Deleting Attributes

The DELETE method of the attributes service removes attributes from the specified entity (a user, an organization, or the server-level). When attributes are removed, both the name and the value of the attribute are removed, not only the value. For possible values of \<entity\> in the URL, see [1.1.2, “Entities with Attributes,” on page 1](the_v2_attributes_service.md).

There are two syntaxes; the following one is for deleting multiple attributes or all attributes at once.

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
<td><p>DELETE</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/</span>&lt;entity&gt;<strong>attributes</strong>?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>name</code></pre></div></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specify an attribute name to remove that attribute. Repeat this argument to delete multiple attributes. When this argument is omitted, all attributes are deleted from the given entity.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content – The attributes were successfully removed from the given entity.</p></td>
<td><p>404 Not Found – When the user ID or organization ID does not match any user or organization. The content includes an error message.</p>
<p>400 Bad Request – When an attribute name is null, blank, or too long (see <a href="the_v2_attributes_service.md">1.1.5, “Attribute Limitations,” on page 1</a>). If one attribute causes an error, the operation stops and returns an error, but attributes that were already deleted remain deleted.</p></td>
</tr>
</tbody>
</table>

The second syntax deletes a single attribute named in the URL from the specified entity.

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
<td><p>DELETE</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/</span>&lt;entity&gt;<strong>attributes</strong>/attrName</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content – The attribute was successfully removed from the given entity.</p></td>
<td><p>404 Not Found – When the user ID, organization ID, or attribute name does not match any user, organization, or attribute. The content includes an error message.</p>
<p>400 Bad Request – When an attribute name is null, blank, or too long (see <a href="the_v2_attributes_service.md">1.1.5, “Attribute Limitations,” on page 1</a>).</p></td>
</tr>
</tbody>
</table>
