---
title: Encrypting User Passwords
description: "As of JasperReports Server 7.5, all encryption in the server relies on cryptographic keys stored in the server's keystore. For more information, see Key and Keystore Management."
---

# Encrypting User Passwords

!!! warning

    As of JasperReports Server 7.5, all encryption in the server relies on cryptographic keys stored in the server's keystore. For more information, see [Key and Keystore Management](../keymanagement/keystore_intro.md).

    The configuration files and properties described in this section are no longer used by this feature. They are documented here only for legacy purposes.

User passwords are stored along with user profiles in JasperReports Server's private database. Password encryption is enabled and passwords are stored as cipher text in the database by default. The following procedure enables system administrators to turn user password encryption on or off. They can also change the encryption algorithm and specify the salt key used to initiate the encryption algorithm.

To Configure User Password Encryption:

1.  As a precaution, back up the server's private `jasperserver` database. To back up the default PostgreSQL database, go to the &lt;js-install&gt; directory and run the following command:

    `pg_dump -U postgres jasperserver > js-backup.sql`

    To back up DB2, Oracle, Microsoft SQL Server, and MySQL databases, refer to your database product documentation.

2.  Stop your application server. Leave your database running.

3.  Export the entire contents of the repository, which includes user profiles and their passwords, with the following commands. Note that there are two dashes (`--`) in front of the command options:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>Windows:</p></td>
    <td><p><code>cd &lt;js-install&gt;\buildomatic</code><br />
    <code>js-export.bat --everything --output-dir js-backup-catalog</code></p></td>
    </tr>
    <tr>
    <td><p>Linux:</p></td>
    <td><p><code>cd &lt;js-install&gt;/buildomatic</code><br />
    <code>js-export.sh --everything --output-dir js-backup-catalog</code></p></td>
    </tr>
    </tbody>
    </table>

    In the export operation, passwords are decrypted using the existing user password ciphers and re-encrypted with the import-export encryption key. This is a separate encryption that ensures that passwords are never in plain text, even when exported. For more information, see "Import and Export" in the JasperReports Server Administrator Guide.

4.  Edit the properties in the following table to configure different ciphers. Both the server and the import-export scripts access the user profiles and must be configured identically. Make the same changes in both files:

    <table>
    <caption><p>User Password Encryption Configuration</p></caption>
    <colgroup>
    <col style="width: 33%" />
    <col style="width: 33%" />
    <col style="width: 33%" />
    </colgroup>
    <tbody>
    <tr>
    <td colspan="3"><p>DEPRECATED User Password Encryption Configuration</p></td>
    </tr>
    <tr>
    <td colspan="3"><p><code>&lt;jasperserver-pro-war&gt;/WEB-INF/applicationContext-security.xml</code><br />
    <code>&lt;js-install&gt;/buildomatic/conf_source/iePro/applicationContext-security.xml</code><br />
    </p></td>
    </tr>
    <tr>
    <td><p>Property</p></td>
    <td><p>Bean</p></td>
    <td><p>Description</p></td>
    </tr>
    <tr>
    <td><code>allowEncoding</code></td>
    <td><p><code>passwordEncoder</code><br />
    </p></td>
    <td><p>With the default setting of <code>true</code>, user passwords are encrypted when stored. When <code>false</code>, user passwords are stored in clear text in JasperReports Server's private database. We do not recommend changing this setting.</p></td>
    </tr>
    <tr>
    <td><p><code>keyInPlainText</code></p></td>
    <td><p><code>passwordEncoder</code></p></td>
    <td><p>When <code>true</code>, the <code>secretKey</code> value is given as a plain text string. When <code>false</code>, the <code>secretKey</code> value is a numeric representation that can be parsed by Java's Integer.decode() method. By default, this setting is false, and the <code>secretKey</code> is in hexadecimal notation (0xAB).</p></td>
    </tr>
    <tr>
    <td><p><code>secretKey</code></p></td>
    <td><p><code>passwordEncoder</code></p></td>
    <td><p>This value is the salt used by the encryption algorithm to make encrypted values unique. This value can be a text string or a numeric representation depending on the value of <code>keyInPlainText</code>.</p></td>
    </tr>
    <tr>
    <td><p><code>secretKeyAlgorithm</code></p></td>
    <td><p><code>passwordEncoder</code></p></td>
    <td><p>The name of the algorithm used to process the key, by default <code>DESede</code>.</p></td>
    </tr>
    <tr>
    <td><p><code>cipher</code><br />
    <code>Transformation</code></p></td>
    <td><p><code>passwordEncoder</code></p></td>
    <td><p>The name of the cipher transformation used to encrypt passwords, by default <code>DESede/CBC/ PKCS5Padding</code>.</p></td>
    </tr>
    </tbody>
    </table>

    !!! warning

        Change the `secretKey` value so it is different from the default.

    The `secretKey`, `secretKeyAlgorithm`, and `cipherTransformation` properties must be consistent. For example, the `secretKey` must be 24 bytes long in hexadecimal notation or 24 characters in plain text for the default cipher (DESede/CBC/PKCS5Padding). Different algorithms expect different key lengths. For more information, see Java's `javax.crypto` documentation.

5.  Next, drop your existing `jasperserver` database, where the passwords had the old encoding, and recreate an empty `jasperserver` database. Follow the instructions for your database server:

    -   Dropping and Recreating the Database in PostgreSQL
    -   Dropping and Recreating the Database in MySQL
    -   Dropping and Recreating the Database in Oracle
    -   Dropping and Recreating in the Database in Microsoft SQL Server

6.  Import your exported repository contents with the following commands. The import operation restores the contents of JasperReports Server's private database, including user profiles. As the user profiles are imported, the passwords are encrypted using the new cipher settings.

    Note that there are two dashes (`--`) in front of the command options:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>Windows:</p></td>
    <td><p><code>cd &lt;js-install&gt;\buildomatic</code><br />
    <code>js-import.bat --input-dir js-backup-catalog</code></p></td>
    </tr>
    <tr>
    <td><p>Linux:</p></td>
    <td><p><code>cd &lt;js-install&gt;/buildomatic</code><br />
    <code>js-import.sh --input-dir js-backup-catalog</code></p></td>
    </tr>
    </tbody>
    </table>

    During the import operation, passwords are decrypted with the import-export encryption key and then re-encrypted in the database with the new user password encryption settings. For more information, see Setting the Import-Export Encryption Key in the JasperReports Server Administrator Guide.

7.  Use a database like the [SQuirreL tool](http://squirrel-sql.sourceforge.net/) to check the contents of the `JIUser` table in the `jasperserver` database and verify that the password column values are encrypted.

8.  Restart your application server. Your database should already be running.

9.  Log into JasperReports Server to verify that encryption is working properly during the log in process.

## Dropping and Recreating the Database in PostgreSQL

1.  Change the directory to `<js-install>/buildomatic/install_resources/sql/postgresql`.

2.  Start psql using an administrator account such as PostgreSQL: `psql -U postgres`

3.  Drop the `jasperserver` database, create a one, and load the `jasperserver` schema:

    ``` sql
    drop database jasperserver;
    create database jasperserver encoding='utf8';
    \c jasperserver
    \i js-pro-create.ddl
    \i quartz.ddl
    ```

## Dropping and Recreating the Database in MySQL

1.  Change the directory to `<js-install>/buildomatic/install_resources/sql/mysql`.

2.  Log in to your MySQL client: `mysql -u root -p`

3.  Drop the `jasperserver` database, create a one, and load the `jasperserver` schema:

    ``` text
    mysql>drop database jasperserver;
    mysql>create database jasperserver character set utf8;
    mysql>use jasperserver;
    mysql>source js-pro-create.ddl;
    mysql>source quartz.ddl;
    ```

## Dropping and Recreating the Database in Oracle

1.  Change the directory to `<js-install>/buildomatic/install_resources/sql/oracle`.

2.  Log in to your SQLPlus client, for example: `sqlplus sys/sys as sysdba`

3.  Drop the `jasperserver` database, create a one, and load the `jasperserver` schema:

    ``` text
    SQL> drop user jasperserver cascade;
    SQL> create user jasperserver identified by password;
    SQL> connect jasperserver/password
    SQL> @js-pro-create.ddl
    SQL> @quartz.ddl
    ```

## Dropping and Recreating in the Database in Microsoft SQL Server

1.  Change the directory to `<js-install>/buildomatic/install_resources/sql/sqlserver`.

2.  Drop the `jasperserver` database, create a one, and load the `jasperserver` schema using the SQLCMD utility:

    ``` bash
    cd <js-install>\buildomatic\install_resources\sql\sqlserver
    sqlcmd -S ServerName -Usa -Psa
    1> DROP DATABASE [jasperserver]
    2> GO
    1> CREATE DATABASE [jasperserver]
    2> GO
    1> USE [jasperserver]
    2> GO
    1> :r js-pro-create.ddl
    2> GO
    1> :r quartz.ddl
    2> GO
    ```
