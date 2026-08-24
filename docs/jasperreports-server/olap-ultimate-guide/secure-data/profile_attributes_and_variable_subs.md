---
title: Attributes and Variable Substitution
description: "An attribute is a name-value pair defined at the user, role, organization, or server instance level; in this example, they correspond to a member of a dimension. Jaspersoft OLAP uses these attributes..."
---

# Attributes and Variable Substitution

An attribute is a name-value pair defined at the user, role, organization, or server instance level; in this example, they correspond to a member of a dimension. Jaspersoft OLAP uses these attributes to determine the access to grant to a user based on her role. Variable substitution in the access grant definition can refer to these attributes when determining access.

For example, take Rita and Alexi; both have the same role and the same access to the Sales Numbers Ad Hoc view, but CZS doesn’t want them to see the same data—Rita should see data about California and Alexi should see data about Osaka. Without attributes, this would only be possible if CZS's access roles were defined along geographical lines. Instead, CZS defines attributes that indicate each user’s geographical affiliations: Rita is responsible for California and Alexi is responsible for Osaka.

!!! note

    For the sake of simplicity, this example only includes user-level attributes. Despite this, variable substitution can be used in conjunction with attributes defined at any level.

If we were only interested in the City level of the dimension, an access grant that used variable substitution would be similar to the following:

|  |
|----|
| \<MemberGrant member="\[Geographic Area\].\[USA\].\[West\].\[CA\].\[%{Cities}\]" access="all"/\> |

This grant gives specific access to USA, West, and California, but uses variable substitution (represented by `[%{Cities}]`) to grant access to whichever cities are defined for the specific user.

CZS also defined attributes for other levels of the Geographical Area dimension. A member grant that searched all of these attributes would be similar to the following:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><p>&lt;MemberGrant member="[Geographical Area].[%{Country}].[%{Region}].[%{State}].[%{Cities}]" access="all"/&gt;<br />
</p></td>
</tr>
</tbody>
</table>

The access grant definition that CZS created, including the attributes, is shown in [Access Grant Definition for CZS](reference_material.md).
