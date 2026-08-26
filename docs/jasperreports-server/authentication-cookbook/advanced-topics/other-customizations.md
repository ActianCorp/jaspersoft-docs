---
title: Other Customizations
description: "Spring Security and JasperReports Server are complex systems that allow many different opportunities for customization, for example:"
---

# Other Customizations

Spring Security and JasperReports Server are complex systems that allow many different opportunities for customization, for example:

-   Modifying the authentication provider to:

    -   Locate external users in different ways.
    -   Extract additional user information from the external authority.
    -   Implement custom mappings of organizations and roles.

-   Writing a new authentication provider to implement external authentication for a new protocol.

-   Modifying or replacing filters to perform synchronization differently.

-   Writing additional filters to take further action during the login sequence.

As with any design, you must determine the benefits and drawbacks in the areas of complexity, cost, and maintenance of your implementation to help you decide your preferred approach.

The best way to customize is to copy one of the sample files and make modifications. Details on customization are beyond the scope of this guide.
