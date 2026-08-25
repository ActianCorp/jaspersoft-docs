---
title: Alternate Import-Export Scripts
description: "Regardless of your installation method, JasperReports Server provides a third way to run import-export commands. Buildomatic is another command-line script that is based on the Apache Ant tool to..."
---

# Alternate Import-Export Scripts

Regardless of your installation method, JasperReports Server provides a third way to run import-export commands. Buildomatic is another command-line script that is based on the [Apache Ant](http://ant.apache.org/) tool to automate installations. It includes targets (sub-commands) to perform import and export operations with the same options as the scripts. The following examples compare the two commands:

|  |  |
|----|----|
| Shell Scripts: | `js-export.sh --everything --output-zip=js-catalog-exp.zip` |
| Buildomatic: | `js-ant export-everything -DexportFile=js-catalog-exp.zip` |

Both types of scripts are located in the `<js-install>/buildomatic` folder.

## Running Import from Buildomatic

The `import` target for ant has the following syntax:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p>Windows:</p></td>
<td><p><code>js-ant import -DimportFile=&lt;filename&gt; [-DimportArgs="&lt;import-options&gt;"]</code></p></td>
</tr>
<tr>
<td><p>Linux and Mac OSX:</p></td>
<td><p><code>./js-ant import -DimportFile=&lt;filename&gt; [-DimportArgs="&lt;import-options&gt;"]</code><br />
</p></td>
</tr>
</tbody>
</table>

The imported file is handled as a ZIP archive if its name ends in .zip, otherwise it's handled as a directory. The `importArgs` argument is optional and can contain more than one import option.

!!! note

    When performing a large import using js-ant, the server should be stopped (or put into a mode with reduced load) to avoid issues with caches, configuration, and security.

The following examples are typical import commands on Windows:

``` bash
js-ant import-help-pro
js-ant import -DimportFile=my-reports.zip
js-ant import -DimportFile=my-datasources -DimportArgs="--update"
```

The following examples are typical import commands on Linux:

``` bash
./js-ant import-help-pro
./js-ant import -DimportFile=my-reports.zip
./js-ant import -DimportFile=my-datasources.zip -DimportArgs="--update"
```

## Running Export from Buildomatic

The `export` target for ant has the following syntax:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p>Windows:</p></td>
<td><p><code>js-ant export -DexportFile=&lt;filename&gt; -DexportArgs="&lt;export-options&gt;"</code></p></td>
</tr>
<tr>
<td><p>Linux and Mac OSX:</p></td>
<td><p><code>./js-ant export -DexportFile=&lt;filename&gt; -DexportArgs="&lt;export-options&gt;"</code><br />
</p></td>
</tr>
</tbody>
</table>

The export file format is a ZIP file or a set of files under a new directory name. If you specify the .zip extension for your output filename, a ZIP archive is created automatically. Otherwise, an uncompressed directory with files and sub-directories is created.

The following examples are typical export commands on Linux and Windows:

``` bash
js-ant export-help-pro
js-ant export -DexportFile=my-domains.zip
    -DexportArgs="--uris /organizations/organization_1/datasources"
js-ant export -DexportFile=my-reports-and-users.zip
    -DexportArgs="--uris /organizations/organization_1/reports
    --users jasperadmin|organization_1,joeuser|organization_1"
js-ant export -DexportFile=my-datasources
    -DexportArgs="--uris /organizations/organization_1/datasources --roles ROLE_USER"
js-ant export -DexportFile=js-everything.zip -DexportArgs="--everything"
```
