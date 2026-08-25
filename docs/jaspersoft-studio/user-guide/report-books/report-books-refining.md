---
title: Refining the Report Book
description: "You can further refine the report data to make your report easier to use, by sorting on additional fields, and by adding pages to the book to introduce each of the sorted sections."
---

# Refining the Report Book

You can further refine the report data to make your report easier to use, by sorting on additional fields, and by adding pages to the book to introduce each of the sorted sections.

## Sorting on Additional Fields

At this point, you could run the report, but the data it returns is sorted by City, which you established in [Creating and Adding Reports to your Report Book](report-books-creating-and-adding.md). To organize the data better, you can now modify the report query to sort by Country as well.

To add a filter to a report in a report book

1.  In the Project Explorer, double-click to open **content_page_one.jrxml** in the designer.

2.  In the Outline view, right-click the Parameters folder and select **Create Parameter**.

3.  In the Properties view, change the name to **country**.

4.  In the Designer, click ![dataset and query button](../assets/images/dataset-and-query-button.png) and modify the query to say:

    `Select * from orders where shipcountry = $P{country} order by shipcity`

5.  Click **OK** to return to the designer.

6.  Click the **Preview** tab at the bottom of the designer to open Input Parameters.

7.  In the country field, enter **Italy** and run the report. The report preview displays only data related to Italy, sorted by city.

8.  Click the Design tab, then save and compile your report.

9.  Open **Sample_Book.jrxml** in the design tab, and click to select **Content_Page_One.jasper** in the Content group.

10. In the **Data** tab in the Properties view, click **Edit Parameters** to open the Report Part Parameters window, and click **Add**.

11. In the Parameter Configuration Dialog, enter the `country` as the parameter name.

12. Click ![jss icon expression editor](../assets/images/jss-icon-expression-editor.png) to open the Expression Editor, and click **Fields** in the left panel.

13. Double-click **SHIPCOUNTRY Field String** to add it to the expression, then click **Finish**.

14. Click **OK** in the Parameter Configuration Dialog, then **Finish** in the Report Part Parameters window.

## Adding Section Introductory Pages

You can insert pages in your report to introduce each section of data, as determined in Sorting on Additional Fields. These pages can include text, images, charts, or any number of other elements, pulled from a data source.

We place an introductory page before each country section and include the country name and a chart representing the number of orders for each city in the country.

To add introductory pages to your report

1.  Click ![jss icon new](../assets/images/jss-icon-new.png) to open the Wizard selection window.

2.  Expand the Jaspersoft Studio folder and select **Jasper Report**. Click **Next**.

3.  In the Report Templates window, select the **Blank A4 Landscape** template. Click **Next**.

4.  In the Report file window, select the **MyReports** folder and change the Blank_A4_Landscape.jrxml file name to `Country_Intro.jrxml`. Click **Next**.

5.  In the Data Source window, select **Sample DB – Database JDBC Connection**, and enter the following query and click **Next**:

    `select count(*) c, shipcity from orders group by shipcity`

6.  In the Fields window, add the following Dataset fields to the Fields panel and click **Next**.

    - C
    - SHIPCITY

7.  In the Group By window, click **Finish**. The Country_Intro.jrxml appears in the Design tab.

Now you can determine what data appears on the intro pages.

To modify the data on the intro pages

1.  With Country_Intro.jrxml open in the Design tab, click the **Title** band and increase its height to 350 pixels.

2.  In the Outline view, right-click Parameters and select **Create Parameter**.

3.  In the Properties view, change the Name from Parameter 1 to `Country`.

4.  In the Designer view, click ![dataset and query button](../assets/images/dataset-and-query-button.png) to open the Dataset and Query Dialog.

5.  Modify the query to say:

    `select count(*) c, shipcity from orders where shipcountry = $P{Country} group by shipcity`

6.  Click **OK**.

7.  Save Country_Intro.jrxml.

8.  In the Outline view, drag **Country** from the Parameters list into the Title band.

9.  Click the Country parameter (\$P{Country}).

10. In the Properties view, click **Text Field**. Increase the font size to 26.

11. Click outside the parameter element.

Next, you can add a chart to the intro pages that provides a graphical representation of the data in the section.

To add a chart to the intro pages

1.  In the Palette view, select and drag **HTML5 Charts** from the Components Pro section and place it under the parameter element in the designer view.

2.  In the Chart type selection dialog, scroll down and select **Pie**. Click **OK**.

3.  Resize the pie chart to fit the space. See [Creating a Simple Chart](../charts-jfree/charts-creating-simple.md) for more information.

4.  Double-click the chart element to open the Chart Properties.

5.  Click the **Chart Data** tab, then click the **Configuration** tab.

6.  In the Categories Levels section, double-click **Level1**.

7.  In the Expression text box, delete "Change Me" and click ![jss icon expression editor](../assets/images/jss-icon-expression-editor.png).

8.  Select Fields from the first column, and double-click **SHIPCITY Field String** to add it to the expression.

9.  Click **Finish**.

10. Update the **Name** field to **"City"** and click **OK**.

11. Back in the Chart Properties dialog, update the following information:

    - **Name**: `Number of orders`
    - **Label Expression**: `"Number of orders"`
    - **Calculation**: Nothing
    - Value Expression: Delete new Integer1, click ![jss icon expression editor](../assets/images/jss-icon-expression-editor.png), and double-click C Field Long, then click **Finish**.

12. Click **OK**, then save the report.

13. Compile **Country_Intro.jrxml** to create a .jasper file.

Now, you can add the Country_Intro page to your book, and configure it to display the correct data.

To add and configure the intro page:

1.  Open Sample_Book.jrxml in the Design tab.
2.  Drag **Country_Intro.jasper** from the Project Explorer into the Content group of Sample_Book.jrxml, and place it to the left of the Content_Page_One.jasper file.
3.  In the Design tab, click to select **Country_Intro.jasper**.
4.  In the Properties view, click **Edit Parameters**.
5.  In the Report Part Parameters window, click **Add** to open the Parameter Configuration dialog.
6.  In the Parameter Name field, enter `REPORT_CONNECTION`.
7.  Click ![jss icon expression editor](../assets/images/jss-icon-expression-editor.png) to open the Expression Editor.
8.  In the first column, select **Parameters**.
9.  From the center column, double-click **REPORT_CONNECTION parameter connection** to add it to the editor field, and click **Finish**. The expression appears in the Parameter Expression field.
10. Click **OK** and confirm that the parameter has been added to the Part Parameters list.
11. Click **Add** to open the Parameter Configuration dialog again.
12. In the Parameter Name field, enter `Country`.
13. Click ![jss icon expression editor](../assets/images/jss-icon-expression-editor.png) to open the Expression Editor.
14. In the first column, select **Fields**.
15. From the center column, double-click **SHIPCOUNTRY Field String** to add it to the editor field, and click **Finish**. The expression appears in the Parameter Expression field.
16. Click **OK** and confirm that the parameter has been added to the Part Parameters list, click **Finish**.
