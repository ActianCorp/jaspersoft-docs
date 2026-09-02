---
title: Customizing the JasperReports Wizard Repository Trees
description: "Having a large number of resources in your repository may slow down the user session when using the JasperReports Wizard. When creating or editing a report using the wizard, JasperReports Server..."
---

# Customizing the JasperReports Wizard Repository Trees

Having a large number of resources in your repository may slow down the user session when using the JasperReports Wizard. When creating or editing a report using the wizard, JasperReports Server searches the repository for the appropriate resource types before opening the repository tree, which displays only the folders containing the found resource types but can result in a long load time if you have a large repository.

You can speed this up by enabling "lazy loading" for specific resource type trees in the UI.

Lazy loading speeds up the load time of the repository tree because JasperReports Server will not search for the resources until you browse to a folder in the tree. The repository tree displays all of the folders in the repository but only displays the appropriate resources when you open a folder. Any folder that does not contain resources that can be used by the report will appear empty.

To enable lazy loading for the JasperReports Wizard's repository trees, you will need to add a new property to the appropriate beans in the repository tree configuration files. The following table contains the configuration files and bean IDs for the JasperReports Wizard's repository trees.

**Repository Tree Configuration Files**

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Configuration File</p></th>
<th><p>Bean ID</p></th>
<th><p>Repository Tree</p></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4"><p><code>&lt;js-webapp&gt;/WEB-INF/flows/repositoryExplorerBean.xml</code></p></td>
<td><code>inputControlResourceTreeDataProvider</code></td>
<td><p>Input Controls</p>
<p>(Controls &amp; Resources page)</p></td>
</tr>
<tr>
<td><code>jrxmlTreeDataProvider</code></td>
<td><p>JRXML Files</p>
<p>(Set Up the Report page)</p></td>
</tr>
<tr>
<td><code>queryTreeDataProvider</code></td>
<td><p>Query</p>
<p>(Locate Query page)</p></td>
</tr>
<tr>
<td><code>fileResourceTreeDataProvider</code></td>
<td><p>File Resources</p>
<p>(Controls &amp; Resources page)</p></td>
</tr>
<tr>
<td><p><code>&lt;js-webapp&gt;/WEB-INF/flows/repositoryExplorerProBean.xml</code></p></td>
<td><p><code>proDsTreeDataProvider</code></p></td>
<td><p>Data Source</p>
<p>(Link a Data Source to the Report page)</p></td>
</tr>
</tbody>
</table>

To enable "lazy loading" for your repository

1.  Open the repository tree configuration file you want to edit.

2.  Locate the bean for the repository tree for which you want to enable lazy loading.

3.  Add the following line to the bean:

    ``` xml
    <property name="lazy" value="true" />
    ```

4.  Save the modified file and restart the application server to see changes.
