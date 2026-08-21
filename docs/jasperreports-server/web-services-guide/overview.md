---
title: Overview
description: "A resource is identified by:"
---

# 1.0.1 Overview

A resource is identified by:

- A name.
- A label.
- A unique Uniform Resource Identifier (URI) that defines the location of the resource in the repository. A URI is similar to a Unix path (for example, /reports/samples/AllAccounts).

A resource can have a set of properties (depending on its type) and a set of children resources.

The resource descriptor is a complex structure that transfers data regarding a specific resource between the server and the client. A request can include only one resource descriptor. Often, the request only includes a small portion of the entire resource descriptor definition: the part that describes the specific details of the resource in question.

For example, when a `resourceDescriptor` is used as an input parameter in a request document (for example, to specify a folder to list or a file to download), the descriptor includes only a small portion of the entire resource descriptor definition: the part that describes the specific resource details in question. In many cases, the only information required to identify a resource in the repository is its `wsType`, `name`, and `URI`.

The resource descriptors that the server sends are completely populated with all the data about the resources being described.

A `resourceDescriptor` tag is defined by the following DTD (Document Type Definition):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>&lt;!ELEMENT resourceDescriptor (label, description?, resourceProperty*, resourceDescriptor*, parameter*)&gt;
&lt;!ATTLIST resourceDescriptor
  name CDATA #REQUIRED
  wsType CDATA #REQUIRED
  uriString CDATA #REQUIRED
  isNew ( true | false ) false
&gt;
&lt;!ELEMENT resourceProperty (value?, resourceProperty*)&gt;
&lt;!ATTLIST resourceProperty
  name CDATA #REQUIRED
&gt;
&lt;!ELEMENT value (#PCDATA)&gt;
&lt;!ELEMENT parameter (#PCDATA)&gt;
&lt;!ATTLIST parameter
  name CDATA #REQUIRED
  isListItem ( true | false ) false
&gt;</code></pre></td>
</tr>
</tbody>
</table>

The following sections describe the DTD:

- [wsType Attribute](wstype_attribute.md)
- [isNew Attribute](isnew_attribute.md)
- [Resource Descriptor Parameters](resource_descriptor_parameters.md)
- [Examples of resourceDescriptor](examples_of_resourcedescriptor.md)
