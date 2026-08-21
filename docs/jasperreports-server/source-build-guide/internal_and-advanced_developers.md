---
title: Jaspersoft Internal Developers and Advanced Developers
description: This chapter is for Jaspersoft Internal Developers and for Advanced Developers who want to use some of the additional options available through the buildomatic property settings.
---

# Jaspersoft Internal Developers and Advanced Developers

This chapter is for Jaspersoft Internal Developers and for Advanced Developers who want to use some of the additional options available through the buildomatic property settings.

## Internal Developers and Advanced Developers

Jaspersoft provides a Maven repository using [Artifactory](https://jfrog.com/artifactory/) to hold all third-party components required to build the server's source code. It also acts as a proxy for the standard public Maven repositories such as repo1.maven.org.

This internal repository is convenient for internal Jaspersoft developers because the developer can point to one location to get all dependencies resolved.

In `default_master.properties, `internal developers should comment out `maven.build.type=repo` and `repo-path=<path>`:

`# maven.build.type=repo`

`# repo-path=<path>`

External developers (customers) who download the

`js-jrs``_10.1.0`

\_src.zip package from jaspersoft.com should set all the properties described in [Configuring the Buildomatic Properties](building_jasperreports_server_source.md) before building JasperReports Server.

Additional buildomatic property settings are available for advanced external developers. If you are an external developer working within an enterprise or on a project that has an internal Maven repository server, you can use the `mirror` value. The following property settings and values enable a local Maven repository:

`maven.build.type=mirror`

`mvn-mirror=<repo-url>`

If you are an external developer with other build configurations to add, you can do this with the `maven.build.type=custom` property setting. If you set this value, the following file will be used as the template to set up the JasperReports Server build configuration:

`<js-path>/buildomatic/conf_source/templates/maven_settings_custom.xml`

You can edit this file to add whatever configurations you want.

When buildomatic auto-setup is complete, you can see the final maven settings file used for the JasperReports Server here:

`<js-path>/buildomatic/build_conf/default/maven_settings_custom.xml`

## Additional Properties in default_master.properties

You can use the properties in the table below for various customizations of the JasperReports Server build:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Property Setting</p></th>
<th><p>Purpose</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>SKIP_TEST_ARG=skipTests</code></p></td>
<td><p>Enable this property to skip unit test execution. This speeds the source build.</p></td>
</tr>
<tr>
<td><p><code>VERBOSE_LOGGING=true</code></p></td>
<td><p>Enable this property to increase the INFO logging from the Maven package.</p></td>
</tr>
<tr>
<td><p><code>OFFLINE_ARG=-o</code></p></td>
<td><p>Enable this property if you want to build in “offline” mode. To run in offline mode, you need to have successfully built JasperServer at least once.</p></td>
</tr>
<tr>
<td><p><code>SKIP_EXPORT_FILES=true</code></p></td>
<td><p>Enable this property to skip the copying of files that set up the command-line import-export configuration. This saves time on file copying.</p></td>
</tr>
<tr>
<td><p><code>maven.build.type=repo</code></p></td>
<td><p>Use this setting for the build type if you have downloaded the source code zip package from the jaspersoft.com site, and you are building the source code as a customer (external developer) would build it. You will also need to set the <code>repo-path</code> property. <code>maven.build.type=repo</code> is the default value used in the sample <span>&lt;dbType&gt;_master.properties</span> files.</p></td>
</tr>
<tr>
<td><p><code>maven.build.type=mirror</code></p></td>
<td><p>If you are an external developer who has a central Maven style repository for your enterprise or project, you can use this setting to specify the local central repository. If you set this property value, you should also set the <code>mvn-mirror</code> property.</p></td>
</tr>
<tr>
<td><p><code>maven.build.type=custom</code></p></td>
<td><p>If you are an external developer whose build requires additional configurations, you can use this property value to support them. In this case, use the following template file:</p>
<p><span> &lt;js-path&gt;/buildomatic/conf_source/templates/<br />
maven_settings_custom.xml</span>.</p>
<p>You can manually edit this file to add more configurations. The file will be processed by buildomatic and copied to its final location after running a buildomatic command:</p>
<p><span>buildomatic/build_conf/default/maven_settings_custom.xml</span></p></td>
</tr>
<tr>
<td><p><code>mvn-mirror=&lt;repo-url&gt;</code></p></td>
<td><p><span>mvn-mirror=http://mvnrepo.jaspersoft.com:8081/artifactory/repo</span></p>
<p>The value shown is the default <span>repo-url</span> used by Jaspersoft internal development.</p></td>
</tr>
<tr>
<td><p><code>repo-path=&lt;path&gt;</code></p></td>
<td><p>Set a local path value for this property if you are using <code>maven.build.type=repo</code> (this is the default configuration from the source code zip download from jaspersoft.com).</p></td>
</tr>
</tbody>
</table>

## Integration Tests

To run optional integration tests, make sure that Chrome, Chromium, or any other browser based on Chromium like Microsoft Edge is installed and executable, then use the following commands:

Commands for Running Integration Tests

- `js-ant drop-js-db`
- `js-ant create-js-db`
- `js-ant init-js-db-pro`
- `js-ant run-integration-tests-pro`

## Location of JavaScript files

In the current version of JasperReports Server, the JavaScript-related files are in the following directory:

\<js-pro-path\>/jasperserver-war/src/main/webapp/scripts/runtime_dependencies/jrs-ui/src

This location may be different in earlier versions. See the JasperReports Server Source Build Guide for your version for more information.

!!! note

    If you customize JavaScript files, you need to optimize the JavaScript after your edits are complete. See the JasperReports Server Ultimate Guide for more information.
