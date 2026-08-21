---
title: Databases
description: "JasperReports Server relies heavily on database access, and cluster deployments add extra load to these shared resources:"
---

# Databases

JasperReports Server relies heavily on database access, and cluster deployments add extra load to these shared resources:

- The shared repository is a critical part of the cluster with very high loads compared to a traditional single-server deployment. With multiple simultaneous connections from multiple nodes, you must ensure that the repository database doesn’t become a bottleneck. Therefore, the architecture, size, and speed of the database hosting the shared repository must be carefully evaluated and specified in the cluster design.

  Alternatively, you can use Amazon RDS as the repository, thus allowing you to create your cluster entirely within Amazon's Web Service offerings. For more information, see [Launching Jaspersoft for AWS](https://aws.amazon.com/marketplace/pp/prodview-2rym5fbrzlshy) on the Jaspersoft Community website.

- A JasperReports Server cluster enables and encourages a large population of users to process more and more data–this is a good thing. But the cluster may stress your reporting databases to their limits if they aren’t given adequate hardware and software. This is another case where knowing what data your users access the most can help you optimize database configuration such as indexing.

- If you implement external authentication or single sign-on, make sure those resources can handle the load that the cluster is expected to generate.
