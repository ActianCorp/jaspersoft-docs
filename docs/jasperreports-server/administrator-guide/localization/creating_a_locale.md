---
title: Creating a Locale
description: "When you want to create other locales for JasperReports Server, translation is only one aspect of localization. Creating a locale includes these tasks:"
---

# Creating a Locale

When you want to create other locales for JasperReports Server, translation is only one aspect of localization. Creating a locale includes these tasks:

- Translating labels and messages

- Creating a Resource Bundle

- Setting Date and Datetime Formats

- Setting Data Format Masks

The tasks in this section require you to edit these files:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>File</p></th>
<th><p>Location</p></th>
<th><p>Purpose of Edits</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>*.properties</code> files</p></td>
<td><p><code>.../WEB-INF/bundles</code><br />
<code>&lt;js-install&gt;/buildomatic/conf_source/ie</code> <span><span>Pro</span> </span><span>/bundles</span></p></td>
<td><p>Translating labels and messages</p></td>
</tr>
<tr>
<td><p><code>jasperserver_config.properties</code></p></td>
<td><p><code>.../WEB-INF/bundles</code></p></td>
<td><p>Changing date formats</p></td>
</tr>
<tr>
<td><p><code>adhoc_masks</code></p></td>
<td><p><code>.../WEB-INF/bundles</code></p></td>
<td><p>Changing format masks</p></td>
</tr>
</tbody>
</table>

## About Properties Files

Resource bundles for JasperReports Server and Jaspersoft OLAP are Java properties files found in the `.../WEB-INF/bundles` directory. The properties files contain all the labels and messages used in JasperReports Server and Jaspersoft OLAP.

A bundle includes a default locale (for example, `jasperserver_messages.properties`), which is written in U.S. English. Then it consists of all the properties files with the same base name, but different locale (such as `jasperserver_messages_fr.properties`). Each file translates all of the strings of the default file into the language given by the locale. The Java programming language has rules for specifying locales and alternate locales and determining which locale in the bundle to use.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>Default Resource Bundles in JasperReports Server</p></th>
</tr>
<tr>
<th><p>File in <span>.../WEB-INF/bundles</span></p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>accessibility_messages.properties</code></p></td>
<td><p>Text spoken in accessibility software such as screen readers.</p></td>
</tr>
<tr>
<td><p><code>AdHocFiltersBundle.properties</code></p></td>
<td><p>Labels and messages for the Ad Hoc Filters panel.</p></td>
</tr>
<tr>
<td><p><code>adhoc_masks.properties</code></p></td>
<td><p>Masks (data formats) for values appearing in the Ad Hoc Editor.</p></td>
</tr>
<tr>
<td><p><code>adhoc_messages.properties</code></p></td>
<td><p>Labels and messages for the Ad Hoc Editor.</p></td>
</tr>
<tr>
<td><p><code>AttributeBundle.properties</code></p></td>
<td><p>Messages for attribute validation.</p></td>
</tr>
<tr>
<td><p><code>AttributeBundles.properties</code></p></td>
<td><p>Messages for attribute dialogs.</p></td>
</tr>
<tr>
<td><p><code>calendar.properties</code></p></td>
<td><p>Labels and messages used by the pop-up calendar dialog.</p></td>
</tr>
<tr>
<td><p><code>.properties</code></p></td>
<td><p>.</p></td>
</tr>
<tr>
<td><p><code>CommonBundle.properties</code></p></td>
<td><p>Bundle for tests.</p></td>
</tr>
<tr>
<td><p><code>createsldatasource_messages</code><br />
<code>.properties</code></p></td>
<td><p>Labels and messages for the Create Domain dialog.</p></td>
</tr>
<tr>
<td><p><code>domain_designer_messages</code><br />
<code>.properties</code></p></td>
<td><p>Labels and messages for the Domain Designer UI.</p></td>
</tr>
<tr>
<td><p><code>HomeBundle.properties</code></p></td>
<td><p>Labels for the home page.</p></td>
</tr>
<tr>
<td><p><code>image_descriptions_messages</code><br />
<code>.properties</code></p></td>
<td><p>Labels and messages for the AWS (Amazon Web Services) machine images.</p></td>
</tr>
<tr>
<td><p><code>jasperreports_highcharts_</code><br />
<code>messages.properties</code></p></td>
<td><p>Messages for charts in the report viewer.</p></td>
</tr>
<tr>
<td><p><code>jasperreports_messages</code><br />
<code>.properties</code></p></td>
<td><p>Labels and messages for the report viewer.</p></td>
</tr>
<tr>
<td><p><code>jasperserver_config.properties</code></p></td>
<td><p>Configuration properties for date formats and email templates.</p></td>
</tr>
<tr>
<td><p><code>jasperserver_messages.properties</code></p></td>
<td><p>Labels and messages used in the main JasperReports Server user interface.</p></td>
</tr>
<tr>
<td><p><code>jsexceptions_messages.properties</code></p></td>
<td><p>Messages used in errors and exceptions, both in the UI and in the log messages.</p></td>
</tr>
<tr>
<td><p><code>LicenseMessages.properties</code></p></td>
<td><p>Labels and messages used when validating licenses.</p></td>
</tr>
<tr>
<td><p><code>logger_descriptions.properties</code> <span><br />
<code>logger_descriptions_pro.properties</code> </span></p></td>
<td><p>Internal log messages.</p></td>
</tr>
<tr>
<td><p><code>pro_nav_messages.properties</code></p></td>
<td><p>Labels and messages for the menu bar and Home page.</p></td>
</tr>
<tr>
<td><p><code>querybuilder_messages.properties</code></p></td>
<td><p>Labels and messages for the Choose Data dialog (for creating a Domain Topic before using Ad Hoc Editor).</p></td>
</tr>
<tr>
<td><p><code>report_option_messages</code><br />
<code>.properties</code></p></td>
<td><p>Labels and messages for the report options dialog.</p></td>
</tr>
<tr>
<td><p><code>ScalableInputControlsBundle</code><br />
<code>.properties</code></p></td>
<td><p>Labels for lists of values in input controls.</p></td>
</tr>
<tr>
<td><p><code>scheduling_ws.properties</code></p></td>
<td><p>Validation messages for the report scheduler.</p></td>
</tr>
<tr>
<td><code>security.properties</code></td>
<td>Messages used by input validation.</td>
</tr>
<tr>
<td><p><code>semanticLayer.properties</code></p></td>
<td><p>Labels and messages for the Domain designer and Ad Hoc data policies.</p></td>
</tr>
<tr>
<td><code>ValidationBundle.properties</code></td>
<td>Messages for dashboard dialogs.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>Default Resource Bundles in Jaspersoft OLAP</p></th>
</tr>
<tr>
<th><p>File in <span>.../WEB-INF/bundles</span></p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>ja_mondrian.properties</code></p></td>
<td><p>Labels and messages in the OLAP settings UI.</p></td>
</tr>
<tr>
<td><p><code>ja-pro_messages.properties</code></p></td>
<td><p>Labels and messages in the commercial edition OLAP viewer.</p></td>
</tr>
<tr>
<td><p><code>mondrian_exception_messages</code><br />
<code>.properties</code></p></td>
<td><p>MDX validation error messages specific to the internal analysis engine.</p></td>
</tr>
</tbody>
</table>

The standalone import and export tools have their own bundles located outside of the web app. The following bundles are located in the WAR file distribution package, under the `buildomatic` folder.

<table>
<thead>
<tr>
<th colspan="2"><p>Default Resource Bundles for js-export.sh and js-import.sh</p></th>
</tr>
<tr>
<th><p>File in <span>buildomatic/conf_source/iePro/bundles</span></p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>ji-export-messages.properties</code></p></td>
<td><p>Labels and messages for <code>js-export --help</code>.</p></td>
</tr>
<tr>
<td><p><code>multi-tenancy-export-messages.properties</code></p></td>
<td><p>Labels and messages for export in commercial editions.</p></td>
</tr>
<tr>
<td><p><code>multi-tenancy-import-messages.properties</code></p></td>
<td><p>Labels and messages export in commercial editions.</p></td>
</tr>
<tr>
<td><p><code>jsexceptions_messages.properties</code></p></td>
<td><p>Messages used in errors and exceptions, both in the UI and in the log messages.</p></td>
</tr>
</tbody>
</table>

## Creating a Resource Bundle

Create a resource bundle by making a copy of each \*.properties file, using the following syntax for the copy's file name:

``` xml
<default_file_name>_<locale>.properties
```

where

`<default_file_name>` is the name of the default version of the properties file, and

`<locale>` is a Java-compliant locale identifier.

For example, consider the core JasperReports Server resource bundle. For various locales, it might be named as follows:

| Language              | File Name                                |
|-----------------------|------------------------------------------|
| Default (English)     | `jasperserver_messages.properties`       |
| French                | `jasperserver_messages_fr.properties`    |
| French in Switzerland | `jasperserver_messages_fr_CH.properties` |

For a list of Java-compliant locales, please refer to the Java documentation.

!!! note

    The resource bundles described in this document consist of locale-specific Java properties files. Java properties files use the [ISO-8859-1](http://en.wikipedia.org/wiki/ISO/IEC_8859-1) (Latin-1) encoding that is the same as ASCII for all English non-accented characters. For international characters that are not in ISO-8859-1, use Unicode escape sequences (for example `\u00e9` is é).

To create a new JasperReports Server resource bundle

1.  Copy each of the properties files (keeping them in the same directory as the originals) and rename them according to your locale.
2.  Translate each `*.properties` file's labels and messages into the new language.<br>
    Some of the strings in the properties files are date formats and format masks that may need to be edited for the new locale. For more information, refer to Setting Date and Datetime Formats.
3.  Save the files.
4.  If the new locale requires specific character encoding or fonts, ensure that JasperReports Server and the third party software it relies on are configured to support them. For more information, refer to [Configuring JasperReports Server for Multibyte Fonts](multi-byte_fonts.md).

!!! note

    The new locale is not available in JasperReports Server until you follow the steps described in [Specifying Additional Locales](offering_a_locale.md).

## Setting Date and Datetime Formats

Each locale may have its own rules for displaying dates and datetime values. System date and datetime formatting is controlled by four patterns that are specified in the `jasperserver_config_<locale>.properties` file associated with a particular locale.

For example in the English resource bundle, the four entries are:

``` properties
date.format=dd-MM-yyyy
datetime.format=dd-MM-yyyy HH:mm
calendar.date.format=%d-%m-%Y
calendar.datetime.format=%d-%m-%Y %H:%M
```

The first two keys are used to parse and format dates and datetime values using an internal `java.util.DateFormat` object across the whole application. These patterns should be non-localized date patterns, in accordance with the Java Development Kit (JDK) syntax.

The other two keys are used by the calendar control, which formats the user-selected date and datetime values in accordance with its own pattern syntax.

To change the system date and datetime formatting for a new locale, edit the strings specified by these keys.

For some locales, you can use a different (non-default) Date/Time format. However, this format is not applied for Input Controls, because the date format for Input Controls is a constant and is set to ISO date/time format (your date and your calendar settings are ignored for Input Controls).

If your existing configurations for Input Controls and your locales are working fine, then no changes are needed and JasperReports Server will proceed sending or getting date/datetime in ISO format as before.

If you prefer to not have Input Controls operating only in ISO date format (for example, when Input Controls are used in Visualize.js implementation), you can enable the new provider added in this release and re-save ad-hoc views/reports if needed.

To use the date/format from `jasperserver_config.properties` for Input Controls, apart from setting formats found in the `config.properties` file, perform the following steps:

1.  Update the `jasperserver_config.properties` file.

2.  Update the `/WEB-INF/js.spring.properties` file:

    1.  Comment out `` `bean.calendarFormatProvider=isoCalendarFormatProvider` `` line.

    - Uncomment `` `bean.calendarFormatProvider=messagesCalendarFormatProvider` `` line.

## Setting Data Format Masks

Each locale may have its own format masks that determine how numbers appear in the Ad Hoc Editor. To make the data format masks vary by locale, you must create an `adhoc_masks` file for the new locale. To do so, copy the file `adhoc_masks.properties` to a new name that specifies the new locale and change the masks defined in the new file. For example, the French file would be named `adhoc_masks_fr.properties`.

!!! note

    The data format masks described in this section are used in the Domains and in the Ad Hoc Editor; they appear in Ad Hoc views as well as JRXML reports based on Domains. They're not applicable to Jaspersoft OLAP.

Customize the available data format masks for dates, integers, and decimals by editing the existing masking entries or adding new ones. The default entries are given in the following table:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Data Format Mask Properties</p></th>
<th><p>Appearance in en_US Locale</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="language-properties highlight"><pre><code><span class="na">ADH_100_MASK_date_0</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">short,hide</span>
<span class="na">ADH_100_MASK_date_1</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">long,hide</span>
<span class="na">ADH_100_MASK_date_2</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">short,medium</span>
<span class="na">ADH_100_MASK_date_3</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">medium,medium</span>

<span class="na">ADH_100_MASK_int_0</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">#,##0</span>
<span class="na">ADH_100_MASK_int_1</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">0</span>
<span class="na">ADH_100_MASK_int_2</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">$#,##0;($#,##0)</span>
<span class="na">ADH_100_MASK_int_3</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">#,##0;(#,##0)</span>

<span class="na">ADH_100_MASK_dec_0</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">#,##0.00</span>
<span class="na">ADH_100_MASK_dec_1</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">0</span>
<span class="na">ADH_100_MASK_dec_2</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">$#,##0.00;($#,##0.00)</span>
<span class="na">ADH_100_MASK_dec_3</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">$#,##0;($#,##0)</span></code></pre></div></td>
<td><p>3/31/09<br />
Mar 31, 2009<br />
March 31, 2009<br />
Mar 31, 2009 23:59:59</p>
<p>-1,234<br />
-1234<br />
($1,234)<br />
(1234)</p>
<p>-1,234.56<br />
-1234<br />
($1,234.56)<br />
($1,234)</p></td>
</tr>
</tbody>
</table>

The data format masks for each type are numbered consecutively from zero; create new masks by adding new entries. The keys of the new entries must follow the convention established in the default entries. For example, a new decimal data format mask might have this ID:

``` text
ADH_100_MASK_dec_4
```

Date format masks are implemented using `java.text.SimpleDateFormat` and JasperReports extensions that provide access to predefined localized data format masks. New datetime masks must be specified in one of the following formats:

- A style for the date part of the value and a style for the time part (separated by comma) or a single style for both parts. A style is one of Short, Medium, Long, Full, Default (which correspond to `java.text.DateFormat` styles) and Hide.
- A pattern that can be supplied to `java.text.SimpleDateFormat`. In this case, internationalization support is limited.

Both integer and decimal data format masks are implemented with `java.text.DecimalFormat`, which localizes characters in the format specification. For example, consider the case of the digit grouping symbol (thousands separator): in French, it is a space; in U.S. English, it is a comma. `DecimalFormat` handles both cases: if the number pattern \#,##0 is used, the number 6000 appears as 6 000 in the French locale and as 6,000 in the U.S. English locale.

For more information about Java's handling of decimal and date format masks, see:

- <http://download.oracle.com/javase/6/docs/api/java/text/DecimalFormat.html>
- <http://download.oracle.com/javase/6/docs/api/java/text/DateFormat.html>

!!! note

    By default, monetary values in Ad Hoc views are masked as USD (United States Dollars). Depending on your data, you may need to support a different currency, support more than one currency, or support currency conversion. These are three very different cases:

    - Supporting a different currency than USD involves changing the monetary masks to use the correct symbol for your currency (for example, replace the `$` symbol in the `ADH_100_MASK_dec_2 and ADH_100_MASK_dec_3` masks). However, changing this symbol does not actually convert currencies in your reports.
    - Supporting other currencies in addition to USD involves adding new masks. However, adding data formats does not actually convert currencies in your reports.
    - Supporting currency conversion is more complicated; you must consider such issues as fluctuations in conversion rates. Oftentimes, a third-party service can be used to perform currency conversion
