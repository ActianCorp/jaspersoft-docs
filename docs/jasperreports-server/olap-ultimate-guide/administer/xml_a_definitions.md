---
title: XML/A Definitions
description: "XML for Analysis, or XML/A, uses SOAP (Simple Object Access Protocol) to define XML message interfaces for the client application to interact with the database server for online analytical..."
---

# XML/A Definitions

XML for Analysis, or XML/A, uses SOAP (Simple Object Access Protocol) to define XML message interfaces for the client application to interact with the database server for online analytical processing, or OLAP, over the Internet. Based on MDX, XML/A provides a standard language interface for sending and processing OLAP requests. For more information, see [http://www.xmla.org/nonmemdefault.asp](http://www.xmla.org/nonmemdefault.asp) or <https://learn.microsoft.com/en-us/previous-versions/sql/sql-server-2005/ms187178(v=sql.90)>.

The advantage of XML/A is that it is agnostic regarding query languages and data sources. That is, XML/A provides a uniform interface to various multidimensional servers, such as Microsoft SQL Server Analysis Services and Mondrian OLAP server, and to various data sources, such as MySQL or PostgreSQL. However, take care when using XML/A, as not all providers behave the same way.

Jaspersoft OLAP provides XML/A support in terms of XML/A definitions for discovering multidimensional metadata, XML/A connections for accessing multidimensional data sources using SOAP, and XML/A OLAP views for querying multidimensional data.

One popular use of XML/A is to allow Excel users to slice and dice OLAP data through Pivot Tables with an ODBO driver. Jaspersoft ODBO Connect is such an ODBO driver, which can connect to Jaspersoft OLAP, Mondrian, and Microsoft SQL Server Analysis Services. To purchase ODBO Connect, please contact your sales representative.

You can create an OLAP view against an XML/A connection just as you did against a Mondrian connection in [OLAP Views](../get-started/olap_views.md). The steps are nearly identical. Simply select an XML/A connection instead of a Mondrian connection when prompted for the connection. Ad Hoc views can also be built against XML/A connections.

For more information about creating XML/A sources and connections, refer to the Jaspersoft OLAP User Guide , which is available at the [Jaspersoft Community site](http://community.jaspersoft.com/).
