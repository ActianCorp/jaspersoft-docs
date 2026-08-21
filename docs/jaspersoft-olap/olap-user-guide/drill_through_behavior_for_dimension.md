---
title: Drill-through Behavior for Dimensions with Parent-child Hierarchies
description: "When a user drills through an aggregated value in their OLAP data, JasperReports Server returns measure information for that member and for all of the members below it, with the notable exception of..."
---

# Drill-through Behavior for Dimensions with Parent-child Hierarchies

When a user drills through an aggregated value in their OLAP data, JasperReports Server returns measure information for that member and for all of the members below it, with the notable exception of dimensions with parent-child hierarchies. Because of a defect in the underlying OLAP engine, drill-through for dimensions with parent-child hierarchies behave unexpectedly. The behavior varies, depending on whether you access the data through Ad Hoc views or Jaspersoft OLAP views:

- In the Ad Hoc Editor, drill-through is prevented. When a crosstab includes a dimension with parent-child hierarchy, and a user clicks the drill-through link, the server returns a message indicating that drill-through is disabled.

- In Jaspersoft OLAP, drill-through returns measures for the current member, but not for members below it in the parent-child hierarchy. Since the data that is returned is partial, it is not reliable.

Because of this issue, Jaspersoft recommends that you avoid using parent-child hierarchies in your dimensions. If you must use parent-child hierarchies, Jaspersoft recommends that you access such dimensions only through Ad Hoc views.

For more information about Ad Hoc views, refer to the JasperReports Server User Guide. For more information about the underlying issue, see Mondrian's issue tracker at <http://jira.pentaho.com/browse/MONDRIAN-388>.
