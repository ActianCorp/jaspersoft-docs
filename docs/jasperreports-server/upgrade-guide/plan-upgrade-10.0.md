---
title: Changes in 10.1 That May Affect Your Upgrade
description: "The migration to JasperReports Server 10.1 and the Jakarta upgrade can bring challenges, particularly with the behavior of resources. You may experience instances where, following the upgrade, the..."
---

# Changes in 10.1 That May Affect Your Upgrade

## Jakarta Upgrade

The migration to JasperReports Server 10.1 and the Jakarta upgrade can bring challenges, particularly with the behavior of resources. You may experience instances where, following the upgrade, the resources either stop functioning or display altered behaviors. This discrepancy is often caused by the variance in Apache Tomcat versions. Jakarta runs on Apache Tomcat 10.1.x, embracing the latest advancements in the Jakarta EE 10 specifications. This transition also involves updating the codebase to align with the new Jakarta namespace.

## Hibernate Upgrade

The application is upgraded to utilize Hibernate version 6. This significant change requires migrating from the legacy XML-based object-relational mappings (`.hbm.xml`) to the modern, annotation-driven JPA approach using @Entity classes.

## New License

Upgrading to JasperReports Server 10.1 includes a new in-house license validator. The license file itself is now named `jaspersoft.jrs.license`, while the application's functionality remains the same regardless of the license. Correct permissions must be set on this new file.

## New Layout Band

The Layout Band has been completely redesigned to provide a more intuitive and user-friendly experience when creating visualizations.

The key changes include:

- Adapts to each visualization type dynamically.

- Presents specific areas for fields and measures that directly correspond to how the visualization is constructed.

- Guides through informative tooltips on where to drag and drop fields and measures.

## csrfguard Library 4.3.0 Changes

The upgradation of csrfguard library from version 3.1.0 to 4.3.0 causes server requests to be rejected.

This is because in the original OWASP library version 4.3.0, the `org.owasp.csrfguard.TokenPerPage` property is set to `true` by default and cannot be set to `false`. The said library does not support it for better security. Having this property set to `true` will create new tokens per API URL within a valid session time.

The JavaScriptServlet API now returns a unique CSRF token for each visited API URL (page). These per-page tokens are generated on the first visit to that URL and remain valid for the entire session. If a page has not been visited, the master token can be used to request a new page-specific token. This per-page token behavior is standard for the library.

## Custom Input Controls

Custom Input Controls for JasperReports Server allow you to create sophisticated report and dashboard interfaces. You can now use custom expressions to dynamically Enable/Disable, Show/Hide, and update the title of Input Controls. This provides users with precise controls for smarter, faster filtering and intuitive complex data analysis.

## Important Notes about Compact and Split installations

- Users are able to upgrade from 9.0 Compact to 10.1 Compact using `samedb` and `newdb`.
- Users are able to upgrade from 9.0 Split to 10.1 Split using using `samedb` and `newdb`.
- Users will not be able to upgrade:
  - From 9.0 Compact to 10.1 Split.
  - From 9.0 Split to 10.1 Compact.

If users need 10.1 Split installations but they are on 9.0 Compact, the required upgrade path is to:

1.  Upgrade 9.0 Compact to 10.1 Compact.
2.  Then, migrate from 10.1 Compact to 10.1 Split.

For more information on these installation options, see the *Installation* and *Upgrade* guides.
