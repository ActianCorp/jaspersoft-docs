---
title: Overview of Data-level Access Using AGXML Schemas
description: An access grant definition depends on elements of the OLAP schema associated with a connection. That OLAP schema must contain cubes with the same name and structure as appear in the access grant...
---

# Overview of Data-level Access Using AGXML Schemas

An access grant definition depends on elements of the OLAP schema associated with a connection. That OLAP schema must contain cubes with the same name and structure as appear in the access grant definition’s CubeGrant elements. If you specify access grants down to the member level, the references to member values in the access grant definition must be in the database defined by the connection.

You create an access grant definition as an XML file with an AGXML file extension. To use it, import it into the repository, or upload it while creating an OLAP client connection, just as you can upload an OLAP schema.

The elements are arranged hierarchically, as shown below. The grant definitions for a role lie within the following nested grant elements: `SchemaGrant, CubeGrant, HierarchyGrant`, and `MemberGrant`. `SchemaGrant` is the outermost element, and `MemberGrant` is the innermost. In general, grants within an element override grants in containing elements.

```
SchemaGrant
    CubeGrant
        HierarchyGrant
            MemberGrant
```

The following table describes the attributes of the grant elements and lists possible attribute values:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th><p>Grant Element</p></th>
<th><p>Attribute</p></th>
<th><p>Attribute Description</p></th>
<th><p>Values</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>SchemaGrant</p></td>
<td><p><code>access</code></p></td>
<td><p>Defines the default access for any object in the schema.</p></td>
<td><ul>
<li><code>all</code></li>
<li><code>none</code></li>
</ul></td>
</tr>
<tr>
<td><p>CubeGrant</p></td>
<td><p><code>access</code></p></td>
<td><p>Defines the default access to hierarchies within the cube specified by its cube attribute.</p>
<p>If the schema contains cubes for which no CubeGrant element appears, then the default access defined at the SchemaGrant level applies to those cubes.</p></td>
<td><ul>
<li><code>all</code></li>
<li><code>none</code></li>
</ul></td>
</tr>
<tr>
<td rowspan="2"><p>HierarchyGrant</p></td>
<td><p><code>access</code></p></td>
<td><p>Defines the role’s access to the hierarchy specified by the <code>hierarchy</code> attribute. If <code>access = custom</code>, MemberGrant sub-elements define the role’s access within the hierarchy.</p>
<p>If a cube contains hierarchies for which no HierarchyGrant element appears, then the default access defined at the CubeGrant level applies to those hierarchies.</p></td>
<td><ul>
<li><code>all</code></li>
<li><code>none</code></li>
<li><code>custom</code></li>
</ul></td>
</tr>
<tr>
<td><code>topLevel</code>
<p><code>bottomLevel</code></p></td>
<td><p>Defines the segment of the hierarchy that users with the given role can see. They can see everything between and including the endpoints. Nothing in an enclosed MemberGrant element can override the <code>topLevel</code> and <code>bottomLevel</code> attributes.</p></td>
<td>(varies)</td>
</tr>
<tr>
<td rowspan="2"><p>MemberGrant</p></td>
<td><p><code>member</code></p></td>
<td><p>Specifies the top level of the hierarchy defined by the enclosing HierarchyGrant element to which the MemberGrant’s <code>access </code>attribute applies. For example, if the member value is [Store].[USA].[CA], the top level to which the <code>access</code> attribute applies is California in the Store hierarchy.</p></td>
<td><p>(varies)</p></td>
</tr>
<tr>
<td><p><code>access</code></p></td>
<td><p>Defines everything including or below the level specified by the member attribute, except that it cannot grant access to anything outside the segment defined by the HierarchyGrant attributes <code>topLevel</code> and <code>bottomLevel</code>.</p></td>
<td><ul>
<li><code>all</code></li>
<li><code>none</code></li>
</ul></td>
</tr>
</tbody>
</table>

The `topLevel` and `bottomLevel` attributes use a dot notation to specify a level in the hierarchy. In the example in [Sample Access Grant Definition](sample_access_grant_definition.md), the `topLevel` attribute for the Store hierarchy has the value `[Store].[Store.Country]`. The `[Store]` designates the Store hierarchy. The `[Store.Country]` designates the Country level of the Store hierarchy.

You can use substitution variables in the grant expressions that specify the values of the `topLevel`, `bottomLevel`, and `member` attributes. The example in [Sample Access Grant Definition](sample_access_grant_definition.md) includes variable substitution.

Jaspersoft OLAP applies grants in the order that you define them. For example, if you grant access to the USA and then deny access to Oregon, an affected user cannot see Oregon or any of its children (for example, Portland). But if you deny access to Oregon and then grant access to the USA, the user can see Oregon and all of its children.

Granting access to a member also grants access to the levels above it, except that the grant cannot override the HierarchyGrant’s `topLevel` attribute. For example, if you deny access to the USA and then grant access to California, an affected user can see California and the USA, but no other states. If the data includes USA totals, they are based on data from all states.

You can test access grant definitions by creating users with various roles and logging in to them. For more information on roles, users, and the **Log in As** feature, refer to the JasperReports Server Administrator Guide and the JasperReports Server Security Guide. The Jaspersoft OLAP Ultimate Guide also includes a detailed implementation example.

!!! note

    Names of roles, users, hierarchical levels, and attributes are all case-sensitive in access grant definitions.
