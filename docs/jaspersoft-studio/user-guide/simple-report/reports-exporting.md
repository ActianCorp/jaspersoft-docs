---
title: Exporting Reports with Jaspersoft Studio
description: "In addition to generating and viewing reports, Jaspersoft Studio allows you to export reports into many formats, including PDF, XLSX, HTML, and others."
---

# Exporting Reports with Jaspersoft Studio

In addition to generating and viewing reports, Jaspersoft Studio allows you to export reports into many formats, including PDF, XLSX, HTML, and others.

## Compiling the Report

When you select the Preview tab in the designer bottom bar, Jaspersoft Studio performs a set of operations to create the final report. The first operation compiles the JRXML source file in a Jasper file. This first step can fail if the elements are not correctly positioned (for example, if an element is placed outside of a band), or if an expression in the report has errors and cannot be compiled.

If the compilation runs successfully, the produced Jasper file is loaded and filled using the active connection or data source. This second operation can also lead to errors. This can happen if the referenced database is not active, an invalid query has been provided, or a null field produced an error in an expression during the filling process. If all operations complete without error, the report is displayed in the integrated viewer. Errors are shown in the Report State window, after clicking the Errors button.

If errors occur during the compilation, the tab focus changes from Preview to Design.

## Preview and Exporting

If the compilation completes and there are no errors in the file, the preview is shown. From there you can browse the generated report and change its visualization, change the data source, or export the report. Note that after changing the data source the report is recompiled automatically. You can also change the preview format as well as save the report in different formats.

When you set a preview format, the report is automatically regenerated in the chosen format, and the corresponding viewer application is opened.

!!! note

    In some cases, bugs in the export format may result in issues in the final output. For example, some versions of Microsoft Word incorrectly render borders on a table element exported to DOCX (the left top and bottom borders are missing). You may be able to find a workaround based on the output format. For example, for the Microsoft Word bug, you might try the following:

    1.  In Jaspersoft Studio, create a style named `Table_Padding`, with 1-pixel left and right padding.
    2.  Apply this style to each table element in the report.

## Choosing Report Templates for PDF

If you are exporting your report to PDF, choose a report template based on the size of the output.

- For most PDF exports, you can use Actual Size, which supports a maximum size of 14,400 px by 14,400 px.

- For reports with an output height exceeding 14,400 px, use a paginated report template that is wide enough for your report. For example, if you have a long report with width less than 842 px, you can use the paginated A4 Landscape theme. A report designer can create additional custom templates in Jaspersoft Studio.

- Reports with output width exceeding 14,400 px are truncated in PDF.

## Encrypting Report Output Format

You can encrypt the report output format (.docx, xls, and .pptx) by adding the following properties into the JRXML file. For example:

- `<property name="net.sf.jasperreports.export.docx.encryption.password" value="ABC"/>` - Used for encrypting the Microsoft word files.

- `<property name="net.sf.jasperreports.export.xls.encryption.password" value="pqr"/>` - Used for encrypting the Excel files.

- `<property name="net.sf.jasperreports.export.pptx.encryption.password" value="123"/>` - Used for encrypting the PowerPoint presentation files.
