---
title: OLAP Connection API
description: This section describes functionality that is available only in Jaspersoft OLAP. Contact Jaspersoft to obtain the software.
---

# OLAP Connection API

!!! info "Important"

    This section describes functionality that is available only in Jaspersoft OLAP. Contact Jaspersoft to obtain the software.

OLAP interactions through the Jaspersoft OLAP user interface and web services based on XML/A are supported by the repository and dedicated APIs. The repository can contain the following OLAP-related objects:

- OlapUnit: This is the data needed for an analysis view. It contains an MDX query and an OLAPClientConnection.

- MondrianConnection: Implementor of OLAPClientConnection. It contains a Mondrian schema and a JDBC or JNDI connection.

- XMLAConnection: Implementor of OLAPClientConnection. It contains a URL to an XML/A service and an optional data security definition.

- MondrianXMLADefinition: Jaspersoft OLAP can operate as an XML/A server on top of Mondrian connections. These objects catalog what can be accessed through XML/A.

The OLAP Connection API provided by Jaspersoft OLAP is simple as most of the underlying functionality is within Mondrian (OLAP query engine, XML/A server) or JPivot (OLAP user interface). This call creates a JPivot-compatible OlapModel, based on the relevant OlapUnit:

``` text
public OlapModel createOlapModel(ExecutionContext context, OlapUnit olapUnit );
```

The call should be made and the model object put into the user session before redirecting to the JPivot JSP viewOlap.jsp. An example is in ViewOlapModelAction:

``` text
OlapUnit olapUnit = (OlapUnit)
      getRepository().getResource(executionContext,viewUri);
OlapModel model =
getOlapConnectionService().createOlapModel(executionContext, olapUnit);
```

The following call retrieves the server-wide Mondrian properties:

``` text
// create a local Mondrian OLAP connection corresponding to a Mondrian connection
// resource defined in the repository MondrianConnection connectionResource = ..get
// the resource from the repository.

mondrian.olap.Util.PropertyList connectProperties =
  olapConnectionService.getMondrianConnectProperties(context,connectionResource);
mondrian.olap.Connection olapConnection =
  mondrian.olap.DriverManager.getConnection(connectProperties, null, false);
  mondrian.olap.Query query = olapConnection.parseQuery(..MDX query..);
  mondrian.olap.Result olapResult = olapConnection.execute(query); ...
```

For details, see the Mondrian Technical Guide.

These calls can be used to validate an OlapUnit object while you are editing in the UI:

``` text
public ValidationResult validate(ExecutionContext context, OlapUnit unit);
public ValidationResult validate(ExecutionContext context,
  OlapUnit unit,
  FileResource schema,
  OlapClientConnection conn,
    ReportDataSource dataSource);
```
