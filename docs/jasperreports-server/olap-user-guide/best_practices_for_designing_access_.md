---
title: Best Practices for Designing Access Control
description: "Best practices for designing access control will emerge as you gain experience with this feature. Here are some suggestions to get you started:"
---

# Best Practices for Designing Access Control

Best practices for designing access control will emerge as you gain experience with this feature. Here are some suggestions to get you started:

- Review the detailed implementation example found in the Jaspersoft OLAP Ultimate Guide to understand the entire implementation process.

- Start with a clear description of the requirements before writing XML.

- Determine the different roles played by users of your application, and assign specific roles to each user.

- Create a hierarchy in each cube that corresponds in a one-to-one way with the different levels of access. That is, make a hierarchical level that corresponds to a user role. Defining the access control requirements before building the schema is much easier than adding access control after designing the schema.

- Build your access control definition iteratively. Start with the smallest definition that you can test. When it works properly, add and test additional increments until you have a complete definition.

- Use an XML editor to help you format access grants properly.
