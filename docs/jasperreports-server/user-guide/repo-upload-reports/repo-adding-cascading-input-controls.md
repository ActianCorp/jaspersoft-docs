---
title: Adding Cascading Input Controls to a Report
description: "JRXML-based reports can include input controls that have dynamic values. The values depend on a user's selection in other input controls. For example, a report has input controls for country, state,..."
---

# Adding Cascading Input Controls to a Report

JRXML-based reports can include input controls that have dynamic values. The values depend on a user's selection in other input controls. For example, a report has input controls for country, state, and city. The options in the State input control depend on the value selected in the Country input control. When the user selects a state, the list of City values includes only those in the selected state. These cascading input controls use queries to determine the values to display in each input control field.

To use input controls as parameters for a query that populates another input control, you use a special syntax to reference a parameter name in the input control's query. The syntax is identical to the `$P{parameter_name}` and `$X{...} syntax` used in queries for .

For example, a report returns data identified by country and city. It includes input controls called COUNTRY and CITY. COUNTRY is a query-based input control that returns the list of countries in the data source. CITY is also a query-based input control, but its query uses COUNTRY as input:

``` sql
select address_city from accounts where $X{EQUALS, address_country, COUNTRY}
```

When the user selects a country from the COUNTRY input control, the value selected is used by the query of the CITY input control. The CITY input control is refreshed to show the list of cities for the chosen country. Making two selections from smaller lists is much clearer and quicker for report users. For an example of viewing a report that has cascading input controls, see [“Cascading Input Controls” on page 1](../reports/reports-cascading-input-controls.md).

Note that there are other ways to use a parameter in a query. For details about the $P and $X syntax and an example of creating a cascading input control, see the JasperReports Server Administrator Guide.
