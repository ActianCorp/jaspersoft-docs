---
title: Connecting to Your Data with JasperReports Server
description: Follow the instructions in the chapter to connect JasperReports Server to Amazon RDS or Redshift. For Amazon Elastic MapReduce (EMR) see Connect to Amazon EMR. For connecting JasperReports Server to...
---

# Connecting to Your Data with JasperReports Server

Follow the instructions in the chapter to connect JasperReports Server to Amazon RDS or Redshift. For Amazon Elastic MapReduce (EMR) see Connect to Amazon EMR. For connecting JasperReports Server to non-Amazon data sources, see Additional Connection Possibilities.

## Launching JasperReports Server on AWS Marketplace

Upon purchasing JasperReports Server on AWS Marketplace or obtaining your BYOL (“Bring Your Own License”) license key from Jaspersoft, make sure you follow the instructions in the Jaspersoft for AWS User Guide to launch the product.

-   If you purchase JasperReports Server directly on AWS Marketplace, the license key is included.
-   If you're using the Jaspersoft BYOL license key option, you can download the BYOL license key from [http://support.tibco.com](http://support.tibco.com/).

## Connect to Amazon RDS or Redshift

JasperReports Server can automatically discover and connect to Amazon Relational Database Server (RDS) and Amazon Redshift using the auto-connect feature.

To connect to Amazon RDS or Redshift

1.  Log into JasperReports Server as an administrator.

2.  Go to **Create** &gt; **Data Source**.![03000004](assets/images/03000004.png)

    Create &gt; Data Source menu

3.  Select **AWS Data Source** from the **Type** dropdown menu.

4.  Enter your EC2 instance credentials. If EC2 instance credentials are not available, then see the Additional Connection Possibilities section below.

5.  Under **AWS Settings**, select **EC2 instance credentials**. ![03000005](assets/images/03000005.png)

    Add Data Source dialog

6.  Enter your database connection info:

    JasperReports Server is able to detect your RDS and Redshift data sources. This is possible because the IAM Role associated with the EC2 instance is allowed to execute the actions "rds:Describe\*" and "redshift:Describe\*". It pre-populates the Database Name, Driver, and URL.

    On the New Data Source page, You must enter the database username and password. For security reasons, Amazon does not store these credentials, and Jaspersoft cannot retrieve them.

    The default database is automatically populated, but you may manually enter another if your RDS or Redshift instance has multiple databases.

    ![03000006](assets/images/03000006.png)

    New Data Source dialog

7.  Test your connection:

You should always test your connection. This button does much more than just testing:

-   It creates a DB Security Group.

    -   It adds the internal IP of the EC2 instance to the security group to authorize ingress to RDS.

        This is possible because the IAM Role provides the instance with credentials like "rds:CreateDBSecurityGroup" and "redshift:AuthorizeClusterSecurityGroupIngress".

    -   If you want to control details of the security group name or specify the IP address manually because you have a complex VPC Topology, then navigate to the menu **Manage &gt; Server Settings &gt; AWS Settings**.

![03000007](assets/images/03000007.png)

Test Connection dialog

1.  Create a Domain:

    Jaspersoft's metadata layer is called "Data Domains". Choose **Create &gt; Domain** from the main menu and follow the wizard to build a domain.

    ![03000008](assets/images/03000008.png)

    Create &gt; Domain menu

2.  Analyze your data:

    Choose **Create &gt; Ad Hoc View**. Find your newly created domain and use the ad hoc environment to begin analyzing your data.

    ![03000009](assets/images/03000009.png)

    Create &gt; Ad Hoc View menu

3.  Next steps:

Refer to the [Online Learning Portal](https://www.jaspersoft.com/bi-training-center) for details on creating domains, performing ad hoc analysis, and creating reports.

## Additional Connection Types

-   AWS Credentials

    We recommend launching Jaspersoft BI on an EC2 instance with an associated IAM Role. This role provides EC2 credentials for your JasperReports Server instance.

    If this option is not available, you can use AWS credentials instead. If you already have AWS Credentials, you can enter the Access Key and Secret Key.

    If you don't have AWS Credentials, you can run the CloudFormation Template "jrs-create-user" to generate credentials.

    <http://www.jaspersoft.com/jrs-create-user?region=us-east-1>

    <http://www.jaspersoft.com/jrs-create-user?region=us-west-2>

    <http://www.jaspersoft.com/jrs-create-user?region=us-west-1>

    <http://www.jaspersoft.com/jrs-create-user?region=eu-west-1>

    <http://www.jaspersoft.com/jrs-create-user?region=ap-northeast-1>

    <http://www.jaspersoft.com/jrs-create-user?region=sa-east-1>

    !!! note

        Running the CloudFormation Template "jrs-create-user" requires using the older AWS CloudFormation console. If you are using the newer, redesigned CloudFormation console, you need to switch back to the previous version to run this template.

    ![0300000A](assets/images/0300000A.png)

    Entering AWS credentials

-   JDBC / JNDI Connections

    NOTE: When using JDBC for data source connections, you're responsible for managing the security groups to allow access from the Jaspersoft server to the data source.

    ![0300000B](assets/images/0300000B.png)

    Using JDBC / JNDI connections

-   Amazon RDS or Redshift

    When connecting to Amazon RDS or Redshift, it is best to use the AWS Data Source type to make configuration easier. If you prefer, you can use JDBC to connect to Amazon RDS or Redshift. To connect using JDBC, choose the JDBC Data Source type. Enter all connection information and test. Alternatively, you can choose JNDI Data Source and refer to a data source defined in Apache Tomcat.

    Benefits of defining your own JDBC connections

-   You have complete control

    Benefits of using AWS Data Sources

-   Jaspersoft provides the driver and URL

-   Data source automatically recovers if the IP address changes

-   Data source automatically recovers if DB Security Groups are modified

## Connect to Amazon EMR

The JasperReports Server auto-connect feature is not supported for Amazon EMR. Connections to EMR need to be configured manually. Please see the Amazon EMR connection page for details: <http://community.jaspersoft.com/jaspersoft-aws/connect-emr>
