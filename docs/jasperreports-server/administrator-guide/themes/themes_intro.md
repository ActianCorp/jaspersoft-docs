---
title: Themes
description: "The features in this section may be restricted by your JasperReports Server software license. If you don't see some of the options described, your current license likely prohibits their use. Contact..."
---

# Themes

!!! info "Important"

    The features in this section may be restricted by your JasperReports Server software license. If you don't see some of the options described, your current license likely prohibits their use. Contact us to learn about your licensed features or to discuss upgrading.

A theme is the set of all CSS (Cascading Style Sheets) and associated images that define the appearance of the user interface. Themes are stored in the Themes folder in the repository, with special menus on theme folders for activating, uploading, and downloading a theme. You can store any number of themes in the repository and switch among them, to change the UI's appearance.

For multi-organization deployments, administrators can set the theme individually for each organization, or rely on theme inheritance to use the same theme everywhere without needing to set it explicitly. Theme inheritance supports a mix of explicit and inherited settings, so that you can override any setting or image in a local organization, but inherit the rest of the theme from the parent or system-wide theme.

!!! warning

    In some cases, the set of files in the default theme changes between versions. Custom themes developed in for earlier version may need to be updated to work with theupdated theme. For more information, see the JasperReports Server Upgrade Guide

This chapter contains the following sections:

- [Introduction to Themes](introduction_to_themes.md)

- [How Themes Work](how_themes_work.md)

- [Administering Themes](administering_themes.md)

- [Creating Themes](creating_themes.md)

- [Working With CSS Files](working_with_css_files.md)
