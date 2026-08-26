---
title: Changing the UI With Themes
description: "You can modify the look of the JasperReports Server user interface by creating a theme: a collection of CSS files and associated images that specify the appearance of all or part of the UI. The..."
---

# Changing the UI With Themes

You can modify the look of the JasperReports Server user interface by creating a theme: a collection of CSS files and associated images that specify the appearance of all or part of the UI. The following sections show how to use themes to change the logo and favicon, change colors and fonts, change the amount of white space, and hide UI elements. Using themes, you can customize the branding of the server or completely remove the branding for embedding.

A theme doesn't change the UI controls or provide security; hidden elements can still be accessed using the correct URL. You need to change the JSP files that control the logic of the server to control *what* users see. Themes only control *how* they see it. Additional customizations are described elsewhere in this guide.

Theme files are stored in the repository and can be downloaded, uploaded, and made active through the UI while the server is running. You don’t need to recompile any JasperReports Server source code or restart the server. For information on how to create, upload, and administer themes, see the JasperReports Server Administrator Guide.

!!! note

    You can upload themes or individual theme files in several ways. You can also upload CSS files and images into an active theme if you already have a custom theme created on the server. For implementation details, see the JasperReports Server Administrator Guide.

Keep the following tips in mind when working with themes:

-   Plan your theme deployment carefully and test it with end-users to ensure it works the way you intend.

-   The server must be running and you must be logged in as an administrator to modify themes. Modifications take effect when you make your new theme files active. You don't need to recompile any code or restart the server.

-   You must create or modify your CSS files in an external editor. Once you have modified the files you want, you can create a theme folder directly in the repository, or create a theme folder offline and upload it as a Zip archive file. Use the method that works best for you.

-   Your themes can be as simple or as complex as you want. You can combine multiple customizations in a single theme; you can also override one file in your theme with another file.

-   In multi-organization deployments, themes defined in a parent organization are expressed in child organizations. Depending on your needs, you may want to implement your theme at the root level or at an organization level. You can also create a set of common customizations in a parent organization and override them in individual child organizations. See the JasperReports Server Administrator Guide for details on the organization hierarchy and how it works with themes.

!!! note

    Customizations for dashboards created in JasperReports Server 6.0 and higher can be placed in `overrides_custom.css`.
