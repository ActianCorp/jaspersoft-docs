---
title: Using Google Drive
description: The login screen of JasperReports Web Studio shows a button that allows you to log in to a Google Drive account and edit reporting resources stored there. But it requires specifying Google OAuth2...
---

# Using Google Drive

The login screen of JasperReports Web Studio shows a button that allows you to log in to a Google Drive account and edit reporting resources stored there. But it requires specifying Google OAuth2 application registration information in the start script of the application using system configuration properties.

The installer does not come with such Google Drive authorization information preset in the application start script and this is why the respective login button is disabled.

In order to enable the Google Drive login button, you need to register your instance of the JasperReports Web Studio with Google Drive by following the steps detailed on this page:

<https://developers.google.com/drive/api/v3/about-auth>

Once you have obtained the client ID and the secret key for your application at Google, you can set them in the start script of the JasperReports Web Application using the following system properties added with a *-D* flag to the command that launches the Java Virtual Machine as follows:

-   `-Djsw.google.client.id=[YOUR_CLIENT_ID]`
-   `-Djsw.google.secret.key=[YOUR_SECRET_KEY]`
