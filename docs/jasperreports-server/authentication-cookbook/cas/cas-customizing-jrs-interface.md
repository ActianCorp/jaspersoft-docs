---
title: Customizing the JasperReports Server Interface for CAS
description: "When a user who's logged into JasperReports Server through CAS clicks the Log Out link, they'll see the JasperReports Server login page, instead of the CAS login page."
---

# Customizing the JasperReports Server Interface for CAS

When a user who's logged into JasperReports Server through CAS clicks the **Log Out** link, they'll see the JasperReports Server login page, instead of the CAS login page.

This is due to the way the Spring framework integrates with CAS. Because all login requests are redirected to CAS, JasperReports Server doesn't know the logged-in or logged-out state of the user. Instead, JasperReports Server treats all requests as if they're already logged in. If the CAS check doesn't go through, JasperReports Server redirects back to the CAS login page. But if the user clicks **Log Out**, this redirection doesn't happen.

To avoid confusion, you can remove or hide the **Log Out** link using the techniques in “Customizing the User Interface” in the JasperReports Server Ultimate Guide.
