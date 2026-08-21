---
title: Requirements of XML Design Files
description: "The relationship of item definitions, column definitions, and actual database columns is the essence of the Domain itself and must be maintained when editing the design file. To be uploaded to a..."
---

# Requirements of XML Design Files

The relationship of item definitions, column definitions, and actual database columns is the essence of the Domain itself and must be maintained when editing the design file. To be uploaded to a Domain, a design file must meet the following conditions:

- It must be well-formed XML. This means that all syntax, spelling, and punctuation are correct so that the file contains a hierarchy of elements, attributes, and content.
- The following symbols cannot be entered directly; they must be escaped using their HTML encoding:

& (`&amp;`), " (`&quot;`), \< (`&lt;`), \> (`&gt;`);

- It must be valid with regard to the XML schema. The XML schema defines allowed XML element and attribute names and how they are nested in a hierarchical structure. This ensures that the elements and attributes are those used by JasperReports Server. The allowed versions of the XML schema of a Domain design are given in the XSD files located in `<install‑dir>/samples/domain‑xsd/`. This document describes the functionality supported by the following version:

`<install-dir>/samples/domain-xsd/schema_1_3.xsd `

- The design file must be internally consistent. You can upload a partial file, but to use the Domain, you must define all the necessary elements of a Domain design. These constraints cannot be expressed in the XSD file because they are outside the scope of an XML schema.

!!! note

    It is possible to create or upload partial Domain files, but to be usable, a Domain file must include certain elements, such as: a data source, one or more tables, and one or more presentation items.

- The tables and columns in the design must be consistent with their external definition in the data source of the Domain. The design must reference valid table and column names in the data source; in particular, table names for a design based on an Oracle RDBMS must include the database schema name. The data source also defines the datatype of a column, and the design must use that column accordingly. As a result, a design file is specific to a given data source and may fail when used in a Domain with a different data source.

The more complex elements of a design file have further constraints:

- SQL queries for a derived table must be valid with respect to the JDBC driver for the data source. The tables and columns in the query must exist in the data source, and the columns in the results must match those declared in the design.
- For a virtual data source that combines data from data sources with different JDBC drivers, SQL queries are validated against Teiid SQL. For more information, see the Teiid Reference Guide under the Documentation link on the [Jaspersoft Support Portal](http://support.jaspersoft.com).
- Expressions for filters and calculated fields must be valid programmatic expressions in Jaspersoft's Domain Expression Language (DomEL). This format is documented in [Domain Expression Language (DomEL)](../domel/domain_expression_language.md).

!!! warning

    The design of a Domain is stored internally in the repository. The XML is only a representation from which the design can be inferred, and it may have some validity errors that cannot be detected. As a result, the Domain resource and the XML may not remain totally synchronized through several cycles of exporting to XML, editing, and uploading. For example, the Domain Designer sometimes renames the result of a join (JoinTree_1), which affects the security file.

    However, the Domain Designer also has limitations and cannot create some valid designs. For example, in a design file, you may select the columns of a table whereas you can only select whole tables on the Tables tab.

A design file is plain text and can be edited in any text editor. The server exports well-formatted XML, and if you want to make only a few changes or simple additions, a text editor is sufficient. For editing the content of the design file, a specialized XML editor ensures that the design file is well formed, so you do not introduce other errors. If you want to make structural changes or write a design file from scratch, use an XML editor that understands the XML schema in the `schema_1_3.xsd` file. By loading both the XML and XSD files, this type of XML editor lets you insert elements and attributes only where they are allowed to ensure that the design file is valid.

However, no editor can enforce the consistency requirements in a design file. The next chapter gives a complete XML reference for the elements and attributes of a design file and the various constraints that apply to each of them.
