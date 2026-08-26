---
title: Sharing Custom Keys
description: "The import and export functionality can be used to share export catalogs between servers that have different keys, for example an old server with custom keys. If you wish to share catalogs between..."
---

# Sharing Custom Keys

The import and export functionality can be used to share export catalogs between servers that have different keys, for example an old server with custom keys. If you wish to share catalogs between two servers that are both on the same release, you can add the keys directly to the server's keystore.

For example, if you have a test server for developing reports and dashboards, and a production server where users need them, you can transfer them by exporting from one and importing into the other. To do so, both servers need the same import-export key, but after installation, each will have a different and random key. The recommended solution is to generate the new key in a new keystore file, and then imports it to both servers.

The following procedure assumes you are familiar with the command-line `keytool` utility. For more information, see the [Java keytool reference](https://docs.oracle.com/en/java/javase/11/tools/keytool.html).

To create and import a custom key to multiple servers:

1.  Generate your custom keys in a keystore. In this example, we generate two keys, which overwrite the default import-export key and the diagnostic key.

    ``` text
    keytool -genseckey -keystore ./mystore -storetype jceks -storepass storepw
    -keyalg AES -keysize 128 -alias importExportEncSecret -keypass myimportexportpw

    keytool -genseckey -keystore ./mystore -storetype jceks -storepass storepw
    -keyalg AES -keysize 128 -alias diagnosticDataEncSecret -keypass mydiagnosticpw
    ```

    Use the keytool utility again to verify your new keys:

    ``` text
    keytool -list -v -keystore ./mystore -storetype jceks

    Enter keystore password: *******
    Keystore type: JCEKS
    Keystore provider: SunJCE
    Your keystore contains 2 entries
    Alias name: diagnosticdataencsecret
    Creation date: Dec 12, 2019
    Entry type: SecretKeyEntry

    *******************************************
    *******************************************

    Alias name: importexportencsecret
    Creation date: Dec 12, 2019
    Entry type: SecretKeyEntry

    *******************************************
    *******************************************
    ```

2.  Copy the keystore file to both servers using a secure method such as `scp`, `sftp`, or `rsync`.

    ``` text
    scp ./mystore jrsusr@bi-test.example.com:/opt/jasperreports-server/jasperreports-server-x.x.x/buildomatic/

    scp ./mystore jrsusr@bi-production.example.com:/opt/jasperreports-server/jasperreports-server-x.x.x/buildomatic/
    ```

3.  Log in to the first server (bi-test) as the system user who installed JasperReports Server (`jrsusr`) and stop the app server. Then import the keys with the following commands:

    ``` bash
    cd /opt/jasperreports-server/jasperreports-server-x.x.x/buildomatic/

    ./js-import.sh --input-key --keystore ./mystore --storepass storepw
    --keyalias importExportEncSecret --keypass myimportexportpw

    ./js-import.sh --input-key --keystore ./mystore --storepass storepw
    --keyalias diagnosticDataEncSecret --keypass mydiagnosticpw
    ```

4.  Log in to the second server (bi-production) as the system user who installed JasperReports Server (`jrsusr`) and stop the app server. Then import the keys with the same commands as above.

5.  Restart both app servers, and now they will use your custom keys.

In this example, the two custom keys were given the same alias as the keys that are created by default in the server's own keystore (`/users/jrsuser/.jrsks`). As a result, the custom keys overwrite the server's default keys, which will be used in any operation where the default keys are used. This has the following consequences:

-   Export catalogs can be shared between the two servers. Any passwords in the export catalog will be encrypted with the new `importExportEncSecret` on one server and decrypted with the same key on the other server. Export catalogs can be moved from the test server to the production server for deployment and vice versa for debugging, without exchanging keys or even specifying key aliases.
-   Log collectors are encrypted with a known key. For security, the diagnostic information in the log collector is encrypted with the `diagnosticDataEncSecret` key. Now when you download the log collector zip file, you need a copy of the mystore keystore file with your new `diagnosticDataEncSecret` key to decrypt it.

!!! warning

    The keystore you created in this procedure contains the same keys as your production server, and could thus be used to access sensitive data. Be sure to delete the copies of the keystore you no longer need, and safeguard the passwords you used in these commands.
