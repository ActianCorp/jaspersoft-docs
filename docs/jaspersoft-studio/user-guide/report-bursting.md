---
title: Report Bursting and Report Splitting
description: "You can burst and split a report in Jaspersoft Studio. Report bursting is done by a report that creates scheduled jobs in a JasperReports Server instance for other reports. When you run a report, it..."
---

# Report Bursting and Report Splitting

You can burst and split a report in Jaspersoft Studio. Report bursting is done by a report that creates scheduled jobs in a JasperReports Server instance for other reports. When you run a report, it results in several other report jobs and the generated output is based on the bursting report execution.

Report splitting works with a single report that can be run in the JasperReports Server scheduler and the output is split into several parts and stored in the repository.

This chapter contains the following sections:

-   Report Bursting

-   [Report Splitting](report-splitting.md)

## Report Bursting

Jaspersoft Studio provides a built-in report bursting feature that allows you to burst a report based on some parameters and generate multiple reports, with each report having specific data. You can send these reports to different recipients with data relevant to them. For example, a single report containing shipping data of countries, such as Mexico, Canada, and the US, can be burst into different reports based on each country.

Report bursting is done by a report that triggers the bursting operation. Because reports have the built-in capability to retrieve records from a database, they can iterate through the records in the database. A bursting report needs a JasperReports Server connection to work with JasperReports Server. This connection is provided by the Jaspersoft Server data adapter and helps to retrieve information from JasperReports Server to trigger the bursting.

### Bursting Scriptlet

A bursting report has a special scriptlet that is a bursting component. This scriptlet is attached to the data set of the bursting report. You can define a scriptlet by using scriptlet properties including, Name, Description, and Class. However, for class, there is a default value provided in Jaspersoft Studio itself, for example, Class: `com.jaspersoft.jasperreports.jrs.bursting.BurstingScriptlet`

A bursting scriptlet ensures it creates a scheduler job for each record in the data source with the required parameters by calling the REST API of the JasperReports Server. The jobs are created automatically during the report execution for each record in the data source.

The scriptlet uses a data adapter to create the connection for `rest_V2/jobs` when the report itself does not use a JasperReports data adapter.

### Bursting a Report

The following example shows how to burst a report and send data of a country related to each recipient.

To burst a report

1.  Create a CSV file with two columns Country and Email, and create a data adapter that points to this CSV file.

2.  Create a report containing two fields country `$F(Country)` and Email address of recipient `$F(Email)`. This report is a bursting report used for bursting operation.

3.  A bursting scriptlet is required for the bursting report. To create a scriptlet, in the **Outline** view, right-click the **Scriptlets**, and select **Create Bursting Scriptlet**. It creates a bursting scriptlet.

    |                                                           |
    |-----------------------------------------------------------|
    | ![create scriptlet](assets/images/create%20scriptlet.PNG) |
    | *Figure 1: Creating a Scriptlet*                          |

4.  To edit the properties of the bursting scriptlet, right-click the bursting scriptlet and select **Edit Bursting Properties**. Bursting scriptlet edit dialog appears.

    |                                                       |
    |-------------------------------------------------------|
    | ![edit scriptlet](assets/images/edit%20scriptlet.PNG) |
    | *Figure 2: Editing a Scriptlet*                       |

5.  On the **Parameters** tab, click **Add** to add the parameter. Report Bursting Parameter dialog appears. Enter the Parameter name and Parameter value that you want to pass to the burst reports. For example:<br>
    **Parameter name**: ShipCountry_1<br>
    **Parameter value**: $F{Country}

    |                                                               |
    |---------------------------------------------------------------|
    | ![bursting parameter](assets/images/bursting%20parameter.PNG) |
    | *Figure 3: Parameter and its Value*                           |

6.  On the **Options Configuration** tab, select the **Essential Options** from the left panel and set the following fields:<br>
    **Server profile**: select the server connection from the dropdown for the bursting report. For example, JasperReports Server Pro.<br>
    **Enabled**: true<br>
    **Job Label**: Sales By Country<br>
    **Report URI**: browse the repository and select the report you want to burst.

    !!! note

        The path to the burst report in a bursting report is interpreted as relative to the user that runs the report. So if the burst report is part of an organization, you cannot have a bursting report that works for both superuser and users from that organization (jasperadmin and joeuser). superuser needs the absolute path and users from the organization needs a relative path. It is recommended to run bursting reports that belong to the same organization as the user.

    <br>

    **Server data adapter**: `JasperReportsServerDataAdapater.jrdax`. This data adapter makes the connection to the JasperReports Server and lets you publish the reports to the server.

    |  |
    |----|
    | ![bursting essential opts](assets/images/bursting%20essential%20opts.png) |
    | *Figure 4: Adding Essential Options* |

7.  Select Output File Options and set the following options:<br>
    **File name**: “Sales-” + $F{Country}<br>
    **Formats**: select the output format for the burst report, for example, PDF or Excel.<br>
    **Sequential File Names by Timestamp**: true<br>
    **Repository Folder URI**: specify the location for the report exports to be generated in the repository, for example, /public/bursting/output. You can choose the output folder using the JasperReports Server picker (browse icon) or the expression editor. Before selecting the output folder, ensure that the output folder exists in the JasperReports Server repository.

    |                                                                     |
    |---------------------------------------------------------------------|
    | ![bursting output opts](assets/images/bursting%20output%20opts.PNG) |
    | *Figure 5: Adding Output File Options*                              |

8.  Select **Job Run Notifications** and enter the following information:

    1.  In the **To** field, enter the email id of the recipients, to do so:

        1.  Click ![jss icon expression editor](assets/images/jss-icon-expression-editor.png) to enter the expression, **Edit property value** dialog appears.

        2.  Select **Use Expression** and click the expression editor.

            |                                                 |
            |-------------------------------------------------|
            | ![burst email](assets/images/burst%20email.PNG) |
            | *Figure 6: Edit Property Value Dialog*          |

        3.  Select **Email Field String**.

            |                                                               |
            |---------------------------------------------------------------|
            | ![burst email field](assets/images/burst%20email%20field.PNG) |
            | *Figure 7: Expression Editor*                                 |

        4.  Click **Finish**.

        5.  Click **OK**.

    2.  In the **Subject** field, enter the subject for the mail to be sent to recipients.

    3.  In the **Message** field, type the message you want to send to recipients.

    4.  Click **OK**.

9.  Run a bursting report.

Burst reports are created in the output folder for different countries in both formats PDF and Excel.
