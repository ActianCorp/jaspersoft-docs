---
title: Error Running Buildomatic Scripts
description: "The buildomatic scripts depend on both Java and Apache Ant. Two common configuration errors are possible when attempting an installation using these scripts (if you are not using the included,..."
---

# Error Running Buildomatic Scripts

The buildomatic scripts depend on both Java and Apache Ant. Two common configuration errors are possible when attempting an installation using these scripts (if you are not using the included, bundled Apache Ant).

## Missing Java JDK

If you have the Java JRE (Java Runtime Environment) instead of the JDK, you will not have all the required utilities. In particular, you may see an error referring to the tools.jar, as in the following message:

``` text
[exec] [ERROR] BUILD FAILURE
[exec] [INFO] ----------------------------------------------------
[exec] [INFO] Compilation failure
[exec] Unable to locate the Javac Compiler in:
[exec]   c:\Program Files\Java\jdkx.x.x_xx\jre\..\lib\tools.jar
[exec] Please ensure you are using JDK x.x or above and
[exec] not a JRE (the com.sun.tools.javac.Main class is required).
[exec] In most cases you can change the location of your Java
[exec] installation by setting the JAVA_HOME environment variable.
```

The solution is to download and install the Sun Java JDK, labeled as the Java SE Development Kit on the Oracle website.

## Forgot to Copy the File ant-contrib.jar

If you are using your own version of Ant and your Ant instance does not have the ant-contrib.jar in the lib directory, you will get an error similar to the following:

``` text
BUILD FAILED
c:\js-builds\jasperserver\buildomatic\install.xml:6:
```

Ant failed to create a task or type. To correct the error, copy `<js-install>/buildomatic/extra-jars/ant-contrib.jar` to your `<apache-ant>/lib` directory.

## Failure with '\$' Character in Passwords in Buildomatic Scripts

If your password in buildomatic scripts includes two of more '\$' characters in a row, Ant will not accept it. This issue does not occur when dollar signs are separated by other characters. For example, `$pas$word$` or `pas$word$` will not fail.

If you have two consecutive dollar signs, you will need to escape each with three more dollar signs. For example, if your password is `pa$$word`, enter it as `pa$$$$$$$$word` in the configuration file. Once you do this, JasperReports Server sets all data connections to `pa$$word`.

## Older Apache Ant Version

We recommend Apache Ant version 1.10. The earliest compatible version is Ant 1.9.

Older versions of Ant cause an error similar to the following:

``` text
BUILD FAILED
c:\js-builds\jasperserver\buildomatic\install.xml:37:
Problem: failed to create task or type componentdef
```

To check your version of Ant and verify that it is at a high enough level, enter:

`ant -version`

If you have an earlier version of Ant, check to see if it is set in your class path by entering:

`echo $CLASSPATH`

To use the JasperReports Server version of Ant, update your `CLASSPATH` variable to point to the `<js-install>/apache-ant/bin` directory.
