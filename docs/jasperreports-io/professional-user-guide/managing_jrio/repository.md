---
title: JasperReports IO Repository
description: The JasperReports IO repository is a folder-based structure where all the resources used to run and create reports are stored and from where they are retrieved when reports are run by the...
---

# JasperReports IO Repository

The JasperReports IO repository is a folder-based structure where all the resources used to run and create reports are stored and from where they are retrieved when reports are run by the JasperReports IO reporting service. You can have the repository on the host machine or an AWS S3 bucket.

The type of repository, its location in the JasperReports IO file structure, and other specific repository implementation properties can be specified in the following configuration file:

``` bash
js-install>/jrio/webapps/jrio/WEB-INF/applicationContext-repository.xml
```

JasperReports IO comes with a repository full of sample reports and resources in the `<js-install>/repository` directory, but you can create your own repository. If you are using JasperReports IO for AWS, you have to create a repository in an S3 bucket. See [Creating a Repository Folder in Your S3 Bucket](../introduction/aws_installation.md) for more information.

## Repository Directory Structure

The JasperReports IO repository is structured as follows:

| Directory | Description |
|----|----|
| data | Contains the data source adapters and data source files for your reports. |
| images | Contains image files used in reports. |
| JR-INF | Contains the configuration files for report execution. |
| reports | Contains report templates. |

Repository Directories for Sample Reports

## Data Sources and Data Adapters

A data adapter is a resource that specifies how and where to obtain data. Specifically, it is an object that contains information about how to connect to or retrieve the data, and the logic to do that. This information includes, URL, user, password, paths, and so on. Data adapters also contain the logic to prepare all parameters for JasperReports IO to run the query and iterate data. All the connections are opened and passed directly to JasperReports during report generation. A data adapter does not contain any data itself, which is stored in data sources.

The sample repository installed with JasperReports IO contains multiple data adapters and data sources in the `<js-install>/repository/data` directory that you can use for your own reports. These data adapters include:

-   JDBC connection
-   CSV connection
-   Excel connection
-   Empty connection
-   JNDI connection
-   Remote XML connection

JasperReports IO can use other types of data adapters that are not included in the sample repository. You can create your own data adapters for JasperReports IO either by using the Data Adapter Wizard in Jaspersoft Studio or by creating a custom data adapter using a JRDAX file.

## Reports

The repository resource that aggregates all information needed to run a report is called a JasperReport. A JasperReport is based on a JRXML file that conforms to the JasperReports Library that JasperReports IO uses to render reports. Users can create reports for JasperReports IO using Jaspersoft Studio.

A JasperReport is a complex resource composed of other resources:

-   The main JRXML file that defines the report.
-   A data source that supplies data for the report.
-   A query if none is specified in the main JRXML.
-   The query may specify its own data source, which overrides the data source defined in the report.
-   Input controls for parameters that users may enter before running the report. Input controls are composed of either a datatype definition or a list of values.
-   Any additional file resources, such as images and fonts.
-   If the report includes subreports, the JRXML files for the subreports.

End users interact with a JasperReport as a single resource, but report creators must define all the component resources. Refer to the Jaspersoft Studio User Guide for more information on creating reports.

### Configuring the Web Application Server to Reference the Repository

On JasperReports IO, the repository containing the sample report templates used by the sample web application is located in the `<jrio-install>/jrio/repository` directory. Since this repository folder is not located within the JasperReports IO web application folder, you need to configure the `<js-install>/jrio/webapps/WEB-INF/applicationContext-repository.xml` file to point the web application to the repository directory.

There are two different ways to point the web application to a repository on the host machine: Using a relative file path using the `WebappRelativeRepositoryFactory` bean or an absolute file path using the `FileRepositoryService` bean.

To use a relative file path, locate the `WebappRelativeRepositoryFactory` bean in the `applicationContext-repository.xml` file and enter the relative file path as the value for the `root` property:

``` xml
<bean class="com.jaspersoft.jrio.common.repository.WebappRelativeRepositoryFactory">
    <property name="jasperReportsContext" ref="baseJasperReportsContext"/>
    <property name="root" value="../../../repository"/>
</bean>
```

Since the web application is deployed to the `<jrio-install>jrio/webapp/jrio` directory, use "`../../../repository`" as the relative file path to point the web application to the repository in the `<jrio-install>/jrio/repository` directory.

If you want to use an absolute file path to the repository directory, change the repository bean class from `com.jaspersoft.jrio.common.repository.WebappRelativeRepositoryFactory` to `com.jaspersoft.jrio.common.repository.FileSystemRepository` and edit the value for the second `<constructor-arg>` to add the absolute file path:

``` xml
<bean class="com.jaspersoft.jrio.common.repository.FileSystemRepository">
    <constructor-arg><ref bean="baseJasperReportsContext"/></constructor-arg>
    <constructor-arg><value>/mnt/jrio-repository</value></constructor-arg>
</bean>
```

Use a slash (`/`) at the beginning of the URI for the root directory.

If you are using an AWS S3 bucket for the repository, refer to the AWS S3 Bucket Repository for instructions on configuring the web application server to use the bucket.

### Configuring the Web Application Server to Use Multiple Repositories

If you use multiple repository directories to store your report templates and resources, JasperReports IO can treat these separate directories as a single repository through absolute file paths. A report works if its JRXML template is in one repository and its resources are in a second. Add a `FileRepositoryService` bean to the `<js-install>/jrio/webapps/WEB-INF/applicationContext-repository.xml` file for each repository that you want to use.

``` xml
<bean class="com.jaspersoft.jrio.common.repository.FileSystemRepository">
    <constructor-arg><ref bean="baseJasperReportsContext"/></constructor-arg>
    <constructor-arg><value>/mnt/repository1</value></constructor-arg>
</bean>

<bean class="com.jaspersoft.jrio.common.repository.FileSystemRepository">
    <constructor-arg><ref bean="baseJasperReportsContext"/></constructor-arg>
    <constructor-arg><value>/mnt/repository2</value></constructor-arg>
</bean>
```

# Managing Amazon Web Services for JasperReports IO

This section describes how to use an AWS S3 bucket for a repository for JasperReports IO, referring to reports stored in an S3 bucket, and customizations for JasperReports IO for AWS.

## AWS S3 Bucket Repository

JasperReports IO comes with a sample configuration setting for connecting your standalone JasperReports IO instance to an AWS S3 bucket as a repository. The S3 bucket can either be public and accessed without credentials or accessed securely using AWS credentials. Locate and the `S3RepositoryService` bean in the `<js-install>/jrio/webapps/WEB-INF/applicationContext-repository.xml` configuration file to implement an AWS S3 bucket for a repository:

``` xml
<bean class="com.jaspersoft.jrio.common.repository.s3.S3RepositoryService">
    <property name="jasperReportsContext" ref="baseJasperReportsContext"/>
    <property name="s3Service">
        <bean class="com.jaspersoft.jrio.common.repository.s3.S3ServiceFactory">
        <property name="region" value="us-east-1"/>
    <!--
        <property name="accessKey" value="put-id-here"/>
        <property name="secretKey" value="put-key-here"/>
    -->
        </bean>
    </property>
    <property name="bucketName" value="jrio-repo-sample"/>
    <property name="pathPrefix" value="jrio-repository/"/>

    <bean class="com.jaspersoft.jrio.common.repository.s3.S3RepositoryPersistenceServiceFactory" factory-method="instance"/>

</bean>
```

You need to enter the region, S3 bucket name, and the path to the repository.

Use the `accessKey` and `secretKey` properties to enter your AWS ID and key. These credentials are optional if the S3 bucket is public.

If you created your JasperReports IO from the CloudFormation template for AWS, this configuration file appears similar to the following:

``` xml
<bean class="com.jaspersoft.jrio.common.repository.s3.S3RepositoryService">
    <property name="jasperReportsContext" ref="baseJasperReportsContext"/>
    <property name="s3Service">
        <bean class="com.jaspersoft.jrio.common.repository.s3.S3ServiceFactory">
        <property name="region" value="${s3.repository.region:null}"/>
    <!--
        <property name="accessKey" value="put-id-here"/>
        <property name="secretKey" value="put-key-here"/>
    -->
        </bean>
    </property>
    <property name="bucketName" value="${s3.repository.bucket:null}"/>
    <property name="pathPrefix" value="${s3.repository.path.prefix:null}"/>
</bean>
```

The `${...}` is automatically populated by user data that was generated when the JasperReports IO instance was created.

You do not have to provide your AWS credentials if you created a S3 bucket or selected an existing one as when creating the JasperReports IO instance using the CloudFormation template. An IAM role is automatically created that allows the JasperReports IO instance to connect to the S3 bucket without having to provide the credentials.

## Referring to Reports in the AWS S3 Bucket Repository

For storing report resources in an AWS S3 bucket, you need to create a folder in the bucket called `remoteRepository`. See [Creating a Repository Folder in Your S3 Bucket](../introduction/aws_installation.md) for instructions on adding this folder to your S3 bucket.

JasperReports IO accesses the reports in the bucket through the REST and JavaScript APIs using relative URIs with `/remoteRepository` as the root directory. For example, if you have a report stored in the repository at `/remoteRepository/reports/myReport.jrxml`, the reference to the API is `/reports/myReport`. When opening the report in the viewer, the URL is:

``` text
 http://<JRIO domain>:<JRIO port>/jrio-docs/viewer/viewer.html?jr_report_uri=/reports/myReport
```

See the REST API and JavaScript API chapters for more information on how to use them.

## JasperReports IO for AWS and VPC Security

When creating your JasperReports IO for AWS instance, you select the VPC and a subnet it belongs to. An AWS VPC isolates its resources to a virtual network with advanced security features to protect the user's resources. AWS VPCs include security features such as subnets within availability zones, IP ranges, route tables, and security groups to protect the resources.

To access the services and resources you want to use, your JasperReports IO for AWS instance needs to be on the same VPC as those services and the appropriate subnets across availability zones. If you have issues connecting your JasperReports IO for AWS instance to the resources and services it needs, you may need to update the AWS security features for the VPC to allow access.

## Customizations for JasperReports IO for AWS

JasperReports IO and JasperReports IO for AWS allows you to use your S3 bucket to store customized configuration files for your JasperReports IO instance. In the S3 bucket, you must recreate the JasperReports IO directory structure for the configuration files in a folder called `customizations`, starting with the folders at the `<jrio-install>` root level, such as `jrio` and `repository`.

If you want to remove the customized file from the instance, you need to copy the original configuration file to the S3 bucket and reboot the instance. This will replace the file on the instance and remove the customizations from JasperReports IO. Deleting the customized file from the S3 bucket without adding a replacement will not remove the customizations when the instance is restarted. JasperReports IO for AWS includes a special `service jrio start/stop` command for starting and stopping the web application.

To upload your customization

1.  On the AWS Management Console homepage, click **S3**.

2.  Find the bucket for your JasperReports IO instance and click the name.

3.  Click **Create Folder** and create a folder called `Customizations`.

4.  Click the name of the `Customizations` folder.

5.  Click **Create Folder** and recreate the paths to your files.

    For example, if you want to upload a configuration file that goes in the `<jrio-install>/jrio/webapps/jrio/WEB-INF/classes` directory, you have to create a folder for each directory in that file path.

6.  After creating the folder paths, browse to the folder for your configuration file.

7.  Click **Upload**.

8.  Click **Add files** and find the configuration file on your local machine.

9.  Click **Upload** to upload the configuration file.

    AWS uploads the file and stores it in the S3 bucket.

10. With the configuration file in place, SSH into your instance using your AWS private key and username.

11. Stop the JasperReports IO instance using the following command:

    ``` bash
    sudo service jrio stop
    ```

12. Start the JasperReports IO instance:

``` bash
sudo service jrio start
```

When the JasperReports IO instance restarts, the changes based on the configuration file is in place.

# Cloud Repositories for JasperReports IO

This section describes how JasperReports IO can use reports and resources stored in the cloud repositories (Google Drive, GitHub, and Dropbox) using OAuth 2.0 standard protocol for authorization.

## OAuth2 Repositories

By default, JasperReports IO comes with three preconfigured OAuth2 repositories for Google Drive, GitHub, and Dropbox. Each of these is defined in a separate configuration file as follows:

``` text
[JRIO_WEB_APP]/WEB-INF/applicationContext-google-drive.xml
[JRIO_WEB_APP]/WEB-INF/applicationContext-github.xml
[JRIO_WEB_APP]/WEB-INF/applicationContext-dropbox.xml
```

To use these repositories, each repository configuration file needs to be updated with actual `clientId` and `secretKey` values. These values are obtained from the target cloud storage providers while registering your JasperReports IO instance with them.

The configuration file for the Google Drive repository appears similar to the following:

``` xml
<bean class="com.jaspersoft.jrio.common.repository.google.GoogleDriveRepositoryService">
   <property name="jasperReportsContext" ref="baseJasperReportsContext"/>
   <property name="googleDriveProvider">
      <bean class="com.jaspersoft.jrio.common.repository.google.RequestTokenGoogleDriveProvider">
         <property name="googleDriveFactory">
            <bean class="com.jaspersoft.jrio.common.repository.google.GoogleDriveFactory">
               <property name="clientId" value="put-client-id-here"/>
               <property name="secretKey" value="put-secret-key-here"/>
             </bean>
         </property>
         <property name="serviceCache">
            <bean class="com.jaspersoft.jrio.common.execution.cache.LocalCacheAccessFactory">
               <property name="cacheContainer" ref="localCacheManager"/>
               <property name="cacheRegion" value="googleDriveServices"/>
            </bean>
         </property>
       </bean>
    </property>
</bean>
```

## Accessing Cloud Repositories

The sample web application helps you connect to the cloud repositories (Google Drive, GitHub, and Dropbox) by providing a login UI. You can access the sample cloud repository login UI if you have the required OAuth2 credentials, namely `clientId `and `secretKey`. These values need to be specify in both repository configuration files and the client application configuration file for `JRIO_DOCS_WEB_APP]/WEB-INF/classes/jasperreports.properties`.

The sample web application acts as a proxy to the JasperReports IO application and acquires the OAuth2 authorization tokens from the cloud services. Then these access tokens are passed to the JasperReports IO, allowing JasperReports IO to load reporting resources from the remote repositories.
