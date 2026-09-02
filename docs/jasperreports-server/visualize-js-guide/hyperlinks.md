---
title: API Usage - Hyperlinks
description: Both reports and dashboards include hyperlinks (URLs) that link to websites or other reports. Visualize.js gives you access to the links so that you can customize them or open them differently. For...
---

# API Usage - Hyperlinks

Both reports and dashboards include hyperlinks (URLs) that link to websites or other reports. Visualize.js gives you access to the links so that you can customize them or open them differently. For links generated in the report, you can customize both the appearance and the container where they are displayed.

This chapter contains the following sections:

-   [Structure of Hyperlinks](../../jasperreports-io/professional-user-guide/jasperreports-server-visualize.js-guide/hyperlinks.md)
-   [Customizing Links](#customizing-links)
-   [Drill-Down in Separate Containers](#drill-down-in-separate-containers)
-   [Accessing Data in Links](#accessing-data-in-links)

## Structure of Hyperlinks

The following JSON schema describes all the parameters on links, although not all are present in all cases.

``` text
"jrLink": {
    "title": "JR Hyperlink",
    "description": "A JSON Schema describing JR hyperlink",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties":{
        "id": {
            "type": "string",
            "description": "Hyperlink id, reflected in corresponding attribute in DOM. Is not used for AdHocExecution hyperlink type."
        },
        "type": {
            "type": "string",
            "description": "Hyperlink type. Default types are LocalPage, LocalAnchor, RemotePage, RemoteAnchor, Reference, ReportExecution, AdHocExecution. Custom hyperlink types are possible"
        },
        "target": {
            "type": "string",
            "description": "Hyperlink target. Default targets are Self, Blank, Top, Parent. Custom hyperlink targets are possible"
        },
        "tooltip": {
            "type": "string",
            "description": "Hyperlink tooltip"
        },
        "href": {
            "type" : "string",
            "description": "Hyperlink reference. Is an empty string for LocalPage, LocalAnchor and ReportExecution hyperlink types"
        },
        "parameters": {
            "type": "object",
            "description": "Hyperlink parameters. Any additional parameters for hyperlink"
        },
        "resource": {
            "type": "string",
            "description": "Repository resource URI of resource mentioned in hyperlink. For LocalPage and LocalAnchor points to current report, for ReportExecution - to _report parameter"
        },
        "pages": {
            "type": ["integer", "string"],
            "description": "Page to which hyperlink points to. Is actual for LocalPage, RemotePage and ReportExecution hyperlink types"
        },
        "anchor": {
            "type": "string",
            "description": "Anchor to which hyperlink points to. Is actual for LocalAnchor, RemoteAnchor and ReportExecution hyperlink types"
        }
    },
    "required": ["type", "id"]
}
```

## Customizing Links

You can customize the appearance of link elements in a generated report in two ways:

-   The `linkOptions` exposes the `beforeRender` event to which you can add a listener with access to the links in the document as element pairs.
-   The normal click event lets you add a listener that can access to a link when it's clicked.

``` javascript
visualize({
    auth: {
        name: "jasperadmin",
        password: "jasperadmin",
        organization: "organization_1"
    }
},function (v) {
    v("#container1").report({
        resource: "/AdditionalResourcesForTesting/Drill_Reports_with_Controls/main_report",
        linkOptions: {
            beforeRender: function (linkToElemPairs) {
                linkToElemPairs.forEach(function (pair) {
                    var el = pair.element;
                    el.style.backgroundColor = "red";
                });
            },
            events: {
                "click": function(ev, link){
                    if (confirm("Change color of link id " + link.id + " to green?")){
                        ev.currentTarget.style.backgroundColor = "green";
                        ev.target.style.color = "#FF0";
                    }
                }
            }
        },
        error: function (err) {
            alert(err.message);
        }
    });
});
```

## Drill-Down in Separate Containers

By using the method of listing for clicks on hyperlinks, you can write a visualize.js script that sets the destination of drill-down report links to another container. This way, you can create display layouts or overlays for viewing drill-down links embedded in your reports. This sample code also changes the cursor for the embedded links, so they are more visible to users.

``` javascript
visualize({
    auth: {
        name: "jasperadmin",
        password: "jasperadmin",
        organization: "organization_1"
    }
}, function (v) {

    v("#main").report({
        resource: "/MyReports/Drill_Reports_with_Controls/main_report",
        linkOptions: {
            beforeRender: function (linkToElemPairs) {
                linkToElemPairs.forEach(showCursor);
            },
            events: {
                "click": function(ev, link){
                   if (link.type == "ReportExecution"){
                        v("#drill-down").report({
                            resource: link.parameters._report,
                            params: {
                                city: [link.parameters.city],
                                country: link.parameters.country,
                                state: link.parameters.state
                            },
                        });
                    }
                     console.log(link);
                }
            }
        },
        error: function (err) {
            alert(err.message);
        }
    });
    function showCursor(pair){
        var el = pair.element;
        if (typeof(el) != "undefined") {
            el.style.cursor = "pointer";
        }
    }

});
```

Associated HTML:

``` html
<script src="http://underscorejs.org/underscore.js"></script>
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<!-- Provide the URL to visualize.js -->
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>
<!-- Provide a container for the main report and one for the drill-down -->
<div>
    <div style="width:830px;" id="main"></div>
    <div style="width:500px;" id="drill-down"></div>
</div>
```

Associated CSS:

``` bash
#main{
   float: left;
}

#drill-down{
    float: left;
}
```

## Accessing Data in Links

In this example, we access the hyperlinks through the `data.links` structure after the report has successfully rendered. From this structure, we can read the tooltips that were set in the JRXML of the report. The script uses the information in the tooltips of all links in the report to create a drop-down selector of city name options.

By using link tooltips, your JRXML can create reports that pass runtime information to the display logic in your JavaScripts.

``` javascript
visualize({
    auth: {
        name: "jasperadmin",
        password: "jasperadmin",
        organization: "organization_1"
    }
}, function (v) {

    var $select = $("#selectCity"),
        report = v.report({
            resource: "/MyReports/Drill_Reports_with_Controls/main_report",
            container: "#main",
            success: refreshSelect,
            error: showError
    });
    function refreshSelect(data){
        console.log(data);
        var options = data.links.reduce(function(memo, link){
                console.log(link);
                return memo + ""+link.tooltip+"";
            },"");
        $select.html(options);
    }

    $("#previousPage").click(function() {
        var currentPage = report.pages() || 1;
        goToPage(--currentPage);
    });

    $("#nextPage").click(function() {
        var currentPage = report.pages() || 1;
        goToPage(++currentPage);
    });

    function goToPage(numder){
        report
            .pages(numder)
            .run()
                .done(refreshSelect)
                .fail(showError);
    }

    function showError(err){
        alert(err.message);
    }

});
```

Associated HTML:

``` html
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<!-- Provide the URL to visualize.js -->
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>
<select id="selectCity"></select>
<button id="previousPage">Previous Page</button>
<button id="nextPage">Next Page</button>
<!-- Provide a container for the main report -->
<div>
    <div style="width:20px;"></div>
    <div style="width:500px;" id="main"></div>
</div>
```

Associated CSS:

``` bash
#main{
   float: left;
}
```
