---
title: Restarting JasperReports Server
description: "When you've configured all the beans in the appropriate files, restart JasperReports Server. Because of the modification to the application server configuration in Configuring Java to Trust the CAS..."
---

# Restarting JasperReports Server

When you've configured all the beans in the appropriate files, restart JasperReports Server. Because of the modification to the application server configuration in [Configuring Java to Trust the CAS Certificate](cas-configuring-java-certificate-trust.md), you must restart the application server, which also restarts JasperReports Server.

Instead of navigating to the JasperReports Server login page, go directly to another page in JasperReports Server, for example your home page:

http://host1:8080/jasperserver/flow.html?\_flowId=homeFlow

If JasperReports Server, CAS, and your certificates are configured correctly, you'll be prompted to log into the CAS server; when you do, you'll be redirected to the JasperReports Server home page for the logged-in user.
