---
title: List Operation
description: "This service lists the contents of the specified folder or report unit. The following sample request lists the contents of the<br> /ContentFiles folder in the repository:"
---

# 1.1 List Operation

This service lists the contents of the specified folder or report unit. The following sample request lists the contents of the<br>
/ContentFiles folder in the repository:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">request</span> <span class="ot">operationName=</span><span class="st">&quot;list&quot;</span> <span class="ot">locale=</span><span class="st">&quot;en&quot;</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;folder&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/ContentFiles&quot;</span>   <span class="ot">isNew=</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;null&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">request</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

Sample response:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">operationResult</span> <span class="ot">version=</span><span class="st">&quot;1.2.0&quot;</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">returnCode</span>&gt;0&lt;/<span class="kw">returnCode</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;html&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;folder&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/ContentFiles/html&quot;</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;html&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.Folder&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;/ContentFiles&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;0&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;pdf&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;folder&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/ContentFiles/pdf&quot;</span> </span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>    <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">label</span>&gt;pdf&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.Folder&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;/ContentFiles&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;</span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;0&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;xls&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;folder&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/ContentFiles/xls&quot;</span> </span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>    <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-31"><a href="#cb1-31" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;xls&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-32"><a href="#cb1-32" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb1-33"><a href="#cb1-33" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.Folder&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-34"><a href="#cb1-34" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-35"><a href="#cb1-35" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;</span>
<span id="cb1-36"><a href="#cb1-36" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;/ContentFiles&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-37"><a href="#cb1-37" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;0&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">operationResult</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

When it lists a folder, the repository web service returns a set of resource descriptors: one for each resource that resides in the specified folder. Use / as the URI of the root folder.

Similarly, when it lists a report unit, the repository web service returns a set of resource descriptors that contain (at a minimum) the main JRXML source file. Since a resource in a report unit can be either a local resource or a reference to another repository resource, you should keep a few details in mind:

-   If a report unit data source is not defined locally, its `wsType` is set to `datasource`, which does not indicate the exact nature of the resource. Its type should simply be `reference`, but since the data source used by the report unit is a special child resource, it’s easy to recognize. The URI of the referenced resource is available in the `PROP_REFERENCE_URI` property.

-   The main JRXML resource’s `wsType` is always set to `jrxml`, even if it’s a reference to an external JRXML resource. By looking at the `PROP_IS_REFERENCE` and `PROP_REFERENCE_URI` properties, you can determine where the resource is actually stored. The `PROP_RU_IS_MAIN_REPORT` property identifies the main JRXML source file of the report unit, even if the order of its children is altered.

-   The purpose of listing a report unit is to get the list of the resources contained in the report unit. To retrieve the entire report unit (report unit resource as well as its children) at the same time, use the `get` service.

    The following Java sample illustrates `wsclient` as an instance of `com.jaspersoft.jasperserver.irplugin.wsclient.WSClient`:

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><div class="language-text highlight"><pre><code>ResourceDescriptor rd = new ResourceDescriptor();
    rd.setWsType( ResourceDescriptor.TYPE_FOLDER );
    rd.setUriString(&quot;/&quot;);
    List lst = wsclient.list(rd);</code></pre></div></td>
    </tr>
    </tbody>
    </table>

    PHP sample:

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><div class="sourceCode" id="cb1"><pre class="sourceCode bash"><code class="sourceCode bash"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="va">$result</span> = ws_list<span class="er">(</span><span class="st">&quot;/&quot;</span><span class="kw">);</span></span>
    <span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="cf">if</span> <span class="kw">(</span><span class="ex">get_class</span><span class="er">(</span><span class="va">$result</span><span class="kw">)</span> <span class="ex">==</span> <span class="st">&#39;SOAP_Fault&#39;</span><span class="kw">)</span></span>
    <span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="kw">{</span></span>
    <span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  <span class="va">$errorMessage</span> = <span class="va">$result</span>-<span class="op">&gt;</span>getFault<span class="er">(</span><span class="kw">)</span><span class="ex">-</span><span class="op">&gt;</span>faultstring<span class="kw">;</span></span>
    <span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="kw">}</span></span>
    <span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="cf">else</span></span>
    <span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="kw">{</span></span>
    <span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  <span class="va">$folders</span> = getResourceDescriptors<span class="er">(</span><span class="va">$result</span><span class="kw">);</span></span>
    <span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a><span class="kw">}</span></span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

    This PHP sample uses the client.php file found in the PHP sample provided with JasperReports Server. This file defines the most important constants you may find useful when integrating with the JasperReports Server web services, as well as useful functions that wrap the `list`, `get`, and the runReport operations.

    The list operation also provides a shortcut to get the list of all resources of a given type in the repository, for example all the reports. This use of the list operation has the following syntax:

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">request</span> <span class="ot">operationName=</span><span class="st">&quot;list&quot;</span>&gt;</span>
    <span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">argument</span> <span class="ot">name=</span><span class="st">&quot;LIST_RESOURCES&quot;</span>/&gt;</span>
    <span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">argument</span> <span class="ot">name=</span><span class="st">&quot;RESOURCE_TYPE&quot;</span>&gt;reportUnit&lt;/<span class="kw">argument</span>&gt;</span>
    <span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">argument</span> <span class="ot">name=</span><span class="st">&quot;PARENT_DIRECTORY&quot;</span>&gt;/reports&lt;/<span class="kw">argument</span>&gt;</span>
    <span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">request</span>&gt;</span></code></pre></div></td>
    </tr>
    <tr>
    <td><div class="language-text highlight"><pre><code>or
    &lt;request operationName=&quot;list&quot;&gt;
      &lt;argument name=&quot;LIST_RESOURCES&quot;/&gt;
      &lt;argument name=&quot;RESOURCE_TYPE&quot;&gt;reportUnit&lt;/argument&gt;
      &lt;argument name=&quot;START_FROM_DIRECTORY&quot;&gt;/reports&lt;/argument&gt;
    &lt;/request&gt;</code></pre></div></td>
    </tr>
    </tbody>
    </table>

    No value is needed for the `LIST_RESOURCES` argument. The value of the `RESOURCE_TYPE` argument can be any value of `wsType` except `folder`. The `PARENT_DIRECTORY` argument is the name of folder in which you want to look for resources. If you want to look for the resources in a branch of the repository, use the `START_FROM_DIRECTORY` argument.

    !!! note

        Using LIST_RESOURCES is the only case in which a request doesn’t require a resource descriptor.

    Several Java methods in `com.jaspersoft.jasperserver.irplugin.wsclient.WSClient` use `LIST_RESOURCES`:

-   `list(String xmlRequest)` - Sends any custom request, including one using `LIST_RESOURCES` as shown above.

-   `listResources(String type)` - Lists all resources of the given type in the repository visible to the logged in user.

-   `listResourcesInFolder(String type, String parentFolder)` - Lists resources of the given type in the folder.

-   `listResourcesUnderFolder(String type, String ancestorFolder)` - Lists resources of the given type in the folder and the entire tree beneath that folder.
