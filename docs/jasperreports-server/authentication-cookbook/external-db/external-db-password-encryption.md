---
title: Setting the Password Encryption
description: "JasperReports Server receives the credentials from the user in the login request as plaintext. If your database stores encrypted user passwords, you must share the encryption key with JasperReports..."
---

# Setting the Password Encryption

JasperReports Server receives the credentials from the user in the login request as plaintext. If your database stores encrypted user passwords, you must share the encryption key with JasperReports Server. The server can then encrypt the password from the user request and compare it to the password from the external database.

As of JasperReports Server 7.5, the server uses a central keystore (.jrsks file) to securely hold all the encryption keys it needs. The Java Cryptography Architecture (JCA) defines the ciphers and the protocols for the keys and the keystore. The encryption used in your external database must be compatible with the JCA and stored in a compatible key. Then you can import that key so it is shared by JasperReports Server. For example, if you have your database's password encryption key in a keystore file, run the following commands as the system user who installed the server:

``` bash
cd <js-install>/buildomatic
js-import.sh --input-key --keystore <path>/mykeystore --storepass password
             --keyalias mydbkey --keypass mydbkeypw
```

The key will be copied to the server's keystore and keep the same properties, including alias and password. You can also import keys as hexadecimal values if necessary. The following command creates a new key with the given algorithm, alias, and password:

``` bash
js-import.sh --input-key "0x59 0xe3 0xd9 0xce 0x7f 0x34 0xab 0x27 0xb8 0xdf 0xc3 0x7e
0x01 0xab 0x4d 0x6c" --keyalg AES --keyalias mydbkey --keypass mydbkeypw
```

In the case where your external database is new and not yet provisioned with users, it will need a key to encrypt passwords. In that case, JasperReports Server can generate the key, store it in the keystore, and you can export it to use in your database. The following commands create a new random key in the keystore and export the same key for use externally:

``` bash
js-import.sh --input-key --genkey --keyalg AES --keysize 128 --keyalias mydbkey
             --keypass mydbkeypw
js-export.sh --destkeystore mystore --deststorepass storepw --keyalias mydbkey
             --keypass mydbkeypw
```

For more information about the keystore and exporting keys, see the JasperReports Server Security Guide.

Once the key is in the server's keystore, configure the `passwordValidator` bean in the applicationContext-externalAuth-db-mt.xml file. Set the bean's property values to match those of the key you have imported. The following example shows how to configure the bean with the keys imported above:

``` xml
<bean id="passwordValidator" class="com.jaspersoft.jasperserver.api.common.crypto.CipherFactory" lazy-init="false">
    <property name="cipherClass" value="com.jaspersoft.jasperserver.api.metadata.common.service.impl.PasswordValidator"/>
    <property name="transformation" value="AES/CBC/PKCS5Padding"/>
    <property name="blockSize" value="16"/>
    <property name="keyAlgorithm" value="AES"/>
    <property name="keySize" value="128"/>
    <property name="keyAliasProp" value="mydbkey.keyalias"/>
    <property name="keyPassProp" value="mydbkey.keypass"/>
</bean>
```

!!! note

    By default, the JasperReports Server keystore supports AES and DES keys. If your database uses a different encryption algorithm, you can configure your own password encoder using the Spring implementations of the `PasswordEncoder` interface. This is an advanced configuration that is beyond the scope of this guide.
