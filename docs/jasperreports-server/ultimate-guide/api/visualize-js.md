---
title: Visualize.js API
description: "The Visualize.js API is a JavaScript library that allows web pages and web applications to embed JasperReports Server. The Visualize.js API was introduced in release 5.6, and Jaspersoft continues to..."
---

# Visualize.js API

The Visualize.js API is a JavaScript library that allows web pages and web applications to embed JasperReports Server. The Visualize.js API was introduced in release 5.6, and Jaspersoft continues to add new features to it. This section gives a brief summary of Visualize.js. For complete documentation, see the *JasperReports Server Visualize.js Guide*.

Being a native JavaScript API, Visualize.js lets you design your own dynamic HTML interface for the reports you want to display and embed the report anywhere in your page or application. This is best demonstrated with a very simple example that consists of a web page containing a list of reports for the user to choose, and a container where you want the report to appear:

``` html
<!--Provide the URL to visualize.js-->
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>
<select id="selected_resource" disabled="true" name="report">
    <option value="/public/Samples/Reports/1._Geographic_Results_by_Segment_Report">Geographic Results by Segment</option>
    <option value="/public/Samples/Reports/2_Sales_Mix_by_Demographic_Report">Sales Mix by Demographic</option>
    <option value="/public/Samples/Reports/3_Store_Segment_Performance_Report">Store Segment Performance</option>
    <option value="/public/Samples/Reports/04._Product_Results_by_Store_Type_Report">Product Results by Store Type</option>
</select>
<!--Provide a container to render your visualization-->
<div id="container"></div>
```

Note that the first line of the HTML above loads the Visualize.js library. You can then write the following JavaScript code to display the report the user selects from the list.

``` javascript
visualize({
    auth: { ...
    }
}, function (v) {

    //render report from provided resource
    v("#container").report({
        resource: $("#selected_resource").val(),
        error: handleError
    });

    $("#selected_resource").change(function () {
        //clean container
        $("#container").html("");
        //render report from another resource
        v("#container").report({
            resource: $("#selected_resource").val(),
            error:handleError
        });
    });

    //enable report chooser
    $(':disabled').prop('disabled', false);

    //show error
    function handleError(err){
        alert(err.message);
    }

});
```

The Visualize.js API renders interactive reports just like JasperReports Server, but within your own page. Users can sort columns, filter values, and even set conditional colors on Visualize.js reports. The Visualize.js API also lets you interact with and modify the DOM (Document Object Model) of the report if you want to make these same changes programmatically.

If your reports accept parameter values, your JavaScript can update the `params` object of the report properties and invoke the `run` function again.

``` text
    // elsewhere in your JavaScript
    // update report with new parameters
    report
        .params({ "Country": ["USA"] })
        .run();
```

The API also provides functions to list the reports in the repository and get the list of report parameters. The example above is trivial, but the power of Visualize.js comes from this simple code. You can create dynamic user interfaces that allow your users to select the reports they want to see and to set the parameters they want.

Furthermore, with JavaScript you can perform database lookups or your own calculations to provide values. Your values could be based on 3rd party API calls triggered from other parts of the page or other pages in your app. When your reports can respond to dynamic events, they become truly embedded and much more relevant to the user.

For further examples and reference documentation, see the *JasperReports Server Visualize.js Guide*.
