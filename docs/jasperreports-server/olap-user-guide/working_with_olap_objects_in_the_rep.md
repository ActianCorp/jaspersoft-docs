---
title: Working with OLAP Objects in the Repository
description: "OLAP views rely on several other types of objects in the repository. This section describes their creation and maintenance, including:"
---

# Working with OLAP Objects in the Repository

OLAP views rely on several other types of objects in the repository. This section describes their creation and maintenance, including:

-   [Working with Data Sources](working_with_data_sources.md)

-   [Working with OLAP Schemas](working_with_olap_schemas.md)

-   [Working with Mondrian Connections](working_with_mondrian_connections.md)

-   [Working with XML/A Connections](working_with_xml_a_connections.md)

-   [Working with XML/A Sources](working_with_xml_a_sources.md)

-   [Working with Access Grant Definitions](working_with_access_grant_definition.md)

!!! note

    An OLAP view references most of these objects indirectly. The same holds true for Ad Hoc views. For example, an OLAP schema is a part of a Mondrian connection. The OLAP view refers to the Mondrian connection that in turn refers to the schema. The following figures can help you understand how the objects relate:

-   [Anatomy of an OLAP View](overview_of_an_olap_view.md)

-   [Anatomy of a Mondrian Connection](working_with_mondrian_connections.md)

-   [Anatomy of an XML/A Connection](working_with_xml_a_connections.md)

-   [Anatomy of an XML/A Source](overview_of_xml_a_sources.md)

The repository objects described in this section are also used by Ad Hoc views that return OLAP data. Such views are created against OLAP client connections (Mondrian or XML/A) using the Ad Hoc Editor. For more information on Ad Hoc views, refer to the JasperReports Server User Guide.
