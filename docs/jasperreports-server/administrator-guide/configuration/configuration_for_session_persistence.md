---
title: Configuration for Session Persistence
description: "Many application servers can store user sessions while a web app is offline, for example when changing JasperReports Server configuration files. The app server remembers all the information about a..."
---

# Configuration for Session Persistence

Many application servers can store user sessions while a web app is offline, for example when changing JasperReports Server configuration files. The app server remembers all the information about a user's session, such as the session ID and what page was being viewed. When the web app restarts, the user session is restored. The user does not have to log in again, and often may not even notice that the server was temporarily unavailable. This is called session persistence.

!!! note

    Sessions do not persist when redeploying a web app in the application server, only when restarting the web app.

JasperReports Server supports a limited form of session persistence. When session persistence is enabled in the app server, sessions can be restored in the following cases:

-   Browsing the repository, expanding folders in the repository tree, and viewing folder contents.

-   Searching the repository, including all search filters and results.

-   Repository permissions dialog, including state and selections.

-   Add folder dialog.

-   Add resource dialogs, including adding or editing a data source, JasperReport, and other repository objects.

-   Copy, cut, and paste resources in the repository.

-   Scheduling a report, including all information such as a schedule and notifications.

If the server becomes unavailable when using the pages or dialogs above, the user can see the pause only when performing an action on these pages, such as submitting. When the server has finished restarting, the user can continue interacting with these UI elements. If the user takes no action while the server is unavailable, they may not even notice the server restart.

However, for other interactive dialogs in JasperReports Server, the state is too large to store in the user session. These features do not support session persistence and unsaved data can be lost:

-   Ad Hoc Editor - The state of the report layout and data in the Ad Hoc Editor cannot be restored.

-   Dashboard designer - The contents and state of the canvas cannot be restored.

-   Interactive report viewer - The data in the report, as well as the state of column sorting and filtering cannot be saved.

-   Domain designer - Any tables, joins, filters, calculated fields, and display names cannot be restored.

-   Administration dialogs - When creating or editing users, organizations, or roles, the information entered in a dialog cannot be restored if it was not submitted.

In the cases listed above, the user's work is interrupted, and any unsaved work is lost. However, when the server restarts, the user does not have to log in again, the server displays a message about the session that could not be fully restored, and redirects the user to the home page. The user must relaunch the interactive feature and recreate any unsaved work.

Session persistence also affects web service calls. The REST API supports a login to store a session ID, and with persistence enabled, that session ID will still be valid when the application server restarts. This simplifies the code when you need to handle timeouts. In general, web service calls do not support interactive work like designing an Ad Hoc view, a dashboard, a Domain, or exploring data in OLAP, so they are not affected by the lack of session persistence in most cases. However, web service calls are affected in the following case:

-   Report execution - All asynchronous API calls for running and exporting reports rely on the large JasperPrint object that cannot be persisted. When the server restarts, the asynchronous calls return errors because the reports could not be saved in the session. Your application needs to detect this error and include code for rerunning the report.

!!! note

    JasperReports Server also supports session replication among multiple instances of the server in a cluster. However, session replication has the same limitations because it is based on session persistence. For more information, see the JasperReports Server Ultimate Guide.

The following procedure gives the configuration in JasperReports Server and the Apache Tomcat application server to enable session persistence. For another application server, refer to that server's documentation.

To configure JasperReports Server and Apache Tomcat for session persistence

1.  Edit the file `.../META-INF/context.xml` to comment out the Manager property as follows:

    ``` text
    <!-- Manager pathname="" /-->
    ```

2.  Edit the file `.../WEB-INF/web.xml` to make the following changes.

    1.   Locate the `ClusterFilter` given in the comments and uncomment it as follows:

    2.   Locate the corresponding mapping for the `ClusterFilter` and uncomment that, too. Also uncomment the `<distributable>` element below it as follows:

    3.  ``` xml
        <filter>
                <filter-name>ClusterFilter</filter-name>
                <filter-class>com.jaspersoft.jasperserver.war.TolerantSessionFilter</filter-class>
            </filter>
        ```

    4.  ``` xml
            <filter-mapping>
                <filter-name>ClusterFilter</filter-name>
                <url-pattern>/*</url-pattern>
            </filter-mapping>
            <distributable/>
        ```

3.  Add the following property to your JVM environment:

    ``` text
     -Dorg.apache.catalina.session.StandardSession.ACTIVITY_CHECK=true
    ```

4.  Restart your Apache Tomcat application server.
