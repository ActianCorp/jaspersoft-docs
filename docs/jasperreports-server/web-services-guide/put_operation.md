---
title: Put Operation
description: The put operation adds new resources to the repository or modifies existing ones. Whether the service adds or modifies a resource depends on whether the request’s isNew resource descriptor attribute...
---

# 1.1 Put Operation

The put operation adds new resources to the repository or modifies existing ones. Whether the service adds or modifies a resource depends on whether the request’s `isNew` resource descriptor attribute is set to `true`. The parent URI of the new resource must exist, and can be the repository root (/). When modifying a resource, you must provide the whole resource descriptor; the changes do not impact child resources.

!!! note

    You cannot use the `put` web service to create report options.

    In the web interface, report options are created when users specify values for a report’s input controls or filters, and then choose to save those settings. A new instance of the report appears as a child of the report itself. Users click the report instance to run the report using the saved values.

The following XML code creates a folder called `test` inside the /reports/samples folder:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">request</span> <span class="ot">operationName=</span><span class="st">&quot;put&quot;</span> <span class="ot">locale=</span><span class="st">&quot;en&quot;</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;test&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;folder&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/reports/samples/test&quot;</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="ot">isNew=</span><span class="st">&quot;true&quot;</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">label</span>&gt;Test&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;This is a test&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;/reports/samples&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>  &lt;/resourceDescriptor&gt;
&lt;/request&gt;</code></pre></div></td>
</tr>
</tbody>
</table>

When adding a file resource, the data must be added as an attachment to the SOAP request, and the `PROP_HAS_DATA` property must be set to `true`. When modifying a file resource, you only need to attach the file if it must be replaced; otherwise `PROP_HAS_DATA` can be set to FALSE. In this case, the properties you provide are changed (for example, the label and the description).

The following Java sample creates a new image resource in the repository using the sample classes provided with JasperReports Server:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>ResourceDescriptor rdis = new ResourceDescriptor();
rdis.setResourceType(ResourceDescriptor.TYPE_IMAGE);
rdis.setName(&quot;testImageName&quot;);
rdis.setLabel(&quot;TestImageLabel&quot;);
rdis.setDescription(&quot;Test Image Description&quot;);
rdis.setParentFolder(&quot;/images&quot;);</code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>rdis.setUriString(rdis.getParentFolder() + &quot;/&quot; + rdis.getName());
rdis.setWsType(ResourceDescriptor.TYPE_IMAGE);
File img = new File(&quot;/some/file/logo.jpg&quot;));
rdis.setHasData(true);
rdis.setIsNew(true);
ResourceDescriptor result = wsclient.addOrModifyResource(rdis, img);</code></pre></div></td>
</tr>
</tbody>
</table>

Working with report units is a bit more complicated. When creating a new report unit, the request must contain a child JRXML resource descriptor where the `PROP_RU_IS_MAIN_REPORT `property is set to `true`. This resource becomes the main JRXML of the report unit. If it is defined locally to the report, the file must be attached to the SOAP request (in this case, the parent URI for report unit’s children is not relevant, and can be set to something like `<report unit parent uri>/<report unit name>_files`).

If the report unit’s main JRXML already resides in the repository, the descriptor is still defined as a JRXML resource (that is, the `wsType` property must be set to `jrxml`), and the `PROP_FILERESOURCE_REFERENCE_URI` property must be set to the URI of the correct JRXML resource in the repository.

A second child resource is recognized during creation: a data source descriptor of the data source that the server will use to run the report. This resource is optional, and can be defined either locally to the report unit or as a reference to another resource in the repository:

-   When the data source is defined locally, the resource’s `wsType` must be a valid data source type, such as `jdbc`, `jndi`, or `bean`.
-   If the data source is defined elsewhere in the repository, its `wsType` must be set to `datasource`, which indicatesan undefined resource that can be used as a data source, and its `PROP_FILERESOURCE_IS_REFERENCE` property must be set to `true`. The resource’s actual URI must be set using the `PROP_FILERESOURCE_REFERENCE_URI` property.

Other resources such as input controls and subreports, must be added separately using the put operation to modify the report unit.

Creating, modifying, and removing resources in a report unit is similar to working with resources in a folder. The main difference is that you must set the request’s `MODIFY_REPORTUNIT_URI` argument to the URI of the report unit you want to modify. You cannot remove the JRXML resource flagged as main JRXML, but can replace or modify it. The repository web service doesn’t allow you to add more than a single data source to the report unit; the report unit is always run against this data source.

!!! note

    When creating reports with parameters, note that the corresponding input controls must be added using a subsequent web service request; you cannot create the input controls in the same web service request that created the report.
