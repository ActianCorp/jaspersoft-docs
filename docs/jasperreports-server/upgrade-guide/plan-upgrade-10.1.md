---
title: Changes in 10.1 That May Affect Your Upgrade
description: "Password history validation is a security enhancement that prevents you from reusing your previous passwords during a reset. Previously, the system did not track password history, allowing users to..."
---

# Changes in 10.1 That May Affect Your Upgrade

## Password History Validation

Password history validation is a security enhancement that prevents you from reusing your previous passwords during a reset. Previously, the system did not track password history, allowing users to use any of the previously used credentials. To align with industry compliance standards and strengthens account security, the system can now validate a new password against the last `N` passwords used by that account.

For more information, see the JasperReports Server Security Guide.

## Password Storage Strategy

The password storage upgrade replaces older, reversible encryption methods with highly secure, one-way hashing algorithms: PBKDF2, SCrypt, and Argon2. This database-agnostic change provides 10x stronger credential protection and eliminates the need to synchronize keystores across clustered deployments.

If you used the samedb upgrade process and chose the modern password strategy, your existing users' passwords must be updated using the migration utility. For details, see the Password Migration section in the JasperReports Server Installation Guide.

For information about the password strategy, see the JasperReports Server Security Guide.

## Castor Serializer to Jackson

We have modernized JasperReports Server’s data binding and serialization framework, replacing legacy Castor with the industry-standard Jackson library. This architectural upgrade delivers faster response times and significantly improves system stability. While this represents a major technical leap forward, the transition is entirely seamless. You will experience a faster, more reliable application with zero manual configuration required.

!!! note

    Resources exported from version 10.1.0 cannot be imported into older versions of the application.

## Oracle 23ai Certification

As of release 10.1.0, to certify Oracle database version 23 and higher, a new `quartz-23onwards.ddl` file is added to support schema changes in quartz tables. Depending on the database version, either `quartz.ddl` or `quartz-23onwards.ddl` will be executed during installation or upgrade.

To support this, a new property, `dbVersion`, is added in the `oracle_master.properties` file. You must set this property in the `default_master.properties` file before running the installation or upgrade.

## Important Notes about Compact and Split installations

- Users are able to upgrade from 10.0 Compact to 10.1 Compact using `samedb` and `newdb`.

- Users are able to upgrade from 10.0 Split to 10.1 Split using `samedb` and `newdb`.

- Users will not be able to upgrade:

  - From 10.0 Compact to 10.1 Split.
  - From 10.0 Split to 10.1 Compact.

If users need 10.1 Split installations but they are on 10.0 Compact, the required upgrade path is to:

1.  Upgrade 10.0 Compact to 10.1 Compact.
2.  Then, migrate from 10.1 Compact to 10.1 Split.

For more information on these installation options, see the *Installation* and *Upgrade* guides.
