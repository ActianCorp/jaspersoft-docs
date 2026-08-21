---
title: Updating XML/A Connection Definitions
description: "Sample XML/A connections are included with the JasperReports Server sample data. If you plan to use XML/A Web Services in your environment, you may want to update the hard coded values in the sample..."
---

# Updating XML/A Connection Definitions

Sample XML/A connections are included with the JasperReports Server sample data. If you plan to use XML/A Web Services in your environment, you may want to update the hard coded values in the sample connections.

If you have Jaspersoft OLAP enabled (via your license), JasperReports Server can make XML/A connections over the Web Services interface. These connections need a user account for authentication. You may have different usernames and passwords than the defaults in the sample data. Additionally, your application server hostnames and port may be different than the default values. In such cases, the connections and resources that rely on them will fail.

The sample connections are:

- Foodmart Sample XML/A connection

- SugarCRM Sample XML/A connection

To validate and update these resources:

1.  Log into JasperReports Server as an administrator (like `jasperadmin`).

<!-- -->

1.  Navigate to the Repository Management page (**View****\>** **Repository**).
2.  Click to expand the **Analysis Components** folder, then the **Analysis Connections** folder. Click to highlight **Foodmart XML/A Connection**, then click **Edit**.
3.  Edit the following fields:

- URI (hostname and port)
- Login Username
- Login Password

1.  Click **Next**, then **Save**.
2.  Make the same updates for **SugarCRM XML/A Connection**.
