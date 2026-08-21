---
title: Using Single Sign-on with JasperReports Server
description: You can use single sign-on (SSO) to connect to a JasperReports Server instance that has been configured to work with the Central Authentication Service (CAS) protocol. For information about...
---

# Using Single Sign-on with JasperReports Server

You can use single sign-on (SSO) to connect to a JasperReports Server instance that has been configured to work with the Central Authentication Service (CAS) protocol. For information about configuring CAS for JasperReports Server, see the JasperReports Server External Authentication Cookbook.

Configure JasperReports Server

Before you begin, configure your JasperReports Server instance for CAS, as described in JasperReports Server External Authentication Cookbook.

Add the CAS server to your Jaspersoft Studio workspace

1.  In Jaspersoft Studio, select **Window \> Preferences** (**Eclipse \> Preferences** on Mac).
2.  In the Preferences window, navigate to **Jaspersoft Studio \> Jaspersoft Server Setting \> Single Sign On Server**.

|                                                                  |
|------------------------------------------------------------------|
| ![jss preferences sso](../assets/images/jss-preferences-sso.png) |
| *Figure 1: Single Sign On Servers in Preferences Dialog*         |

1.  In the **Single Sign On Servers** pane, click **Add**.
2.  Enter the **URL** of your **CAS** server along with the **Username** and **Password** that you want to use for access.

|                                                        |
|--------------------------------------------------------|
| ![jss sso server](../assets/images/jss-sso-server.png) |
| *Figure 2: SSO Server Settings Dialog*                 |

1.  Click **OK**.

The CAS server is added to the list of available single sign-on servers.

1.  Click **OK**.

Configure your JasperReports Server connection to use CAS

1.  In Jaspersoft Studio, open the **Repository Explorer**, then click the **Create a JasperReports Server Connection** icon ![create server connection icon](../assets/images/create-server-connection-icon.png).
2.  Select **Advanced Settings**.
3.  Enable the **Use Single Sign On** option.

The **Account** section of the **Server Profile Wizard** changes.

|  |
|----|
| ![jss2jrs publishing jrl advancedsettings](../assets/images/jss2jrs-publishing-jrl-advancedsettings.png) |
| *Figure 3: Setting Single Sign-on in the Server Profile Wizard* |

1.  If the server hosts multiple organizations, enter the ID of the organization to which you belong. This can be the root organization (in which case you can leave this entry bar blank) or another organization.
2.  Select the CAS server that you want to use for this connection from the **SSO Server** menu.
3.  Click **Test Connection** to test the connection. This may take some time, especially the first time you connect.
4.  Click **OK** in the confirmation dialog.
5.  Click **OK** to create the connection.
