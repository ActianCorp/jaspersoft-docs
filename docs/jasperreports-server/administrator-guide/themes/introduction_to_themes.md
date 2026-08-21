---
title: Introduction to Themes
description: The default appearance of the JasperReports Server user interface (UI) can easily be modified to suit your needs.
---

# Introduction to Themes

The default appearance of the JasperReports Server user interface (UI) can easily be modified to suit your needs.

The UI's appearance is determined by CSS (Cascading Style Sheets). A theme is a collection of CSS files and associated images that specify the appearance for all or part of the UI. A theme controls only the UI's looks, such as fonts, colors, lines, spacing, and images. It has no effect on content or functionality.

Themes are defined globally at the repository root and individually for each organization. Only administrators can set the theme. Administrators can add, upload, edit, copy, and delete the files that make up the theme, just like other resources in the repository. The repository allows special actions on theme folders for downloading and uploading themes as ZIP (compressed archive) files, and for activating the theme. Themes are active immediately without needing to restart the server.

!!! note

    Themes are fully integrated with the multi-organization architecture in JasperReports Server. Some features of themes discussed in this chapter apply only to deployments that are licensed to use multiple organizations. However, single-organization deployments use the same architecture, for example there are overrides and inheritance between themes in the single default organization and the system root.

Themes are hierarchical and very flexible, allowing administrators to easily change the global appearance or set organization-specific overrides. For example, all of the following scenarios are possible with themes:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Scenario</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Use the default theme unchanged.</p></td>
<td><p>If the default theme suits your needs, there's no need to customize it or develop new themes.<span> After a standard installation, the default theme is set at the root level and is automatically inherited by all organizations so every user sees the server with the same interface.</span></p></td>
</tr>
<tr>
<td><p>Quickly modify the default theme.</p></td>
<td><p>You can specify overrides of individual CSS rules or replace images in the default theme. After creating and uploading the new files, your theme is active immediately.<span> Theme inheritance ensures that every organization sees your theme immediately as well.</span></p></td>
</tr>
<tr>
<td><p>Create an entirely new theme.</p></td>
<td><p>With CSS experience or Jaspersoft Professional Services, you can change the entire look and feel of the server. You can create a custom theme to match or blend with nearly any other web design.<span> Inheritance again ensures that every organization uses the new theme, while allowing you to manage it from a single set of files.</span></p></td>
</tr>
<tr>
<td><p>Override themes to customize the UI for each organization.</p></td>
<td><p>You can give each organization or suborganization a customization of the default theme, for example a new logo, while retaining all other aspects. The benefit of this approach is that the default theme can still be modified and inherited by all organizations, while retaining each organization's overrides.</p>
<p>This approach can be combined with the previous one, so that organization-specific overrides are applied to a custom theme.</p></td>
</tr>
<tr>
<td><p>Create a new theme in each organization.</p></td>
<td><p>For SaaS vendors, each organization can be a different client that needs a special interface. Themes allow each organization to fully define the UI and still retain override and inheritance for its own suborganizations. In such deployments, each organization admin can create or modify the appearance of his own user interface.</p></td>
</tr>
</tbody>
</table>
