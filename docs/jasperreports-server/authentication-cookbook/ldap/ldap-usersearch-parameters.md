---
title: Specifying userSearch Parameters
description: "Use the userSearch bean to find users if they don't match a simple pattern. In particular, if you're authenticating users for one or more organizations, it is likely user entries are in multiple..."
---

# Specifying userSearch Parameters

Use the `userSearch` bean to find users if they don't match a simple pattern. In particular, if you're authenticating users for one or more organizations, it is likely user entries are in multiple branches of your directory.

To search for user entries, locate the helper bean `userSearch` in sample-applicationContext-externalAuth-LDAP\[-mt\].xml and specify the following information:

- An optional branch RDN where user entries are located. If not specified, the search includes your entire LDAP directory starting from the base DN of the LDAP URL specified in [Setting the LDAP Connection Parameters](ldap-setting-connection-parameters.md).
- An LDAP filter expression to compare any attribute or combination of attributes with the login name. JasperReports Server substitutes the login name entered by the user for the `{0}` placeholder to perform the search.
- Whether or not the search should extend to all subtrees beneath the branch DN or, when no branch DN is specified, beneath the base DN.

!!! note

    When you enter a location for user search, make sure to use only the relative DN. Do not include the base DN that you set up when creating the LDAP connection parameters.

The following example shows the syntax of the bean’s constructor and property:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">bean</span> <span class="ot">id=</span><span class="st">&quot;userSearch&quot;</span> <span class="ot">class=</span><span class="st">&quot;com.jaspersoft.jasperserver.api.security.</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="st">              externalAuth.wrappers.spring.ldap.JSFilterBasedLdapUserSearch&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">constructor-arg</span> <span class="ot">index=</span><span class="st">&quot;0&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;ou=users&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">constructor-arg</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">constructor-arg</span> <span class="ot">index=</span><span class="st">&quot;1&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;(uid={0})&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">constructor-arg</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">constructor-arg</span> <span class="ot">index=</span><span class="st">&quot;2&quot;</span>&gt;&lt;<span class="kw">ref</span> <span class="ot">bean=</span><span class="st">&quot;ldapContextSource&quot;</span> /&gt;&lt;/<span class="kw">constructor-arg</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">property</span> <span class="ot">name=</span><span class="st">&quot;searchSubtree&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;true&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">property</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">bean</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The combination of these three parameters lets you optimize the search for your user entries and reduce the load on your LDAP directory. For example, if your users are located in a dedicated branch of your LDAP structure, specify it in the first constructor argument to avoid searching the entire tree.
