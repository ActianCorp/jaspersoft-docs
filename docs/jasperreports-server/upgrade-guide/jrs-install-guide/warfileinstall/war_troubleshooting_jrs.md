---
title: Troubleshooting Your Server Configuration
description: This section helps you troubleshoot the most common installation problems.
---

# Troubleshooting Your Server Configuration

This section helps you troubleshoot the most common installation problems.

## Startup Problems

If you encounter a problem while trying to run a new JasperReports Server, it may be due to an incorrect database configuration. Another reason could be an error in the application server configuration files. For information about resolving these types of errors, see [Troubleshooting](../../../installation-guide/troubleshooting/troubleshooting.md).

## Error Running a Report

If you have trouble running reports in your new JasperReports Server instance, see [Error Running a Report](../../../installation-guide/troubleshooting/database_related_problems.md) in [Troubleshooting](../../../installation-guide/troubleshooting/troubleshooting.md).

## Error Running js-install Scripts (js-install .bat/sh)

The js-install script creates an output log that captures standard output and error output. If you encounter problems during the execution of the script, or if you want to remember which options you chose, open the output log file.

To troubleshoot problems running js-install scripts

1.  Open the output log file available at:

    `<js-install>/buildomatic/logs/js-install-<date>-<number>.log`

2.  Try to find the first error encountered by the `js-install` steps.

    - Go to the end of the output log.
    - Scroll back through lines of error messages until you find the first error logged. Typically, this error causes more errors later in the log.
    - Finding the original error is the way to understand the problem. However, this can often be tricky because Java stack traces with the Spring application component framework can make the error output quite long.

3.  Incorrect settings in the `default_master.properties` file cause most problems, which you can correct by editing your `default_master.properties` settings. Common errors are:

- Typos in the path for the application server
- Misspelling the hostname or password for the database

To recreate your `default_master.properties` settings

1.  Open the file `<js-install>/buildomatic/default_master.properties`, make corrections, and save it.
2.  Re-run the `js-install` script.

The `js-install` script uses the current values in the `default_master.properties` file.

To help isolate errors, run the `js-install` scripts in `test` mode.

### js-install Script Test Mode

You can run the `js-install` and `js-upgrade` scripts in `test` mode using the `test` option. In `test` mode, the `js-install` scripts check your `default_master.properties` settings and validate the application server location and connection to the specified database. Using `test` mode can help debug issues, such as an incorrect database password. Your system isn’t altered when executing the script in `test` mode.

To run the js-install script in test mode on Windows

1.  Navigate to the buildomatic directory:

    `cd <js-install>/buildomatic`

2.  Enter the following command to run the js-install script in `test` mode:

`js-install`` .bat test`

To run the js-install script in test mode on Linux or Mac OSX

1.  Navigate to the buildomatic directory:

    `cd <js-install>/buildomatic`

2.  Enter the following command to run the `js-install` script in `test` mode:

`./``js-install`` .sh test`

## Problem Connecting to a Cloud Database Instance

A cloud database instance (such as Amazon EC2) typically disables unused IP ports. When the `js-install` script runs, it validates the database hostname using the built-in ant operation `<isreachable>`. This operation is similar to a network `ping` and may stop responding if the port is unavailable. In this case, the `validateHost` step can be commented out in the `buildomatic/validation.xml` file. See the comment in the `do-pre-install-test` target.

## Error Exporting Reports, Ad Hoc Views, and Dashboards

The export of Reports, Ad Hoc Views, and Dashboards fails when Tomcat is run as root in the JasperReports Server installation on Linux. The Tomcat log file displays an error, for example:

``` text
2020-06-11T17:32:19,031 ERROR SecureExceptionHandlerImpl,http-nio-8080-exec-8:116 - com.github.kklisura.cdt.launch.exceptions.ChromeProcessTimeoutException: Failed while waiting for chrome to start: Timeout expired! Chrome output: [0611/173218.897370:ERROR:zygote_host_impl_linux.cc(89)] Running as root without --no-sandbox is not supported. See https://crbug.com/638180.
```

To resolve this, set the following property in the `jasperreports.properties` file:

- `net.sf.jasperreports.chrome.argument.no-sandbox=true`

After setting this property, restart JasperReports Server to enable it.

For information about configuring this property, see the JasperReports Server Administrator Guide.
