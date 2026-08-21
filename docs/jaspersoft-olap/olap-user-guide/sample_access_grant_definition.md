---
title: Sample Access Grant Definition
description: "The following sample access grant definition (called Foodmart Grant and found in the repository at /analysis/schemas) is used with the Foodmart Mondrian connection, (found in the repository at..."
---

# Sample Access Grant Definition

The following sample access grant definition (called Foodmart Grant and found in the repository at `/analysis/schemas`) is used with the Foodmart Mondrian connection, (found in the repository at `/analysis/connections`):

```
<Roles>
 <Role name="StateManager">
  <SchemaGrant access="none">
   <CubeGrant cube="Sales" access="all">
    <HierarchyGrant hierarchy="[Store]"
                    access="custom"
                    topLevel="[Store].[Store Country]">
     <MemberGrant member="[Store].[USA].[%{State}]"
                  access="all"/>
    </HierarchyGrant>
    <HierarchyGrant hierarchy="[Customers]"
                    access="custom"
                    topLevel="[Customers].[State Province]"
                    bottomLevel="[Customers].[City]">
     <MemberGrant member="[Customers].[USA].[%{State}]"
                  access="all"/>
    </HierarchyGrant>
    <HierarchyGrant hierarchy="[Gender]"
                    access="none"/>
   </CubeGrant>
  </SchemaGrant>
 </Role>
</Roles>
```

!!! note

    This example describes only how user-level attributes can be used in an access grant the way that functionality existed in releases before 6.0. This approach still works. In 6.0, we added support for hierarchical attributes, which can be assigned at the server and organization in addition to the user level. These new hierarchical attributes can also be used to secure the data displayed in your OLAP views. The XML for using these attributes in an access grant file follows the same pattern as applies to user-level attributes.

    For more information about attributes, see the JasperReports Server Administrator Guide and the JasperReports Server Security Guide.

This schema defines access permissions for a role called StateManager. In this example, the `SchemaGrant` element defines `none` as the default access for all objects in the schema. Users with the StateManager role cannot access anything, unless a lower level grant overrides the default.

The cube attribute has the value `Sales`, so the definition is for the Sales cube. The access attribute has the value `all`. This gives users with this role access to the entire Sales cube. Again, lower-level grants can override this one.

`HierarchyGrant` elements define access to the Store, Customers, and Gender hierarchies. Users with this role cannot see any of the gender hierarchies. The other two HierarchyGrant elements define custom access to the Store and Customers hierarchies.

The member grants in this example use substitution variables like `%{State}` to represent substitutions from the list of attributes. These particularize the grant to the specific user associated with the StateManager role. For example, suppose that user John has StateManager as one of his roles. Also suppose that John's user account defines an attribute called State, which is set to CA,OR,WA. If you create a view for John, the line:

```
<MemberGrant member="[Customers].[USA].[%{State}]"
access="all"/>
```

in the above example is interpreted to mean:

```
<MemberGrant member="[Customers].[USA].[CA,OR,WA]"
access="all"/>
```
