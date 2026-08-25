---
title: Working With Custom Java Classes
description: "Some customizations require writing Java classes to perform some part of the new functionality. Even if you don’t modify the source code of JasperReports Server, you must compile your code with the..."
---

# Working With Custom Java Classes

Some customizations require writing Java classes to perform some part of the new functionality. Even if you don’t modify the source code of JasperReports Server, you must compile your code with the server to deploy your custom features. When you redeploy the web application the files running in the application server are replaced with those you just compiled. For this reason, you must make all of your changes in the source code.

Customizations that involve changes to Java source code have the following requirements:

- You must download the source code distribution and set up an environment where you can build it.

- All files being changed must be edited in the source code, even the interpreted files. This section gives the path to all files in \<js-src\>, which represents the root of the source code. Pay close attention to the path names, because many are similar.

- In order to see the changes, you must build the source code and redeploy the web application.

To build and deploy the source code, follow the instructions in the JasperReports Server Source Build Guide within each distribution:

|  |  |
|----|----|
| Commercial Editions: | <https://www.jaspersoft.com/support> |
| Community Project: | [https://community.jaspersoft.com](https://community.jaspersoft.com/) |

In most cases, once you've successfully built and deployed the source code once, you don't need to edit the properties files or JVM settings when you rebuild after adding new customizations. You also don't need to create or load the databases.

The following procedure is an example of the steps for building and re-deploying the web app after making changes to the source code. This example uses the commercial source code distribution and assumes you're using Apache Tomcat in a Windows environment.

To rebuild the source code

1.  Make sure that all your file changes are saved in the \<js-src\> tree.

2.  Stop the application server.

3.  Select the ****Start Menu \> Accessories****, right-click **Command Prompt**, and select **Run as Administrator**.

    !!! note

        If you do not run Command Prompt as administrator, the build can fail during the deployment phase due to permissions problems when adding and deleting files.

4.  Go to the buildomatic directory in the source distribution:

    `cd <js-src>/jasperserver/buildomatic`

5.  Enter the following commands, checking for the BUILD SUCCESSFUL message upon completion of each one:

    `js-ant build-ce`

    `js-ant build-pro`

    `js-ant deploy-webapp-pro`

6.  Restart Tomcat.
