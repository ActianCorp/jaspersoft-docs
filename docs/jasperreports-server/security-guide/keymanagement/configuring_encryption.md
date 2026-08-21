---
title: Configuring Encryption
description: "In a normal server installation for evaluation or production environments, once the server is installed or upgraded, the use of the keystore is transparent and requires no further configuration. If..."
---

# Configuring Encryption

In a normal server installation for evaluation or production environments, once the server is installed or upgraded, the use of the keystore is transparent and requires no further configuration. If you need to handle keys for old servers, you can use the import and export tool so that servers have the keys they need.

For special situations, it is possible to customize the server’s use of encryption, such as configuring specific ciphers or cipher length. For example, the server only supports the AES (Advanced Encryption Standard) and DES (Data Encryption Standard) algorithms for encryption by default. If you wish to use a different algorithm such as RSA (Rivest–Shamir–Adleman), you need to change the cipher implementation to one that supports RSA. Configuring encryption is best done before installation, but can also be done after.

However, the specifics of configuring encryption in JasperReports Server are beyond the scope of this document. This section is intended only to introduce the concepts and guidelines for advanced use cases. Administrators wishing to customize encryption settings must be proficient in the cryptography libraries of the Java Cryptography Architecture (JCA) and know the risks to avoid.

Before you consider modifying the encryption configuration, keep in mind the following:

- Always make a backup of the server and original keystore files before configuring encryption. The keystore files are unique to every installation and the server is inaccessible without them.
- If you need to modify the encryption settings, do it before provisioning your server with production data.
- Even if the server has no production data, you should export the entire repository along with the export key before proceeding. Default accounts such as superuser and jasperadmin must be reimported later to work with your new encryption settings.
- You must be familiar with the cryptographic concepts and details of the keystore APIs. For more information, see the Java Cryptography Architecture (JCA) Reference Guide and its section on [key management](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html#KeyManagement).
- Encryption may be configured in the .jrsksp file and also in beans and properties in other configuration files. This may create a complex configuration where values override other settings, and what appears in the keystore properties file may not be the final configuration at runtime. While this may be desirable or necessary for your configuration, it creates complex dependencies and risk.
- Be sure to document your new configuration, including any secondary configuration file dependencies.
- Incorrect configuration of the keystore or importing with the wrong keys may corrupt your data or make it impossible to access the server. Therefore, it is critical to know and test your encryption configuration and import procedure. Testing on an isolated and empty evaluation server instance is recommended.
- Be sure to securely delete any draft copies of your encryption configuration and wipe any test servers to ensure the security of your production server.
- After configuring the encryption, importing your export catalog, and testing your server, remember to back up your new keystore files, including any other configuration files that may contribute to the encryption settings.

For security, the .jrsksp file is Base64 encoded so that it is not a plain text file. To read and modify the file, the system user who installed the server must decode the file, for example:

|          |                                                    |
|----------|----------------------------------------------------|
| Windows: | `certutil -decode .jrsksp myconfig.txt`            |
| Linux:   | `cat ~/.jrsksp | openssl base64 -d > myconfig.txt` |

Inside the keystore is the configuration for each of the following keys:

| Key Alias | Description |
|----|----|
| `buildSecret` | Key for encrypting passwords and sensitive values in configuration files in the file system. |
| `importExportEncSecret` | Key for all import and export operations of the new server. |
| `deprecatedImportExportEncSecret` | Key for importing from previous versions of the server. |
| `passwordEncSecret` | Key for encrypting user passwords and other sensitive content in the server’s internal database (the repository). |
| `deprecatedPasswordEncSecret` | Key for upgrading to 7.5 without exporting everything. However, the best practice is to export everything, modify the configuration, and reimport, as described in the upgrade section. |
| `diagnosticDataEncSecret` | Key for encryption of log collector output. Use js-export to export this key and decrypt the output file. |
| `httpParameterEncSecret` | The key used for HTTP parameter encryption in releases prior to 7.5, now deprecated. If upgrading from a previous release, this key needs to be exported from the old keystore, and imported into the server. |
| `deprecatedHttpParameterEncSecret` | This key is not used. |

If you have added the key to the keystore with the js-import command, then they have their alias and password defined here as well.

Configuration properties are typical Java properties (name=value), one per line. Special precaution needs to be taken while working with the .jrsksp properties because certain symbols must be escaped with a backslash. For example, `#`, `:`, `\`, and `=` are represented as `\#`, `\:`, `\\`, and `\=` to be interpreted correctly.

Configuration values with the same name may be set in other files and take precedence. This may be necessary for certain configurations, but it is more complicated and may lead to errors. If possible, keep all the encryption settings in the `.jrsksp` file.

The values of the keys themselves are encrypted and stored in the `.jrsksp` file. Only the Java keytool utility in the JDK (Java Development Kit) can read, write, or modify keys in the keystore file.

The procedure for configuring encryption depends on whether you can do it before installation, which is easier, or after.

## Configuring Encryption Before Installation

The easiest way to customize the encryption on your server is to modify configuration files before doing a WAR file installation. That way, the installation scripts use your settings when generating keys and the keystore, and all encryption is performed once with the properties you want.

You may need to install an evaluation server to access it's `.jrsksp` file and determine which settings you want to modify. Of course, you should also test your custom encryption configuration on test installations before installing your production servers.

The default values of properties may be modified by defining them in `default_master.properties`, after copying the appropriate `<name>_master.properties` file and before running the installation scripts. For example, you could specify predefined passwords for each key instead of randomly generated ones. When the installation runs, it performs the keystore creation and all initial encryption using your configuration.

After the installation is successful, you should be sure to back up and then delete any files that contain sensitive encryption configuration values such as passwords. Also document your custom installation for ease of maintenance and support.

## Configuring Encryption After Installation

If possible, you should customize your encryption configuration before you install the server. In case if it is not possible, you can configure encryption after the fact, but the procedure is much longer, depending on the settings you need to change. For example, changing the password of a key does not impact contents that are already encrypted, but changing the strength of the password cipher means you need to re-encrypt all user passwords.

The following procedure gives the general steps for changing the encryption configuration of a server after it has been installed and provisioned. This assumes that your changes require the server’s contents to be re-encrypted.

1.  Export the entire contents of the server including the import-export cipher.
2.  Stop the server.
3.  Decode the `.jrsksp` file as described above, and make changes to its settings. It is also possible to add encryption configuration settings in the `applicationContext-security.xml` file if necessary.
4.  Depending on what you modify in the configuration, you may need to generate or modify keys using the keytool utility. For example, if you want a stronger cipher, you need to generate the longer key to replace the existing one. If you change a password in the properties file, you must also set the password in the keystore with keytool. Ensure the keystore is updated in the same way as the `.jrsksp` properties file.
5.  After all, the modifications `.jrsksp` file must be Base64 encoded and replaced in the user’s home directory with the updated keystore (`.jrsks`) file.
6.  Restart the server.
7.  Import your server’s export catalog with its old export key (if the export key has changed). If the configuration is coherent and the keys are correct, you should be able to log in.

As mentioned previously, the details and complexity of these procedures are beyond the scope of this document. You must have the knowledge and experience with the Java Cryptography Architecture to successfully modify the encryption configuration.

## Legacy Encryption Configurations

In previous releases of the server, encryption was often defined in configuration files and could be modified. As of release 7.5, all encryption keys are stored in the server's keystore (`.jrsks`) with the matching configuration in the keystore properties file (`.jrsksp`). However, in certain cases where you wish to customize how the encryption works, you could use the legacy configuration.

The following sections describe legacy encryption configurations that have been replaced by the keystore functionality, but could be used as documentation for advanced encryption configuration. In general, if you configure a key through a configuration file, it is used instead of the key from the keystore:

- [Static Key Encryption](../user-security/encrypting_user_session_login.md) for HTTP parameters.

- [Encrypting User Passwords](../user-security/encrypting_user_passwords.md) in the internal database.

- [Encryption Options](../application-security/encrypting_passwords_in_files.md) for encrypting passwords in configuration files.
