---
title: New Features and Changes
description: This section describes new features and changes introduced in the following JasperReports® Server for AWS Marketplace (JRS for AWS) releases. This includes the specific changes made to the Amazon...
---

# New Features and Changes

This section describes new features and changes introduced in the following JasperReports® Server for AWS Marketplace (JRS for AWS) releases. This includes the specific changes made to the Amazon Machine Images (AMIs) and CloudFormation Templates (CFTs) for JRS for AWS.

## Version 9.0.0

## AMI Changes

AMI changes for JRS for AWS 9.0.0 include:

- Latest Amazon Linux 2 base AMI

## Marketplace Template Changes

Marketplace CFT changes for JRS for AWS 9.0.0 include:

- Dropped support of the following ec2 instance types: m5.large
- Set m5.xlarge as the default instance type, added support of m5.xlarge, m5.2xlarge, r5a.xlarge, r5a.2xlarge instance types
- Dropped support of GovCloud

## Quick Start Template Changes

Quick Start Cluster CFT changes for JRS for AWS 9.0.0 include:

- Dropped support of Quick Start CFT

## Version 8.0.1

## AMI Changes

AMI changes for JRS for AWS 8.0.1 include:

- Latest Amazon Linux 2 base AMI.
- Tomcat 9.0.54, Java 11, and PostgreSQL 12.
- New approach to fetch Tomcat from Apache archive to remove dependency from Amazon repository:
  - An additional upgrade_tomcat.sh script is placed in /etc/jasperserver which can be used to downgrade/upgrade Tomcat to the desired version. The script expects one parameter which should be the tomcat tar file path, for example: `/etc/jasperserver/upgrade_tomcat.sh`<br>
    <https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.52/bin/apache-tomcat-9.0.52.tar.gz><br>
    This script can be called in the cfn-init part of templates as well, to include Tomcat changes at runtime.
- Included *cfn-bootstrap* package while building the AMI and removed install command from the templates.
- Implemented single init systemd service to perform all required boot-time operations and configuration. Previously such operations were run by separate 3 chkconfig services.
- Modified service file for Tomcat to take values from an additional environment file if found. This feature is implemented for cluster templates to set the memory parameters for JasperReports® Server ( *-XX:MinRAMPercentage* and *-XX:MaxRAMPercentage*).
- For Cluster templates, an additional repository database check is added. If a db with the same name as the desired repository database is already present in RDS, then it skips the DB creation and installation, including sample DBs.

## Marketplace Template Changes

Marketplace CFT changes for JRS for AWS 8.0.1 include:

- Added a section in cfn-init to create an environment file to be picked up by the Tomcat service. This sets *MinRam* and *MaxRam* percentages to utilize the instance memory efficiently. Additional environment variables can also be defined by the user if needed (only for cluster templates).
- Removed *cfn-bootstrap* package install step as now it is a part of AMI.
- Replaced Classic Load Balancer with Application Load Balancer on cluster templates.
- Replaced LaunchConfig with LaunchTemplate (AWS recommendation is to use LaunchTemplate)
- Restricted permission to only resources created as part of template deployment in comparison to previous open permissions to all. This breaks the auto discovery feature of data sources for RDS and Redshift. If needed, the user can add those permissions in the role created to the resources. For more information, see the JasperReports® Server User Guide.

## Quick Start Template Changes

Quick Start Cluster CFT changes for JRS for AWS 8.0.1 include:

- Added extra parameters for RDS security Group in the existing infrastructure template and accordingly updated RDS and new infra templates. This ensures that the correct ingress rule to RDS is created by the template.
- Replaced LaunchConfig with LaunchTemplate (AWS recommendation is to use launchTemplate).
- Added a section in cfn-init to create an env file to be picked up by the Tomcat service. This sets *MinRam* and *MaxRam* percentages to utilize the instance memory efficiently. Additional env variables can also be defined in this by the user if needed.

## Version 7.9.x

## AMI Changes

AMI changes for JasperReports® Server 7.9.x include:

- Latest Amazon Linux 2 base AMI
- Tomcat 9.0.54, Java 11, and PostgreSQL 11

## Version 7.8.1

## AMI Changes

AMI changes for JasperReports® Server 7.8.1 include:

- Latest Amazon Linux 2 base AMI.
- Tomcat 9.0.54, Java 11, and PostgreSQL 11.
- New approach to fetch Tomcat from Apache archive to remove dependency from Amazon repository:
  - An additional upgrade_tomcat.sh script is placed in /etc/jasperserver which can be used to downgrade/upgrade Tomcat to the desired version. The script expects one parameter which should be the tomcat tar file path, for example: `/etc/jasperserver/upgrade_tomcat.sh`<br>
    <https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.52/bin/apache-tomcat-9.0.52.tar.gz><br>
    This script can be called in the *cfn-init* part of templates as well, to include Tomcat changes at runtime.
- Included *cfn-bootstrap* package while building the AMI and removed install command from the templates.
- Implemented single init systemd service to perform all required boot-time operations and configuration. Previously such operations were run by separate 3 chkconfig services.

## Version 7.5.2

## AMI Changes

AMI changes for JasperReports® Server 7.5.2 include:

- Latest Amazon Linux 2 base AMI (upgraded from Linux 1).
- Apache Tomcat 9.0.54, Java 11, and PostgreSQL 11.
- New approach to fetch Tomcat from Apache archive to remove dependency from Amazon repository:
  - An additional upgrade_tomcat.sh script is placed in /etc/jasperserver which can be used to downgrade/upgrade Tomcat to the desired version. The script expects one parameter which should be the tomcat tar file path, for example: `/etc/jasperserver/upgrade_tomcat.sh`<https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.52/bin/apache-tomcat-9.0.52.tar.gz><br>
    This script can be called in the *cfn-init* part of templates as well, to include Tomcat changes at runtime.
- Included *cfn-bootstrap* package while building the AMI and removed install command from the templates.
- Implemented single init systemd service to perform all required boot-time operations and configuration. Previously such operations were run by separate 3 chkconfig services.
