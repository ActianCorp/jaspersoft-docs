---
title: System Configuration
description: "You can change the default behavior of JasperReports Server by editing the system's configuration. The configuration is defined by a set of properties and their values."
---

# System Configuration

You can change the default behavior of JasperReports Server by editing the system's configuration. The configuration is defined by a set of properties and their values.

The properties are stored in configuration files located in various folders under the &lt;js-install&gt; directory, which is the root of your JasperReports Server installation. To change the configuration, you edit these files and then restart the server.

A few of the most commonly edited properties are available to the system admin through the user interface (UI). Changes to these properties take effect immediately, are stored in the repository, and override the equivalent values stored in files, even after the server restarts

This chapter describes a subset of the properties in the configuration files. Settings that affect security are covered in *JasperReports Server Security Guide*. Configuration of the auditing and monitoring features is covered in [“Configuring Auditing and Monitoring” on page 1](../diagnostics/configuring_auditing_and_monitoring.md). More options are described in the JasperReports Server Installation Guide.

Because the locations of files described in this chapter vary with your application server, the paths specified here are relative to the deployed WAR file for the application. For example, the applicationContext.xml file is shown as residing in the WEB-INF folder; if you use the Tomcat application server bundled with the installer, the default path to this location is:

`C:\Program Files\jasperreports-server-10.1\apache-tomcat\webapps\jasperserver` -pro \\WEB-INF

!!! warning

    Use caution when editing the properties described in this chapter. Inadvertent changes may cause unexpected errors throughout JasperReports Server that may be difficult to troubleshoot. Before changing any files, back them up to a location outside of your JasperReports Server installation.

    Do not modify settings that are not described in the documentation. Even though some settings may appear straightforward, values other than the default may not work properly and can cause errors.

This chapter contains the following sections:

-   [Configuration Settings in the User Interface](configuration_settings_in_the_ui.md)

-   [Configuration for Using Proxies](configuration_for_using_proxies.md)

-   [Configuration for Session Persistence](configuration_for_session_persistence.md)

-   [Enabling Compression in Tomcat](enabling_compression_in_tomcat.md)

-   [Configuring Ad Hoc](configuring_ad_hoc.md)

-   [Enabling Data Snapshots](enabling_data_snapshots.md)

-   [Enabling Data Staging](enabling_data_staging.md)

-   [Configuring Cloud Services](configuring_cloud_services.md)

-   [Configuring Domains](configuring_domains.md)

-   [Configuring JasperReports Library](configuring_jasperreports_library.md)

-   [Disabling Open In Editor Option](disabling_open_in-editor.md)

-   [Configuring Input Control Behavior](configuring_input_control_behavior.md)

-   [Configuring the Scheduler](configuring_the_scheduler.md)

-   [Configuring Report Thumbnails](configuring_report_thumbnails.md)

-   [Show/Hide Multiple Columns in Interactive Tables](control-visibility-of-show-hide-column-in-interactive-tables.md)

-   [Configuring the Heartbeat](configuring_the_heartbeat.md)

-   [Configuring the Online Help](configuring_the_online_help.md)

-   [Configuring JasperReports Web Studio Access](integrating_jrws_into_jrs.md)

-   [Configuration for File Resource Type](configuration_for_file_resource.md)

-   [Configuration for Repository files](configuration_for_repository_files.md)

-   [Configuring Password Storage Strategy and Password History](configuring-password-encryption-strategy.md)
