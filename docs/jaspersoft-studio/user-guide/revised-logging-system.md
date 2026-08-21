---
title: Revised Logging System
description: "Starting version 10.0.0 , Jaspersoft Studio features a revised logging mechanism. The logging process is restructured, providing a centralized system using Apache Log4j2 to capture all application..."
---

# Revised Logging System

Starting version 10.0.0 , Jaspersoft Studio features a revised logging mechanism. The logging process is restructured, providing a centralized system using Apache Log4j2 to capture all application events. This new architecture consolidates 'everything' happening within Jaspersoft Studio, unifying output from the various underlying Java logging frameworks that are shipped, including:

- Log4j 1.x

- Log4j2.x

- SLF4J

- Apache Commons Logging (1.2x, 1.3x)

- java.util.logging

All logging behavior is now controlled by a single configuration file, `log4j2.xml`, located in the installation folder. You can easily modify this file for specific logging during debug sessions or normal use.

You can customize the location of this configuration file using the VM argument `-Dlog4j.configurationFile` in the `Jaspersoft Studio Professional.ini` file.

## Configuration File and Appenders

The standard configuration of the `log4j2.xml` config file is as follows:

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">

    <Appenders>
        <EclipseIOConsole name="EclipseIOConsole">
            <PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n"/>
        </EclipseIOConsole>
        <Console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n"/>
        </Console>
        <!--
        <RollingFile name="RollingFile"
                     fileName="logs/jaspersoftstudio_main.log"
                     filePattern="logs/jaspersoftstudio_main-%d{yyyy-MM-dd}-%i.log.gz">
            <PatternLayout>
                <Pattern>%d{yyyy-MM-dd HH:mm:ss} %p %c [%t] %m%n</Pattern>
            </PatternLayout>
            <Policies>
                <TimeBasedTriggeringPolicy/>
                <SizeBasedTriggeringPolicy size="25 MB"/>
            </Policies>
            <DefaultRolloverStrategy max="20"/>
        </RollingFile>
        -->
    </Appenders>

    <Loggers>

        <!-- SAMPLE: Advanced logging for Xtext framework problems debug -->
        <!--
        <Logger name="org.eclipse.xtext" level="trace" additivity="false">
            <AppenderRef ref="EclipseIOConsole"/>
            <AppenderRef ref="Console"/>
            <AppenderRef ref="RollingFile"/>
        </Logger>
        -->

        <!-- SAMPLE: Debug logging Highcharts Chrome related stuff -->
        <!--
        <Logger name="com.github.kklisura.cdt" level="debug" additivity="false">
            <AppenderRef ref="EclipseIOConsole"/>
            <AppenderRef ref="Console"/>
            <AppenderRef ref="RollingFile"/>
        </Logger>
        <Logger name="net.sf.jasperreports.chrome" level="debug" additivity="false">
            <AppenderRef ref="EclipseIOConsole"/>
            <AppenderRef ref="Console"/>
            <AppenderRef ref="RollingFile"/>
        </Logger>
        -->

        <!-- SAMPLE: Debug logging HTML PRO component stuff -->
        <!--
        <Logger name="com.jaspersoft.jasperreports.htmlcomponent" level="debug" additivity="false">
            <AppenderRef ref="EclipseIOConsole"/>
            <AppenderRef ref="Console"/>
            <AppenderRef ref="RollingFile"/>
        </Logger>
        -->

        <!-- SAMPLE: Debug logging for JDBC operations -->
        <!--
        <Logger name="net.sf.jasperreports.engine.query" level="debug" additivity="false">
            <AppenderRef ref="EclipseIOConsole"/>
            <AppenderRef ref="Console"/>
            <AppenderRef ref="RollingFile"/>
        </Logger>
        <Logger name="net.sf.jasperreports.data.jdbc" level="debug" additivity="false">
            <AppenderRef ref="EclipseIOConsole"/>
            <AppenderRef ref="Console"/>
            <AppenderRef ref="RollingFile"/>
        </Logger>
        <Logger name="net.sf.jasperreports.dataadapters" level="debug" additivity="false">
            <AppenderRef ref="EclipseIOConsole"/>
            <AppenderRef ref="Console"/>
            <AppenderRef ref="RollingFile"/>
        </Logger>
        -->

        <!-- Default logging -->
        <Root level="info">
            <AppenderRef ref="Console"/>
            <AppenderRef ref="EclipseIOConsole"/>
            <!--<AppenderRef ref="RollingFile"/>-->
        </Root>
    </Loggers>

</Configuration>
```

The default logging configuration includes the following key features:

- By default, two main appenders are enabled:

  - `EclipseIOConsole`: Displays logging information directly within the dedicated console section of the Jaspersoft Studio user interface.

  - `Console`: Outputs messages to the standard system console.

- The `RollingFile` appender is included but disabled by default. To enable file-based logging, you must correctly configure the target destination and other necessary settings..

- The default level is set to INFO to prevent console windows from being cluttered with excessive, low-priority messages.

- Several commented-out sample sections are provided. You can use these as templates to customize the configuration, such as enabling DEBUG logging for specific operations (for example, JDBC).

!!! note

    Configuring the file location using the `-Dlog4j.configurationFile` argument in the Jaspersoft Studio `.ini` file can be tricky due to operating system differences in path handling.

    - Depending on the operating system, both relative and absolute paths may behave inconsistently. There is a critical difference between forward slashes ( / ) and backslashes ( \\ ) when specifying paths across operating systems (especially Windows vs. Linux/macOS).

    - Windows sample:

      - Set `-Dlog4j.configurationFile=log4j2.xml` to use the configuration file located within the standard installation folder.

      - Use `-Dlog4j.configurationFile=file:///C:/dev/logging/log4j2.xml` to specify a configuration file located in a specific folder on the C: drive.

## User Interface Changes

The **Preferences** section that previously held logging configurations is replaced with a simple informative message. This message guides users on how to properly configure logging in the newer versions.

![revised logging ui 1](assets/images/revised-logging-ui-1.png)

You can access the dedicated Jaspersoft Studio console view by opening the standard Console view and selecting it from the available options.

![revised logging ui 2](assets/images/revised-logging-ui-2.png)

The following example illustrates the logging output when JDBC operations are set to the 'debug' level.

![revised logging ui 3](assets/images/revised-logging-ui-3.png)
