---
title: The permissions Service
description: The restv2/permissions service reads and sets permissions on resources in the repository.
---

# The permissions Service

The rest_v2/permissions service reads and sets permissions on resources in the repository.

This chapter includes the following sections:

- Permission Constants
- Viewing Multiple Permissions
- Viewing a Single Permission
- Setting Multiple Permissions
- Setting a Single Permission
- Deleting Multiple Permissions
- Deleting a Single Permission

## Permission Constants

In the permissions service, the syntax allows you to specify the resource, the recipient (user name or role name), and the permission value within the URL. This makes it simpler to set permissions because you do not need to send a resource descriptor to describe the permissions. To set, modify, or delete permissions, you must use credentials or login with a user that has "administer" permissions on the target resource.

The permissions for each user and each role are indicated by the following values. These values are not a true mask; they should be treated as constants:

- No access: 0
- Administer: 1
- Read-only: 2
- Read-write: 6
- Read-delete: 18
- Read-write-delete: 30
- Execute-only: 32

Because a permission can apply to either a user or a role, the permissions service uses the concept of a recipient. A recipient specifies whether the permission applies to a user or a role, and gives the ID of the user or role, including any organization, for example:

role:/ROLE_ADMINISTRATOR (this is a root role and thus has no organization specified).

user:/organization_1/joeuser

Recipients are listed when viewing permissions, and they are also used to set a permission. A recipient can be specified in a URL parameter when allowed, but in this case, the slash (/) character must be encoded as %2F.

There are two qualities of a permission:

- The assigned permission is one that is set explicitly for a given resource and a given user or role. Not all permissions are assigned, in which case the permission is inherited from the parent folder.
- The effective permission is the permission that is being enforced, whether it is assigned or inherited.

!!! note

    There is one permission that is not defined: you cannot read or write the permission for ROLE_SUPERUSER on the root.

## Viewing Multiple Permissions

The GET method of the permissions service lists permissions on a given resource according to several arguments.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/permissions</span>/path/to/resource/?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>effective<br />
Permissions</span></p></td>
<td><p>Boolean<br />
optional</p></td>
<td colspan="2"><p>When set to true, the effective permissions are returned. By default, this argument is false and only assigned permissions are returned.</p></td>
</tr>
<tr>
<td><p><span>recipientType</span></p></td>
<td><p>String<br />
optional</p></td>
<td colspan="2"><p>Either <code>user</code> or <code>role</code>. When not specified, the recipient type is the role.</p></td>
</tr>
<tr>
<td><p><span>recipientId</span></p></td>
<td><p>String<br />
optional</p></td>
<td colspan="2"><p>Id of the user or role. In environments with multiple organizations, specify the organization as <span>%2F&lt;orgID&gt;%2F&lt;recipientID&gt;</span> (%2F is the / character).</p></td>
</tr>
<tr>
<td><p><span>resolveAll</span></p></td>
<td><p>Boolean<br />
optional</p></td>
<td colspan="2"><p>When set to true, shows the effective permissions for all users and all roles.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml (default)</span></p>
<p><span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The body describes the requested permissions for the resource.</p></td>
<td><p>400 Bad Request - When the recipient type is invalid.</p>
<p>404 Not Found - When the specified resource URI is not found in the repository or the recipient ID cannot be resolved.</p></td>
</tr>
</tbody>
</table>

For example, the following request shows all permission for a resource, similar to the permissions dialog in the user interface:

GET http://localhost:8080/jasperserver-pro/rest_v2/permissions/public?resolveAll=true

``` xml
<permissions>
  <permission>
    <mask>0</mask>
    <recipient>user:/anonymousUser</recipient>
  </permission>
  <permission>
    <mask>0</mask>
    <recipient>user:/organization_1/CaliforniaUser</recipient>
  </permission>
  ...
  <permission>
    <mask>2</mask>
    <recipient>role:/ROLE_USER</recipient>
    <uri>/public</uri>
  </permission>
</permissions>
```

## Viewing a Single Permission

Specify the recipient in the URL to see a specific assigned permission. To view effective permissions, use the form above.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/permissions</span>/path/to/resource;recipient=<br />
&lt;recipient&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>recipient</span></p></td>
<td><p>string required</p></td>
<td colspan="2"><p>The recipient format specifies the <code>user</code> or <code>role</code>, the object ID, and the organization ID if necessary. The slash character must be encoded, for example:</p>
<p><span>user:%2Forganization_1%2Fjoeuser</span></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span> (default)</p>
<p><span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The body describes the requested permission.</p></td>
<td><p>404 Not Found - When the specified resource URI or recipient is invalid, or when the recipient does not have any assigned permission (only inherited).</p></td>
</tr>
</tbody>
</table>

## Setting Multiple Permissions

The POST method assigns any number of permissions to any number of resources specified in the body of the request. All permissions must be newly assigned, and the request will fail if a recipient already has an assigned (not inherited) permission. Use the PUT method to update assigned permissions.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/permissions</span></span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/collection+json</span></p></td>
<td colspan="2"><p>A JSON object that describes a set of permissions, for example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;permission&quot;</span> <span class="fu">:</span><span class="ot">[</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;/properties&quot;</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;recipient&quot;</span><span class="fu">:</span><span class="st">&quot;role:/ROLE_USER&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;mask&quot;</span><span class="fu">:</span><span class="st">&quot;1&quot;</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;/properties&quot;</span><span class="fu">,</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;recipient&quot;</span><span class="fu">:</span><span class="st">&quot;role:/ROLE_ADMINISTRATOR&quot;</span><span class="fu">,</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;mask&quot;</span><span class="fu">:</span><span class="st">&quot;32&quot;</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a><span class="ot">]</span><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The request was successful.</p></td>
<td><p>400 Bad Request - A permission is already assigned or the given permission mask is invalid.</p></td>
</tr>
</tbody>
</table>

The PUT method modifies exiting permissions (already assigned).

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>PUT</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/permissions</span>/path/to/resource</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/collection+json</span></p></td>
<td colspan="2"><p>A JSON object that describes a set of permissions. Because a single resource is specified in the URL, all permissions apply to the same resource, and the server ignores the <code>uri</code> field in the JSON object.</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;permission&quot;</span> <span class="fu">:</span><span class="ot">[</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;/foo&quot;</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;recipient&quot;</span><span class="fu">:</span><span class="st">&quot;role:/organization_1/ROLE_MANAGER&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;mask&quot;</span><span class="fu">:</span><span class="st">&quot;30&quot;</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;/bar&quot;</span><span class="fu">,</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;recipient&quot;</span><span class="fu">:</span><span class="st">&quot;user:/organization_1/joeuser&quot;</span><span class="fu">,</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;mask&quot;</span><span class="fu">:</span><span class="st">&quot;32&quot;</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a><span class="ot">]</span><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The request was successful.</p></td>
<td><p>400 Bad Request - If a recipient or mask is invalid.</p>
<p>404 Not Found - If the resource in the URL is invalid.</p></td>
</tr>
</tbody>
</table>

## Setting a Single Permission

The POST method accepts a single permission descriptor.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/permissions</span></span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><p>A JSON object that describes a single permission on a single resource, for example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;/properties&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;recipient&quot;</span><span class="fu">:</span><span class="st">&quot;role:/ROLE_USER&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;mask&quot;</span><span class="fu">:</span><span class="st">&quot;1&quot;</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The request was successful.</p></td>
<td><p>400 Bad Request - The permission is already assigned or the given mask is invalid.</p></td>
</tr>
</tbody>
</table>

The PUT method accepts a resource and recipient in the URL.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>PUT</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/permissions</span>/path/to/resource;recipient=<br />
&lt;recipient&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>recipient</span></p></td>
<td><p>string required</p></td>
<td colspan="2"><p>The recipient format specifies the <code>user</code> or <code>role</code>, the organization if necessary, and the object ID. The slash characters must be encoded, for example:</p>
<p><span>user:%2Forganization_1%2Fjoeuser</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><p>A JSON object that describes only the mask, for example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;recipient&quot;</span><span class="fu">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;mask&quot;</span><span class="fu">:</span><span class="st">&quot;2&quot;</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The request was successful, and the response body contains the single permission that was modified.</p></td>
<td><p>400 Bad Request - If the mask is invalid.</p>
<p>404 Not Found - If the resource or the recipient in the URL is invalid.</p></td>
</tr>
</tbody>
</table>

## Deleting Multiple Permissions

The DELETE method removes all assigned permissions from the designated resource. After returning successfully, all effective permissions for the resource are inherited.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/permissions</span>/path/to/resource</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content - The request was successful.</p></td>
<td><p>404 Not Found - If the resource in the URL is invalid.</p></td>
</tr>
</tbody>
</table>

## Deleting a Single Permission

Specify a recipient in the URL of the DELETE method to remove only that permission.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/permissions</span>/path/to/resource;recipient=<br />
&lt;recipient&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>recipient</span></p></td>
<td><p>string required</p></td>
<td colspan="2"><p>The recipient format specifies the <code>user</code> or <code>role</code>, the organization if necessary, and the object ID. The slash characters must be encoded, for example:</p>
<p><span>user:%2Forganization_1%2Fjoeuser</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content - The request was successful.</p></td>
<td><p>404 Not Found - If the resource or the recipient in the URL is invalid.</p></td>
</tr>
</tbody>
</table>
