---
title: XML/A Against JasperReports Servers Hosting Multiple Organizations
description: "When your JasperReports Server instance hosts multiple organizations, clients that retrieve data from it using XML/A must specify an organization. JasperReports Server looks for the requested XML/A..."
---

# XML/A Against JasperReports Servers Hosting Multiple Organizations

When your JasperReports Server instance hosts multiple organizations, clients that retrieve data from it using XML/A must specify an organization. JasperReports Server looks for the requested XML/A source in that organization. If it does not find it in that organization, it then looks in for the XML/A source in Public folders. The server passes data from the first XML/A source that it finds that matches the specified ID. Since resources in Public folders are shared with all users regardless of their organization, Jaspersoft recommends caution in putting XML/A data sources in Public folders. When done thoughtfully, this configuration can ensure that XML/A requests are always fulfilled, but the approach necessarily exposes the data to a wider group of users than keeping the XML/A source in a more tightly secured location.

!!! note

    When acting as an XML/A server, a server instance that hosts multiple organizations expects the user’s organization ID to be passed in with the credentials. Since the superuser is not associated with any organization, you cannot pass the organization ID with the credentials. Because of this limitation, Jaspersoft strongly recommends that you specify a user associated with an organization (and pass the organization ID along with the username) when connecting via XML/A. For more information, see [Creating an XML/A Connection to JasperReports Server](creating_an_xml_a_connection_to_jasp.md) and [XML/A Security](xml_a_security.md).
