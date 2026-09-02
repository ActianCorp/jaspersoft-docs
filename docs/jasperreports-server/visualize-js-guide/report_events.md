---
title: API Usage - Report Events
description: "Depending on the size of your data, the report function can run for several seconds or minutes, just like reports in the JasperReports Server UI. You can listen for events that give the status of..."
---

# API Usage - Report Events

Depending on the size of your data, the `report` function can run for several seconds or minutes, just like reports in the JasperReports Server UI. You can listen for events that give the status of running reports and display pages sooner.

This chapter contains the following sections:

-   [Tracking Completion Status](#tracking-completion-status)
-   [Tracking Report Container Size](#tracking-report-container-size)
-   [Listening for Page Totals](#listening-for-page-totals)
-   [Listening for the Last Page](#listening-for-the-last-page)
-   [Customizing a Report's DOM Before Rendering](#customizing-a-reports-dom-before-rendering)

## Tracking Completion Status

By listening for the `reportCompleted` event, you can give information or take action when a report finishes rendering.

``` javascript
visualize({
    auth: { ...
    }
}, function (v) {
    var report = v.report({
        // run example with a very long report
        resource: "/public/Samples/Reports/RevenueDetailReport",
        container: "#container",
        events: {
            reportCompleted: function(status) {
                alert("Report status: "+ status+ "!");
            }
        },
        error: function(error) {
            alert(error);
        },
    });
});
```

## Tracking Report Container Size

By listening for the `responsiveBreakpointChanged` event, you can track when the container size has been passed from one interval to another.

``` javascript
visualize({
    auth: {...
    }
}, function(v) {
     let reportConfig = {
         resource: "/public/ResponsiveReport",
         container: "#container",
         reportContainerWidth: getContainerWidth(),
         events: {
               responsiveBreakpointChanged: function(error) {
                    if (error) {
                        console.log(error);
                     } else {
                         report.destroy();
                      // rerun report
                         reportConfig.reportContainerWidth = getContainerWidth();
                         report = v.report(reportConfig);
                            }
                       }
                    },
                    error: (e) => console.error(e.message || e)
            };
            let report = v.report(reportConfig);

            function getContainerWidth() {
                  return document.getElementById("container").clientWidth;
           }
 });
```

## Listening for Page Totals

By listening for the `changeTotalPages` event, you can track the filling of the report.

``` javascript
visualize({
    auth: { ...
    }
}, function (v) {
    var report = v.report({
        resource: "/public/Samples/Reports/AllAccounts",
        container: "#container",
        error: function(error) {
        alert(error);
        },
        events: {
            changeTotalPages: function(totalPages) {
            alert("Total Pages:" + totalPages);
        }
        }
    });
});
```

## Listening for the Last Page

Listening for the `pageFinal` event, lets you know when the last page of a running report has been generated.

``` javascript
visualize({
    auth: { ...
    }
}, function (v) {
    var report = v.report({
        // run example with a very long report
        resource: "/public/Samples/Reports/RevenueDetailReport",
        container: "#container",
        events: {
            pageFinal: function(el) {
                console.log(el);
                alert("Final page is rendered!");
            },
            reportCompleted: function(status) {
                alert("Report status: "+ status+ "!");
            }
        },
        error: function(error) {
            alert(error);
        },
    });
});
```

## Customizing a Report's DOM Before Rendering

By listening for the `beforeRender` event, you can access the Document Object Model (DOM) of the report to view or modify it before it is displayed. In the example the listener finds `span` elements and adds a color style and an attribute `my-attr="test"` to each one.

``` javascript
visualize({
    auth: { ...
    }
}, function (v) {
    // enable report chooser
    $(':disabled').prop('disabled', false);

    //render report from provided resource
    startReport();

    $("#selected_resource").change(startReport);

    function startReport () {
        // clean container
        $("#container").html("");
        // render report from another resource
        v("#container").report({
            resource: $("#selected_resource").val(),
            events:{
                beforeRender: function(el){
                    // find all spans
                    $(el).find(".jrPage td span")
                         .each(function(i, e){
                               // make them red
                               $(e).css("color","red")
                                   .attr("data-my-attr", "test");
                          });
                    console.log($(el).find(".jrPage").html());
                }
            }
        });
    };
});
```

The HTML page that displays the report uses a static list of reports in a drop-down selector, but otherwise needs only a container element. This is similar to the basic report example in [Rendering a Report](../../jasperreports-io/professional-user-guide/jasperreports-server-visualize.js-guide/displaying_reports.md), except that the JavaScript above will change the report before it's displayed.

``` html
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<!-- Provide the URL to visualize.js -->
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>
<select id="selected_resource" disabled="true" name="report">
    <option value="/public/Samples/Reports/1._Geographic_Results_by_Segment_Report">Geographic Results by Segment</option>
    <option value="/public/Samples/Reports/2_Sales_Mix_by_Demographic_Report">Sales Mix by Demographic</option>
    <option value="/public/Samples/Reports/3_Store_Segment_Performance_Report">Store Segment Performance</option>
    <option value="/public/Samples/Reports/04._Product_Results_by_Store_Type_Report">Product Results by Store Type</option>
</select>
<!-- Provide a container to render your visualization -->
<div id="container"></div>
```
