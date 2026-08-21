---
title: XML/A Security
description: The default configuration uses HTTP Basic authentication to challenge requests for the /xmla path. If the client does not have a valid JasperReports Server username and password in its XML/A...
---

# XML/A Security

The default configuration uses HTTP Basic authentication to challenge requests for the /xmla path. If the client does not have a valid JasperReports Server username and password in its XML/A connection source, the connection fails, unless the username and password are left blank. In this case, the credentials of the logged in user are passed by the client application to the remote server.

Put another way, when creating an XML/A connection, you can either specify a username and password for all users to share, or you can leave the username and password blank, so that the connection passes the current user’s name and password to the server.

!!! note

    With HTTP Basic authentication, clear-text passwords are transmitted in the header of an HTTP request unless you have configured JasperReports Server to use encrypted passwords. For more information, refer to the JasperReports Server Security Guide.

!!! warning

    Regardless of the authentication method you use, clear-text passwords are also transmitted in the body of the XML/A request. Because of the security risk inherent in this approach, Jaspersoft recommends that you always specify a username and password when defining an XML/A connection to prevent your users’ passwords from being transmitted. Do not use the superuser account. For more information, see section [Working with XML/A Connections](working_with_xml_a_connections.md).
