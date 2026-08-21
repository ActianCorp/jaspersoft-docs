---
title: Localizing Reports
description: "You can adapt reports to global audiences by localizing input controls and field names:"
---

# Localizing Reports

You can adapt reports to global audiences by localizing input controls and field names:

- Input controls – The server supports multi-lingual prompts and static lists of values in reports.
- Field names – The server supports multi-lingual field names in reports.

A `$R` expression that you write in the report design triggers linguistic changes in the report output for different locales. Each `$R` expression refers to a name-value pair (your translations) in a resource bundle. A resource bundle file is a text file that has a `.properties` extension. You create a resource bundle in Jaspersoft Studio or a text editor. You set the base name of the resource bundle in the header of the JRXML file:

``` xml
<jasperReport name=”StoreSales” pageWidth=”595” pageHeight=”842” columnWidth=”515”
leftMargin=”40” rightMargin=”40” topMargin=”50” bottomMargin=”50”
resourceBundle=”simpleTable”>
```

For example, `simpleTable` is the base name of the resource bundle file for this report. If you prefer using a graphical user interface to coding in XML, use Jaspersoft Studio to set the base name of the resource bundle.
