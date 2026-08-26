---
title: Setting Up the JasperReports Server License
description: JasperReports Server requires a license and comes with an evaluation license. Please contact Jaspersoft Technical Support or your sales representative to get your commercial license.
---

# Setting Up the JasperReports Server License

JasperReports Server requires a license and comes with an evaluation license. Please contact [Jaspersoft Technical Support](https://www.jaspersoft.com/support) or your sales representative to get your commercial license.

The license file is in the following location:

`<js-install>/jaspersoft.jrs.license`

The license file specifies the terms of your license, such as the following:

-   Expiration date, number of users, and/or number of CPUs

-   Features licensed separately from the basic commercial license, such as multi-tenancy

Jaspersoft receives information about your system periodically. The information is used only to monitor compliance with your license. No personal information is collected or transmitted.

## Default License Configuration for All Application Servers

At startup JasperReports Server automatically looks for the jasperserver.license file in the home directory of the system user running the application server. License Locations lists the application server user home directories for supported operating systems.

To configure the license:

1.  Stop the application server.
2.  Copy the `jaspersoft.jrs.license` file in `<js-install>` to the directory for your operating system.

| Operating System |   |
|----|----|
| Linux | /home/&lt;user&gt;/ |
| Mac OSX | /Users/&lt;user&gt;/ |
| Windows 10 installed from WAR file | C:\\Users\\&lt;user&gt;\\ |
| Windows 10 installed from the binary installer | C:\\Users\\ |
| Windows 10 using an existing Tomcat Windows service | C:\\WINDOWS\\system32\\config\\systemprofile |

License Locations

## User-Defined License Location

If you prefer to put your license in another directory, modify your application server startup script to set a JAVA_OPT value to explicitly point to that directory.

### Alternate License Setup for Tomcat

If your license is not located in the home directory of the application server user, you can set a `JAVA_OPT` value to explicitly point to your license.

On Windows:

1.  In the file `<tomcat>\bin\setclasspath.bat`, locate the following line:

    `set JAVA_ENDORSED_DIRS=%BASEDIR%\common\endorsed`

    Alternatively, create an empty file called `<tomcat>/bin/setenv.bat`.

2.  Below that line or in the new file, insert the following line:

`set JAVA_OPTS=%JAVA_OPTS% -Djs.license.directory="<js-install>"`

For example:

`set JAVA_OPTS=%JAVA_OPTS% -Djs.license.directory="C:\jasperserver-bin"`

On Linux and Mac OSX:

1.  In the file `<tomcat>/bin/setclasspath.sh`, locate the following line:

    `JAVA_ENDORSED_DIRS="$BASEDIR"/common/endorsed`

    Alternatively, create an empty file called &lt;tomcat&gt;/bin/setenv.sh.

2.  Below that line or in the new file, insert the following line:

`export JAVA_OPTS="$JAVA_OPTS -Djs.license.directory=<js-install>"`

For example:

`export JAVA_OPTS="$JAVA_OPTS -Djs.license.directory=/home/user/jasperserver-bin"`

### Alternate License Setup for Bundled Tomcat as a Windows Service

The Windows binary installer installs the bundled Tomcat component as a Windows Service by default.

To specify a specific folder to hold the `jaspersoft.jrs.license`:

1.  Open the following file for editing:

    `cd <js-install>/apache-tomcat/bin/service.bat`

2.  Look for the second line of two lines that set JVM options, specifically the line which contains the license string. For example, `-Djs.license.directory=C:\Jaspersoft\10.1.0`.

3.  Update the line to point to your license location, for example:

`-Djs.license.directory=C:\MyLicenses`

Because Tomcat is installed as a service, you need to re-install the service. From a Windows Command shell, enter these commands (Note: the cmd shell will disappear when these commands are run. You need to open a new cmd shell for each command.). To open a cmd shell: `Start Menu > Run... > cmd`:

``` bash
cd <js-install>\apache-tomcat\scripts
serviceinstall.bat REMOVE
serviceinstall.bat INSTALL
```

The Tomcat service is removed and then installed. After execution of these commands, the service is running.

### Alternate License Location for Existing Tomcat as a Windows Service

Windows 10

If you have an existing Tomcat as a Windows Service under Windows 10, copy your license to the home folder for the SYSTEM user. The location is:

`C:\WINDOWS\system32\config\systemprofile\jaspersoft.jrs.license`

### Alternate License Setup for JBoss

If your license is not located in the home directory of the application server user, you can set a `JAVA_OPT` value to explicitly point to your license.

On Windows

1.  In the file `<jboss>\bin\standalone.conf.bat`, locate the following line:

    `set JAVA_OPTS=%JAVA_OPTS% -Dprogram.name=%PROGNAME%`

2.  Below that line, insert the following line:

`set JAVA_OPTS=%JAVA_OPTS% -Djs.license.directory="<js-install>"`

For example:

`set JAVA_OPTS=%JAVA_OPTS% -Djs.license.directory="C:\jasperserver-bin"`

On Linux and Mac OSX

1.  In the file `<jboss>/bin/standalone.conf`, locate the following line:

    `export JAVA_OPTS="$JAVA_OPTS -Dprogram.name=$PROGNAME"`

2.  Below that line, insert this line:

`export JAVA_OPTS="$JAVA_OPTS -Djs.license.directory=<js-install>"`

For example:

`export JAVA_OPTS="$JAVA_OPTS -Djs.license.directory=/home/user/jasperserver-bin"`
