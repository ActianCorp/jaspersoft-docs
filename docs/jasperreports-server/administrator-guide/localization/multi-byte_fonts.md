---
title: Configuring JasperReports Server for Multibyte Fonts
description: "Although translation packs for Chinese and Japanese ship with JasperReports Server, the fonts that it uses by default do not support those languages. Therefore, if your organization requires those..."
---

# Configuring JasperReports Server for Multibyte Fonts

Although translation packs for Chinese and Japanese ship with JasperReports Server, the fonts that it uses by default do not support those languages. Therefore, if your organization requires those fonts, you need to configure JasperReports Server for them.

While the fonts JasperReports Server uses are generally dictated by the JRXML files that define your reports, some font configuration is required for special circumstances. For example, you can configure Jaspersoft OLAP to offer different options in the **Chart Default Font** field in the Chart Options dialog. But note that, in order to use a font, the font must be available to the host's operating system. This section describes steps you may need to take, depending on the functionality you use and the locales you support.

The tasks in this section require you to edit these files:

| File Name | Location | Purpose of Edits |
|----|----|----|
| `jpivot_internal_messages.properties` | `.../WEB-INF/internal` | Specifying chart fonts for Jaspersoft OLAP Community |
| `Ja_pro_internal_messages.properties` | `.../WEB-INF/internal` | Specifying chart fonts for Jaspersoft OLAP Professional and Enterprise |
| `userConfig.xml` | `.../WEB-INF/jpivot/print` | Embedding fonts in PDF |

## Enabling East Asian Fonts

The default configuration of the Java Runtime Environment (JRE) does not support East Asian fonts. If your locale requires such a font, you need to configure your users' computers for the fonts and update their JRE.

To configure a Microsoft Windows computer (XP and later) for East Asian fonts

!!! note

    Details of this procedure vary, depending on your version of Windows.

1.  In the **Control Panel**, click **Region and Language**.
2.  In the **Region and Language** dialog, select the **Keyboards and Languages** tab.
3.  On the tab, install the language(s) that you need.
4.  If necessary, install the related keyboard modifications.
5.  Close the control panel.
6.  Locate the `fontconfig.properties.src` file in the `C:\Program Files\<JRE_directory>\lib` folder.
7.  In the file, locate the following line:<br>
    `sequence.allfonts=alphabetic/default,dingbats,symbol`
8.  Change the line to include the East Asian fonts that you need, such as the following:<br>
    `sequence.allfonts=alphabetic/default,dingbats,symbol,korean,japanese,chinese-ms936,chinese-ms950`
9.  At the end of the file, check to be sure that the fonts you selected are listed, as in the following:<br>
    `filename.Gulim=gulim.TTC`. If the fonts are not listed, add them.
10. Save and close the file.
11. Rename the file to `fontconfig.properties` in the file system.

## Configuring Ad Hoc Charts for Asian Fonts

The default font for the legend of an Ad Hoc chart does not support some Asian characters, such as Japanese kana glyphs. Default fonts for Ad Hoc reports are defined in the following file:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Changing Ad Hoc Chart Legend Fonts</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/adhoc/themes/actual_size.&lt;ver&gt;.jrxml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>style name=</code><br />
<code>    "ChartLegend"</code><br />
<code>fontName=</code></p></td>
<td><p><code>"fontName="</code><br />
&lt;default&gt;<br />
<br />
</p>
<p><code>"SansSerif"</code></p></td>
<td><p>The default value, DejaVu Sans, does not include kana glyphs, and thus the legend contains blank symbols.</p>
<p>If the server machine has system Japanese fonts available, setting the value to SansSerif should work in most Java font configurations.</p></td>
</tr>
</tbody>
</table>

!!! note

    After making changes to the `actual_size.<ver>.jrxml` file and importing the modified file into JasperReports Server, you must create new Ad Hoc reports for charts that contain Asian characters using the modified report template.

If Japanese fonts are not installed in the server machine, you can install them and create a custom report template to support them in the following manner:

1.  Package a Japanese font as a font extension JAR.
2.  Add the new JAR to the `.../WEB-INF/lib` folder of the JasperReports Server WAR file.
3.  Log into JasperReports Server as an administrator and export the Actual Size template from the `Public > Templates` folder in the repository. The procedures for exporting and importing a template are described in the *JasperReports Server Ultimate Guide*.
4.  In the exported file folder, find `resources/public/templates/actual_size.<ver>.jrxml.data` and rename the file to remove the `.data` extension.
5.  Open `actual_size.<ver>.jrxml` to edit it.
6.  Locate the following line:<br>
    `style name="ChartLegend" ... fontName="DejaVu Sans"`<br>
    Modify the line as follows:<br>
    `fontName="SansSerif"`
7.  In JasperReports Server, browse to the **Public &gt; Templates** folder in the repository.
8.  Right-click the **Templates** folder and select **Add Resource &gt; File &gt; JRXML** from the context menu to import the edited `actual_size.<ver>.jrxml` file as a new custom report template.

You can use the new custom report template for charts that contain Asian characters.

## Embedding Fonts in PDF Output for OLAP Views

!!! note

    By default, JasperReports Server can create PDF (Portable Document Format) files with many different fonts. However, if you experience font problems in the PDF output, you may need to take the steps described in this section to make the fonts available to JasperReports Server's XSL Formatting Object (XSL-FO) processor.

    You must have distribution rights to a font in order to embed it in a PDF file.

When users export OLAP views in PDF format, JasperReports Server generates the PDF output using Apache FOP (Formatting Objects Processor). In order for FOP to render fonts properly, you must install the font itself (for example, a TTF file) on the server host, create a font metrics file (using Apache's `org.apache.fop.fonts.apps.TTFReader` utility), and update the `userConfig.xml` file to associate the font with its metrics. For more information, refer to the [Apache FOP documentation](https://xmlgraphics.apache.org/fop/2.2/embedding.html).

You can embed any Unicode font using this procedure, though larger font files may have significantly larger memory footprints. To keep memory requirements small, we recommend you use the smallest font file you can, such as SimHei to support Chinese, Japanese, and Korean.
