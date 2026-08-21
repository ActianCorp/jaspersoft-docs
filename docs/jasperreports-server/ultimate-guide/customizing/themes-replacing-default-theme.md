---
title: Replacing the Default Theme
description: "In general, we recommend creating new themes with CSS and image files that override those of the provided default theme. However, there may be cases where the default theme must be replaced."
---

# Replacing the Default Theme

In general, we recommend creating new themes with CSS and image files that override those of the provided default theme. However, there may be cases where the default theme must be replaced.

!!! note

    The `<js-webapp>/themes` folder contains a copy of the default theme and other sample themes. These files are provided as examples for copying and creating new themes. Even though these theme files appear in the source code and in the deployed web application, they are never used to render the UI.

    Although it's possible to configure the server to load the theme from files, this disables the dynamic theme mechanism and has other effects. We do not recommend such a configuration.

Like all themes, the default theme is stored in the repository, in the server’s private database. The theme’s propagation and inheritance will work only if the theme files exist in the repository before the server is started. You can achieve this two ways:

- Use the import utility to import your theme as the default root theme while the server is stopped (the repository database must be running). In commercial editions that have the organizations architecture, when the server restarts, it propagates your new default theme to all other theme folders.

- Insert your default theme during installation. During installation, there are scripts or manual commands that create the repository database and populate it with the initial contents by performing an import before the server starts. Those initial contents include the default root theme. If you're proficient with buildomatic commands and database initialization, you can locate the files used to populate the repository and insert your own default theme.

In both cases, you must create a valid repository catalog containing your custom theme in the `/Themes/default` folder of the catalog. Your catalog must contain the valid XML description for each of the files, for example by exporting a copy of your theme and renaming contents of the exported catalog. The details of changing the default theme through either of these methods is beyond the scope of this guide.

!!! warning

    Creating a default theme is difficult and prone to error:

    - Your version of the default theme must be a complete theme that contains all files named in `<js-webapp>/WEB-INF/decorators/decoratorCommonImports.jsp`.

    - Your default theme must provide rules for rendering all the elements used by the UI, otherwise pages may not render properly.

    - Your default theme cannot use the `overrides_custom.css` file, because themes that override your default theme may include this file. By convention, this file is reserved for non-default themes to override the default theme.

    - During an upgrade of the server, your default theme may be overwritten or the new version may not be backwardly compatible with your theme. See [Upgrading With UI Customizations](ui-customizations-and-upgrade.md).
