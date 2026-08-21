---
title: Working with Java in Eclipse
description: "For users who are unfamiliar with Eclipse, this section describes how to compile a class in Eclipse and add it to a project in Jaspersoft Studio."
---

# Working with Java in Eclipse

For users who are unfamiliar with Eclipse, this section describes how to compile a class in Eclipse and add it to a project in Jaspersoft Studio.

First, if you have never used Java in the Eclipse RCP, you must enable the Java perspective. You only have to do this once.

To enable the Java perspective in Eclipse

1.  Select **Window \> Open Perspective** on the main menu bar.
2.  In the **Open Perspective** dialog, click **Show All**.
3.  Select Java and click **OK**.
4.  When prompted, click **OK** to enable Java development.

The Eclipse UI changes to the Java perspective. A Java icon ![jss icon java perspective](assets/images/jss-icon-java-perspective.png) is added to the top right of the Eclipse window. In future, you can switch to this perspective by clicking ![jss icon java perspective](assets/images/jss-icon-java-perspective.png). To switch back to the Jaspersoft Studio perspective, click the **Report Design** icon ![jss icon report perspective](assets/images/jss-icon-report-perspective.png).

To create a Java project

1.  Select **File \> New \> Project** or click ![jss icon new](assets/images/jss-icon-new.png) on the main toolbar and select **Project** from the menu.
2.  In the **New Project** wizard, click **Java** to expand it, and select **Java Project**, then click **Next**.
3.  Enter a name for your project. For this example, use SimpleChartCustomizer.
4.  Click **Finish**.

To add libraries to your Java project

1.  Right-click your project name in the Package Explorer and select **Build Path \> Add Libraries**.
2.  In the **Add Library** dialog, select JasperReports Libraries, then click **Finish**.

The selected library is added to SimpleChartCustomizer.

1.  Right-click your project name in the Package Explorer and select **Build Path \> Add Libraries**.
2.  In the **Add Library** dialog, select **JasperReports Library Dependencies**, then click **Finish**.

For example, if you are creating a chart customizer, the library dependencies you have added include the JFreeCharts libraries.

To create a Java package and add a file

1.  Open your project in Package Explorer.
2.  Right-click the src folder and select **New \> Package**. The **New Java Package** dialog opens.
3.  Enter a name for your package. For this example, enter `com.jaspersoft.studio.sample.customizer`.
4.  Click **Finish**.
5.  Drag your Java file from a folder on your file system to the package folder in Eclipse.
6.  In the **File Operation** dialog, select **Copy files** and click **OK**.

To build a Java project and export a JAR file

1.  Right-click the project folder and select **Build Project** from the menu.
2.  Right-click the project folder and select **Export**.
3.  In the **Export** dialog, select **Java \> JAR file** and click **Next**.
4.  On the **JAR File Specification** page, make sure that your project is selected and that **Export generated class files and resources** is checked.
5.  Enter a name for your JAR and an export destination.
6.  Click **Finish**.

## Adding a JAR to Jaspersoft Studio

To add a JAR to a Jaspersoft Studio project

1.  If you have been using the Java perspective in Eclipse, click ![jss icon report perspective](assets/images/jss-icon-report-perspective.png) to return to the Report Design perspective.
2.  Right-click your project in Project Explorer and select **New \> Folder**. Enter lib as the name of the folder.
3.  Copy your JAR files to this folder. To do this:
4.  Drag the JAR files from the folder in the file system to the lib folder in the Eclipse user interface.
5.  In the **File Operation** dialog, select **Copy files** and click **OK**.
6.  Right-click your project and select **Refresh**.
7.  Select all the JAR files, then right-click one of them and select **Build Path \> Add to Build Path**.

The JAR files are added to your project.
