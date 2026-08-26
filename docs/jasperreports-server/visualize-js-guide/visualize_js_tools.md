---
title: Visualize.js Tools
description: This chapter provides two extended code examples that you can use to test various parts of your own Visualize.js scripts.
---

# Visualize.js Tools

This chapter provides two extended code examples that you can use to test various parts of your own Visualize.js scripts.

This chapter contains the following sections:

-   Checking the Scope in Visualize.js
-   CSS Diagnostic Tool

## Checking the Scope in Visualize.js

This example reads and displays the properties in the scope after `visualize.report` finishes rendering a report (success).

``` javascript
visualize({
    auth: { ...
    }
}, function (v) {

    createReport();

    $("#selected_resource").change(function () {
        //clean container
        $("#container").html("");
        createReport();
    });

     //enable report chooser
    $(':disabled').prop('disabled', false);

     function createReport(){
        //render report from another resource
        v("#container").report({
            resource: $("#selected_resource").val(),
            success: function(){
                 setTimeout(function () {
                    console.log("------------------Scope Check Results---------------------------");
                    console.log(scopeChecker.compareProperties(propertiesNames));
                    console.log("----------------------------------------------------------------");
                }, 5000);
            },
            error:handleError
        });
    }
    //show error
    function handleError(err){
        alert(err.message);
    }
});
```

The ScopeChecker is another JavaScript used in this example. It can either be a separate .js file or included in your HTML file as shown in this example:

``` javascript
<!-- JavaScript for ScopeChecker -->
<script>
    function ScopeChecker(scope) {
        this.scope = scope;
    }

    ScopeChecker.prototype.getPropertiesCount = function() {
        return this.getPropertiesNames().length;
    };

    ScopeChecker.prototype.getPropertiesNames = function() {
        return Object.keys(this.scope);
    };

    ScopeChecker.prototype.compareProperties = function(scope1PropertiesNames, scope2PropertiesNames) {
        if (!scope1PropertiesNames) {
            throw "Properties for scope 1 not specified";
        }
        if (!scope2PropertiesNames) {
            scope2PropertiesNames = this.getPropertiesNames();
        }

        var comparisonResult = {
            added: [],
            removed: [],
            madeUndefined: [],
            pollution: []
        };

        var i, j;
        for (i = 0; i < scope1PropertiesNames.length; i++) {
            comparisonResult.removed.push(scope1PropertiesNames[i]);
            for (j = 0; j < scope2PropertiesNames.length; j++) {
                if (scope1PropertiesNames[i] === scope2PropertiesNames[j]) {
                    comparisonResult.removed.pop();
                    break;
        }   }   }

        for (i = 0; i < scope2PropertiesNames.length; i++) {
            comparisonResult.added.push(scope2PropertiesNames[i]);
            for (j = 0; j < scope1PropertiesNames.length; j++) {
                if (scope2PropertiesNames[i] === scope1PropertiesNames[j]) {
                    comparisonResult.added.pop();

                    break;
        }   }   }
        for (i = 0; i < comparisonResult.added.length; i++) {
            if (this.scope[comparisonResult.added[i]] === undefined) {
                comparisonResult.madeUndefined.push(comparisonResult.added[i]);
            } else {
                comparisonResult.pollution.push(comparisonResult.added[i]);
        }   }

        return comparisonResult;
    };

    var propertiesNames = [];
    var scopeChecker = new ScopeChecker(window);
    propertiesNames = scopeChecker.getPropertiesNames();
</script>
<!-- Provide the URL to visualize.js -->
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>
<select id="selected_resource" name="report">
    <option value="/public/Samples/Reports/1._Geographic_Results_by_Segment_Report"
        >Geographic Results by Segment</option>
    <option value="/public/Samples/Reports/2_Sales_Mix_by_Demographic_Report"
        >Sales Mix by Demographic</option>
    <option value="/public/Samples/Reports/3_Store_Segment_Performance_Report"
        >Store Segment Performance</option>
    <option value="/public/Samples/Reports/04._Product_Results_by_Store_Type_Report"
        >Product Results by Store Type</option>
</select>
<!-- Provide a container to render your visualization -->
<div id="container"></div>
```

## CSS Diagnostic Tool

The CSS diagnostic tool lets you load various CSS libraries and see how they interact or interfere with the CSS that Visualize.js uses to render reports. It lets you choose your JasperReports Server from a static list, so that you may try different themes on different servers. After you load a report using `visualize.report`, you can choose to load a variety of popular CSS libraries and see if they affect your report. The list of reports to choose from is also a static list, as shown in the HTML code below.

The key feature of this tool is the ability to set the `isolateDOM` property on the visualize.report function call. This property modifies the CSS of the report so it doesn't conflict with other CSS libraries. The downside is that you can't use the `defaultJiveUi` property in conjunction with `isolateDOM`, and the tool enforces this by clearing the former if you select the latter.

Save the Javascript, HTML, and CSS for the CSS Diagnostic Tool to your environment and edit the files to use your server instances, reports, and Visualize.js code.

``` javascript
// ************ SETTINGS **********
var serverUrls = [
    "http://test.example.com:8080/jasperserver-pro",
    "http://cust.example.com:8080/jasperserver-pro",
    "http://localhost:8080/jasperserver-pro",
    "http://bi.example.com:8080/jasperserver-pro"
];
urlUsed = 3; // default used (one css loads from this server before visualize)
var reportsList =;
// ********************************
function setupLoaderV() {
    var html,
        radioTpl = '<input id="#id" type="radio" value="#value" name="confServer" /><label for="#id" title="#title" >#label</label><br/>';
    for (var i = 0, l = serverUrls.length; i < l; i++) {
        html = radioTpl.replace(/#id/g, "serverUrl_" + i)
            .replace(/#value/g, i)
            .replace(/#title/g, serverUrls[i])
            .replace("#label", serverUrls[i].split("/")[2]);

        $("#serverUrlsDiv").append(html);
        $("#serverUrl_" + i).prop("checked", i === urlUsed);
    }
}
function onLoad() {
    setupLoaderV();
    $( "#buttons_ui button:first" ).button({
      icons: {
        primary: "ui-icon-locked"
      },
      text: false
    }).next().button({
      icons: {
        primary: "ui-icon-locked"
      }
    }).next().button({
      icons: {
        primary: "ui-icon-gear",
        secondary: "ui-icon-triangle-1-s"
      }
    }).next().button({
      icons: {
        primary: "ui-icon-gear",
        secondary: "ui-icon-triangle-1-s"
      },
      text: false
    });
    var availableTags = [
      "ActionScript",
      "AppleScript",
      "Asp",
      "BASIC",
      "C",
      "C++",
      "Clojure",
      "COBOL",
      "ColdFusion",
      "Erlang",
      "Fortran",
      "Groovy",
      "Haskell",
      "Java",
      "JavaScript",
      "Lisp",
      "Perl",
      "PHP",
      "Python",
      "Ruby",
      "Scala",
      "Scheme"
    ];
    $( "#tags" ).autocomplete({
      source: availableTags
    });
    $("#datepicker-user").datepicker();
    $("#datepicker-user2").datepicker();
    $( "#tabs" ).tabs();

    $("#loadV").click(loadV);
    fillSheetList();
    loadCSS();
    $(window).on("keypress", function(e){
        var char = e.charCode - 49;
        if (char < 1 && char > 9) return;
        var input = $("#sheetList > li > input")[char];
        if (!input) return;
        $(input).trigger( "click" )
    });
    $("#isolateDOM").change(function() {
        $("#defaultJiveUi").attr({
            "disabled": $(this).is(':checked') ? "disabled" : null,
            "checked": false
        });
    });
}

function loadCSS() {

    var CSSlibs = [
        { disable: true, href: serverUrls[urlUsed] + "/themes/reset.css" },
        { disable: true, href: "//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" },
        { disable: true, href: "//cdnjs.cloudflare.com/ajax/libs/normalize/3.0.1/normalize.min.css" },
        { disable: true, href: "//cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.css" },
        { disable: true, href: "http://yui.yahooapis.com/3.16.0/build/cssreset/cssreset-min.css" },
        { disable: true, href: "http://tantek.com/log/2004/undohtml.css" },
        { disable: true, href: "//cdnjs.cloudflare.com/ajax/libs/sanitize.css/2.0.0/sanitize.css" },
        { disable: false, href: "http://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/vader/jquery-ui.css" }
    ];
    var head = $("head"),
        link;

    for (var i = 0, l = CSSlibs.length; i < l; i++) {
        link = $("<link rel='stylesheet' type='text/css' href='" + CSSlibs[i].href + "' />");
        head.append(link);
        if (CSSlibs[i].disable) {
            link.on("load", (function(link){
                return function() {
                    $(link)[0].disabled = true;
                    fillSheetList();
                }
            })(link));
        }
        link.on("error", (function(link){
            return function() {
                $(link)[0].href += "-LOAD_ERROR"
                fillSheetList();
            }
        })(link));
    }
}
function loadV() {
    var locale = $('#confLocale').val() || "en";
    urlUsed = $('input[name="confServer"]:checked', '#containerLoadV').val();
    var useOptimize = $('#confOptimized').is(":checked");
    $.getScript(serverUrls[urlUsed] + "/client/visualize.js?_opt=" + useOptimize.toString(), function () {
        visualize({
            auth: {
                name: "superuser",
                password: "superuser",
                locale: locale
            }
        }, function (v) {
            fillSheetList();
            $("#loadV").remove();
            $("#loadReports").show();

            $("#addReport").on("click", function(){
                var uri = $(),
                    defaultJiveUi,
                    isolateDOM
                createReport(
                    v,
                    $("#selected_resource").val(),
                    $("#defaultJiveUi").is(':checked'),
                    $("#isolateDOM").is(':checked')
                );
            });
        });
    });
    $("#loadV").html("Loading...").attr("disabled", "disabled");
       $("#containerLoadV").addClass("disabled").children("input").attr("disabled", "disabled");
}
function createReport(v, uri, defaultJiveUi, isolateDOM) {
    var reportIndex = (+new Date() + "").substr(-5);
    console.log(reportIndex)
    reportsList[reportIndex] = "";
    fillReportsList();
    $("#reportContainer").append("<div id='vis_" + reportIndex + "'></div>");
    $("#vis_" + reportIndex).addClass("qwe");
    v.report({
        server: serverUrls[urlUsed],
        resource: uri,
        container: "#vis_" + reportIndex,
        error: function (err) {
            alert(err.message);
        },
        defaultJiveUi: { enable: defaultJiveUi },
        isolateDOM: isolateDOM || false,
        success: function () {
            fillSheetList();
            reportsList[reportIndex] = uri;
            fillReportsList();
            //processIC(v, uri);
        }
    });

}
function processIC (v, reportUri) {
    var inputControls = v.inputControls({
        resource: reportUri,
        success: function(data) {
            console.log(data);
        }
    });
}
function fillReportsList() {
    $("#reportsList").html("");
    for (var reportIndex in reportsList) {
        if (!reportsList.hasOwnProperty(reportIndex)) continue;
        var uri = reportsList[reportIndex];
        //if (uri)
        var li = $("<li>" + (/[^\/][\w\.]+$/g.exec(reportsList[reportIndex]) || "Loading...") + " (<a href='#'>remove</a>)</li>");
        $("#reportsList").append(li);
        li.children("a").click((function (reportIndex) {
            return function (e) {
                e.preventDefault();
                $("#vis_" + reportIndex).remove();
                delete reportsList[reportIndex];
                $(e.target).parent().remove();
            };
        })(reportIndex));

    }

}
function fillSheetList() {
    var sheets = $("link");
    var checkboxLI = '<li>#index: <input type="checkbox" id="#id" checked="checked"><label for="#id" title="#title">#label</label></li>',
        sheetPath = '',
        sheetPathSplitted = '',
        html = "";

    $("#sheetList").html("");

    for (var i = 0; i < sheets.length; i++) {

        if (sheets[i].href === null) continue;
        sheetPath = sheets[i].href;

        sheetPathSplitted = sheetPath.split("/");
        html = checkboxLI.replace(/#id/g, "sheetItem_" + i)
            .replace(/#index/g, i+1)
            .replace("#title", sheetPath)
            .replace("#label", sheets[i].label || sheetPathSplitted[sheetPathSplitted.length - 1]);

        $("#sheetList").append(html);
        $("#sheetItem_" + i).change(function (e) {
            var id = this.id.split("_")[1];
            $("link")[id].disabled = !$(this).is(':checked');
        });
        $("#sheetItem_" + i)[0].checked = !$("link")[i].disabled;
    }
}
```

The HTML for the CSS diagnostic tool contains a static list of reports to load. Add your own reports to this list.

``` html
<script type="text/javascript">
    window.addEventListener("load", onLoad);
</script>
<div style="width:327px;float: left;border-right:1px solid #333;margin-right:2px">
     <h4>Settings</h4>

    <div>
        <div id="containerLoadV">
            <div id="serverUrlsDiv"></div>
            <label for="confLocale">Locale: </label>
            <input id="confLocale" value="en" />
            <!-- options -->
            <br/>
            <input id="confOptimized" type="checkbox" />
            <label for="confOptimized" >- use optimized javascript </label>
            <br/>
            <button id="loadV">Load visualize</button>
            <br/>
        </div>
        <div id="loadReports" style="display:none;">
            <div>Add report:</div>
            <input id="defaultJiveUi" type="checkbox" checked="checked" />
            <label for="defaultJiveUi" >- default JIVE UI </label>
            <br/>
            <input id="isolateDOM" type="checkbox" />
            <label for="isolateDOM" >- isolate DOM </label>
            <br/>

            <select id="selected_resource" name="report" style="width:195px">
                <option value="">-</option>
                <option value="/public/Samples/Reports/1._Geographic_Results_by_Segment_Report"
                    >Geographic Results by Segment</option>
                <option value="/public/Samples/Reports/2_Sales_Mix_by_Demographic_Report"
                    >Sales Mix by Demographic</option>
                <option value="/public/Samples/Reports/3_Store_Segment_Performance_Report"
                    >Store Segment Performance</option>
                <option value="/public/Samples/Reports/04._Product_Results_by_Store_Type_Report"
                    >Product Results by Store Type</option>
            </select>
            <button id="addReport">Add</button>
        </div>
        <p>Loaded reports list:</p>
        <ul id="reportsList" style="overflow-wrap: break-word;display:inline;"></ul>
        <div style="border-top:1px solid #333;width:100%"></div>
        <h4>Stylesheets list:</h4>
        <em>Use 1-9 keys to enable\disable css libs.</em>
        <ul id="sheetList" style="display:inline;"></ul>
    </div>

    <div style="border-top:1px solid #333;width:100%"></div>

    <div style="width:320px;">
         <h4>User components</h4>

        <!-- detepicker -->
        <div style="height: 240px;">
            <div id="datepicker-user"></div>
        </div>
        <input id="datepicker-user2"/>
        <!-- /datepicker -->
        <!-- autocomplete -->
        <div class="ui-widget">
            <label for="tags">Autocomplete</label>
            <input id="tags"/>
        </div>
        <!-- autocomplete -->
        <!-- tabs -->
        <div id="tabs">
          <ul>
            <li><a href="#tabs-1">Nunc</a></li>
            <li><a href="#tabs-2">Pr dor</a></li>
            <li><a href="#tabs-3">A laia</a></li>
          </ul>
          <div id="tabs-1">
            <p>Proin elit arcu Aliquam sodales tortor vitae ipsum. Aliquam nulla. Duis aliquam molestie erat. Ut et mauris vel pede varius sollicitudin. Sed ut dolor nec orci tincidunt interdum. Phasellus ipsum. Nunc tristique tempus lectus.</p>
          </div>
          <div id="tabs-2">
            <p>Morbi tincidunt, tellus pellentesque pretium posuere, felis lorem euismod felis, eu ornare leo nisi vel felis. Mauris consectetur tortor et purus.</p>
          </div>
          <div id="tabs-3">
            <p>Ut sagittis. Donec nisi lectus, feugiat porttitor, tempor ac, tempor vitae, pede. Aenean vehicula velit eu tellus interdum rutrum. Maecenas commodo. Pellentesque nec elit. Fusce in lacus. Vivamus a libero vitae lectus hendrerit hendrerit.</p>
          </div>
        </div>
        <!-- /tabs -->
        <!-- buttons -->
        <div id="buttons_ui">
            <button>Button with icon only</button>
            <button>Button with icon on the left</button>
            <button>Button with two icons</button>
            <button>Button with two icons and no text</button>
        </div>
        <!-- /buttons -->
    </div>

</div>
<div style="margin-left:330px;height:100%">
    <div id="reportContainer"></div>
</div>
```

Associated CSS:

``` text
.qwe {
    height: 100%;
}
#reportContainer {
    height: 100%;
}
body, html {
    height: 100%;
}
#containerLoadV.disabled {
    color: #666;
}

/**
  * Break something: modify the CSS here to something visibly wrong.
  * Add more elements, classes, or IDs to see if they affect Visualize.js content.
  */

table {
    font-size: 25px;

}
```
