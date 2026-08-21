---
title: Creating a Blank Ad Hoc Report
description: "To create a blank Ad Hoc report:"
---

# Creating a Blank Ad Hoc Report

To create a blank Ad Hoc report:

1.  Start with a blank JRXML file.
2.  Drag and drop the Ad Hoc Component from the Studio palette into the report.

This automatically adds the following properties:

- `<propertyname="com.jaspersoft.ji.adhoc"value="1"/>`
- `<propertyname="com.jaspersoft.ji.adhoc.new"value="true"/>`
- `<property name="com.jaspersoft.jasperserver.adhoc.table.flattened.data.set" value="true"/>`

Additionally, the following properties can also be modified for the Ad Hoc Component:

- `<property name="com.jaspersoft.jasperserver.adhoc.display.title" value="true"/>`
- `<property name="com.jaspersoft.jasperserver.adhoc.style.template" value="/somepath_here"/>`

!!! note

    You cannot have more than one Ad Hoc component in an Ad Hoc report template JRXML.
