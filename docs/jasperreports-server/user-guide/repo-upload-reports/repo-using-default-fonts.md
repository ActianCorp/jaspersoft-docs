---
title: Using Default Fonts in JasperReports Server
description: "By default, the server uses three fonts for reports:"
---

# Using Default Fonts in JasperReports Server

By default, the server uses three fonts for reports:

- DejaVu Sans
- DejaVu Serif
- DejaVu Sans Mono

Using the DejaVu fonts included, the server ensures availability of fonts in all environments. The PDF is pixel-perfected every time.

The DejaVu fonts replace the Java logical fonts used in previous versions of the server:

- SansSerif

- Serif

- Monospaced

  <div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>SansSerif, Serif, Monospaced can still be used, but are deprecated because these Java logical fonts map to different TTF files in different environments, and run the risk of text being cut when exported to PDF due to font metric mismatches. Also, these Java logical fonts are not recognized by some browsers, resulting in font substitutions. For example, Firefox in a Windows environment renders the SansSerif logical font as Serif.</p>
  </div>

When using the DejaVu fonts coming from font extensions, you do not need to set any other font attributes (such as the `pdfXXX` attributes) in the JRXML or specify font mapping. The font extension file that makes these fonts available sets font attributes and mapping.

For more information about DejaVu, refer to its SourceForge project at:

http://dejavu-fonts.org/wiki/index.php?title=Main_Page.

!!! note

    <span id="adding_reports_3864650317_39411"></span><span id="adding_reports_3864650317_94897"></span><span id="adding_reports_3864650317_78194"></span>When you upload a TrueType font to the repository, the file name must include the correct extension (.TTF).
