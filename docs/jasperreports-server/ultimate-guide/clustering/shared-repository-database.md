---
title: Shared Repository Database
description: "The keystone of the JasperReports Server cluster is the shared repository database. All JasperReports Server instances must be configured to access the same repository, thus ensuring that they..."
---

# Shared Repository Database

The keystone of the JasperReports Server cluster is the shared repository database. All JasperReports Server instances must be configured to access the same repository, thus ensuring that they display the same folders, the same reports, and the same resources. Because the repository also stores users, roles, organizations, and security definitions, every server in the cluster behaves identically regardless of which instance actually processes the client connection.

For example, when a user logs in, the user account, organization, and roles are retrieved from the shared repository. When the user browses folders, all resources are the same as seen from any instance in the cluster, and all access permissions apply. If the user runs a report based on a Domain Topic, the report, the Domain Topic, the Domain, and any security files are all retrieved from the repository.

All repository operations are thread-safe, meaning that all JasperReports Server instances can perform operations simultaneously, while internal locks in the software prevent operations that would conflict. If a user edits and saves a report, another user running the report sees either the old report or the new one based on exactly when the request was made. As with many large systems serving numerous clients, users must coordinate their work to avoid overwriting each other's changes. For the same reason, administrators should make changes to shared resources during off-hours to prevent conflicts with active user sessions.

Because the repository database is such a critical element of the JasperReports Server cluster, you should implement it on an equally scalable and available system, based on the predicted peak load and average load in your cluster. For example, the repository could be a cluster itself, with its own load balancer, or any other architecture that is compatible with a database product supported by JasperReports Server. In addition, the repository database must implement data protection measures you require, such as on-site and off-site backups.

You can also use Amazon RDS (Relational Database Service) as the repository to take advantage of its built-in scalability, high-availability, and backup security. If your server nodes are also EC2 (Elastic Compute Cloud) instances, you can create an entirely virtual cluster within Amazon's Web Service offerings. For more information, see [Launching Jaspersoft for AWS](https://aws.amazon.com/marketplace/pp/prodview-2rym5fbrzlshy) on the Jaspersoft Community website.

Regardless of the architecture of the repository database, it's critical that it act as a single logical repository identified with a single IP address that all JasperReports Server instances can access.
