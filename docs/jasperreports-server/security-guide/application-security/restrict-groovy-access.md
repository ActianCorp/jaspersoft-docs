---
title: Restricting Groovy Access
description: "This section describes functionality that can be restricted by the software license for JasperReports Server. If you do not see some of the options described in this section, your license may..."
---

# Restricting Groovy Access

!!! note

    This section describes functionality that can be restricted by the software license for JasperReports Server. If you do not see some of the options described in this section, your license may prohibit you from using them. To find out what you are licensed to use, or to upgrade your license, contact Jaspersoft.

JasperReports Server relies on Apache Groovy in a number of contexts, including:

- When a Domain definition includes a security file that determines which users or roles have access to various data.
- When a calculated field in an Ad Hoc view or Domain relies on a Groovy expression.

By default, Groovy is given broad access within your application server, which is a good approach to certain design, testing, and evaluation tasks. However, some production systems should be configured to restrict Groovy to more limited access by creating a whitelist that only includes the classes Groovy should access. Once configured, the server returns an error when the Groovy compiler encounters code that does not conform to the whitelist.

Groovy's access is set at the server level; configure it by editing properties files as well as a Groovy source file:

1.  Configure the `groovyRunner` to enable the restriction in general.
2.  Configure the preprocessor to enable the restriction for Groovy expressions in DomEL.
3.  Optionally configure the whitelist to allow Groovy access to additional classes.

First, enable the Groovy restriction:

<table>
<thead>
<tr>
<th colspan="3"><p>Groovy Restriction</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-semanticLayer.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>groovyCustomizerFactory</code></p></td>
<td><p><code>groovyRunner</code></p></td>
<td><p>Uncomment this property to enable the restriction.</p></td>
</tr>
</tbody>
</table>

In addition to enabling the Groovy restriction, configure the DomEL preprocessor:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>DomEL Restriction</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-datarator.xml</code></p></td>
</tr>
<tr>
<td><p>Attribute</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>preprocessGroovy</code></p></td>
<td><p><code>defaultPreprocessor</code><br />
</p></td>
<td><p>Set this value to true to apply the Groovy restriction to all DomEL expressions that rely on the <code>groovy()</code> function.</p></td>
</tr>
</tbody>
</table>

Optionally, you can extend the whitelist by adding additional classes that you want Groovy to access:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>Groovy Whitelist</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Groovy Source File</p></td>
</tr>
<tr>
<td colspan="2"><p><code>.../groovy/com/jaspersoft/commons/groovy/GroovyCustomizerFactoryImpl.groovy</code></p></td>
</tr>
<tr>
<td><p>Class</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>GroovyCustomizerFactoryImpl</code></p></td>
<td><p>List of classes that Groovy can access. Enclose each classname in quotes and delimit each entry with a comma. For example:</p>
<p><code>def receiversWhiteList = [</code></p>
<p><code>'java.lang.Byte',</code></p>
<p><code>'java.lang.Character',</code></p>
<p><code>...</code></p>
<p><code>]</code></p>
<p>The last entry should not be followed by a comma.</p></td>
</tr>
</tbody>
</table>

Which classes you might restrict Groovy from accessing depends largely on your usage patterns, environment, and security concerns. Because of this, we cannot provide specific advice about what you should whitelist. However, we have some general recommendations of classes you would or would not want to whitelist.

For example, Groovy can be used to run commands in the server host's operating system using a string literal such as `rm -rf /".execute()`. Therefore, `java.lang.String` should not be added to the whitelist.

However, some classes, like those in the default list, are considered much safer. For example, the class `org.apache.commons.lang3.StringUtils` consists solely of static utility string methods, so if it is in the whitelist, you can call `StringUtils.isEmpty()` to check for an empty string, instead of calling `isEmpty()` on a string directly.

!!! note

    When you enable and configure the whitelist, be sure to test your JasperReports Server environment thoroughly.

If you have been running your server without this restriction, and then enable and configure it, some functionality may fail. For example, Domains that include a security file may return errors, since they rely on Groovy to evaluate the `principalExpression`. The failure is likely because the Groovy expression calls classes that are not in your whitelist. However, your best course of action is not necessarily to add those classes to the whitelist, as it may be difficult to debug. It is better to create a method in `BaseGroovyScript` and call it from the Domain security expression. For details, see our article on [the Jaspersoft community site](http://community.jaspersoft.com/).

For details about Groovy, see [Apache's Groovy web site](http://groovy-lang.org/).
