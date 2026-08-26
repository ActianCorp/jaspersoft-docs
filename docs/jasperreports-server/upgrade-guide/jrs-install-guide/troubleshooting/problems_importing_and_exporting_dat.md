---
title: Problems Importing and Exporting Data from the Repository
description: "You may see the following errors when you have international characters in repository objects, for example, in user IDs."
---

# Problems Importing and Exporting Data from the Repository

## Exporting a Repository That Contains UTF-8

You may see the following errors when you have international characters in repository objects, for example, in user IDs.

### Error During Export

An Upgrade usually requires exporting your database. If you're using MySQL and getting this null pointer exception, it may be caused by an incorrect character in the `js.jdbc.properties` file:

`java.lang.NullPointerException`

`ResourceExporter.exportResource(ResourceExporter.java:258)`

Check the URL in this file in &lt;js-install&gt;buildomatic/build_conf/default/; it should look like this:

`jdbc:mysql://localhost:3306/jasperserver?useUnicode=true&characterEncoding=UTF-8`

Note the ampersand `&`. It's incorrect if it appears as `&amp;`. The `&amp;` is correct only in an HTML or XML context. It's incorrect in a properties file.

### Error During Export from Repository on Oracle

Oracle requires a specific JVM property to handle UTF-8 characters properly. If the export is empty and this error occurs when attempting to compress the result:

`ERROR ExporterImpl:129 - java.util.zip.ZipException: ZIP file must have at least one entry`

If you have stored your repository database on an Oracle RDBMS, modify the last line of both `<js-install>/buildomatic/js-export.*` files as follows:

From: `java -classpath ...`

To: `java ``-Doracle.jdbc.defaultNChar=true`` -classpath ...`
