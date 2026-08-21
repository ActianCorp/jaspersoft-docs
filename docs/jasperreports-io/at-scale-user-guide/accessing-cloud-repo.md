---
title: Accessing Cloud Repositories
description: "The sample web application helps you connect to the cloud repositories (Google Drive, GitHub, and Dropbox) by providing a login UI. You can access the sample cloud repository login UI if you have the..."
---

# Accessing Cloud Repositories

The sample web application helps you connect to the cloud repositories (Google Drive, GitHub, and Dropbox) by providing a login UI. You can access the sample cloud repository login UI if you have the required OAuth2 credentials, namely clientId and secretKey. These values should be specified in both repository configuration files and client application configuration file `[JRIO_DOCS_WEB_APP]/WEB-INF/classes/jasperreports.properties`.

The sample web application acts as a proxy to the Jaspersoft IO At-Scale application and acquires the OAuth2 authorization tokens from the cloud services. Then these access tokens are passed to the Jaspersoft IO At-Scale, allowing Jaspersoft IO At-Scale to load reporting resources from the remote repositories.
