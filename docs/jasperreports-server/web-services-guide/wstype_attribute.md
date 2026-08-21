---
title: wsType Attribute
description: "The wsType attribute defines the nature of the resource. The possible values for this attribute are:"
---

# wsType Attribute

The `wsType` attribute defines the nature of the resource. The possible values for this attribute are:

| wsType Value | Description |
|----|----|
| aws | Amazon Web Services data source |
| bean | Data source of type Spring bean |
| contentResource | The output of a report |
| dataSource | Generic data source – This type is normally used for a data source ReportUnit child resource when it is not defined locally to the ReportUnit. |
| dataType | Datatype (used with the input controls) |
| folder | Folder |
| font | Font file (normally a True Type font) |
| img | Image file |
| inputControl | Input control |
| jar | JAR file |
| jdbc | Data source of type JDBC |
| jndi | Data source of type JNDI |
| jrxml | JRXML source file |
| lov | List of values (used with input controls) |
| olapMondrianCon | OLAP Mondrian connection. A direct connection to an OLAP source. |
| olapMondrianSchema | OLAP Mondrian Schema |
| olapXmlaCon | OLAP XMLA connection. A remote connection to an OLAP source. |
| prop | Resource bundle file (ending with .properties) for specific reports |
| query | Query used to retrieve data from a data source |
| reference | Reference to another resource. References are only present in report units |
| reportUnit | A complete report that can be run in JasperReports Server |
| virtual | Virtual data source – This type has a child ResourceDescriptor for each data source contained in the virtual data source. |
| xmlaConnection | XML/A Connection |

Values for wsType

For all the other resource types found in the repository, the repository web service sets the attribute `wsType` to `UNKNOWN`.
