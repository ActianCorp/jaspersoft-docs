---
title: Import and Export Through the Command Line
description: "If you installed JasperReports Server from the binary installer, the command-line utilities are configured by the installer. If you installed the WAR file distribution, you must follow the..."
---

# Import and Export Through the Command Line

!!! warning

    If you installed JasperReports Server from the binary installer, the command-line utilities are configured by the installer. If you installed the WAR file distribution, you must follow the instructions in Configuring Import-Export Utilities before you can run the utilities.

The import and export utilities are shell scripts in the `<js-install>/buildomatic` folder:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p>Windows:</p></td>
<td><p><code>&lt;js-install&gt;/buildomatic/js-import.bat</code><br />
<code>&lt;js-install&gt;/buildomatic/js-export.bat</code></p></td>
</tr>
<tr>
<td><p>Linux:</p></td>
<td><p><code>&lt;js-install&gt;/buildomatic/js-import.sh</code><br />
<code>&lt;js-install&gt;/buildomatic/js-export.sh</code></p></td>
</tr>
</tbody>
</table>

The examples in this chapter use the shortened Windows commands without the optional .bat extension on the command line. If you are running JasperReports Server on Linux, be sure to add the `.sh` file extension.

When using the import and export utilities, keep the following in mind:

- JasperReports Server should be stopped when using the import and export utilities. This is very important for the import utility to avoid issues with caches, configuration, and security.

- All command-line options start with two dashes (`--`).

- You must specify either a directory or a zip file to export to or import from.

- The import and export commands include additional options to import and export keys between servers that need to share export catalogs. The options for sharing keys are documented in the JasperReports Server Security Guide. Once keys have been shared between servers, the commands in this chapter can be used without specifying keys.

- If you are exporting or importing organizations, you must be aware of resource dependencies outside of the organization that may block the operation. For more information, see [Dependencies During Import and Export](import_and_export_catalogs.md).

- Ensure the output location specified for an export is writable to the user running the command.

- All URIs are repository paths originating at the root (`/`). In commercial editions of the server, even those with a single default organization, the path must include the organization unless you specify `--organization` option, for example:

  `/organizations/organization_1/reports/interactive/CustomersReport`

!!! warning

    The import and export scripts provide access to the repository and internal database of the server. Even though all passwords are encrypted during export, a catalog may still contain sensitive URLs and data. You should set permissions on the host file system and operating system to secure the scripts and any catalogs you export.

## Exporting from the Command Line

Usage: `js-export [OPTIONS]`

!!! note

    We recommend you stop your server instance before running the export utility. For instructions see the JasperReports Server Installation Guide.

Use this command to export repository resources such as reports, images, dashboards, domains,, or entire folders to a catalog file. You can also export scheduled jobs, organizations, users, roles, and metadata such as repository access times and auditing events. The export output is known as a catalog. It is either a zip archive file or a set of files in a folder structure.

The `js-export` command includes additional options for exporting cryptographic keys. For more information about this special use case, see the JasperReports Server Security Guide.

<table>
<caption><p>Options in <code>js-export</code> Command</p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Option</p></th>
<th><p>Explanation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>--everything</code></p></td>
<td><p>Exports everything<span> except audit and monitoring data</span>: all repository resources, permissions, report jobs, <span>organizations, </span>users, and roles. If any server settings have been modified in the UI, those are also included.<span> May be combined with <code>--organization</code> to export everything in just one organization.</span></p>
<p>This option is equivalent to:<br />
<code>--uris --repository-permissions --report-jobs --calendars --users --roles</code></p></td>
</tr>
<tr>
<td><p><code>--help</code></p></td>
<td><p>Displays brief information about the available options.</p></td>
</tr>
<tr>
<td><p><code>--include-access-events</code></p></td>
<td><p>Exports repository events (date, time, and username of last modification).</p></td>
</tr>
<tr>
<td><p><code>--output-dir</code></p></td>
<td><p>Path of a location to export the catalog in a folder structure.</p></td>
</tr>
<tr>
<td><p><code>--output-zip</code></p></td>
<td><p>Path and filename to export the catalog as a zip file.</p></td>
</tr>
<tr>
<td><p><code>--report-jobs</code></p></td>
<td><p>Comma-separated list of repository report unit and folder URIs for which report unit jobs should be exported. For a folder URI, this option exports the scheduled jobs of all reports in the folder and all subfolders.</p></td>
</tr>
<tr>
<td><p><code>--calendars</code></p></td>
<td><p>When specified, the export includes all calendars of all types (holiday, recurring, ...) defined in the scheduler. When calendars are present in an export catalog, they are always processed and added on import.</p></td>
</tr>
<tr>
<td><p><code>--uris</code></p></td>
<td><p>Comma-separated list of folder or resource URIs to export from the repository. If the URI specifies a folder, the export operation exports all resources and folders contained in the folder. In addition, it recurses through all its subfolders.</p></td>
</tr>
<tr>
<td><code>--resource-types</code></td>
<td>Comma-separated list of resource types to export. The available resource types are: <span><span>adhocDataView,</span></span><span> awsDataSource, beanDataSource, customDataSource, </span><span><span>dashboard</span></span><span>, dataType, file, folder, inputControl, jdbcDataSource, jndiJdbcDataSource, listOfValues, mondrianConnection, mondrianXmlaDefinition, olapUnit, query, reportUnit, virtualDataSource, xmlaConnection</span>.</td>
</tr>
<tr>
<td><p><code>--repository-permissions</code></p></td>
<td><p>This option exports repository permissions with each exported resource or folder. This option should only be used with <code>--uris</code>.</p></td>
</tr>
<tr>
<td><code>--skip-dependent-resources</code></td>
<td>Exports resources without their dependencies, for example a report without its external data source, input control definitions, or image files.</td>
</tr>
<tr>
<td><code>--organization</code></td>
<td>Specify the ID of an organization to export. When specified, only resources, users, and roles from this organization (and its suborganizations) are exported. When specified, all URIs are relative to this organization.</td>
</tr>
<tr>
<td><code>--skip-suborganizations</code></td>
<td>When used with <code>--organization</code>, specifies that suborganizations (and their resources, users, and roles) should not be exported.</td>
</tr>
<tr>
<td><p><code>--roles</code></p></td>
<td><p>Comma-separated list of roles to export. If no roles are specified with this option, all roles are exported.</p></td>
</tr>
<tr>
<td><p><code>--role-users</code></p></td>
<td><p>Use only with <code>--roles</code>. This option exports all users belonging to each exported role.</p></td>
</tr>
<tr>
<td><p><code>--users</code></p></td>
<td><p>Comma-separated list of users to export. If no users are specified with this option, all users are exported. Exporting a user includes all user attributes and all roles assigned to each user.<span> When specifying users, you must give their organization ID if applicable, for example:</span></p>
<p><code>--users superuser, "jasperadmin|organization_1"</code></p></td>
</tr>
<tr>
<td><p><code>--users-roles</code></p></td>
<td><p>Use only with <code>--users</code>. This option exports all roles belonging to each exported user.</p></td>
</tr>
<tr>
<td><code>--include-attributes</code></td>
<td>Specify this flag to export attributes on any user<span>, organization,</span> or root level that is exported.</td>
</tr>
<tr>
<td><code>--skip-attribute-values</code></td>
<td>When used with <code>--include-attributes</code>, specifies that only attribute names are exported, values are null.</td>
</tr>
<tr>
<td><p><code>--include-audit-events</code></p></td>
<td><p>Includes audit data for all resources and users in the export.</p></td>
</tr>
<tr>
<td><p><code>--include-monitoring-events</code></p></td>
<td><p>Includes monitoring data for all resources and users in the export.</p></td>
</tr>
<tr>
<td><code>--include-server-settings</code></td>
<td>Includes persistent server settings, such as Log Settings, Ad Hoc Settings, Ad Hoc Cache, and OLAP Settings.</td>
</tr>
<tr>
<td><code>--report-alerts</code></td>
<td><p>Comma-separated list of repository report unit and folder URIs for which report unit alerts should be exported. For a folder URI, this option exports the alerts of all reports in the folder and all subfolders.</p></td>
</tr>
</tbody>
</table>

!!! warning

    User passwords are encrypted during the export by default, but exported catalogs may contain sensitive data. Take appropriate measures to secure the catalog file from unauthorized access.

Examples:

- Export everything in the repository:

  ``` bash
  js-export --everything --output-dir myExport
  ```

- Export the /reports/interactive/CustomersReport report unit to a catalog folder:

  ``` bash
  js-export --uris /organizations/organization_1/reports/interactive/CustomersReport --output-dir myExport
  ```

- Export the /images and /reports folders:

  ``` bash
  js-export --uris /organizations/organization_1/images /organizations/organization_1/reports --output-dir myExport
  ```

- Export all resources (except users, roles, and job schedules) and their permissions to a zip catalog:

  ``` bash
  js-export --uris / --repository-permissions --output-zip myExport.zip
  ```

- Export all resources and report jobs:

  ``` bash
  js-export --uris / --report-jobs / --output-dir myExport
  ```

- Export the report jobs of the /reports/interactive/CustomersReport report unit:

  ``` bash
  js-export --report-jobs /organizations/organization_1/reports/interactive/CustomersReport --output-dir myExport
  ```

- Export all roles and users:

  ``` bash
  js-export --roles --users --output-dir myExport
  ```

- Export ROLE_USER and ROLE_ADMINISTRATOR roles along with all users belonging to either role:

  ``` bash
  js-export --roles ROLE_USER, ROLE_ADMINISTRATOR --role-users --output-dir myExport
  ```

- Export all resources in an organization, but not its suborganizations:

  ``` bash
  js-export --organization organization_1 --skip-suborganizations --uris /
  ```

  <div class="admonition note">
  <p class="admonition-title">Note</p>

                      <p>The folder named Temp at the root and in every organization is a special folder. None of the folders or resources in a Temp folder are exported.</p>

  </div>

## Importing from the Command Line

See Import and Export Through the Command Line for guidelines when running the command-line utilities.

!!! warning

    When using the js-import command-line utility, the server must be stopped to avoid issues with caches, configuration, and security. For instructions see the JasperReports Server Installation Guide.

Usage: `js-import [OPTIONS]`

Use this command to read the catalog from your file system and create the resources in the JasperReports Server repository. The import command can also create entities such as organizations, users, roles, and attributes. The catalog must be one created by the export interface or the `js-export` command, either as a ZIP archive file or a folder structure.

Exported catalogs may contain encrypted passwords. If you are importing to a different server, you must configure an encryption key on both servers. See [The Import-Export Encryption Keys](import_and_export_catalogs.md) for details.

The `js-import` command includes additional options for importing cryptographic keys. For more information about this special use case, see the JasperReports Server Security Guide.

<table>
<caption><p>Options in <code>js-import</code> Command</p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Option</p></th>
<th><p>Explanation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>--help</code></p></td>
<td><p>Displays brief information about the available options.</p></td>
</tr>
<tr>
<td><p><code>--input-dir</code></p></td>
<td><p>Path for importing a catalog from a directory.</p></td>
</tr>
<tr>
<td><p><code>--input-zip</code></p></td>
<td><p>Path and filename for importing a catalog from a zip file.</p></td>
</tr>
<tr>
<td><p><code>--update</code></p></td>
<td><p>Resources in the catalog replace those in the repository if their URIs and types match.</p></td>
</tr>
<tr>
<td><p><code>--skip-user-update</code></p></td>
<td><p>When used with <code>--update</code>, users in the catalog are not imported or updated. Use this option to import catalogs without overwriting currently defined users.</p></td>
</tr>
<tr>
<td><code>--organization</code></td>
<td>If the import catalog is from an organization, it specifies the target organization where it should be imported. The organization ID should match the ID of the organization in the import catalog, if not, use the <code>--merge-organizaiton</code> option.</td>
</tr>
<tr>
<td><code>--merge-organization</code></td>
<td>Use this option when <code>--organization</code> is specified but it does not match the ID of the organization in the import catalog. When merging organizations, the contents of the import override the target organization for any user, role, or resource with the same name. A merged organization takes the organization ID of the imported organization.</td>
</tr>
<tr>
<td><code>--broken-dependencies</code></td>
<td><p>Specifies the action to take when importing a resource with a broken dependency. One of the following values:</p>
<ul>
<li><code>skip</code> – Does not import the resource with the broken dependency, but continues to import other resources.</li>
<li><code>include</code> – Attempts to import the resource with the broken dependency. The import succeeds if there is already a resource in the destination that satisfies the dependency. If the dependency is not satisfied in the destination, the resource is skipped and the import continues.</li>
<li><code>cancel</code> – Stops the import operation.</li>
</ul></td>
</tr>
<tr>
<td><p><code>--include-access-events</code></p></td>
<td><p>Restores access events (date, time, and username of last modification) on imported resources.</p></td>
</tr>
<tr>
<td><p><code>--include-audit-events</code></p></td>
<td><p>Imports any audit data in the catalog.</p></td>
</tr>
<tr>
<td><p><code>--include-monitoring-events</code></p></td>
<td><p>Imports any monitoring data in the catalog.</p></td>
</tr>
<tr>
<td><p><code>--include-server-settings</code></p></td>
<td><p>Determines whether the system configuration is updated from the catalog. There are two prerequisites for the catalog to contain configuration settings:</p>
<ul>
<li>The originating server settings must be modified through the UI (Log Settings<span>, Ad Hoc Settings, Ad Hoc Cache,</span> and OLAP Settings). For more information, see <a href="../configuration/configuration_settings_in_the_ui.md">Configuration Settings in the User Interface</a>.</li>
<li>The catalog must be exported with the "everything'" option from the user interface or the command-line utility.</li>
</ul>
<p>Imported server settings take effect when the server is started.</p></td>
</tr>
<tr>
<td><code>--skip-themes</code></td>
<td>This flag is required when importing a catalog that includes a theme from some Release 5 server versions. If you need to import a custom theme, use the Theme UI to download it from the source server and upload it to the target server. In some cases, you may need to take more extensive steps. For more information, see <a href="../themes/creating_themes.md">Downloading and Uploading Theme ZIP Files</a>.</td>
</tr>
<tr>
<td><code>--include-alerts</code></td>
<td><p>Includes data alert when importing the report.</p></td>
</tr>
</tbody>
</table>

Examples:

- Import the `myExport.zip` catalog archive file:

  ``` bash
  js-import --input-zip myExport.zip
  ```

- Import the `myDir` catalog folder, replacing existing resources if their URIs and types match those found in the catalog:

  ``` bash
  js-import --input-dir myDir --update
  ```

- Import the `myExport.zip` catalog archive file but ignore any users found in the catalog:

  ``` bash
  js-import --input-zip myExport.zip --update --skip-user-update
  ```

- Import the `myDir` catalog folder with access events:

  ``` bash
  js-import --input-dir myDir --include-access-events
  ```

When a resource in the target repository has the same URI as on that you are importing, the default behavior is left as it is and the existing resource remains unchanged (no overwriting occurs).

To delete the existing resource and replace it with a new one (of the same type and with the same URI), use the `--update` option. Note that, if the resource in the export catalog is a different type than the existing resource, the server returns an error and skips the update operation.

When you import a user whose roles exist in the repository, the user is given those roles. User properties are imported with the user.

When you import access events, the date and time of the last modification before export is restored on import for every resource. The catalog folder has to be created with access events. If you do not import access events, or if they do not exist in the imported files, then the date and time of the import are used.

## Configuring Import-Export Utilities

If you installed JasperReports Server from the binary installer, the import-export utilities are configured by the installer. If you installed the WAR file distribution, you must configure several files before you can use the import-export utilities.

Alternatively, see [Alternate Import-Export Scripts](alternate_import-export_scripts.md) because the alternate scripts do not require any configuration, regardless of the installation method.

To configure the import-export utilities

1.  Depending on the database you use, copy the installation configuration file:

    from: `<js-install>/buildomatic/sample_conf/<database>_master.properties`

    to: `<js-install>/buildomatic/default_master.properties`

2.  Edit the `default_master.properties` file to set values specific to your installation. For more information about the settings in this file, see the JasperReports Server Installation Guide.

    !!! note

        Oracle users can set the `sysUsername` and `sysPassword` to the same name as `dbUsername` and `dbPassword` in the `default_master.properties`. The system username and password are not required because js-import and js-export do not make changes to the database schema.

3.  Run the following command:

    ``` bash
     js-ant clean-config gen-config
    ```

    This command generates the following files with the values that you added to the `default_master.properties` file:

    - `<js-install>/buildomatic/build_conf/default/js.jdbc.properties`

    - `<js-install>/buildomatic/build_conf/default/js.quartz.properties` (only for DB2 and PostgreSQL)

4.  Make sure that the JDBC driver for your database is located in the following folder:

    ``` xml
    <js-install>buildomatic/conf_source/iePro/lib
    ```

    If necessary, you can find links for downloading JDBC drivers from the Jaspersoft [Community website.](http://community.jaspersoft.com/wiki/downloading-and-installing-database-drivers)
