---
title: Specifying userDnPatterns Parameters
description: "If you have a fixed structure of user entries and the login name of the user appears in the RDN of your user entries, you can configure the JSBindAuthenticator bean with patterns to match them. The..."
---

# Specifying userDnPatterns Parameters

If you have a fixed structure of user entries and the login name of the user appears in the RDN of your user entries, you can configure the `JSBindAuthenticator` bean with patterns to match them. The patterns are not included in the sample file, but can easily be added:

1.  In sample-applicationContext-externalAuth-LDAP\[-mt\].xml, locate the `ldapAuthenticationProvider` bean. The unnamed bean of class `JSBindAuthenticator` is the first constructor argument.
2.  Add the `userDnPatterns` property in `JSBindAuthenticator`.
3.  Configure one or more patterns for matching the RDNs of user entries. For each value in the list, the server substitutes the login name entered by the user for the `{0}` placeholder, then creates a DN by appending the base DN from the LDAP URL. The LDAP URL is specified in [Setting the LDAP Connection Parameters](ldap-setting-connection-parameters.md). JasperReports Server attempts to bind to the LDAP directory with the DN created with each pattern in the order they are given.

!!! note

    When you enter a pattern for RDN matching, make sure to use only the relative DN. Do not include the base DN that you set up when creating the LDAP connection parameters.

In the example below, JasperReports Server looks for a user whose given login name appears in the `uid` attribute of the RDN in the `ou=users` branch of the LDAP directory:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">bean</span> <span class="ot">id=</span><span class="st">&quot;ldapAuthenticationProvider&quot;</span> <span class="ot">class=</span><span class="st">&quot;com.jaspersoft.jasperserver.api.security.</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="st">    externalAuth.wrappers.spring.ldap.JSLdapAuthenticationProvider&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">constructor-arg</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">bean</span> <span class="ot">class=</span><span class="st">&quot;com.jaspersoft.jasperserver.api.security.externalAuth.wrappers.</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="st">          spring.ldap.JSBindAuthenticator&quot;</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">constructor-arg</span>&gt;&lt;<span class="kw">ref</span> <span class="ot">bean=</span><span class="st">&quot;ldapContextSource&quot;</span>/&gt;&lt;/<span class="kw">constructor-arg</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">property</span> <span class="ot">name=</span><span class="st">&quot;userDnPatterns&quot;</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">list</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">value</span>&gt;uid={0},ou=users&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">list</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">property</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">bean</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">constructor-arg</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>  ...</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">bean</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

Notice that the domain name value only specifies ou=users. This is combined with the base DN defined by the `external.ldapUrl` property in the default_master.properties file or the `constructor-arg` value in the `ldapContextSource` bean to create the full DN.
