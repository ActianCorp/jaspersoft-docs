---
title: Troubleshooting
description: We recommend Apache Ant version 1.10.latest.
---

# Troubleshooting

## Build Troubleshooting

### Name Undefined Error (Old Ant Version)

We recommend Apache Ant version 1.10.*latest*.

If you are not using the version of Apache Ant included with the JasperReports Server source code package, you could get the following error when running the buildomatic scripts:

``` text
BUILD FAILED
c:\js-builds\jasperserver\buildomatic\install.xml:6: Problem: failed to create task or type if
Cause: The name is undefined.
Action: Check the spelling.
Action: Check that any custom tasks/types have been declared.
Action: Check that any <presetdef>/<macrodef> declarations have taken place.
```

Solution

The buildomatic scripts require Ant version 1.10.7 or higher, and the ant-contrib.jar file needs to be included in your ant/lib directory. We recommend Ant version 1.10.*latest*. If you are running with your own Ant version, you can copy this jar to your \<ant-home\>/lib directory:

From:

\<js-src\>/apache-ant/lib/ant-contrib.jar

or

\<js-src\>/jasperserver/buildomatic/extra-jars/ant-contrib.jar

To:

|                                       |                   |
|---------------------------------------|-------------------|
| `<ant-home>/lib`                      | (General example) |
| `C:\apache-ant-1.10.`*`latest`*`\lib` | (Windows example) |
| `/usr/share/java/apache-ant/lib`      | (Linux example)   |
| `/usr/share/ant/lib`                  | (Mac example)     |

## Database Troubleshooting

The most common errors encountered when building JasperReports Server involve the database connection. For information about database connection problems, see the Troubleshooting Appendix of the JasperReports Server Installation Guide.

## Maven Troubleshooting

### Maven Error on Linux or Mac

If Maven is installed on Linux via rpm, apt-get, or yum (or on Mac), the Maven binary and the Maven libraries are probably in separate locations. This can potentially cause a problem with the source build.

#### /usr/boot Does Not Exist Error

When building under Linux or Mac, you may get an error similar to the following:

``` text
BUILD FAILED
/home/devuser/js-builds/jasperserver/buildomatic/bin/dev.xml:91:
/usr/boot does not exist
```

The Buildomatic scripts attempt to find the MAVEN_HOME setting and can be unsuccessful when the maven binary is installed in the `/usr/bin/mvn` location. The workaround is to update your<br>
`default_master.properties` file:

`cd <js-src>/jasperserver/buildomatic`

`edit default_master.properties`

Uncomment the maven.home line so that it looks like this:

`maven.home = /usr/share/maven2`                   (Linux)

For Mac, the location of the Maven library files is slightly different:

`maven.home = /usr/share/maven`                      (Mac)

### Clear JasperReports Server Artifacts in Maven Local Repository

If you add new code to an existing source build environment, such as a bug fix source patch update, you can clear the JasperReports Server artifacts in your Maven local repository to ensure that the newly built artifacts contain the necessary new content. Maven updates the artifacts automatically, but if you have trouble building or pulling in the modified code, you can try deleting these artifact trees.

To clear existing JasperReports Server artifacts

1.  Go to the repository directory:

    ``` bash
    cd <home-dir-path>/.m2/repository
    ```

2.  Remove the old version by deleting the following directory and its contents:

    |               |                                  |
    |---------------|----------------------------------|
    | `jaspersoft`: | Commercial version artifact tree |

### Clear Entire Local Repository

If you want to rebuild everything, remove all the cached jars in your Maven local repository. To do this, you can delete (or rename) the entire local repository.

Then when you build JasperServer, all dependencies are re-downloaded.

`cd <home-dir-path>/.m2`

`rm -rf repository`

!!! note

    These steps must be performed if you are using the js-jrs\_

    `js-jrs``_10.1.0`

    \_repo.zip package.

### Maven Warnings

Maven generates verbose warnings during the artifact validation process. For example, the following warning was generated, even though the required JAR file was downloaded successfully:

``` text
[WARNING] Unable to get resource from repository jasperServer (file://C:/svn/js-buildlds/jasperserver-repo
Downloading: http://repo1.maven.org/maven2/commons-logging/commons-logging/1.0/commons-logging-1.0.pom
163b downloaded
```

### Old Maven Binary

In general, it is best to use the most current stable version of the Maven tool. We recommend the Apache Maven version 3.9.

## Other Build Troubleshooting

### Error When Building Database Scripts

When compiling in the jasperserver-repository-hibernate/build-db directory, you might see an error containing the following message:

``` text
[ERROR] BUILD ERROR
[INFO] ------------------------------------------------------------------------
[INFO] Error executing ant tasks
Embedded error: Source file does not exist!
```

The most likely problem is that your .m2/settings.xml file does not point to the correct source location, and the build step did not find the Quartz scripts. The settings.xml file should contain the path to the quartz script corresponding to your database, for example:

\<js.quartz.script\>/home/\<user\>/\<js-src\>/jasperserver/scripts/quartz/tables\_\<database\>.sql\</js.quartz.script\>

If you use the buildomatic script, you should not get this kind of error.
