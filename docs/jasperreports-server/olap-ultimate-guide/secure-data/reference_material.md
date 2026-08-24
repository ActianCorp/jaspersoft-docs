---
title: Reference Material
description: "The CZS-sales.xml OLAP schema defines a cube that is based on the salesfact2012 table. It uses three measures: Unit Sales, Store Cost, and Store Sales. The cube can be analyzed with its two..."
---

# Reference Material

## OLAP Schema

The CZS-sales.xml OLAP schema defines a cube that is based on the sales_fact_2012 table. It uses three measures: `Unit Sales`, `Store Cost`, and Store Sales. The cube can be analyzed with its two dimensions: `Geographical Area` and `Product`.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><p>&lt;Schema name="CZS-sales"&gt;</p>
<p>&lt;Dimension name="Geographical Area"&gt;</p>
<p>&lt;Hierarchy hasAll="true" primaryKey="store_id" primaryKeyTable="store"&gt;</p>
<p>&lt;Join leftKey="region_id" rightKey="region_id"&gt;</p>
<p>&lt;Table name="store" /&gt;</p>
<p>&lt;Table name="region" /&gt;</p>
<p>&lt;/Join&gt;</p>
<p>&lt;Level name="Country" table="region" column="sales_country" type="String"</p>
<p>uniqueMembers="true" levelType="Regular" hideMemberIf="Never" /&gt;</p>
<p>&lt;Level name="Region" table="region" column="sales_region" type="String"</p>
<p>uniqueMembers="false" levelType="Regular" hideMemberIf="Never" /&gt;</p>
<p>&lt;Level name="State" table="store" column="store_state" type="String"</p>
<p>uniqueMembers="true" levelType="Regular" hideMemberIf="Never" /&gt;</p>
<p>&lt;Level name="City" table="store" column="store_city" type="String"</p>
<p>uniqueMembers="false" levelType="Regular" hideMemberIf="Never" /&gt;</p>
<p>&lt;Level name="Store Name" table="store" column="store_name" type="String"</p>
<p>uniqueMembers="true" levelType="Regular" hideMemberIf="Never"&gt;</p>
<p>&lt;Property name="Store Type" column="store_type" type="String" /&gt;</p>
<p>&lt;Property name="Store Manager" column="store_manager" type="String" /&gt;</p>
<p>&lt;Property name="Store Sqft" column="store_sqft" type="Numeric" /&gt;</p>
<p>&lt;Property name="Street address" column="store_street_address"</p>
<p>type="String" /&gt;</p>
<p>&lt;/Level&gt;</p>
<p>&lt;/Hierarchy&gt;</p>
<p>&lt;/Dimension&gt;</p></td>
</tr>
<tr>
<td><p>&lt;Dimension name="Product"&gt;</p>
<p>&lt;Hierarchy hasAll="true" primaryKey="product_id" primaryKeyTable="product"&gt;</p>
<p>&lt;Join leftKey="product_class_id" rightKey="product_class_id"&gt;</p>
<p>&lt;Table name="product" /&gt;</p>
<p>&lt;Table name="product_class" /&gt;</p>
<p>&lt;/Join&gt;</p></td>
</tr>
<tr>
<td><p>&lt;Level name="Product Family" table="product_class" column="product_family"</p>
<p>type="String" uniqueMembers="true" levelType="Regular" hideMemberIf="Never" /&gt;</p>
<p>&lt;Level name="Product Department" table="product_class"</p>
<p>column="product_department" type="String" uniqueMembers="false"</p>
<p>levelType="Regular" hideMemberIf="Never" /&gt;</p>
<p>&lt;Level name="Product Category" table="product_class" column="product_category"</p>
<p>type="String" uniqueMembers="false" levelType="Regular" hideMemberIf="Never" /&gt;</p>
<p>&lt;Level name="Product Subcategory" table="product_class"</p>
<p>column="product_subcategory" type="String" uniqueMembers="false"</p>
<p>levelType="Regular" hideMemberIf="Never" /&gt;</p>
<p>&lt;Level name="Brand Name" table="product" column="brand_name" type="String"</p>
<p>uniqueMembers="false" levelType="Regular" hideMemberIf="Never" /&gt;</p>
<p>&lt;Level name="Product Name" table="product" column="product_name" type="String"</p>
<p>uniqueMembers="true" levelType="Regular" hideMemberIf="Never" /&gt;</p>
<p>&lt;/Hierarchy&gt;</p>
<p>&lt;/Dimension&gt;</p></td>
</tr>
<tr>
<td><p>&lt;Cube name="Sales" cache="true" enabled="true"&gt;</p>
<p>&lt;Table name="sales_fact_2006" /&gt;</p>
<p>&lt;DimensionUsage source="Geographical Area" name="Geographical Area"</p>
<p>foreignKey="store_id" /&gt;</p>
<p>&lt;DimensionUsage source="Product" name="Product" foreignKey="product_id" /&gt;</p>
<p>&lt;Measure name="Unit Sales" column="unit_sales" formatString="Standard"</p>
<p>aggregator="sum" /&gt;</p>
<p>&lt;Measure name="Store Cost" column="store_cost" formatString="#,###.00"</p>
<p>aggregator="sum" /&gt;</p>
<p>&lt;Measure name="Store Sales" column="store_sales" formatString="#,###.00"</p>
<p>aggregator="sum" /&gt;</p>
<p>&lt;/Cube&gt;</p>
<p>&lt;/Schema&gt;</p></td>
</tr>
</tbody>
</table>

## Access Grant Definition for CZS

The CZS-sales-grant.agxml access grant definition is modeled after the CZS-sales.xml OLAP schema and defines access for users with the ROLE_SALES_MANGER and ROLE_SALES_REP access roles. It uses variable substitution to refer to attributes that determine the data the user can see in the Ad Hoc view.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><p>&lt;Roles&gt;</p>
<p>&lt;Role name="ROLE_SALES_MANAGER"&gt;</p>
<p>&lt;SchemaGrant access="none"&gt;</p>
<p>&lt;CubeGrant cube="Sales" access="all"&gt;</p>
<p>&lt;HierarchyGrant hierarchy="[Geographical Area]" access="custom"</p>
<p>topLevel="[Geographical Area].[State]"</p>
<p>bottomLevel="[Geographical Area].[City]"&gt;</p>
<p>&lt;MemberGrant member="[Geographical Area].[%{Country}].[%{Region}].[%{State} access="all"/&gt;</p>
<p>&lt;/HierarchyGrant&gt;</p>
<p>&lt;HierarchyGrant hierarchy="[Product]" access="custom"</p>
<p>topLevel="[Product].[Product Family]"</p>
<p>bottomLevel="[Product].[Product Department]"&gt;</p>
<p>&lt;MemberGrant member="[Product].[Electronics].[%{ProductDepartment}]" access="all"/&gt;</p>
<p>&lt;/HierarchyGrant&gt;</p>
<p>&lt;/CubeGrant&gt;</p>
<p>&lt;/SchemaGrant&gt;</p>
<p>&lt;/Role&gt;</p>
<p>&lt;Role name="ROLE_SALES_REP"&gt;</p>
<p>&lt;SchemaGrant access="none"&gt;</p>
<p>&lt;CubeGrant cube="Sales" access="all"&gt;</p>
<p>&lt;HierarchyGrant hierarchy="[Geographical Area]" access="custom"</p>
<p>topLevel="[Geographical Area].[City]"</p>
<p>bottomLevel="[Geographical Area].[City]"&gt;</p>
<p>&lt;MemberGrant member="[Geographical Area].[%{Country}].[%{Region}].[%{State}].[%{Cities}]" access="all"/&gt;</p>
<p>&lt;/HierarchyGrant&gt;</p>
<p>&lt;HierarchyGrant hierarchy="[Product]" access="custom"</p>
<p>topLevel="[Product].[Product Family]"</p>
<p>bottomLevel="[Product].[Product Department]"&gt;</p>
<p>&lt;MemberGrant member="[Product].[Electronics].[%{ProductDepartment}]" access="all"/&gt;</p>
<p>&lt;/HierarchyGrant&gt;</p>
<p>&lt;/CubeGrant&gt;</p>
<p>&lt;/SchemaGrant&gt;</p>
<p>&lt;/Role&gt;</p>
<p>&lt;/Roles&gt;</p></td>
</tr>
</tbody>
</table>
