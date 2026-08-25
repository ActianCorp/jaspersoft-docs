---
title: Configuring Password Storage Strategy and Password History
description: "JasperReports Server keeps accounts secure and compliant with standards like PCI DSS, NIST and ISO/IEC 27001 by combining modern password storage with history validation."
---

# Configuring Password Storage Strategy and Password History

JasperReports Server keeps accounts secure and compliant with standards like PCI DSS, NIST and ISO/IEC 27001 by combining modern password storage with history validation.

With the new password storage strategy, the system now utilizes advanced, database-agnostic, one-way hashing algorithms (Password-Based Key Derivation Function 2 (PBKDF2), Scrypt, and Argon2) to eliminate the risks of reversible encryption and provide significantly stronger credential protection. This significantly enhances security while simplifying cluster management by removing the need for keystore synchronization for user login credentials, which no longer require reversible encryption.

If you are doing a fresh install or an upgrade, you need to set your password strategy and algorithm in the `default_master.properties` file so it applies during setup. For a server that is already up and running, administrators can just update these settings in the `js.password-storage-config.properties` file and restart the app server to apply the changes.

The password history validation feature enhances account security and ensures compliance with industry standards (for example, PCI DSS, NIST, ISO/IEC 27001) by preventing users from reusing previous credentials. By default, the feature is disabled (for backward compatibility). Administrators must explicitly enable it and define the number of previous passwords to retain via the `js.spring.properties` property file.

For more information, see the Password History Validation and the Configuring Password Storage Strategy sections in the JasperReports Server Security Guide.
