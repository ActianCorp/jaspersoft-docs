---
title: Domain and Security Recommendations
description: "When defining a Domain and its security, keep these recommendations in mind:"
---

# Domain and Security Recommendations

When defining a Domain and its security, keep these recommendations in mind:

-   A Domain should cover a large subject area and include data with multiple uses. Define joins to create data islands that each contain related information; the data islands themselves can contain completely unrelated data. For example, you could include both human resources and sales data in a single Domain; users would see only the information relevant to their job responsibilities. For an example of this type of Domain, refer to the SuperMart example that can be installed with JasperReports Server.
-   When defining a Domain, don’t create too many item groups, and avoid very deep structures with many levels. Such complexity makes the Domain harder to use.
-   Logging can help you troubleshoot any problems you encounter while implementing Domain security. For more information, refer to [1.1.1, “Enabling Logging,” on page 1](domain-security-testing.md).
-   Refer to [http://groovy.codehaus.org](http://groovy.codehaus.org/) for information on the Groovy expressions that Domain security files support. Note that, while the server does validate Groovy expressions, the validation is very light weight and doesn’t detect all improperly formed expressions.
-   If the names of tables and fields in your data source change, you can edit the Domain design XML file so that the resource names match the new names in the database. Then, upload the new version of the file; your reports that rely on the Domain will work properly without being updated individually. If you have defined a security file for this Domain, you must also edit the resource names in the security file.
-   Start with the simplest item or resource grant, and when that works, expand upon it. Start simple and iterate until you have the full set of access grants needed. Follow good troubleshooting practices, such as changing only a single aspect of the security file before testing the results of the change.
-   Use an XML editor to create your security file. While the server validates the schema against its own XML definition, a typical XML editor can identify issues like unclosed tags. For example, open the security file with Internet Explorer; if it returns errors, use them to identify and correct your XML.
-   Once your Domain is created, create several Domain Topics that focus on specific aspects of the Domain or specific data your end-users will want to review regularly. To do so, click **Create &gt; Ad Hoc Report**, select your Domain, and use the **Data, Filters**, and **Display** pages to customize the contents and the way it's displayed, then use the **Topics** page to save the new Domain Topic.
-   When creating a security file, be sure to use the IDs of items and groups as they are defined in the Domain design file exported from the Domain Designer.
-   If you modify the Domain, you should also export the design file and update the security file with any IDs that have changed. Update the security file using the **Change** function on the Edit Domain page of the Domain Designer.

A typical security file has the following structure:

``` xml
<securityDefinition xmlns="http://www.jaspersoft.com/2007/SL/XMLSchema"
          version="1.0" itemGroupDefaultAccess="granted">
 <resourceAccessGrants>    <!-- Begin row-level security -->
  <resourceAccessGrantList id="expense_join_resource_access_grant" label="aLabel"
               resourceId="expense_join">
   <resourceAccessGrants>
    <resourceAccessGrant id="expense_join_ROLE_SUPERMART_MANAGER_store_row_grant">
     <principalExpression>
      authentication.getPrincipal().getRoles().any{ it.getRoleName() in
      ['ROLE_SUPERMART_MANAGER'] }
     </principalExpression>
     <filterExpression>s.store_country in ('USA') and s.store_state in ('CA')
     </filterExpression>
    </resourceAccessGrant>
    ...
   </resourceAccessGrants>
  </resourceAccessGrantList>
  ...
 </resourceAccessGrants>
 <itemGroupAccessGrants>    <!-- Begin column-level security -->
  <itemGroupAccessGrantList id="expense_join_item_group_access_grant_group"
       label="aLabel" itemGroupId="expense_join" defaultAccess="denied">
   <itemGroupAccessGrants>
    <itemGroupAccessGrant id="expense_join_super_user_item_group_grant"
               access="granted">
     <principalExpression>
      authentication.getPrincipal().getRoles().any{ it.getRoleName() in
      ['ROLE_ADMINISTRATOR'] }
     </principalExpression>
    </itemGroupAccessGrant>
    ...
   </itemGroupAccessGrants>
  </itemGroupAccessGrantList>
  ...
 </itemGroupAccessGrants>
</securityDefinition>
```
