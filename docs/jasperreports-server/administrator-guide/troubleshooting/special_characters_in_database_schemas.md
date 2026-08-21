---
title: Special Characters in Database Schemas
description: "Some databases allow you to use spaces and special characters in their database schema. These spaces and symbols can thus appear in table names and column names. However, in order to define Domains,..."
---

# Special Characters in Database Schemas

Some databases allow you to use spaces and special characters in their database schema. These spaces and symbols can thus appear in table names and column names. However, in order to define Domains, JasperReports Server relies on a restricted set of symbols. Databases having table names and column names with forbidden symbols will cause Domain errors and be unusable with Domains.

As of JasperReports Server 6.0, Domains allow the following symbols:

| Symbols Allowed in Table Names | Symbols Allowed in Column Names         |
|--------------------------------|-----------------------------------------|
| `<space> @ # $ % & _ /`        | `<space> @ # $ % & ( ) _ [ ] : , + - /` |

These symbols have been tested with the following databases:

- SQL Server
- DB2
- PostgreSQL
