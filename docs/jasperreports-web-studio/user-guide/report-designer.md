---
title: Report Designer
description: "JasperReports Web Studio's main feature is the editor for JRXML report templates. Like Jaspersoft Studio, the editor has three tabs:"
---

# Report Designer

JasperReports Web Studio's main feature is the editor for JRXML report templates. Like Jaspersoft Studio, the editor has three tabs:

- Visual report designer

- JRXML source editor

- Report preview

You can switch between these tabs using buttons at the upper-right corner of the application window.

## Visual Report Designer

The visual report designer consists of a Designing Area, **Outline**, **Palette**, and **Properties** panel.

![jrws palette outline designer](assets/images/jrws_palette_outline_designer.png)

The **Palette** contains all the elements from which the report is built. Drag an element from the **Palette** into the designer.

The **Outline** shows the structure of the layout part of the report. You can view, add, and delete the bands from here. You can also view the order of the elements in a container.

The Designing Area shows the large layout composed of the bands and elements. Drag the elements to arrange them in the desired layout. Keep in mind that this is very close to the report rendered in the HTML format. Reports rendered in PDF or other formats may look a bit different.

Selecting an element in the **Outline** or Designing Area automatically shows its properties in the **Properties** panel. Elements could have hundreds of properties that are organized in categories. It is possible to filter properties by name by using the search box at the bottom of the view. In the same place, there is an icon to set more filters, to show or not deprecated properties, or all JasperReports custom properties.

A special category of properties is styles. If an element uses a style, properties inherit the value of the parent style. These values are shown in the light gray color. In general, if the property shows the value in the light gray color, this is the default or calculated from the properties value, black color is used for the actual value.

### Snap to Geometry

You can use this feature to align various elements in the Designing Area. When moving and resizing an element, a magnetic effect helps an element to align with the band borders and the location and size of other elements. When multiple elements are selected, the magnetic effect works on the whole bounding box that contains the selected elements.

![SnaptoGeometry](assets/images/SnaptoGeometry.png)

### Context Menu

Use the context menu from the **Outline** to align and resize the elements in the Designing Area. Right-click on an element to use any of the following options:

- **Fit Both**: Fits the element within the container in the Designing Area.

- **Delete**: Deletes the element.

- **Copy**: Copies the element.

- **Paste**: Pastes the element.

- **Duplicate**: Creates a copy of the element.

- **Enclose in Frame**: Encloses the elements in a frame. Set properties for the frame to apply them to all the elements within the frame at the same time.

  - If you select an element within a frame, a new option ![SelectParentFrame](assets/images/SelectParentFrame.png) to select all the elements in the frame is available.

  - Only when a frame is selected, the **Lock Frame** option is displayed. This action locks the elements in the frame. The elements cannot be selected or dragged and dropped. You can **Unlock Frame** to perform the actions as required.

- **Center Element**: Aligns the element to the center.

- **Adapt to Container**: Aligns the element to **Fit Width**, **Fit Height**, or **Fit Both** (width and height), within the container in which it is placed.

- **Arrange**: Arranges the element **To Back**, **To Front**, **Backward**, or **Forward**.

- **Align in Container**: Aligns the element within the container.

Whenever you select an element from **Outline**, the context menu actions that you see for the element are also available in the horizontal mini toolbar. The mini toolbar is displayed when you click an element. It provides the option to duplicate, delete, copy, and when you click the ellipses, a list of sub-menu options are shown.

![contextMenu](assets/images/contextMenu.png)

![ContextMenu1](assets/images/ContextMenu1.png)

### Images

This feature enables you to add an image to the report with ease. Drag the **Image** element from the **Palette** to the desired location on the report page.

![ImagePreview](assets/images/ImagePreview.png)

Click the **Search** icon in **Expression** to select an image. If it a simple image, its displayed in the designer.

![ImagePreview1](assets/images/ImagePreview1.png)

![imagePreview2](assets/images/imagePreview2.png)

Edit a text element or expression inline. Double-click a **Text Field** or **Static Text** element to quickly change the expression and text. Use the **Properties** panel to change element properties, such as **Color** or **Font**.

![InlineText](assets/images/InlineText.png)

![InlineText1](assets/images/InlineText1.png)

You can also edit expressions inline. Double-click an expression, and in the **Expression** editor, edit the expression inline.

![InlineExpression](assets/images/InlineExpression.png)

### Tables

To create tables in a report, drag the **Table** element from the **Palette** to the desired location on the report page.<br>
In the Table Wizard, you can see the **Open Dataset Tab** only if there are no subdataset defined in the report. The table element must have a subdataset to work correctly. You have to create a subdataset to have a table in the report, click **Open Datasets Tab** to navigate to the **Dataset** tab. Click **Cancel** to terminate the process.

![TableWizard1](assets/images/TableWizard1.png)

In the **Dataset** tab, select an existing one or define a new dataset and ensure that the data adapter for the created dataset is correctly browsed and configured.

Now you drag and drop **Table** component from **Palette** to summary band. In the **Table Wizard**, select the dataset from the **Dataset** dropdown.

Select the **Connection** from the dropdown, for how the table should connect to the datasource.

Click **Next**, to navigate to the next step, or click Cancel to

![TableWizard2](assets/images/TableWizard2.png)

In the next tab, select the fields of the dataset that can be used to produce the tables column. Click **\>** to transfer the field(s) from the left side to the right. Click **\<** to move the field(s) from right to left side.

To move all the fields from left side to the right, Click **\>\>** or click **\<\<** to move fields from right to left side

![TableWizard3](assets/images/TableWizard3.png)

Click **Next**, or click **Previous**, to navigate to the previous screens.

The Table Wizard now displays the sample of the Table. The **Cell Colors**, **Borders** and **Visible Sections** can be adjusted accordingly.

![TablwWizard4](assets/images/TablwWizard4.png)

Click **Finish**, to generate the Table. Now you can Preview the table.

You can also edit the existing table, double-click the table to open the table editor.

![Table1](assets/images/Table1.png)

Drag a cell to resize it.

![Table2](assets/images/Table2.png)

Add and delete columns in the table editor using either context menu or the mini toolbar.

![Table3](assets/images/Table3.png)

Drag the Fields to the table columns to add data to the table.![Table4](assets/images/Table4.png)

Save the report and Preview the data from the Report view.

![Table5](assets/images/Table5.png)

To add a column header, drag one of the Fields to the header row. You can also convert the field value to static text.

![Table7](assets/images/Table7.png)

Select elements independently using the Shift key.

In this example, the first and second rows are selected. You can view the details in the Outline pane.

![Table8](assets/images/Table8.png)

To add a row, go to Outline, right-click Table Header, and from the context menu, click Add Row.

![Table9](assets/images/Table9.png)

Select two or more cells to Merge Cells.

![Table10](assets/images/Table10.png)

You can Separate Cells too.

![Table11](assets/images/Table11.png)

#### Add or Delete Sections

In **Outline**, when you hover any section of the table, except the **Detail**, a ![cross](assets/images/cross.png) is shown on the right. If you click ![cross](assets/images/cross.png), the section is deleted.

![Table12](assets/images/Table12.png)

Similarly, if a section is not available, its is displayed in light gray with a + icon next to it. You can click the icon to add the section.

![Table13](assets/images/Table13.png)

If the dataset connected to the table contains groups, the names of the groups are displayed as additional sections in the Outline of the table.

Click ![cross](assets/images/cross.png) to delete the group.

![Table14](assets/images/Table14.png)

Click + to create the group.

![Table15](assets/images/Table15.png)

![Add from Outline](assets/images/Add_from_Outline.png)

#### Support for Columns

Create tables with multiple columns using this feature. Go to the **Properties** panel and add the required **Number Of Columns**. The Designing Area is evenly divided into columns specified in the **Properties** panel. The area other than the first column is grayed out. The grayed out area represents where columns continue once information is populated.

![ColumnSupport](assets/images/ColumnSupport.png)

You can resize and adjust the elements to fit the column space.

![SupportForColumn](assets/images/SupportForColumn.png)

Preview the data. The data is displayed in two-column spaces.

For example, in the following screenshot, the data populated the next 2 columns once the first two were completely used.

![SupportForColumn1](assets/images/SupportForColumn1.png)

### Crosstab

This feature enables you to add a crosstab to the report with ease. Drag the Crosstab element from the Palette to the Summary section on the report page.

- In the **Crosstab Wizard**, select the dataset from the Dataset dropdown.

  ![CrosstabWizard1](assets/images/CrosstabWizard1.png)

  Click **Next**, to go to the next screen or click **Cancel**, to terminate the operation

- In the next tab, to define at least one column group, select one or more fields and click **\>** to transfer the field(s) from the left side to the right. You can also move the field(s) from the right side to the left.

  To move all the fields from left side to the right, Click **\>\>**.

  Click **Next** to add the row group fields, or click **Previous** to navigate to the previous screen.

  ![CrosstabWizard2](assets/images/CrosstabWizard2.png)

- In the next tab, to define at least one row group, select one or more fields and click **\<** to move the field(s) from left to the right side.

  To move all the fields from right side to the left, click **\<\<**.

  Once you select a field for a column or a row group, the following options are available on the right-hand side:

  - **Field**: Displays the name of the field.

  - **Order**: Enables you to choose the option to display the details in order. You can select, Ascending, or Descending from the dropdown menu.

  - **Total Position**: None, Start, End.

  - **Calculation**: None, Count, Sum, Average, Lowest, Highest, Standard Deviation, Variance, System, First, Distinct Count.

  Click **Next**.

!!! note

    If a field is already selected in the column group, you cannot view the same field in the row group.

- To define at least one measure, select one or more fields and click \> to move the field(s) from the left side to the right. You can also move the field(s) from the right side to the left.

  Click **Next**.

- The **Crosstab Wizard** now displays a sample of the Crosstab. The **Cell Colors** and **Borders** can be adjusted. You can use the **Show Grid** toggle to control the display of the borders in the crosstab.

  You can change the colors by clicking the color box next to the **Total Color**, **Group Color**, **Measure Color**, **Detail Color** and **Border Color** respectively. The color changes dynamically.

  ![CrosstabWizardColorBorder](assets/images/CrosstabWizardColorBorder.png)

  Click **Finish**, to generate the crosstab.

The Crosstab is created on the **Summary** band of the report.

Now you can **Preview** the report. Scroll up and down the page and navigate to any page you want.

### Dataset

You can go to the **Dataset** panel to configure the report datasets from the list. Each dataset in the **Properties** panel has **Fields**, **Parameters**, **Variables**, **Groups**, and a list of other properties. Use **Show Query Editor** to show the query editor and all related tools.

![ShowQueryEditor](assets/images/ShowQueryEditor.png)

The **Metadata** panel helps visualize the structure of most of the JDBC databases or CSV, XLS, XML, and JSON files. The **Parameters** panel is for setting the values for the parameters. In the query editor area, depending on the language, a text editor with syntax highlighting helps edit the query. **Query Preview** is useful to run the query and see what data it returns.

![jrws show query editor](assets/images/jrws_show_query_editor.png)

### Drag and Drop Fields

To simplify report creation, drag the fields from the **Dataset** panel into the report design. The designer creates a **Text Field** with the corresponding expression automatically.

### Validation and Refactoring

Dataset objects are used as references by all kinds of elements inside the report. There is a validator of the model. In case there are problems, a red icon appears at the bottom-right corner. Click the icon to see the problems.

In case dataset, fields, parameters, and variables are either renamed or deleted, the designer tries to refactor expressions or other references in the model.

### Copy and Paste Elements

To copy and paste elements in the report layout designer, you can use any one of the following options:

- Select the component and use the standard browser shortcut keys (Ctrl+C and Ctrl+V) from the keyboard.

OR

- Right-click on the component and from the context menu, select **Copy** and then **Paste**.

### Expression Editor

The **Expression** editor is composed from two panes. The left-hand side pane lists the dataset objects that you can use in the expression. The right-hand side panel shows the expression itself.

![jrws expression editor](assets/images/jrws-expression-editor.png)

You can replace a selected text with an expression. To do this, edit the expression using the **Expression** editor, and select the text in the expression text area. On double-clicking the field, the selected text is replaced with the expression of the field. You can drag the elements from the left panel to the text area.

## JRXML Source Editor

Report templates for JasperReports Web Studio are text files with .jrxml extension. You can use the **Source Editor** to manually modify a template by editing the XML code.

![jrws source editor](assets/images/jrws-source-editor.png)

## Report Preview

This is the place to consume and test reports. This view provides user interfaces to give values to parameters, select the format to generate, and navigate the report. Report navigation could be done in different ways. On the top toolbar, there are controls to select the desired page, search through the report, or use bookmarks to navigate in the report. The bookmarks are present on the left side of the page, with toolbar buttons being linked only to sub-reports that are referred to by the main report.

![jrws preview](assets/images/jrws-preview.png)

When a report is previewed, it is executed at the backend by JasperReports® IO. JasperReports IO is an HTTP-based reporting service for JasperReports® Library, providing an interface to the JasperReports Library reporting engine through the use of a REST API and a JavaScript API. The REST API provides services for running, exporting, and interacting with reports. The JavaScript API allows you to embed reports and their input controls into your web pages and web applications using JavaScript frameworks for the layout and style sheets (CSS) to control the look and feel. JasperReports IO provides multiple configurable options, including the ability to limit execution of certain report expressions for security reasons.

Following is the list of security-related configuration changes:

- **Enabling the Java Security Manager**:

  In the Professional edition, the Java Security Manager can be enabled by uncommenting the following lines in:

  - `start.sh` script:

    `#JRWS_SECURITY_ARGS="-Djava.security.manager -Djava.security.policy=${ROOT_PATH}/jrws/security.policy`

    OR

  - `start.bat` script:

    `#rem set "JRWS_SECURITY_ARGS=-Djava.security.manager -Djava.security.policy=%~dp0\jrws\security.policy`

  In the Enterprise edition, set the `javaSecurityEnabled` Helm chart values flag to `true`.

- **Report expression class filtering**

  To enable report expression class filtering in the Standalone edition, set `net.sf.jasperreports.report.class.filter.enabled=true` in the `applicationContext-common.xml` file.

  In the Enterprise edition, set the `reportExpressionsClassFilterEnabled` Helm chart flag to `true`.

  More classes can be allowed in report expression by setting `net.sf.jasperreports.report.class.whitelist.* properties` in `applicationContext-common.xml` or via the `jrioReporting.config.jasperReportsProperties` Helm chart values property.

- **Repository Jars class loading**

  In the Standalone edition, to disable loading classes from repository jars, set the `classLoadingEnabled` property of the `jrioContextProvider` bean to `false` in the `applicationContext-common.xml` file.

  In the Enterprise edition, set the `repositoryClassLoadingEnabled` Helm chart values flag to `false`.

## Data Adapter Editors

An important aspect of reporting is acquiring the data for the reports. This data usually comes from relational databases, files, or other specialized data storage systems.

The way to acquire report data in JasperReports Web Studio is by using data adapters, which are specialized files containing information about how to get the data.

Data adapters could be of the following types: Random, Empty, QueryExecutor, relational database connections (JDBC), MongoDB, Mondrian, locally stored or remotely retrieved data files of CSV, XML, JSON, XLS type, and so on.

JasperReports Web Studio features a specialized editor that allows creating and editing these Data Adapter types.

![jrws data adapter editor](assets/images/jrws-data-adapter-editor.png)

## Image Editors

There is basic support for images. By default, JasperReports Web Studio shows an image supported by the browser. For some image types, there is an image editor, which helps to modify an existing image.

![jrws image editor](assets/images/jrws_image_editor.png)

## Text Editors

Most of the text files are editable with a simple text editor. However, for many types, JasperReports Web Studio supports syntax highlighting and some more advanced editor functions like folding, and validation. This could be very useful for files like properties, CSS, HTML, XML, JSON, SH, SQL. The text editor supports functionalities including search and replace text, pretty formatting. To see all the keyboard shortcuts, click the question mark icon on the toolbar.

![jrws text editor](assets/images/jrws-text-editor.png)

## Editor for JR-INF/context.xml

These files provide configuration for report execution. It could contain some properties that are used for reports or classpath. To see a more detailed description of these files, refer to the JasperReports® IO guides.

![jrws editor jrinf](assets/images/jrws-editor-jrinf.png)
