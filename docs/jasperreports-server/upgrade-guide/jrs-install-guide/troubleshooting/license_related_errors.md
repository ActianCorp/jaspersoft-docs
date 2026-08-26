---
title: License-related Errors
description: "Normally, the JasperReports Server installer includes an evaluation license file that you replace with a commercial license file, as described in Installing a New License File. If JasperReports..."
---

# License-related Errors

## License Not Found Errors

Normally, the JasperReports Server installer includes an evaluation license file that you replace with a commercial license file, as described in [Installing a New License File](../../../installation-guide/binary-installer/post_installation_steps.md). If JasperReports Server returns an error after you replace the license file, the most likely causes are:

-   You didn't clear your application server’s work directory, as explained in [Installing a New License File](../../../installation-guide/binary-installer/post_installation_steps.md). Delete the work directory, restart the application server, and try logging into JasperReports Server again.

-   The `Djs.license.directory` property in your application server startup environment is incorrectly set:

For example, in Windows the correct setting looks like this:

`-Djs.license.directory=<js-install>`

In Linux, the correct setting looks like this:

`-Djs.license.directory=/opt/10.1.0`

The specified directory must contain the license file, named `jasperserver.license`. The property is set in JAVA_OPTS in the `standalone.conf` file. It must contain the location of your license file, which is usually the `<js-install>` directory:

|  |  |
|----|----|
| Tomcat: | `<tomcat>/bin/setclasspath.bat/.sh or bin/setenv.bat/.sh` |
| JBoss: | `<jboss>\bin\standalone.conf.bat` or `<jboss>/bin/standalone.conf` |

## License Not Found or License Corrupt Error with Tomcat as a Service

If you have Tomcat running as a service in Windows, the installer attempts to make the proper updates so the server license file is found at when you start the application server. If the installer is unsuccessful, make sure you took the steps described in [License File for Existing Tomcat as Windows Service](../../../installation-guide/binary-installer/post_installation_steps.md).
