---
title: Reloading the JasperReports® Server Web App
description: "When you customize interpreted files such as the JSP, JavaScript, and properties files, you need to reload them in the JasperReports Server web application for your changes to take effect. The..."
---

# Reloading the JasperReports® Server Web App

When you customize interpreted files such as the JSP, JavaScript, and properties files, you need to reload them in the JasperReports Server web application for your changes to take effect. The standard installation of the server includes only shortcut actions for starting and stopping the bundled application server and database server. If you have other web applications that you don’t want to stop, or if you're doing a lot of customization and testing, it's simpler and quicker to simply reload the web app without restarting the application server.

Each application server has its own management console that lets you view and control deployed web apps. This example shows how to manage the JasperReports Server web app using the GUI in Apache Tomcat.

1.  If you have not configured any users on your Apache Tomcat server, you must first add a user and give it the `manager-gui` role. To do this:

    1.  Edit the file `<js-install>/apache-tomcat/conf/tomcat-users.xml`.
    2.  Create a user if necessary and give it the `manager-gui` role. You can give the user any name and password you prefer.
    3.  Restart your Apache Tomcat server for this change to take effect.

    ``` xml
    <tomcat-users>
      <role rolename="manager-gui"/>
      <user username="tomcat" password="tomcat" roles="manager-gui"/>
    </tomcat-users>
    ```

2.  Once you have created a manager-gui user, open the Apache Tomcat Manager page in a browser:<br>
    `http://<host>:<port>/manager/html/`, where `<host>` and `<port>` are where you installed the server. For a default installation, use `http://localhost:8080/manager/html/`.

3.  When prompted, log in with your manager user credentials.

4.  On the Apache Tomcat management interface, scroll down to find the jasperserver\[-pro\] application, and click **Reload**.

5.  Confirm your reload of the web app and, when the page reloads, open the JasperReports Server login page to see your changes. If the manager doesn’t reload, there was likely an error in the files, and you must stop and restart the app server.
