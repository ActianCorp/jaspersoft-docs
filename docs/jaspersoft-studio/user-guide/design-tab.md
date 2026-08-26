---
title: The Design Tab
description: "You design a report using the Design tab, which is divided into different horizontal portions, named bands, where you can place report elements. When the report design is combined with the data to..."
---

# The Design Tab

You design a report using the Design tab, which is divided into different horizontal portions, named bands, where you can place report elements. When the report design is combined with the data to generate the print, each band is printed multiple times based on its function (and according to the rules that the report designer has set). For instance, the page header is repeated at the beginning of every page, while the detail band is repeated for each record.

Jaspersoft Studio provides a graphical interface for creating JRXML files. The layout is visual, so you can ignore the underlying structure of the JRXML. You can specify the precise page locations of different types of text and data, such as title, footers, detailed records, groups, and summary information. Some portions of a page defined in this way are reused, others stretch to fit the content, and so on. Additional tools let you add charts and subreports, set up an optional query to retrieve data out of a data source, and more.

# Understanding Bands

The Design tab is divided into nine predefined bands to which new groups are added. In addition, Jaspersoft Studio manages a heading band (group header) and a recapitulation band (group footer) for every group.

A band is as wide as the page width (right and left margins excluded). However, its height, even if it is established during the design phase, can vary during print creation according to the contained elements; it can “lengthen” toward the bottom of a page in an arbitrary way. This typically occurs when bands contain subreports or text fields that have to adapt to the content vertically. Generally, the height specified by the user should be considered “the minimal height” of the band. Not all bands can be stretched dynamically according to content. In particular the column footer, page footer, and last page footer bands are statically sized.

The sum of all band heights (except for the background) must be less than or equal to the page height minus the top and bottom margins.

## Band Types

The following table contains brief descriptions of the available bands:

| Band Name | Description |
|----|----|
| Title | The title band is the first visible band. It is created only once and can be printed on a separate page. It is not possible during design to exceed the report page height (top and bottom margins are included). If the title is printed on a separate page, this band height is not included in the calculation of the total sum of all band heights. |
| Page Header | The page header band allows you to define a page header. The height specified during the design phase usually does not change during the creation process, except for the insertion of vertically resizable components such as text fields. The page header appears on all printed pages in the position defined during the design phase. Title and summary bands do not include the page header when printed on a separate page. |
| Column Header | The column header band is printed at the beginning of each detail column. Usually labels containing the column names of a tabular report are inserted in this band. |
| Group Header | A report can contains zero or more group bands that permit the collection of detailed records in real groups. A group header is always accompanied by a group footer (both can be independently visible or not). Different properties are associated with a group. They determine its behavior from the graphic point of view. It is possible to force a group header on a new page or in a new column and to print this band on all pages if the bands below it overflow the single page (as a page header, but at group level). It is possible to fix a minimum height required to print a group header: if it exceeds this height, the group header band is printed on a new page (please note that a value too large for this property can create an infinite loop during printing). |
| Group Footer | The group footer band completes a group. Usually it contains fields to view subtotals or separation graphic elements, such as lines. |
| Column Footer | The column footer band appears on at the end of every column. Its dimensions are not resizable at run time (not even if it contains resizable elements such as subreports or text fields with a variable number of text lines). |
| Page Footer | The page footer band appears on every page where there is a page header. Like the column footer, it is not resizable at run time. |
| Last Page Footer | If you want to make the last page footer different from the other footers, it is possible to use the special last page footer band. If the band height is 0, it is completely ignored, and the layout established for the common page is used for the last page. |
| Summary | The summary band allows you to insert fields containing total calculations, means, or any other information you want to include at the end of the report. |
| Background | The background enables you to create watermarks and similar effects, such as a frame around the whole page. It can have a maximum height equal to the page height. |

# Specifying Report Properties

To view or edit report properties, select the report root node in the Outline view. The report properties are shown in the Properties view.

To change the page dimensions of a report, click the Report tab in the Properties view for the report, then click **Edit Page Format** to open the Page Format dialog. Here you can edit the width, height, units, orientation, and margins of the report.

The unit of measurement used by Jaspersoft Studio and JasperReports is the pixel. However, it is possible to specify report dimension using other units of measurement, such as centimeters, millimeters, or inches. Note that because the dimensions management is based on pixels, some rough adjustments can take place when viewing the same data using different units of measurement. The following table shows standard page sizes and their dimensions in pixels.

| Page Type   | Dimensions in Pixels |
|-------------|----------------------|
| Letter      | 612x792              |
| Note        | 540x720              |
| Legal       | 612x1008             |
| A0          | 2380x3368            |
| A1          | 1684x3368            |
| A2          | 1190x1684            |
| A3          | 842x1190             |
| A4          | 595x842              |
| A5          | 421x595              |
| A6          | 297x421              |
| A7          | 210x297              |
| A8          | 148x210              |
| A9          | 105X148              |
| A10         | 74X105               |
| B0          | 2836x4008            |
| B1          | 2004x2836            |
| B2          | 1418x2004            |
| B3          | 1002x1418            |
| B4          | 709x1002             |
| B5          | 501x709              |
| ARCH_E      | 2592x3456            |
| ARCH_D      | 1728x2593            |
| ARCH_C      | 1296x1728            |
| ARCH_B      | 864x1296             |
| ARCH_A      | 648x864              |
| FLSA        | 612x936              |
| FLSE        | 612x936              |
| HALFLETTER  | 396x612              |
| 11X17       | 792x1224             |
| LEDGER      | 1224x792             |

By modifying width and height, it is possible to create a report of whatever size you like. Although Jaspersoft enables you to create pixel-perfect reports, the page orientation options, Landscape or Portrait, are there because they are used by certain report exporters. The page margin dimensions are set by means of the four options on the **Page Margin** tab.

## Columns

Pages, one or more of which make up a report, present bands that are independent from the data (such as the title or the page footers) and other bands that are printed only if there are one or more data records to print (such as the group headers and the detail band). These last sections can be divided into vertical columns to take advantage of the available space on the page. A column does not concern the record field, but it does concern the detail band. This means that if you have a record with 10 fields and you desire a table view, 10 columns are not needed. However, the element must be placed correctly to have a table effect. Ten columns are returned when long record lists (that are horizontally very narrow) are printed.

Next, let us set up columns in a report as an example. Create a report from **File &gt; New &gt; Jasper Report**. Choose the **BlankA4** template and name it `ColumnExample`. Use **Sample DB - Database JDBC Connection** for the data adapter, with the following SQL query: `select * from orders`. Fields from the database are discovered. Double-click `SHIPNAME` to add it to the report field and click **Next** twice. Finally, click **Finish**.

From the outline view, drag the `SHIPNAME` field in the report in the detail band, resize the detail band, and remove the unused bands. Go to the Preview tab to see the compiled report.

By default the number of columns is 1, and its width is equal to the entire page, except the margins. The space between columns is zero by default. Most of the page is unused. If multiple columns are used, this report would look better. On the Page Format dialog set the number of columns to two and compile the report to see the changes.

Jaspersoft Studio automatically calculates the maximum column width according to the margins and the page width. If you want to increase the space between the columns, increase the value of the **Space** field.

The restricted area is used to mark every column after the first, to show that all the elements should be placed in the first column. The other columns are replicated automatically during compilation. If you want you can also put elements in the other columns, but in most cases you need only the first. It is not recommended that you use parts of the report as margins and columns after the first, if they have to be considered as though they were a continuation of the first.

Multiple columns are commonly used for print-outs of very long lists (for example, a phone directory). It is important to remember that when you have more than one column, the width of the detail band and of linked bands is reduced to the width of the columns.

The sum of the margins, column widths, and space between columns has to be less than or equal to the page width. If this condition is not met, the compilation results in an error.

## Advanced Options

From the **Properties** view of the report, there are many other options for the report configuration. Select the report root node from the outline view, and in the **Properties** view you see:

-   **Report Name**: It is a logical name, independent from the source file's name, and is used only by the JasperReports library (for example, to name the produced Java file when a report is compiled).

-   **Title on a new page**: This option specifies that the title band is to be printed on a new page, which forces a page break at the end of the title band. In the first page only, the title band is printed. However, this page is still included in the total page count.

-   **Summary on a new page**: This option is similar to **Title on a new page** except that the summary band is printed as the last page. If you need to print this band on a new page, the new page only contains the summary band.

-   **Summary with page header and footer**: This option specifies if the summary band is to be accompanied by the page header and the page footer.

-   **Float Column Footer**: This option forces the printing of the column footer band immediately after the last detail band (or group footer) rather than the end of the column. This option is used, for example, when you want to create tables using the report elements.

-   **When no data type**: When an empty data is supplied as the print number (or the SQL associated with the report returns no records), an empty file is created (or a stream of zero bytes is returned). This default behavior can be modified by specifying what to do in the case of absence of data. The possible values for this field are:

-   **No Pages**: This is the default value. The final result is an empty buffer.

    -   **Blank Page**: This returns an empty page.
    -   **All Sections No Detail**: This returns a page containing all bands except for the detail band.

-   **Ignore Pagination**: This option specifies whether to ignore pagination for the report. When the `isIgnorePagination` property is set to true, the report-filling engine ignores the page break-related settings inside the report template and generate the document on a single, very long page.

-   **Create Bookmarks**: This option creates bookmarks for the defined hyperlink references.
