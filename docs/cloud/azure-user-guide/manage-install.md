---
title: Managing Your Installation
description: "After launching the Jaspersoft VM on Azure, you can manage the installation, which includes:"
---

# Managing Your Installation

After launching the Jaspersoft VM on Azure, you can manage the installation, which includes:

-   Applying a license for Jaspersoft for Azure
-   Upgrading Azure instance
-   Retrieving logs
-   Stopping and restarting the tomcat

Installation directory:

`/opt/jaspersoft/jasperreports-pro`

License directory:

`/opt/jaspersoft/tomcat/webapps/jasperserver-pro`

## Applying a License for Jaspersoft for Azure

Bringing your own SQL Server license through License Mobility, also referred to as BYOL. It means using an existing SQL Server Volume License with Software Assurance in an Azure VM. A SQL Server VM using BYOL only charges for the cost of running the VM, not for SQL Server licensing. Given that you have already acquired licenses and Software Assurance through a Volume Licensing program.

To use BYOL with a SQL Server VM, you must have a license for SQL Server Standard or Enterprise and Software Assurance. This is a required option through some volume licensing programs and an optional purchase with others.

To create an Azure VM running SQL Server 2017 with one of these bring-your-own-license images, see the VMs prefixed with "{BYOL}":

-   [SQL Server 2017 Enterprise Azure VM](https://portal.azure.com/#create/Microsoft.BYOLSQLServer2017EnterpriseWindowsServer2016)
-   [SQL Server 2017 Standard Azure VM](https://portal.azure.com/#create/Microsoft.BYOLSQLServer2017StandardonWindowsServer2016)

For more information on Azure licenses, contact [Azure support](https://azure.microsoft.com/en-us/support/options/).
