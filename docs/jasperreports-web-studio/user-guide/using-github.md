---
title: Using GitHub
description: The login screen of JasperReports Web Studio also features a login button for connecting to GitHub. It allows the user to create and modify report template files stored in the GitHub project...
---

# Using GitHub

The login screen of JasperReports Web Studio also features a login button for connecting to GitHub. It allows the user to create and modify report template files stored in the GitHub project associated with the respective account.

The GitHub login button is disabled by default. The OAuth2 application registration information must be specified in the application start script using the system configuration properties. The startup page provides authorization information. This allows the application to access remote GitHub repositories. The access can be obtained by registering your local instance of JasperReports Web Studio with GitHub by following the steps detailed on this page:

<https://docs.github.com/en/rest/guides/basics-of-authentication>

The client ID and the secret key provided by GitHub for your registered application can be set in the start script of the JasperReports Web Studio. Use *-D* arguments in the command that open the Java Virtual Machine:

- `-Djsw.github.client.id=[YOUR_CLIENT_ID] `
- `-Djsw.github.secret.key=[YOUR_SECRET_KEY]`
