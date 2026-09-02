---
title: Installing JasperReports IO For Amazon Web Services
description: This section covers the JasperReports IO For Amazon Web Services (AWS) Hourly offering. You can purchase the product directly on the AWS Marketplace.
---

# Installing JasperReports IO For Amazon Web Services

This section covers the JasperReports IO For Amazon Web Services (AWS) Hourly offering. You can purchase the product directly on the AWS Marketplace.

## Prerequisites

You need a few things before you can install and run JasperReports IO on Amazon Web Services:

-   An Amazon Web Services account.<br>
    If you already have an account, [log in to AWS](https://console.aws.amazon.com/).<br>
    To create an AWS account, go to [Amazon Web Services sign in page](https://console.aws.amazon.com/), click the **Create a new AWS account** button, and follow the instructions.

    !!! note

        If you have a personal Amazon.com account stored in your browser, AWS uses that account by default. You need to sign out of Amazon or, preferably, use a different browser to set up an AWS account separate from your personal account.

-   A valid Amazon key pair in your account. If you do not have a valid key pair, follow the instructions on the AWS documentation site: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>

-   The Required Permissions for using our CloudFormation template.

## Required Permissions

Using our CF templates typically requires some admin permissions. AWS permissions required to launch a new JasperReports IO instance include:

-   CloudFormation create stack and events
-   Create and run EC2 instances
-   Create EC2 security groups
-   Create IAM resources
-   Create S3 bucket
-   Create CloudWatch log (if selected)

## Accepting Terms of Use

You need to accept the terms of use for both the AWS Marketplace and Jaspersoft. This is a single process with multiple steps.

To accept the license agreement

1.  Go to [Jaspersoft listing](https://aws.amazon.com/marketplace/search/results/ref=sp_navgno_search_box?page=1&searchTerms=jaspersoft) on the Amazon Marketplace. You can use the link provided here, or use the Marketplace search function to locate the page.
2.  Click the link for the JasperReports IO For AWS product.<br>
    This page shows the total projected charges plus EC2 charges. Simply visiting a page does not place your order.
3.  Click **Continue** to go to the Launch page.
4.  Verify the information on this page and click **Accept Terms**.<br>
    When your order is processed, you may receive an email confirmation.

## Supported Instance Types

The following is a list of the instance types supported for JasperReports IO:

-   T2 Micro (t2.micro)
-   T2 Medium (t2.medium)

Performance may vary based on system attributes such as network, bandwidth, memory requirements for a given use case, query requirements, and the like.

For more information about EC2 instance types, see the AWS documentation: <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>

## Creating a JasperReports IO Instance from a CloudFormation Template

A stack is a collection of AWS resources that you create and delete as a single unit. Our CloudFormation template creates the following resources and bundles them into a usable stack:

-   IAM role
-   S3 bucket
-   EC2 instance with JasperReports IO installed, configured, and using the IAM role for appropriate credentials.

To create a JasperReports IO instance

1.  Open the Launching Jaspersoft for AWS web page.

2.  Click the **Launch Jaspersoft IO for AWS** tab.

3.  Click the URL for your region. The **Select Template** page appears. By default, AWS provides a stack template source URL. Do not change this.

4.  Click **Next**. The **Specify Details** page appears.

5.  In the **Stack Name** field, give your CloudFormation stack a unique name.

6.  Select an **InstanceType** from the dropdown. See [Supported Instance Types](#supported-instance-types) for more information.

7.  In the **KeyName** field, enter an existing key pair name.

8.  In the **RemoveSamples** field, select whether to remove the sample web application and reports from your JasperReports IO instance's repository.

9.  Choose the **VpcId** from your account.

10. Choose the **SubnetId** from the VPC.

11. Choose whether to create a publicly accessible IP address for the instance using **EnablePublicIp**. Default is set to True. Select **False** to refuse.

12. In the **SecuredIp** field, enter the IP address and mask for SSH access.

13. Choose whether to enable CloudWatch logs for your instance by selecting Yes for **CloudWatchIntegration**.

14. In the **S3BucketName** field, enter the name of the S3 bucket where you want to store your JasperReports IO reports and customizations. The S3 bucket must be in the same region as your JasperReports IO instance. A new S3 bucket is created if you leave the field empty.

    !!! note

        If you enter an existing S3 bucket's name incorrectly, you experience errors when using JasperReports IO because the S3 bucket does not exist. See [Correcting an Invalid S3 Bucket](#correcting-an-invalid-s3-bucket) for instructions on fixing the issue.

15. Click **Next**. The **Options** page appears.

16. Add any tags that you want to use to simplify the administration of your infrastructure. A tag consists of a key/value pair and will flow to resources inside your stack. You can add up to 10 unique keys to each instance, along with an optional value for each key.

17. If you want all operations for the stack limited to a certain role, use the **Permissions** section to choose the role.

18. In the **Rollback Triggers** section, set alarms you want CloudFormation to use to monitor the creation of the stack. If any alarms are triggered, CloudFormation stops of the creation of the stack and rolls it back.

19. Expand the **Advanced** section and set your notification, timeout, and other options.

20. Click **Next**. The **Review** page appears. Double-check your template, parameter, and option information.

21. Click the acknowledgment checkbox, then click **Create**. You see your stack name listed in a table. While it is being created the Status column displays `CREATE_IN_PROGRESS`. After a few minutes, the status should change to `CREATE_COMPLETE`. If the status changes to `ROLLBACK` instead of `CREATE_COMPLETE`, you may need to accept the Terms of Use. Check the Events tab for more information.

22. Select your complete instance and click the **Outputs** tab. Here you find the name of the S3 bucket for your repository, the link for the CloudWatch log, and the Getting Started URL for logging into the JasperReports IO web application if you enabled a publicly accessible IP address.

## Creating a Repository Folder in Your S3 Bucket

When setting up your JasperReports IO instance, you need to create a repository folder in your S3 bucket to store the resources to create and run your reports.

To create a repository folder

1.  On the AWS Management Console home page, click **S3**.
2.  Click the name of the bucket for your instance or cluster.
3.  Click **Create Folder**.
4.  Enter `remoteRepository` for the name of the folder.
5.  Select **None (use bucket settings)** for the encryption setting.
6.  Click **Save**. AWS creates the `remoteRepository` folder.

You can create the repository directories for your report resources in the new `remoteRepository` folder and upload your files. See [Managing JasperReports IO](../managing_jrio/managing_jrio.md) for more information on the repository directory structure.

## Correcting an Invalid S3 Bucket

If you enter the incorrect name for an existing S3 bucket when creating your instance, you need to update the settings for the instance and associated IAM role to point them to the correct S3 bucket.

To correct the S3 bucket

1.  On the AWS Management Console home page, click **EC2**.

2.  Click **Instances** in the sidebar.

3.  Click the instance with the invalid S3 bucket in the table.

4.  Click **Actions &gt; Instance State &gt; Stop** to stop the instance.

5.  Click **Actions &gt; Instance Settings &gt; View/Change User Data**.

6.  Locate the `s3.repository.bucket` and replace the invalid S3 bucket name with the correct one.

7.  Click **Save**.

8.  Return to the AWS Management Console home page and click **IAM**.

9.  Click **Roles** in the sidebar.

10. Click the name of the IAM role created for your JasperReports IO instance in the table.

11. On the **Permissions** tab, expand the policy and click **S3** under Service. The tab displays a list of S3 actions.

12. Click **Edit Policy**.

13. Click the **JSON** tab.

14. Locate `Resource` and replace the invalid S3 bucket name with the correct one. For example:

    ``` json
    {
                "Statement": [
                {
                "Action": [
                "s3:Get*",
                "s3:List*"
                ],
                "Resource": [
                "arn:aws:s3:::jrio-jrios3bucket-12",
                "arn:aws:s3:::jrio-jrios3bucket-12/*"
                ],
                "Effect": "Allow"
                }
                ]
            }
    ```

15. Click **Review the policy**.<br>
    AWS displays the S3 service that you are updating. You can click **S3** to review the service before committing your changes.

16. Click **Save changes**.<br>
    AWS updates the IAM role with the S3 bucket changes.

17. Return to the AWS Management Console home page and click **IAM**.

18. Restart your instance.
