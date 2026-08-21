---
title: Adding Dashboard Web Page Domain Whitelist Attributes to Server Attributes
description: We have enhanced the reliability and security of the JasperReports Server dashboard creation process. The system now includes comprehensive validation checks on all web page inputs. This critical...
---

# Adding Dashboard Web Page Domain Whitelist Attributes to Server Attributes

We have enhanced the reliability and security of the JasperReports Server dashboard creation process. The system now includes comprehensive validation checks on all web page inputs. This critical update ensures that only safe, properly formed content can be saved, protecting users from potential Stored Cross-Site Scripting (XSS) vulnerabilities and securing their dashboards.

This is achieved by adding the `dashboardWebpageDomainWhitelist` attribute on the **Server Attributes** page. It can be found under **Manage \> Server Settings**. The default value is empty.

This new feature strengthens dashboard security by whitelisting specific web page domains and linking them to server attributes, giving administrators more control over access. Additionally, role-based permissions are introduced to ensure that only authorized users can change these settings.

The Stored XSS vulnerability is addressed by implementing a new server-side mechanism which is introduced to control access based on user roles, adding another layer of security.

The server is configured to authenticate users. The system now retrieves a configuration for dashboard web page whitelist values.

- If a user is authenticated and has the right profile attributes, the system looks for their dashboard web page whitelist values in a hierarchical order (User \> Organization \> Server).

- If the user is not authenticated or if no whitelist values are found at any level, they are assigned empty values.

## Hierarchical Attribute Search

The system uses a hierarchical search pattern to find the correct dashboard web page whitelist values. It checks for the whitelist in this specific order:

- User level: The system first looks for the attribute directly in the user's profile.

- Organization level: If no attribute is found there, it then searches the logged-in user's organization and any parent organizations.

- Server level: Finally, if the attribute is still not found, the system uses the default values set at the server level.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Attribute (<code>dashboardWebpageDomainWhitelist</code>) Configuration</p></th>
</tr>
</thead>
<tbody>
<tr>
<th><p>Hierarchy level</p></th>
<th><p>Value</p></th>
<th><p>Description</p></th>
</tr>
&#10;<tr>
<td><p>at server level</p></td>
<td><p>&lt;blank&gt;<br />
</p></td>
<td><p>This is the default value of the attribute (attribute defined with an empty value).</p>
<p>It does not accept any input value at web dashlet creation and functions as an 'All values are invalid' for the dashlet.</p></td>
</tr>
<tr>
<td><p>at server level</p></td>
<td><p>*</p></td>
<td>All URLs are supported for web dashlet.</td>
</tr>
<tr>
<td><p>at server level</p></td>
<td><p><code>https://www.example.com</code></p>
<p>**Note** You can have multiple URLs at the same level (server, organization, or user) by separating them with a comma.</p></td>
<td><p>The attribute value must be available across all levels (server, organization, and user). The system should allow only the value <code>https://www.example.com</code> for the web dashlet. This same behavior must be maintained for any exported dashboards containing that web dashlet.</p></td>
</tr>
<tr>
<td><ul>
<li><p>at server level</p></li>
<li><p>at org1 level</p></li>
</ul></td>
<td><ul>
<li><p><code>http://serverexample1.com</code></p></li>
<li><p><code>http://orgexample1.com</code></p></li>
</ul></td>
<td><ul>
<li><p>The specified URL (<code>http://serverexample1.com</code>) is only supported in the web dashlet for organizations and users where the attribute's hierarchical structure makes it available.</p></li>
<li><p>The specified URL for org1, <code>http://orgexample1.com</code>, must be used in the web dashlet because the server-level URL is not available at the organization level. This same URL will then apply to all users belonging to org1.</p></li>
</ul></td>
</tr>
<tr>
<td>at user level</td>
<td><code>http://userexample1.com</code></td>
<td>The web dashlet should use the URL <code>http://userexample1.com</code> for specific users, as the server and organization-level URLs are not accessible or defined at the user level.</td>
</tr>
</tbody>
</table>

## Validation Rules in Dashboard Web Page Section

When you add the **Web page URL** to a dashboard, the system performs a domain check:

- The URL's domain must match a domain listed in the `dashboardWebpageDomainWhitelist`.

- If the `dashboardWebpageDomainWhitelist` is empty, no domains are accepted.

- If the whitelist contains an asterisk (\*) , all domains are accepted.

If you try to add a domain that is not allowed, an error message is shown:

**Invalid domain. Add the domain to the allowlist from Manage \> Server Settings \> Server Attributes.**

## Dashboard Import With Web Dashlet

When importing a dashboard, the system handles Web dashlets differently depending on their URL status.

- If the Web dashlet has a whitelisted URL, the import is successful and the dashlet loads correctly.

- If the Web dashlet has a non-whitelisted URL, the import is still successful, but the dashlet shows an error message instead of its content.

  **Invalid domain. Add the domain to the allowlist from Manage \> Server Settings \> Server Attributes.**

!!! note

    Even after deleting this attribute from the **Server Attributes** page, the attribute still appears with a default "empty" value when the page is refreshed.
