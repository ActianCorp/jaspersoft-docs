---
title: Types Defined in the WSDL
description: "The WSDL defines several types that are returned by operations of the service. The types belong to the http://www.jasperforge.org/jasperserver/ws namespace. The namespace is only an identifier; it is..."
---

# Types Defined in the WSDL

The WSDL defines several types that are returned by operations of the service. The types belong to the `http://www.jasperforge.org/jasperserver/ws` namespace. The namespace is only an identifier; it is not a valid URL. For the complete reference, refer to the WSDL document.

These are the objects returned when accessing Domains:

- `SimpleMetaData`. Encapsulates all the sets and items in a Domain structure.
- `SimpleMetaLevel`. Represents an item set in the Domain. It may contain items, other item sets, or both.
- `SimpleMetaItem`. An item in the Domain. Unlike a level or set, an item is a source of data referenceable in a query.
- `ResultSetData`. Object returned by a Domain query. It contains column names and rows of data.
- `DataRow`. Contains values for each column in a row.
