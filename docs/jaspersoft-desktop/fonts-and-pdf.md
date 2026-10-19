# Fonts and PDF

A report names its fonts; the engine has to find them wherever the report runs: in the preview,
when an application fills it, on JasperReports Server. A font that is only installed on your
computer is found here, and missing elsewhere. This page is about making a report look the same
everywhere, and above all in PDF.

## The fonts a report can use

The **Name** of a text's font, on the **Text Field** or **Static Text** tab of **Properties**, lists:

- the fonts of the **font extensions** the report can use: the fonts JasperReports includes
  (**DejaVu Sans**, **DejaVu Serif**, **DejaVu Sans Mono**) and those in the libraries of the
  workspace (see [Workspace settings](workspace-settings.md));
- the fonts installed on this computer.

The designer and the preview draw the text with the font the engine uses, so what you see is what
the PDF has, line breaks included.

## Why a font extension

A font extension is a `.jar` (or `.zip`) holding font files and a description of them. With it:

- the font travels with the report: an application, a server, a colleague's computer get it from
  the extension, not from the fonts their system happens to have;
- the PDF **embeds** it, so the document looks the same on any reader, and characters of any
  language print;
- the engine measures the text with the same font on every machine, so a text that fits here fits
  there.

A font of the computer has none of this: the PDF names it without embedding it, a reader that does
not have it shows another, and a server without it refuses the report, with an error such as
`Font "Open Sans" is not available to the JVM`.

**Use the DejaVu fonts, or a font extension, for every report that leaves your computer.**

## Making a font extension

A font extension is two small files and the fonts, in a `.zip`:

```
jasperreports_extension.properties
fonts/fonts.xml
fonts/OpenSans-Regular.ttf
fonts/OpenSans-Bold.ttf
fonts/OpenSans-Italic.ttf
fonts/OpenSans-BoldItalic.ttf
```

`jasperreports_extension.properties` says where the description is:

```properties
net.sf.jasperreports.extension.registry.factory.fonts=net.sf.jasperreports.engine.fonts.SimpleFontExtensionsRegistryFactory
net.sf.jasperreports.extension.simple.font.families.myfonts=fonts/fonts.xml
```

`fonts/fonts.xml` describes each family: its files, and that the PDF is to embed it.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<fontFamilies>
  <fontFamily name="Open Sans">
    <normal><![CDATA[fonts/OpenSans-Regular.ttf]]></normal>
    <bold><![CDATA[fonts/OpenSans-Bold.ttf]]></bold>
    <italic><![CDATA[fonts/OpenSans-Italic.ttf]]></italic>
    <boldItalic><![CDATA[fonts/OpenSans-BoldItalic.ttf]]></boldItalic>
    <pdfEncoding><![CDATA[Identity-H]]></pdfEncoding>
    <pdfEmbedded><![CDATA[true]]></pdfEmbedded>
    <exportFonts>
      <export key="net.sf.jasperreports.html"><![CDATA['Open Sans', Arial, sans-serif]]></export>
    </exportFonts>
  </fontFamily>
</fontFamilies>
```

- The **name** of the family is what reports write in their **Name**.
- **Identity-H** lets the PDF print the characters of any language.
- **exportFonts** says what an HTML export asks the browser for.

Zip the files (the `.properties` at the top of the archive), add the `.zip` to the workspace in
**Settings › Libraries**, and the font is in the list of every report of the workspace.

Check the license of a font before you put it in an extension you share: most fonts allow it,
not all.

## Where else the extension goes

- **An application** puts the `.jar` or `.zip` on its class path, with JasperReports.
- **JasperReports Server** needs it too: its administrator adds it to the server (in the
  `WEB-INF/lib` of the web application), and restarts it. Until then, a report that names the font
  fails there, or prints with another font.

## The PDF properties of a text

The **Text Field** and **Static Text** tabs also have **PDF Font Name**, **PDF Encoding** and **PDF
Embedded**. They are the way of old versions of JasperReports, and they do not travel with the
report: leave them empty and use a font extension.

## Characters that print as squares or not at all

The font has no drawing for them: a font made for Latin letters has none for Chinese or Arabic, for
example. Use a font that has them (DejaVu Sans covers many alphabets; the Noto fonts cover
almost all), in a font extension with **Identity-H**.
