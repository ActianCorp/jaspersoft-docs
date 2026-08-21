---
title: Setting httpOnly for Cookies
description: "The application server that hosts JasperReports Server handles the session cookie. To prevent malicious scripts on a client from accessing the user connection, you should set the application server..."
---

# Setting httpOnly for Cookies

The application server that hosts JasperReports Server handles the session cookie. To prevent malicious scripts on a client from accessing the user connection, you should set the application server to use httpOnly cookies. This tells the browser that only the server may access the cookie, not scripts running on the client. This setting safeguards against cross-site scripting (XSS) attacks. Consult the documentation for your application server on how to set httpOnly cookies.
