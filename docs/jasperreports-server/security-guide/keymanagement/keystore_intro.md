---
title: Key and Keystore Management
description: JasperReports Server uses cryptographic keys internally to secure sensitive content such as database passwords in the configuration and user passwords in the database and export catalogs. The keys...
---

# Key and Keystore Management

JasperReports Server uses cryptographic keys internally to secure sensitive content such as database passwords in the configuration and user passwords in the database and export catalogs. The keys are used to encrypt information before storage and decrypt it on retrieval.

The keys themselves are sensitive security items that must be carefully stored and safeguarded. A keystore is a standard file that holds keys and protects them with passwords. The Java Cryptography Architecture (JCA) provides the ciphers and the protocols that protect the keys and the keystore. Administrators use the command-line `keytool` to manage keys in the keystore, and the server accesses keys as permitted through Java APIs.

As of JasperReports Server 7.5, key and keystore management has been updated to improve consistency and secure all sensitive server and user data inside and outside the server application. Administrators should become familiar with the new procedures and how to upgrade keys and the keystore from previous versions if necessary.

Because the keystore and keys are created during installation, the user account that performs the installation is the owner of the keystore file and holder of the keystore passwords. If either the keystore or its passwords are lost, the server can no longer function and the data it contains may become inaccessible, so be sure to keep backup copies.

This chapter contains the following sections:

- [Managing Keys During Installation](keys_during_installation.md)
- [Managing Keys for Import and Export](import_and_export.md)
- [Sharing Custom Keys](custom_keys.md)
- [Configuring Encryption](configuring_encryption.md)
