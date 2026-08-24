---
title: About Access Grant Definitions
description: An access grant definition is an XML file that specifies each role’s access rights to various parts of the data defined in a cube. It refers to access roles defined in JasperReports Server as well as...
---

# About Access Grant Definitions

An access grant definition is an XML file that specifies each role’s access rights to various parts of the data defined in a cube. It refers to access roles defined in JasperReports Server as well as levels in dimensions defined in a particular cube. An access grant definition can control access at any level of your dimensions, and like an OLAP schema, it follows the Mondrian XML format.

CZS started by securing their data along the Geographical Area dimension of the cube. A simple access grant for this dimension might be similar to the following:

|  |
|----|
| \<MemberGrant member=“\[Geographic Area\].\[USA\].\[West\].\[CA\]” access=“all”/\> |

This member grant gives the role in question full access to the CA (California) member of the dimension. California is at the state level of the dimension; you could just as easily grant access to all of the West region or to individual cities.

The following code fragment shows the above member grant in the context of a full role definition. It grants the ROLE_CA role access to all California data:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><p>&lt;Roles&gt;</p>
<p>&lt;Role name="ROLE_CA"&gt;</p>
<p>&lt;SchemaGrant access="none"&gt;</p>
<p>&lt;CubeGrant cube="Sales" access="all"&gt;</p>
<p>&lt;HierarchyGrant hierarchy="[Geographical Area]" access="custom"</p>
<p>topLevel="[Geographical Area].[State]"</p>
<p>bottomLevel="[Geographical Area].[City]"&gt;</p>
<p>&lt;MemberGrant member="[Geographical Area].[USA].[Western].[CA]" access="all"/&gt;</p>
<p>&lt;/CubeGrant&gt;</p>
<p>&lt;/SchemaGrant&gt;</p>
<p>&lt;/Role&gt;</p>
<p>&lt;Roles&gt;</p></td>
</tr>
</tbody>
</table>

Returning to the business case requirements, CZS also wants to grant access based on the Product dimension. To do so, they could add a hierarchy grant like the following one to the cube grant:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><p>&lt;Roles&gt;</p>
<p>&lt;Role name ="ROLE_CA"&gt;</p>
<p>&lt;SchemaGrant access="none"&gt;</p>
<p>&lt;CubeGrant cube="Sales" access="all"&gt;</p>
<p>&lt;HierarchyGrant hierarchy="[Geographical Area]" access="custom"</p>
<p>topLevel="[Geographical Area].[State]"</p>
<p>bottomLevel="[Geographical Area].[City]"&gt;</p>
<p>&lt;MemberGrant member="[Geographical Area].[USA].[Western].[CA]" access="all"/&gt;</p>
<p>&lt;/HierarchyGrant&gt;</p>
<p>&lt;HierarchyGrant hierarchy="[Product]" access="custom"</p>
<p>topLevel="[Product].[Product Family]"</p>
<p>bottomLevel="[Product].[Product Department]"&gt;</p>
<p>&lt;MemberGrant member="[Product].[Electronics].[WirelessDevices]" access="all"/&gt;</p>
<p>&lt;/HierarchyGrant&gt;</p>
<p>&lt;/CubeGrant&gt;</p>
<p>&lt;/SchemaGrant&gt;</p>
<p>&lt;/Role&gt;</p>
<p>&lt;/Roles&gt;</p></td>
</tr>
</tbody>
</table>

Additionally, CZS could use an AGXML file to define access for multiple roles, as in the following example, which grants access to a second role called ROLE_SF:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><p>&lt;Roles&gt;</p>
<p>&lt;Role name="ROLE_CA"&gt;</p>
<p>&lt;SchemaGrant access="none"&gt;</p>
<p>&lt;CubeGrant cube="Sales" access="all"&gt;</p>
<p>&lt;HierarchyGrant hierarchy="[Geographical Area]" access="custom"</p>
<p>topLevel="[Geographical Area].[State]"</p>
<p>bottomLevel="[Geographical Area].[City]"&gt;</p>
<p>&lt;MemberGrant member="[Geographical Area].[USA].[Western].[CA] access="all" /&gt;</p>
<p>&lt;/HierarchyGrant&gt;</p>
<p>&lt;HierarchyGrant hierarchy="[Product]" access="custom"</p>
<p>topLevel="[Product].[Product Family]"</p>
<p>bottomLevel="[Product].[Product Department]"&gt;</p>
<p>&lt;MemberGrant member="[Product].[Electronics].[Wireless Devices]" access="all" /&gt;</p>
<p>&lt;/HierarchyGrant&gt;</p>
<p>&lt;/CubeGrant&gt;</p>
<p>&lt;/SchemaGrant&gt;</p>
<p>&lt;/Role&gt;</p>
<p>&lt;Role name="ROLE_SF"&gt;</p>
<p>&lt;SchemaGrant access="none"&gt;</p>
<p>&lt;CubeGrant cube="Sales" access="all"&gt;</p>
<p>&lt;HierarchyGrant hierarchy="[Geographical Area]" access="custom"</p>
<p>topLevel="[Geographical Area].[City]"</p>
<p>bottomLevel="[Geographical Area].[City]"&gt;</p>
<p>&lt;MemberGrant member="[Geographical Area].[USA].[Western].[CA].[San Francisco]" access="all" /&gt;</p>
<p>&lt;/HierarchyGrant&gt;</p>
<p>&lt;HierarchyGrant hierarchy="[Product]" access="custom"</p>
<p>topLevel="[Product].[Product Family]"</p>
<p>bottomLevel="[Product].[Product Department]"&gt;</p>
<p>&lt;MemberGrant member="[Product].[Electronics].[Irrelevances]" access="all" /&gt;</p>
<p>&lt;/HierarchyGrant&gt;</p>
<p>&lt;/CubeGrant&gt;</p>
<p>&lt;/SchemaGrant&gt;</p>
<p>&lt;/Role&gt;</p>
<p>&lt;/Roles&gt;</p></td>
</tr>
</tbody>
</table>

However, the complexity of a complete implementation structured as shown would require reams of XML and an access role configuration that took into account geographical location. To avoid this complexity, CZS defined user-level attributes that describe each user in terms of geography and product. Then, using variables to represent the attributes, they wrote access grant definitions, as described in the following sections.
