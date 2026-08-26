---
title: Using Customized Configuration Files for Server Instances
description: JasperReports Server allows you to use the S3 bucket for your CloudFormation stack to store customized configuration files for creating your EC2 instances. Uploading the configuration files to the S3...
---

# Using Customized Configuration Files for Server Instances

JasperReports Server allows you to use the S3 bucket for your CloudFormation stack to store customized configuration files for creating your EC2 instances. Uploading the configuration files to the S3 bucket apply the customizations to every instance created from the stack, including instances created as part of a cluster. In the S3 bucket, you must recreate the JasperReports Server structure for the configuration files, starting with the `conf` and `webapp` folders at the Tomcat root level.

!!! warning

    If you want to remove the customized file from an EC2 instance, you need to copy the original configuration file to the S3 bucket and reboot the instance. This replaces the file on the instance and remove the customizations from JasperReports Server. Deleting the customized file from the S3 bucket without adding a replacement cannot remove the customizations when the instance is rebooted.

To upload your customization

1.  On the AWS Management Console homepage, click **CloudFormation**.

2.  Click the name of the CloudFormation stack for your cluster.

3.  Find the name of the stack's S3 bucket on the **Outputs** tab.

4.  Return to the AWS Management Console homepage and click **S3**.

5.  Find the bucket for your cluster and click the name.

6.  Click **Create Folder**. Recreate the paths to your configuration files starting with the `conf` and `webapp` folders.

7.  After creating the folder paths, browse to the folder for your configuration file.

8.  Click **Upload**.

9.  Click Add files and find the configuration file on your local machine.

10. Click **Upload** to upload the configuration file.

    AWS uploads the file and stores it in the S3 bucket.

11. With the configuration file in place, reboot or terminate the cluster from the **EC2** **&gt;** **Instances** **&gt;** **Instances** page.

When the cluster is rebooted or recreated, the changes based on the configuration file can be in place.
