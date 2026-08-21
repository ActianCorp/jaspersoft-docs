---
title: Securing Data in a Domain
description: "You may need to restrict access to the data in a Domain accessed by multiple users. For example, you may allow managers to analyze data across their department but allow individual contributors to..."
---

# Securing Data in a Domain

You may need to restrict access to the data in a Domain accessed by multiple users. For example, you may allow managers to analyze data across their department but allow individual contributors to see only their own data. For this purpose, Domains support security files.

!!! note

    This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit you from using them. To find out what you are licensed to use, or to upgrade your license, contact Jaspersoft.

    This chapter describes tasks only administrators can perform.

When Domain security is properly configured, a user sees only the data they're meant to see. You define Domain security by writing data access filtering rules in XML and uploading them as a new security file in the Domain Designer. These rules are powerful and flexible, and can be based on multiple aspects like user roles or attributes.

The power of this solution is best presented as an example business case. This section describes a fictional company’s implementation of Domains in JasperReports Server—from both a business perspective and an implementation perspective.

!!! note

    As of release 6.0, JasperReports Server supports hierarchical attributes (user, organization, and server levels). The examples in this chapter still work, but they do not demonstrate the cascading functionality of hierarchical attributes. See [Using Server Attributes in Design Files](../domain_syntax/using_server_attributes.md) for information on implementing hierarchical attributes.

For details about the basics of Domains, see [Understanding Domains](../understanding_domains/introduction.md), [Working with the Domain Designer](../domain_designer/intro.md), [Working with Domain Files](../domain_files/working_with_domain_files.md), and [XML Design File Reference](../domain_syntax/xml_design_file_reference.md). For information about how recent changes to application configuration may effect Domain security, see the JasperReports Server Security Guide.

This chapter includes the following sections:

- [Business Case](domain-business-case.md)
- [Process Overview](domain-process-overview.md)
- [Sales Domain](sales-domain.md)
- [Roles, Users, and Profile Attributes](roles-users-attributes.md)
- [Setting Up Logging and Testing](domain-security-testing.md)
- [Creating a Domain Security File](creating-a-security-file.md)
- [Testing and Results](verfiying-domain-security.md)
- [Domain and Security Recommendations](recommendations.md)
