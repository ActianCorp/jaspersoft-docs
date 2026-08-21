---
title: Creating a Sales Numbers Ad Hoc View
description: "Having created the attributes, access grant definition, and a Mondrian connection, CZS then created the actual Sales Numbers Ad Hoc view to run against the Mondrian connection. This Ad Hoc view..."
---

# Creating a Sales Numbers Ad Hoc View

Having created the attributes, access grant definition, and a Mondrian connection, CZS then created the actual Sales Numbers Ad Hoc view to run against the Mondrian connection. This Ad Hoc view pointed to the Mondrian connection that includes the czs-sales-grant.agxml access grant definition file. CZS used the Ad Hoc Editor to add members of the geographical dimension and product dimensions, as well as the store sales, unit sales, and store cost measures into a crosstab.

Once the Ad Hoc view was created, CZS updated the repository object permissions so that each access role (ROLE_SALES_MANAGER and ROLE_SALES_REP) had Read access to the view. Read access is required to open Ad Hoc views.

For instructions on access control, refer to the JasperReports Server Administrator Guide. For instructions on creating OLAP views and Ad Hoc views, refer to the OLAP views Jaspersoft OLAP User Guide.
