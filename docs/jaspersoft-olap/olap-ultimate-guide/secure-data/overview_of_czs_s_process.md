---
title: "Overview of CZS's Process"
description: "After defining their business case (as above), CZS took these steps to implement the Sales Numbers view:"
---

# Overview of CZS's Process

After defining their business case (as above), CZS took these steps to implement the Sales Numbers view:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>Step</p></th>
<th><p>Described in Section …</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>1</p></td>
<td><p>Identified the dimensions on which to base access control. CZS chose the Geographical Area and Product Department dimensions.</p></td>
<td><p><a href="configuring_czs_s_olap_view.md">Dimensions</a></p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>Identified and created access roles. CZS identified two roles: one for managers and another for sales reps. Both are granted access to the Ad Hoc view.</p></td>
<td><p><a href="determining_roles.md">Determining Roles</a></p></td>
</tr>
<tr>
<td><p>3</p></td>
<td><p>Assigned the appropriate roles to each user based on each employee’ responsibilities.</p></td>
<td><p><a href="selecting_users_for_the_roles.md">Selecting Users for the Roles</a></p></td>
</tr>
<tr>
<td><p>4</p></td>
<td><p>Identified the attributes that are defined for each user. CZS identified five attributes: Country, Region, State, Cities, and <span>ProductDepartment</span>.</p></td>
<td><p><a href="profile_attributes_and_variable_subs.md">Attributes and Variable Substitution</a> and <a href="assigning_profile_attributes.md">Assigning Attributes</a></p></td>
</tr>
<tr>
<td><p>5</p></td>
<td><p>Defined the correct values for each user’s attributes by editing user accounts.</p></td>
<td><p><a href="assigning_profile_attributes.md">Defining Attributes for Users</a> and the <span>JasperReports Server Administrator Guide</span></p></td>
</tr>
<tr>
<td><p>6</p></td>
<td><p>Created an AGXML (access grant definition XML) file that defines the access granted to users with each role and attribute.</p></td>
<td><p><a href="assigning_profile_attributes.md">Using Attributes in an Access Grant Definition</a> and<br />
<a href="reference_material.md">Reference Material</a></p></td>
</tr>
<tr>
<td><p>7</p></td>
<td><p>Created a Mondrian connection that pointed to their sales data and included the sales access grant definition.</p></td>
<td><p><a href="creating_a_mondrian_connection_czs.md">Creating a Mondrian Connection</a></p></td>
</tr>
<tr>
<td><p>8</p></td>
<td><p>Created the Ad Hoc view that points to the Mondrian connection.</p></td>
<td><p><a href="generating_a_sales_olap_view.md">Generating a Sales Numbers Ad Hoc View</a></p></td>
</tr>
<tr>
<td><p>9</p></td>
<td><p>Tested the views of various users.</p></td>
<td><p><a href="testing_the_results.md">Testing the Results</a></p></td>
</tr>
</tbody>
</table>
