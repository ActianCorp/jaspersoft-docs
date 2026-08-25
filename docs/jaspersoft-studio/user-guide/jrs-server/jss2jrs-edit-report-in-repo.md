---
title: Editing a Report
description: "In the Repository Explorer, the !jss repo explorer report unit icon means a report unit, and !jss repo explorer jrxml means a JRXML file. When you work with a JRXML file in the Repository, Jaspersoft..."
---

# Editing a Report

In the **Repository Explorer**, the ![jss repo explorer report unit](../assets/images/jss-repo-explorer-report-unit.png) icon means a report unit, and ![jss repo explorer jrxml](../assets/images/jss-repo-explorer-jrxml.png) means a JRXML file. When you work with a JRXML file in the Repository, Jaspersoft Studio operates on a copy of the file. You need to upload the JRXML file to put it back into the repository when finished.

To edit a JRXML file in the Repository

1.  In the **Repository Explorer**, right-click the JRXML file, and select **Open in Editor**. The JRXML appears in the **Design** tab.

    The JRXML is stored locally in your workspace. The default location is in the user directory of your operating system. For example, in Windows, the default workspace is `C:\Users\<username>\JaspersoftWorkspace\MyReports`.

2.  Edit the file, either in the **Design** tab or in the **Source** tab. For example, in the **Repository Explorer** navigate to the Images\JR Logo image resource, and drag it into to the report's Title band. The logo appears in the **Design** tab.

3.  Click **Save**. If you are prompted to publish the report, click **Yes**.

4.  Specify a server and a repository location. To save the JRXML to the same report unit where you opened it, click **Next**.

    If the report relies on resources, you are asked if you want to overwrite the resources currently in the repository. If you added resources to the report, you are prompted to add them to the repository.

5.  Click **Next** and specify a data source for the report. You cannot change a data source through the **Publish Wizard**.

Click **Finish**. Your changes are saved to the repository.

To edit a Report Unit in the Repository

1.  In the **Repository Explorer**, right-click the report unit and select **Properties**.

2.  On the **Resource Editor** tab, change the name and description.

3.  On the **Report Unit** tab, you can change the JRXML file for the report, either by selecting one from the repository, or uploading one through Jaspersoft Studio.

4.  On the **Data Source** tab, select the data source from the repository or from Jaspersoft Studio.

5.  On the **Input Controls** tab, set the display properties for any input controls:

    - **Pop-up Screen**: the controls are shown on-top of the report viewer.
    - **Separate Page**: the controls are shown in a different page than the report viewer.
    - **Top of Page**: the controls are shown at the top of the report viewer.
    - **In Page**: the controls are shown next to the report viewer.

    !!! note

        Input controls can be created in the JasperReports Server repository and referenced in reports. If you want to use an input control from JasperReports Server in a report, the input control must meet two conditions:

        - The parameter name in the input control must correspond to the name of the parameter in the report. No error occurs for a mismatch, but at run time NULL is passed instead of the actual value of the parameter.
        - The input control and its corresponding parameter must be of compatible datatypes (for example, both must be text types or date types). If there is a mismatch, the report fails and an exception is returned.

        See the JasperReports Server Administrator Guide for more information.

6.  You can also use the JSP field to modify the appearance of the controls. Specify a name of a JSP file in WEB-INF of the server's host to define the page that displays input controls.

7.  Click **Finish**.
