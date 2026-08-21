---
title: Other Shared Resources
description: "As with the repository database, the server instances in the cluster usually share any resource they need to access, including:"
---

# Other Shared Resources

As with the repository database, the server instances in the cluster usually share any resource they need to access, including:

- Data sources: These are defined in the shared repository, so all servers in the cluster access the same data sources. Queries, reports, and Domains are all stored in the repository as well, so a report has access to exactly the same data, regardless of which instance the user session or job is running on. Make sure that data source and OLAP connections defined in the repository are able to handle connections from multiple nodes simultaneously.

!!! note

    Data sources can be defined as either JDBC connections directly to a database or JDBC connections from the application server to the database exposed through JNDI. We recommend using JNDI data sources because the application server often has better connection pooling and management than JasperReports Server.

    However, JNDI data sources require two definitions, one in the repository and one in the application server. You must make sure that the JNDI definitions are identical on every application server in the cluster. Otherwise, the JNDI data source defined in the shared repository won’t work for every instance of JasperReports Server. For more information, see [JasperReports Server Instances](jasperreports-server-instances.md).

- Email services: These are defined in each server instance’s configuration files for sending the output of finished jobs. When servers are configured identically, every instance uses the same email services.

- External authentication: An optional server configuration that allows JasperReports Server to access an external user database to verify login credentials. As described in the JasperReports Server External Authentication Cookbook, external authentication requires extensive configuration and sometimes customization. When implementing external authentication in a cluster, all instances must be configured identically to avoid security holes.

For resources that are configured in server files, such as email and external authentication, each node could have its own custom configuration. For example, each node could have its own email server to handle the notifications it sends. However, the dedicated resource then becomes a point of failure that disables the corresponding server instance if the resource fails. In either case, shared resources are often clusters themselves, in order to provide the same reliability and scalability as the JasperReports Server cluster.

When resources are shared, they have a single address and set of credentials for access. This means that all JasperReports Server instances have identical configurations and are therefor easier to deploy and maintain.
