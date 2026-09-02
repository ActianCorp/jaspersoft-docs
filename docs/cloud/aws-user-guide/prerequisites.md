---
title: Prerequisites
description: "You need a few things before you can install and run Jaspersoft Business Intelligence on Amazon Web Services:"
---

# Prerequisites

You need a few things before you can install and run Jaspersoft Business Intelligence on Amazon Web Services:

-   An Amazon Web Services (AWS) account.

If you already have an account, [log into AWS](http://aws.amazon.com/).

To create an AWS account, go to [the Amazon Web Services sign up page](http://aws.amazon.com/), click **Create an AWS account** (at the upper-right corner of the page) and follow the instructions.

!!! note

    If you have a personal Amazon.com account stored in your browser, AWS uses that account by default. You need to sign out of Amazon or, preferably, use a different browser to set up an AWS account separate from your personal account.

-   A valid Amazon key pair in your account. If you do not have a valid key pair, follow the instructions on the AWS documentation site: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>
-   The [Required Permissions](#required-permissions) for using our CloudFormation templates and connecting to a data source
-   If you plan to use Jaspersoft for AWS BYOL, you need an annual subscription license. To purchase licenses for BYOL contact Jaspersoft Sales

!!! note

    The procedures in this section work for all Jaspersoft AWS Cloud offerings:

    -   Jaspersoft Reporting and Analytics for AWS (BYOL)

    -   Jaspersoft for AWS with Multi-Tenancy (Hourly)

    -   Jaspersoft Reporting and Analytics for AWS (Hourly)

## Required Permissions

Depending on how you use Jaspersoft for AWS, you need various permission sets.

Using our CloudFormation (CF) templates

Using our CF templates typically requires some admin permissions. AWS permissions required to launch a new JasperReports Server instance include:

-   CloudFormation create stack and events
-   Create and run EC2 instances
-   Create EC2 security groups
-   Create IAM resources

AWS permissions required to launch the template to create a JasperReports Server role or user include:

-   Create IAM resources
-   Grant access to RDS, Redshift, and EC2

Connecting to the data source

Permissions required to connect to the data source include:

-   Access to RDS and/or Redshift
-   Permissions to create and modify the database security groups in each
-   Permissions to create and modify EC2 security groups

Please note that this document does not address connectivity to Amazon Elastic MapReduce (EMR).
