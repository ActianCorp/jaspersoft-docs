---
title: "Understanding the repo: Syntax"
description: "In some cases, you may see the repo: syntax used to refer to a location in a JasperReports Server repository. The repo: syntax can be used to refer to any type of resource, such as reports, images,..."
---

# Understanding the repo: Syntax

In some cases, you may see the `repo:` syntax used to refer to a location in a JasperReports Server repository. The `repo:` syntax can be used to refer to any type of resource, such as reports, images, data sources, and input controls. The `repo:` syntax can be used in two ways:

- `repo:` used without a path – A resource of a report. This syntax is generated when a resource is selected when a report is published to the repository. For example, if you upload an image as a resource of a report, you might see JRXML like this:

``` xml
<imageExpression class="java.lang.String">
    <![CDATA["repo:AllAccounts_Res2"]]>
</imageExpression>
```

When you publish a report to JasperReports Server and upload your resources, Jaspersoft Studio updates the JRXML in the published report to use the `repo:` syntax to refer to the uploaded resources in the repository.

- `repo:` used with a path – A resource saved somewhere in the repository. For example, to refer to an image in the repository, you might see JRXML like this:

``` xml
<imageExpression class="java.lang.String">
    <![CDATA["repo:/Images/myimage.jpg"]]>
</imageExpression>
```

In a multi-organization deployment of JasperReports Server, the path used in a `repo:` expression is relative to the organization of the current user. For example, if User1 in Organization_1 accesses the report, JasperReports Server looks for myimage.jpg in the Images folder of Organization_1. If User2 in Organization_2 accesses the report, JasperReports Server looks for myimage.jpg in the Images folder of Organization_2.
