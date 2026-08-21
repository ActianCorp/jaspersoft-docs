---
title: Migration and Compatibility
description: "This section includes the following topics:"
---

# Migration and Compatibility

This section includes the following topics:

- Upgrade Paths

- Upgrade File

- Database Changes

- Upgrade from Community Project

- Important Upgrade Information

## Upgrade Paths

Your current version determines your upgrade path:

|                                                         |
|---------------------------------------------------------|
| ![jrs upgrade path](assets/images/jrs-upgrade-path.png) |
| Paths for Upgrading to Version 10.1                     |

You can upgrade directly to 10.1.0 from version 9.

|           |       |
|-----------|-------|
| Version 9 | 9.0.0 |

!!! note

    If your instance is JasperReports® Server 9.0.0 Compact, you can only upgrade to 10.1.0 Compact. If your instance is JasperReports® Server 9.0.0 Split, you can only upgrade to 10.1.0 Split.

If you have any of the version 8 instances, you must first upgrade to version 9.0.0 before upgrading to 10.1.0.

|           |       |       |       |
|-----------|-------|-------|-------|
| Version 8 | 8.0.x | 8.1.x | 8.2.x |

!!! note

    If your instance is JasperReports® Server 8.2.0 Compact, you can only upgrade to 9.0 Compact. If your instance is JasperReports® Server 8.2.0 Split, you can only upgrade to 9.0 Split.

If you have any of the version 7 instances, you must first upgrade to the latest version of 8.0.x before upgrading to 10.1.0.

|           |       |       |       |       |       |
|-----------|-------|-------|-------|-------|-------|
| Version 7 | 7.1.x | 7.2.x | 7.5.x | 7.8.x | 7.9.x |

If you have any of the version 6 instances, you must first upgrade to the latest version of 7.1.x, then upgrade to 8.0.x, before finally upgrading to 10.1.0.

|           |       |       |       |       |       |
|-----------|-------|-------|-------|-------|-------|
| Version 6 | 6.0.x | 6.1.x | 6.2.x | 6.3.x | 6.4.x |

## Upgrade File

To upgrade, start with the WAR File Distribution ZIP:

js-jrs_10.1.0

\_bin.zip

Download it from [Jaspersoft Technical Support](https://www.jaspersoft.com/support) .

The complete upgrade procedure is described in JasperReports® Server Upgrade Guide.

## Database Changes

Between certain versions of the server, we have changed the repository database to add new functionality. There are changes between 8.x.x, 9.0.0 and 10.1.0.

## Upgrade from Community Project

If your current instance is the Community version, you can follow the *Upgrade from Community Project* chapter of JasperReports® Server Upgrade Guide to upgrade to the Commercial version.

## Important Upgrade Information

There are major changes that must be considered when upgrading to JasperReports® Server 10.1.0. For details about how to upgrade, see *JasperReports® Server Upgrade Guide*.
