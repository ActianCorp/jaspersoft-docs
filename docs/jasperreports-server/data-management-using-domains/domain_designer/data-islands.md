---
title: Understanding Data Islands
description: "Elements in the Data Presentation design panel are grouped into data islands. Each data island comes from a join tree or unjoined table, but data islands differ from join trees in a number of..."
---

# Understanding Data Islands

Elements in the **Data Presentation** design panel are grouped into data islands. Each data island comes from a join tree or unjoined table, but data islands differ from join trees in a number of important ways. Join trees represent the logical model for data in the Domain and data islands represent the business model presented to the users.

| Join Tree (or Unjoined Table) | Data Island |
|----|----|
| Each join tree is unique and does not connect to any other join tree. | Each data island is unique and does not connect to any other data island. |
| Structure is organized in tables and fields. | Structure is organized in sets and items. |
| Directly reflects the structure of the tables and columns in the database, along with derived tables, calculated fields, and table and column copies (aliases). | Lets you group elements in sets to create a structure that better reflects your business model. You can exclude tables and columns you do not want to expose to the user, without removing them from the original join tree. |
| Table and column names come from database or internal Domain Designer naming (for calculated fields, derived tables, and table copies). | Sets and items can be renamed. Names that appear to users can be defined in localization bundles based on strings assigned in the data island. |
