---
title: Upgrading With UI Customizations
description: "One consideration when customizing the user interface is how those customizations can be maintained during upgrades to JasperReports Server. As explained in 1.1, “Customizing the UI With Web App..."
---

# Upgrading With UI Customizations

One consideration when customizing the user interface is how those customizations can be maintained during upgrades to JasperReports Server. As explained in [1.1, “Customizing the UI With Web App Files,” on page 1](customizing-ui-with-web-app-files.md), where and how you make changes affects how easy it is to maintain them.

- Changes to the CSS files and images of a theme are stored in the repository, which is preserved through updates. However, the CSS in the new version may refer to different IDs and classes, or to image files with different names. Also, the overrides in an old theme may not have the desired appearance when applied to a new theme.

- Commercial versions of JasperReports Server on Tomcat have an overlay upgrade procedure. Overlay upgrade allows you to pause the upgrade after the new files have been installed and manually migrate your customizations. Be careful to copy only your modifications from the saved file into the new server files. In some cases, the existing modifications no longer apply to the files or mechanisms in the new server. See the JasperReports Server Upgrade Guide for more information.

- Because the server is distributed as a WAR file, changes to files in an installed version or an existing WAR file are likely to be overwritten during regular upgrade. Sometimes, you can save a copy of the modified files and redo the changes in the new installation or WAR file. In this case, you must be careful to copy only your modifications from the saved file into the new server files. In other cases, the existing modifications no longer apply to the files or mechanisms in the new server.

- Keeping your changes in a copy of the source code lets you take advantage of source control to update and merge your changes into the code for the new server. However, in the case of major releases UI mechanisms sometimes change, and the files with your modifications may no longer exist or be relevant in the new code.

!!! warning

    In general, new releases of the server attempt to provide backward compatibility of the mechanisms described in this chapter, especially minor (“dot”) releases. However, in order to improve the UI and provide new features, Jaspersoft cannot guarantee that all customizations still apply, or even that they will use the same mechanism, especially in major releases.
