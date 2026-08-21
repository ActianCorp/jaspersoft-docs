---
title: API Usage - Interactive Reports
description: "Most reports rendered in the JasperReports Server native interface have interactive abilities such as column sorting provided by a feature called JIVE: Jaspersoft Interactive Viewer and Editor. The..."
---

# API Usage - Interactive Reports

Most reports rendered in the JasperReports Server native interface have interactive abilities such as column sorting provided by a feature called JIVE: Jaspersoft Interactive Viewer and Editor. The JIVE UI is the interface of the report viewer in JasperReports Server, and the same JIVE UI is replicated on reports generated in clients using Visualize.js.

Not only does the JIVE UI allow users to sort and filter regular reports, it also provides many opportunities for you to further customize the appearance and behavior of your reports through Visualize.js .

This chapter contains the following sections:

- Interacting With JIVE UI Components
- Using Floating Headers
- Changing the Chart Type
- Changing the Chart Properties
- Undo and Redo Actions
- Sorting Table Columns
- Filtering Table Columns
- Formatting Table Columns
- Conditional Formatting on Table Columns
- Sorting Crosstab Columns
- Sorting Crosstab Rows
- Implementing Search in Reports
- Providing Bookmarks in Reports
- Disabling the JIVE UI

## Interacting With JIVE UI Components

The `visualize.report` interface exposes the `updateComponent` function that gives your script access to the JIVE UI. Using the `updateComponent` function, you can programmatically interact with the JIVE UI to do such things as set the sort order on a specified column, add a filter, and change the chart type. In addition, the `undoAll` function acts as a reset.

For the API reference of the `visualize.report` interface, see [Report Functions](../../jasperreports-io/professional-user-guide/jasperreports-server-visualize.js-guide/displaying_reports.md).

First, your script must enable the default JIVE UI to make its components available after running a report:

```
var report = v.report({
    resource: "/public/SampleReport",
    defaultJiveUi : {
        enabled: true
    }
});
...
var components = report.data().components;
```

The components that can be modified are columns and charts. These components of the JIVE UI have an ID, but it may change from execution to execution. To refer to these components, create your report in JRXML and use the `net.sf.jasperreports.components.name` property to name them. In the case of a column, this property should be set on the column definition in the table model. In Jaspersoft Studio, you can select the column in the Outline View, then go to **Properties \> Advanced**, and under **Misc \> Properties** you can define custom properties.

Then you can reference the component by this name, for example a column named `sales`, and use the `updateComponent` function to modify it.

```
report.updateComponent("sales", {
    sort : {
        order : "asc"
    }
});
```

Or:

```
report.updateComponent({
    name: "sales",
    sort : {
        order : "asc"
    }
});
```

We can also get an object that represents the named component of the JIVE UI:

```
var salesColumn = report
                    .data()
                    .components
                    .filter(function(c){ return c.name === "sales"})
                    .pop();
```

The following example shows how to create buttons whose click events modify the report through the JIVE UI. This example assumes you have a report whose components already have names, in this case, columns named `my_accounts` and `my_dept`, and a chart named `revenue`:

```
visualize({
    auth: { ...
    }
}, function (v) {
    //render report from provided resource
    var report = v.report({
        resource: "/public/SampleReport",
        container: "#container",
        success: printComponentsNames,
        error: handleError
    });

    $("#resetAll").on("click", function(){
        report.undoAll();
    });

    $("#changeAccounts").on("click", function () {
        report.updateComponent("my_accounts", {
            sort: {
                order: "asc"
            },
            filter: {
                operator: "greater_or_equal",
                value: 15000
            }
        }).fail(handleError);
    });

    $("#changeDept").on("click", function () {
        report.updateComponent("my_dept", {
            sort: {
                order: "desc"
            }
        }).fail(handleError);
    });

    $("#changeChart").on("click", function () {
        report.updateComponent("revenue", {
             chartType: "Pie"
        }).fail(handleError);
    });

    //show error
    function handleError(err){
        alert(err.message);
    }

    function printComponentsNames(data){
        data.components.forEach(function(c){
            console.log("Component Name: " + c.name, "Component Label: "+ c.label);
        });
    }

});
```

The associated HTML has buttons that will invoke the JavaScript actions on the JIVE UI:

```
<!-- Provide the URL to visualize.js -->
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>
<button id="resetAll">Reset All</button>
<button id="changeAccounts">View Top Accounts</button>
<button id="changeDept">Sort Departments</button>
<button id="changeChart">Show Pie Chart</button>
<!-- Provide a container for the report -->
<div id="container"></div>
```

## Using Floating Headers

One feature of the JIVE UI for tables and crosstabs is the floating header. When you turn on floating headers, the header rows of a table or crosstab float at the top of the container when you scroll down. The report container must allow scrolling for this to take effect. This means that CSS property `overflow` with values like `scroll` or `auto` must be specifically set for the report container.

To turn on floating headers for your interactive reports, set the following parameters when you enable the JIVE UI:

```
var report = v.report({
    resource: "/public/SampleReport",
    defaultJiveUi : {
        floatingTableHeadersEnabled: true,
        floatingCrosstabHeadersEnabled: true
    }
});
```

## Changing the Chart Type

If you have the name of a chart component, you can easily set a new chart type and redraw the chart.

```
var mySalesChart = report
                    .data()
                    .components
                    .filter(function(c){ return c.name === "salesChart"})
                    .pop();

mySalesChart.chartType = "Bar";

report
    .updateComponent(mySalesChart)
    .done(function(){
        alert("Chart type changed!");
    })
    .fail(function(err){
        alert(err.message);
    });
```

Or:

```
report
    .updateComponent("salesChart", {
          chartType: "Bar"
    })
    .done(function(){
        alert("Chart type changed!");
    })
    .fail(function(err){
        alert(err.message);
    });
```

The following example creates a drop-down menu that lets users change the chart type. You could also set the chart type according to other states in your client.

This code also relies on the `report.chart.types` interface described in [Discovering Available Charts and Formats](../../jasperreports-io/professional-user-guide/jasperreports-server-visualize.js-guide/displaying_reports.md).

```
visualize({
    auth: { ...
    }
}, function (v) {

    //persisted chart name
    var chartName = "geo_by_seg",
        $select = buildControl("Chart types: ", v.report.chart.types),
        report = v.report({
            resource: "/public/Reports/1._Geographic_Results_by_Segment_Report",
            container: "#container",
            success: selectDefaultChartType
        });

    $select.on("change", function () {
        report.updateComponent(chartName, {
                chartType: $(this).val()
            })
            .done(function (component) {
                chartComponent = component;
            })
            .fail(function (error) {
                alert(error);
            });
    });

    function selectDefaultChartType(data) {
        var component = data.components
                            .filter(function (c) {
                                   return c.name === chartName;
                            })
                            .pop();
        if (component) {
            $select.find("option[value='" + component.chartType + "']")
                   .attr("selected", "selected");
        }
    }
    function buildControl(name, options) {

        function buildOptions(options) {
            var template = "<option>{value}</option>";
            return options.reduce(function (memo, option) {
                return memo + template.replace("{value}", option);
            }, "")
        }

        console.log(options);

        if (!options.length) {
            console.log(options);
        }

        var template = "<label>{label}</label><select>{options}</select><br>",
            content = template.replace("{label}", name)
                .replace("{options}", buildOptions(options));

        var $control = $(content);
        $control.insertBefore($("#container"));
        return $control;
    }

});
```

As shown in the following HTML, the control for the chart type is created dynamically by the JavaScript:

```
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<!-- Provide the URL to visualize.js -->
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>
<!-- Provide a container for the report -->
<div id="container"></div>
```

## Changing the Chart Properties

Those chart components that are based on Highcharts have a lot of interactivity such as built-in zooming and animation. The built-in zooming lets users select data, for example columns in a chart, but it can also interfere with touch interfaces. With Visualize.js, you have full control over these features and you can choose to allow your users access to them or not. For example, animation can be slow on mobile devices, so you could turn off both zooming and animation. Alternatively, if your users have a range of mobile devices, tablets, and desktop computers, then you could give users the choice of turning on or off these properties themselves.

The following example creates buttons to toggle several chart properties and demonstrates how to control them programmatically. First the HTML to create the buttons:

```
<script src="http://localhost:8080/jasperserver-pro/client/visualize.js"></script>

<button id="disableAnimation">disable animation</button>
<button id="enableAnimation">enable animation</button>
<button id="resetAnimation">reset animation to initial state</button>

<button id="disableZoom">disable zoom</button>
<button id="zoomX">set zoom to 'x' type</button>
<button id="zoomY">set zoom to 'y' type</button>
<button id="zoomXY">set zoom to 'xy' type</button>
<button id="resetZoom">reset zoom to initial state</button>

<div id="container"></div>
```

Here are the API calls to set the various chart properties:

```
visualize({
    auth: {
        name: "jasperadmin",
        password: "jasperadmin",
        organization: "organization_1"
    }
}, function (v) {

    var report = v.report({
        resource: "/public/Samples/Reports/01._Geographic_Results_by_Segment_Report",
        container: "#container",
        error: function(e) {
            alert(e);
        }
    });

    function changeChartProperty(prop, value) {
        var chartProps = report.chart();

        if (typeof value === "undefined") {
            delete chartProps[prop];
        } else {
            chartProps[prop] = value;
        }

        report.chart(chartProps).run().fail(function(e) { alert(e); });
    }

    $("#disableAnimation").on("click", function() {
        changeChartProperty("animation", false);
    });

    $("#enableAnimation").on("click", function() {
        changeChartProperty("animation", true);
    });

    $("#resetAnimation").on("click", function() {
        changeChartProperty("animation");
    });

    $("#disableZoom").on("click", function() {
        changeChartProperty("zoom", false);
    });

    $("#zoomX").on("click", function() {
        changeChartProperty("zoom", "x");
    });

    $("#zoomY").on("click", function() {
        changeChartProperty("zoom", "y");
    });

    $("#zoomXY").on("click", function() {
        changeChartProperty("zoom", "xy");
    });

    $("#resetZoom").on("click", function() {
        changeChartProperty("zoom");
    });
});
```

## Undo and Redo Actions

As in JasperReports Server, the JIVE UI supports undo and redo actions that you can access programmatically with Visualize.js. As in many applications, undo and redo actions act like a stack, and the `canUndo` and `canRedo` events notify your page you are at either end of the stack.

```
visualize({
    auth: { ...
    }
}, function (v) {

    var chartComponent,
        report = v.report({
            resource: "/public/Samples/Reports/1._Geographic_Results_by_Segment_Report",
            container: "#container",
            events: {
                canUndo: function (canUndo) {
                    if (canUndo) {
                        $("#undo, #undoAll").removeAttr("disabled");
                    } else {
                        $("#undo, #undoAll").attr("disabled", "disabled");
                    }
                },
                canRedo: function (canRedo) {
                    if (canRedo) {
                        $("#redo").removeAttr("disabled");
                    } else {
                        $("#redo").attr("disabled", "disabled");
                    }
                }
            },
            success: function (data) {
                chartComponent = data.components.pop();
                $("option[value='" + chartComponent.chartType + "']").attr("selected", "selected");
            }
        });

    var chartTypeSelect = buildChartTypeSelect(report);

    chartTypeSelect.on("change", function () {
        report.updateComponent(chartComponent.id, {
            chartType: $(this).val()
        })
            .done(function (component) {
            chartComponent = component;
        })
            .fail(function (error) {
            console.log(error);
            alert(error);
        });
    });

    $("#undo").on("click", function () {
        report.undo().fail(function (err) {
            alert(err);
        });
    });

    $("#redo").on("click", function () {
        report.redo().fail(function (err) {
            alert(err);
        });
    });

    $("#undoAll").on("click", function () {
        report.undoAll().fail(function (err) {
            alert(err);
        });
    });
});
function buildChartTypeSelect(report) {

    var chartTypes = report.schema("chart").properties.chartType.enum,
        chartTypeSelect = $("#chartType");

    $.each(chartTypes, function (index, type) {
        chartTypeSelect.append("" + type + "");
    });

   return chartTypeSelect;
}
```

Associated HTML:

```
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<!-- Provide the URL to visualize.js -->
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>

<select id="chartType"></select>
<button id="undo" disabled="disabled">Undo</button>
<button id="redo" disabled="disabled">Redo</button>
<button id="undoAll" disabled="disabled">Undo All</button>
<!-- Provide a container for the report -->
<div id="container"></div>
```

## Sorting Table Columns

This code example shows how to set the three possible sorting orders on a column in the JIVE UI: ascending, descending, and no sorting.

```
visualize({
    auth: { ...
    }
}, function (v) {
    var report = v.report({
        resource: "/public/Samples/Reports/5g.AccountsReport",
        container: "#container",
        error: showError
    });

    $("#sortAsc").on("click", function () {
        report.updateComponent("name", {
            sort: {
                order: "asc"
            }
        })
        .fail(showError);
    });

    $("#sortDesc").on("click", function () {
        report.updateComponent("name", {
            sort: {
                order: "desc"
            }
        })
        .fail(showError);
    });

    $("#sortNone").on("click", function () {
        report.updateComponent("name", {
            sort:
        }).fail(showError);
    });

    function showError(err) {
        alert(err);
    }
});
```

Associated HTML:

```
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script src="http://underscorejs.org/underscore-min.js"></script>
<!-- Provide the URL to visualize.js -->
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>

<button id="sortAsc">Sort NAME column ASCENDING</button>
<button id="sortDesc">Sort NAME column DESCENDING</button>
<button id="sortNone">Reset NAME column</button>

<!-- Provide a container for the report -->
<div id="container"></div>
```

## Filtering Table Columns

This code example shows how to define filters on columns of various data types (dates, strings, numeric) in the JIVE UI. It also shows several filter operator such as `equal`, `greater`, `between`, `contain` (for string matching), and `before (for times and dates)`.

```
visualize({
    auth: { ...
    }
}, function (v) {
    var report = v.report({
             resource:"/public/viz/report_with_different_column_types",
            container: "#container",
            error: function(err) {
                alert(err);
            }
        });

    $("#setTimestampRange").on("click", function() {
        report.updateComponent("column_timestamp", {
            filter: {
                operator: "between",
                value: [$("#betweenDates1").val(), $("#betweenDates2").val()]
            }
        }).fail(handleError);
    });
    $("#resetTimestampFilter").on("click", function() {
        report.updateComponent("column_timestamp", {
            filter:
        }).fail(handleError);
    });
    $("#setBooleanTrue").on("click", function() {
        report.updateComponent("column_boolean", {
            filter: {
                operator: "equal",
                value: true
            }
        }).fail(handleError);
    });

    $("#resetBoolean").on("click", function() {
        report.updateComponent("column_boolean", {
            filter:
        }).fail(handleError);
    });

    $("#setStringContains").on("click", function() {
        report.updateComponent("column_string", {
            filter: {
                operator: "contain",
                value: $("#stringContains").val()
            }
        }).fail(handleError);
    });

    $("#resetString").on("click", function() {
        report.updateComponent("column_string", {
            filter:
        }).fail(handleError);
    });

    $("#setNumericGreater").on("click", function() {
        report.updateComponent("column_double", {
            filter: {
                operator: "greater",
                value: parseFloat($("#numericGreater").val(), 10)
            }
        }).fail(handleError);
    });

    $("#resetNumeric").on("click", function() {
        report.updateComponent("column_double", {
            filter:
        }).fail(handleError);
    });

    $("#setTimeBefore").on("click", function() {
        report.updateComponent("column_time", {
            filter: {
                operator: "before",
                value: $("#timeBefore").val()
            }
        }).fail(handleError);
    });

    $("#resetTime").on("click", function() {
        report.updateComponent("column_time", {
            filter:
        }).fail(handleError);
    });
});

function handleError(err) {
     console.log(err);
     alert(err);
}
```

Associated HTML:

```
<script src="http://code.jquery.com/jquery-2.1.0.js"></script>
<script src="http://underscorejs.org/underscore-min.js"></script>
<!-- Provide the URL to visualize.js -->
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>

<input type="text" value="2014-04-10T00:00:00" id="betweenDates1"/> -
<input type="text" id="betweenDates2" value="2014-04-24T00:00:00"/>
<button id="setTimestampRange">Set timestamp range</button>
<button id="resetTimestampFilter">Reset timestamp filter</button>
<br/><br/>
<button id="setBooleanTrue">Filter boolean column to true</button>
<button id="resetBoolean">Reset boolean filter</button>
<br/><br/>
<input type="text" value="hou" id="stringContains"/>
<button id="setStringContains">Set string column contains</button>
<button id="resetString">Reset string filter</button>
<br/><br/>
<input type="text" value="40.99" id="numericGreater"/>
<button id="setNumericGreater">Set numeric column greater than</button>
<button id="resetNumeric">Reset numeric filter</button>
<br/><br/>
<input type="text" value="13:15:43" id="timeBefore"/>
<button id="setTimeBefore">Set time column before than</button>
<button id="resetTime">Reset time filter</button>

<!-- Provide a container for the report -->
<div id="container"></div>
```

## Formatting Table Columns

The JIVE UI allows you to format columns by setting the alignment, color, font, size, and background of text in both headings and cells. You can also set the numeric format of cells, such as the precision, negative indicator, and currency. Note that the initial appearance of any numbers also depends on the locale set either by default on JasperReports Server, or specified in your script request, as described in [Requesting the Visualize.js Script](../../jasperreports-io/professional-user-guide/jasperreports-server-visualize.js-guide/visualize_js_api_reference.md).

```
visualize({
    auth: { ...
    }
}, function (v) {
    var columns,
    report = v.report({
        resource: "/public/viz/report_with_different_column_types",
        container: "#container",
        events: {
            reportCompleted: function (status, error) {
                if (status === "ready") {
                    columns = _.filter(report.data().components, function (component) {
                        return component.componentType == "tableColumn";
                    });

                    var column4 = columns[4];

                    $("#label").val(column4.label);

                    $("#headingFormatAlign").val(column4.headingFormat.align);
                    $("#headingFormatBgColor").val(column4.headingFormat.backgroundColor);
                    $("#headingFormatFontSize").val(column4.headingFormat.font.size);
                    $("#headingFormatFontColor").val(column4.headingFormat.font.color);
                    $("#headingFormatFontName").val(column4.headingFormat.font.name);
                    if (column4.headingFormat.font.bold) {
                        $("#headingFormatFontBold").attr("checked", "checked");
                    } else {
                        $("#headingFormatFontBold").removeAttr("checked");
                    }
                    if (column4.headingFormat.font.italic) {
                        $("#headingFormatFontItalic").attr("checked", "checked");
                    } else {
                        $("#headingFormatFontItalic").removeAttr("checked");
                    }
                    if (column4.headingFormat.font.underline) {
                        $("#headingFormatFontUnderline").attr("checked", "checked");
                    } else {
                        $("#headingFormatFontUnderline").removeAttr("checked");
                    }

                    $("#detailsRowFormatAlign").val(column4.detailsRowFormat.align);
                    $("#detailsRowFormatBgColor").val(column4.detailsRowFormat.backgroundColor);
                    $("#detailsRowFormatFontSize").val(column4.detailsRowFormat.font.size);
                    $("#detailsRowFormatFontColor").val(column4.detailsRowFormat.font.color);
                    $("#detailsRowFormatFontName").val(column4.detailsRowFormat.font.name);
                    if (column4.detailsRowFormat.font.bold) {
                        $("#detailsRowFormatFontBold").attr("checked", "checked");
                    } else {
                        $("#detailsRowFormatFontBold").removeAttr("checked");
                    }
                    if (column4.detailsRowFormat.font.italic) {
                        $("#detailsRowFormatFontItalic").attr("checked", "checked");
                    } else {
                        $("#detailsRowFormatFontItalic").removeAttr("checked");
                    }
                    if (column4.detailsRowFormat.font.underline) {
                        $("#detailsRowFormatFontUnderline").attr("checked", "checked");
                    } else {
                        $("#detailsRowFormatFontUnderline").removeAttr("checked");
                    }

                    $("#detailsRowFormatPatternNegativeFormat").val(
                        column4.detailsRowFormat.pattern.negativeFormat);
                    $("#detailsRowFormatPatternPrecision").val(
                        column4.detailsRowFormat.pattern.precision);
                    $("#detailsRowFormatPatternCurrency").val(
                        column4.detailsRowFormat.pattern.currency || "");

                    if (column4.detailsRowFormat.pattern.percentage) {
                        $("#detailsRowFormatPatternPercentage").attr("checked", "checked");
                    } else {
                        $("#detailsRowFormatPatternPercentage").removeAttr("checked");
                    }

                    if (column4.detailsRowFormat.pattern.grouping) {
                        $("#detailsRowFormatPatternGrouping").attr("checked", "checked");
                    } else {
                        $("#detailsRowFormatPatternGrouping").removeAttr("checked");
                    }
                }
            }
        },
        error: function (err) {
            alert(err);
        }
    });

    $("#changeHeadingFormat").on("click", function () {
        report.updateComponent(columns[4].id, {
            headingFormat: {
                align: $("#headingFormatAlign").val(),
                backgroundColor: $("#headingFormatBgColor").val(),
                font: {
                    size: parseFloat($("#headingFormatFontSize").val()),
                    color: $("#headingFormatFontColor").val(),
                    underline: $("#headingFormatFontUnderline").is(":checked"),
                    bold: $("#headingFormatFontBold").is(":checked"),
                    italic: $("#headingFormatFontItalic").is(":checked"),
                    name: $("#headingFormatFontName").val()
                }
            }
        }).fail(function (e) {
            alert(e);
        });
    });

    $("#changeDetailsRowFormat").on("click", function () {
        report.updateComponent(columns[4].id, {
            detailsRowFormat: {
                align: $("#detailsRowFormatAlign").val(),
                backgroundColor: $("#detailsRowFormatBgColor").val(),
                font: {
                    size: parseFloat($("#detailsRowFormatFontSize").val()),
                    color: $("#detailsRowFormatFontColor").val(),
                    underline: $("#detailsRowFormatFontUnderline").is(":checked"),
                    bold: $("#detailsRowFormatFontBold").is(":checked"),
                    italic: $("#detailsRowFormatFontItalic").is(":checked"),
                    name: $("#detailsRowFormatFontName").val()
                },
                pattern: {
                    negativeFormat: $("#detailsRowFormatPatternNegativeFormat").val(),
                    currency: $("#detailsRowFormatPatternCurrency").val() || null,
                    precision: parseInt($("#detailsRowFormatPatternPrecision").val(), 10),
                    percentage: $("#detailsRowFormatPatternPercentage").is(":checked"),
                    grouping: $("#detailsRowFormatPatternGrouping").is(":checked")
                }
            }
        }).fail(function (e) {
            alert(e);
        });
    });

    $("#changeLabel").on("click", function () {
        report.updateComponent(columns[4].id, {

            label: $("#label").val()
        }).fail(function (e) {
            alert(e);
        });
    });
});
```

The associated HTML has static controls for selecting all the formatting options that the script above can modify in the report.

```
<script src="http://code.jquery.com/jquery-2.1.0.js"></script>
<script src="http://underscorejs.org/underscore-min.js"></script>
<!-- Provide the URL to visualize.js -->
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>

<div style="float: left;">
    <h3>Heading format for 5th column</h3>
    Align:  <select id="headingFormatAlign">
                <option value="left">left</option>
                <option value="center">center</option>
                <option value="right">right</option></select>
    <br/>
    Background color: <input type="text" id="headingFormatBgColor" value=""/>
    <br/>
    Font size: <input type="text" id="headingFormatFontSize" value=""/>
    <br/>
    Font color: <input type="text" id="headingFormatFontColor" value=""/>
    <br/>
    Font name: <input type="text" id="headingFormatFontName" value=""/>
    <br/>
    Bold: <input type="checkbox" id="headingFormatFontBold" value="true"/>
    <br/>
    Italic: <input type="checkbox" id="headingFormatFontItalic" value="true"/>
    <br/>
    Underline: <input type="checkbox" id="headingFormatFontUnderline" value="true"/>
    <br/><br/>
    <button id="changeHeadingFormat">Change heading format</button>
</div>
<div style="float: left;">
    <h3>Details row format for 5th column</h3>
    Align: <select id="detailsRowFormatAlign">
        <option value="left">left</option>
        <option value="center">center</option>
        <option value="right">right</option></select>
    <br/>
    Background color: <input type="text" id="detailsRowFormatBgColor" value=""/>
    <br/>
    Font size: <input type="text" id="detailsRowFormatFontSize" value=""/>
    <br/>
    Font color: <input type="text" id="detailsRowFormatFontColor" value=""/>
    <br/>
    Font name: <input type="text" id="detailsRowFormatFontName" value=""/>
    <br/>
    Bold: <input type="checkbox" id="detailsRowFormatFontBold" value="true"/>
    <br/>
    Italic: <input type="checkbox" id="detailsRowFormatFontItalic" value="true"/>
    <br/>
    Underline: <input type="checkbox" id="detailsRowFormatFontUnderline" value="true"/>
    <br/><br/>
    <b>Number pattern:</b>
    <br/>
    Negative format: <input type="text" id="detailsRowFormatPatternNegativeFormat"/>
    <br/>
    Precision: <input type="text" id="detailsRowFormatPatternPrecision"/>
    <br/>
    Currency: <select id="detailsRowFormatPatternCurrency">
                    <option value="">----</option>
                    <option value="USD">USD</option>
                    <option value="EUR">EUR</option>
                    <option value="GBP">GBP</option>
                    <option value="YEN">YEN</option>
                    <option value="LOCALE_SPECIFIC">LOCALE_SPECIFIC</option>
            </select>
    <br/>
    Thousands grouping: <input type="checkbox" id="detailsRowFormatPatternGrouping" value="true"/>
    <br/>
    Percentage: <input type="checkbox" id="detailsRowFormatPatternPercentage" value="true"/>
    <br/><br/>
    <button id="changeDetailsRowFormat">Change details row format</button>
</div>
<div style="float: left;">
    <h3>Change label of 5th column</h3>
    <br/>
    Label <input type="text" id="label"/>
    <br/>
    <button id="changeLabel">Change label</button>
</div>
<div style="clear: both;"></div>

<!-- Provide a container for the report -->
<div id="container"></div>
```

## Conditional Formatting on Table Columns

The JIVE UI also supports conditional formatting so that you can change the appearance of a cell's contents based on its value. This example highlights cells in a given column that have a certain value by changing their text color and the cell background color. Note that the column name must be known ahead of time, for example by looking at your JRXML.

```
visualize({
    auth: { ...
    }
}, function (v) {
    // column name from JRXML (field name by default)
    var salesColumnName = "sales_fact_ALL.sales_fact_ALL__store_sales_2013",
        report = v.report({
            resource: "/public/Samples/Reports/04._Product_Results_by_Store_Type_Report",
            container: "#container",
            error: showError
        });

    $("#changeConditions").on("click", function() {
            report.updateComponent(salesColumnName, {
                conditions: [
                    {
                        operator: "greater",
                        value: 10,
                        backgroundColor: null,
                        font: {
                            color: "FF0000",
                            bold: true,
                            underline: true,
                            italic: true
                        }
                    },
                    {
                        operator: "between",
                        value: [5, 9],
                        backgroundColor: "00FF00",
                        font: {
                            color: "0000FF"
                        }
                    }
                ]
            })
            .then(printConditions)
            .fail(showError);
    });

    function printConditions(component){
        console.log("Conditions: "+ component.conditions);
    }

    function showError(err) {
           alert(err);
    }
});
```

This example has a single button that allows the user to apply the conditional formatting when the report is loaded:

```
<script src="http://code.jquery.com/jquery-2.1.0.js"></script>
<script src="http://underscorejs.org/underscore-min.js"></script>
<!-- Provide the URL to visualize.js -->
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>

<button id="changeConditions">Change conditions for numeric column</button>

<!-- Provide a container for the report -->
<div id="container"></div>
```

## Sorting Crosstab Columns

Crosstabs are more complex and do not have as many formatting options. This example shows how to sort the values in a given column of a crosstab (the rows are rearranged). Note that the code is slightly different than Sorting Table Columns.

```
visualize({
    auth: {
        name: "superuser",
        password: "superuser"
    }
}, function (v) {
    var column2,
    report = v.report({
        resource: "/public/MyReports/crosstabReport",
        container: "#container",
        events: {
            reportCompleted: function (status, error) {
                if (status === "ready") {
                    var columns = _.filter(report.data().components, function (component) {
                        return component.componentType == "crosstabDataColumn";
                    });

                    column2 = columns[1];
                    console.log(columns);
                }
            }
        },
        error: function (err) {
            alert(err);
        }
    });

    $("#sortAsc").on("click", function () {
        report.updateComponent(column2.id, {
            sort: {
                order: "asc"
            }
        }).fail(function (e) {
            alert(e);
        });
    });

    $("#sortDesc").on("click", function () {
        report.updateComponent(column2.id, {
            sort: {
                order: "desc"
            }
        }).fail(function (e) {
            alert(e);
        });
    });

    $("#sortNone").on("click", function () {
        report.updateComponent(column2.id, {
            sort:
        }).fail(function (e) {
            alert(e);
        });
    });
});
```

The associated HTML has the buttons to trigger the sorting:

```
<script src="http://code.jquery.com/jquery-2.1.0.js"></script>
<script src="http://underscorejs.org/underscore-min.js"></script>
<!-- Provide the URL to visualize.js -->
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>

<button id="sortAsc">Sort 2nd column ascending</button>
<button id="sortDesc">Sort 2nd column descending</button>
<button id="sortNone">Do not sort on 2nd column</button>

<!-- Provide a container for the report -->
<div id="container"></div>
```

## Sorting Crosstab Rows

This example shows how to sort the values in a given row of a crosstab (the columns are rearranged).

```
visualize({
    auth: { ...
    }
}, function (v) {
    var row,
    report = v.report({
        resource: "/public/MyReports/crosstabReport",
        container: "#container",
        events: {
            reportCompleted: function (status, error) {
                if (status === "ready") {
                    row = _.filter(report.data().components, function (component) {
                        return component.componentType == "crosstabRowGroup";
                    })[0];
                }
            }
        },
        error: function (err) {
            alert(err);
        }
    });

    $("#sortAsc").on("click", function () {
        report.updateComponent(row.id, {
            sort: {
                order: "asc"
            }
        }).fail(function (e) {
            alert(e);
        });
    });

    $("#sortDesc").on("click", function () {
        report.updateComponent(row.id, {
            sort: {
                order: "desc"
            }
        }).fail(function (e) {
            alert(e);
        });
    });

    $("#sortNone").on("click", function () {
        report.updateComponent(row.id, {
            sort:
        }).fail(function (e) {
            alert(e);
        });
    });
});
```

The associated HTML has the buttons to trigger the sorting:

```
<script src="http://code.jquery.com/jquery-2.1.0.js"></script>
<script src="http://underscorejs.org/underscore-min.js"></script>
<!-- Provide the URL to visualize.js -->
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>

<button id="sortAsc">Sort rows ascending</button>
<button id="sortDesc">Sort rows descending</button>
<button id="sortNone">Do not sort rows</button>

<!-- Provide a container for the report -->
<div id="container"></div>
```

## Implementing Search in Reports

The JIVE UI supports a search capability within the report. The following example relies on a page with a simple search input.

```
<input id="search-query" type="input" />
<button id="search-button">Search</button>
<!--Provide container to render your visualization-->
<div id="container"></div>
```

Then you can use the search function to return a list of matches in the report. In this example, the search button triggers the function and passes the search term. It uses the console to display the results, but you can use them to locate the search term in a paginated report.

```
visualize({
    auth: {
        name: "jasperadmin",
        password: "jasperadmin",
        organization: "organization_1"
    }
}, function (v) {

    //render report from provided resource
    var report = v.report({
        resource: "/public/Samples/Reports/AllAccounts",
        error: handleError,
        container: "#container"
    });

    $("#search-button").click(function(){
        report
        .search($("#search-query").val())
            .done(function(results){
                !results.length && console.log("The search did not return any results!");
                for (var i = 0; i < results.length; i++) {
                    console.log("found " + results[i].hitCount + " results on page: #" +
                                results[i].page);
                }
            })
            .fail(handleError);
    });


    //show error
    function handleError(err){
        alert(err.message);
    }

});
```

The search function supports several arguments to refine the search:

```
    $("#search-button").click(function(){
        report
        .search({
            text: $("#search-query").val(),
            caseSensitive: true,
            wholeWordsOnly: true
        })
           ...
```

## Providing Bookmarks in Reports

The JIVE UI also supports bookmarks that are embedded within the report. You must create your report with bookmarks, but then Visualize.js can make them available on your page. The following example has a container for the bookmarks and one for the report:

```
<div>
    <h4>Bookmarks</h4>
    <div id="bookmarksContainer"></div>
</div>
<!--Provide container to render your visualization-->
<div id="container"></div>
```

Then you need a function to read the bookmarks in the report and place them in the container. A handler then responds to clicks on the bookmarks.

```
visualize({
    auth: {
        name: "jasperadmin",
        password: "jasperadmin",
        organization: "Organization_1"
    }
}, function (v) {

    //render report from provided resource
    var report = v.report({
        // resource: "/public/Samples/Reports/AllAccounts",
        resource: "/reports/interactive/TableReport",
        error: handleError,
        container: "#container",
        events: {
            bookmarksReady: handleBookmarks
        }
    });

    //show error
    function handleError(err){
        alert(err.message);
    }

    $("#bookmarksContainer").on("click", ".jr_bookmark", function(evt) {
        report.pages({
            anchor: $(this).data("anchor")
        }).run();
    });

    // handle bookmarks
    function handleBookmarks(bookmarks, container) {
        var li, ul = $("<ul/>");
        !container && $("#bookmarksContainer").empty();
        container = container || $("#bookmarksContainer");

        $.each(bookmarks, function(i, bookmark) {
            li = $("<li><span class='jr_bookmark' title='Anchor: " + bookmark.anchor + ", page: " + bookmark.page + "' data-anchor='" + bookmark.anchor + "' data-page='" + bookmark.page + "'>" + bookmark.anchor + "</span></li>");
            bookmark.bookmarks && handleBookmarks(bookmark.bookmarks, li);
            ul.append(li);
        });

        container.append(ul);
    }
});
```

## Disabling the JIVE UI

The JIVE UI is enabled by default on all reports that support it. When the JIVE UI is disabled, the report is static and neither users nor your script can interact with the report elements. You can disable it in your `visualize.report` call as shown in the following example:

```
visualize({
    auth: { ...
    }
}, function (v) {
    v.report({
        resource: "/public/Samples/Reports/RevenueDetailReport",
        container: "#reportContainer",
        defaultJiveUi: { enabled: false },
        error: function (err) {
            alert(err.message);
        }
    });
});
```

Associated HTML:

```
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>
<p>JIVE UI is disabled on this Visualize.js report:</p>
<div id="reportContainer">Loading...</div>
```
