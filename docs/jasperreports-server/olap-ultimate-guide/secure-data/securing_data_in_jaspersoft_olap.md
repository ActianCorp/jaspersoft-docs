---
title: Securing Data in Jaspersoft OLAP
description: "This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit..."
---

# Securing Data in Jaspersoft OLAP

!!! info "Important"

    This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit you from using them. To find out what you're licensed to use, or to upgrade your license, contact Jaspersoft.

When a particular set of data is accessed by different people, you may need to restrict the data that are displayed to each one. For example, you might allow employees to see only their own personnel data, supervisors to see selected portions of the data of the workers they supervise, and human resources staff to see everyone’s complete data.

Jaspersoft OLAP commercial editions’ data security enables administrators to define data access for users in a flexible, scalable way. When properly configured, a user only sees the data that the company wants him to see. To define this access, add data access filtering rules (grants) to the Mondrian connections defined in Jaspersoft OLAP. When combined with user profile data, these rules are powerful and flexible.

The power of this solution is best presented through a sample business case. This section describes a fictional company’s implementation from both a business perspective and an implementation perspective.

For details about the basics of Jaspersoft OLAP, refer to the Jaspersoft OLAP User Guide. It is included in the product distribution.

This chapter has these sections:

-   [Securing Jaspersoft OLAP Data: A Business Case](securing_jaspersoft_olap_data__a_bus.md)
-   [Overview of CZS’s Process](overview_of_czs_s_process.md)
-   [Understanding Access Grant Definitions and Attributes](understanding_access_grant_definitio.md)
-   [Configuring CZS’s OLAP view](configuring_czs_s_olap_view.md)
-   [Reference Material](reference_material.md)

!!! note

    This chapter assumes that you have the administrator role. It describes a number of tasks that only administrators can perform.
