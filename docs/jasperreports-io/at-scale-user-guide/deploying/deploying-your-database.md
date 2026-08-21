---
title: Deploying Your Database
description: "Jaspersoft IO At-Scale creates its own connections to the database containing your reporting data. Even when using the JasperReports Server repository, JRIO At-Scale accesses only the metadata for..."
---

# Deploying Your Database

Jaspersoft IO At-Scale creates its own connections to the database containing your reporting data. Even when using the JasperReports Server repository, JRIO At-Scale accesses only the metadata for JDBC data sources to create its own connections. This JDBC datasource must be accessible from inside the JRIO AtScale cluster and JRS instance.

Jaspersoft recommends putting the database into the same VPC as the JRIO At-Scale cluster, whether it is a database deployed on-premises or in the cloud, such as Amazon Relational Database Service (RDS). In the case of RDS, you should update the RDS database security group as required, so that JRIO At-Scale and JasperReports Server will be able to run queries against the database.
