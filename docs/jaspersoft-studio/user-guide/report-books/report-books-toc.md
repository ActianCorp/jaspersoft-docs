---
title: Configuring the Table of Contents
description: Your report book is organized and the reports are populated with data. Now you can configure your Table of Contents so your users can find the information they need.
---

# Configuring the Table of Contents

Your report book is organized and the reports are populated with data. Now you can configure your **Table of Contents** so your users can find the information they need.

The **Table of Contents** is derived from a special data source created by JasperReports and included as a property in the report book. This property, `net.sf.jasperreports.bookmarks.data.source.parameter`, collects bookmarks from the report book's content pages. So you need to add bookmarks to your reports.

To add bookmarks

1.  Open **Country_Intro.jrxml** in the Design tab.
2.  Click the **Country** parameter in the Title band.
3.  In the Properties view, click **Hyperlink**.
4.  Expand the **Anchor and Bookmark** section.
5.  Click ![jss icon expression editor](../assets/images/jss-icon-expression-editor.png) to open the Expression Editor, and click **Parameters**.
6.  Double-click **Country Parameter String** to add it to the expression, then click **Finish**.
7.  In the Properties view, change the Bookmark Level to 1.
8.  Click outside the design space in the Design tab, then click **Report** in the Properties view.
9.  Click to enable **Create bookmarks**.
10. Open the **Content_Page_One.jrxml** in the Design tab.
11. Click the **\$F{SHIPCITY}** text band.
12. In the Properties view, click **Hyperlink**.
13. Expand the **Anchor and Bookmark** section.
14. Click ![jss icon expression editor](../assets/images/jss-icon-expression-editor.png) to open the Expression Editor, and click **Fields**.
15. Double-click **SHIPCITY Field String** to add it to the expression, then click **Finish**.
16. In the Properties view, change the Bookmark Level to 2.
17. Save all files, and compile the Sample_Book.jrxml.
