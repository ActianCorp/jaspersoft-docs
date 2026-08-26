---
title: JavaScript API Reference - Errors
description: This chapter describes common errors and explains how to handle them with Visualize.js.
---

# JavaScript API Reference - Errors

This chapter describes common errors and explains how to handle them with Visualize.js.

This chapter describes common errors and explains how to handle them with the JasperReports IO Javascript API.

This chapter contains the following sections:

-   Error Properties
-   Common Errors
-   Catching Initialization and Authentication Errors
-   Catching Search Errors
-   Validating Search Properties
-   Catching Report Errors
-   Catching Input Control Errors
-   Validating Input Controls

## Error Properties

The properties structure for `Generic Errors` is defined as follows:

``` json
{
    "title": "Generic Errors",
    "description": "A JSON Schema describing Visualize Generic Errors",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "errorCode": {
           "type": "string"
        },
        "message": {
            "type": "string"
        },
        "parameters":{
            "type": "array"
        }
    },
    "required": ["errorCode", "message"]
}
```

## Common Errors

The following table lists common errors, their messages, and causes.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Error</th>
<th><span>Message</span> - Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Page or app not responding</td>
<td><em>{no_message}</em> - If your page or web application has stopped working without notification or errors, check that the server providing <span>visualize.js</span> <span>JasperReports IO JavaScript API</span> is accessible and returning scripts.</td>
</tr>
<tr>
<td><code>unexpected.error</code></td>
<td><em>An unexpected error has occurred</em> - In most of cases this is either a JavaScript exception or an HTTP 500 (Internal Server Error) response from server.</td>
</tr>
<tr>
<td><code>schema.validation.error</code></td>
<td><em>JSON schema validation failed: {error_message}</em> - Validation against schema has failed. Check the <code>validationError</code> property in object for more details.</td>
</tr>
<tr>
<td><code>unsupported.</code><br />
<code>configuration.error</code></td>
<td><em>{unspecified_message}</em> - This error happens only when <code>isolateDom = true</code> and <code>defaultJiveUi.enabled = true</code>. These properties are mutually exclusive.</td>
</tr>
<tr>
<td><code>authentication.error</code></td>
<td><em>Authentication error</em> - Credentials are not valid or session has expired.</td>
</tr>
<tr>
<td><code>container.not.found.error</code></td>
<td><em>Container was not found in DOM</em> - The specified container was not found in the DOM:error.</td>
</tr>
<tr>
<td><code>report.execution.failed</code></td>
<td><em>Report execution failed</em> - The report failed to run on the server.</td>
</tr>
<tr>
<td><code>report.execution.cancelled</code></td>
<td><em>Report execution was canceled</em> - Report execution was canceled.</td>
</tr>
<tr>
<td><code>report.export.failed</code></td>
<td><em>Report export failed</em> - The report failed to export on the server.</td>
</tr>
<tr>
<td><code>licence.not.found</code></td>
<td><span><span>JRS missing appropriate license</span> </span> <span><span>JRIO missing appropriate license</span></span>- The server's license was not found.</td>
</tr>
<tr>
<td><code>licence.expired</code></td>
<td><span><span>JRS missing appropriate license</span> </span> <span><span>JRIO missing appropriate license</span></span> - The server's license has expired.</td>
</tr>
<tr>
<td><code>resource.not.found</code></td>
<td><em>Resource not found in Repository</em> - Either the resource doesn't exist in the repository or the user doesn't have permissions to read it.</td>
</tr>
<tr>
<td><code>export.pages.out.range</code></td>
<td><em>Requested pages {0} out of range</em> - The user requested pages that don't exist in the current export.</td>
</tr>
<tr>
<td><code>input.controls.</code><br />
<code>validation.error</code></td>
<td><em>{server_error_message}</em> - The wrong input control params were sent to the server.</td>
</tr>
</tbody>
</table>

## Catching Initialization and Authentication Errors

Visualize.js is designed to have many places where you can catch and handle errors. The visualize function definition, as shown in [Contents of the Visualize.js Script](visualize_js_api_reference.md), is:

``` text
function visualize(properties, callback, errorback, always)
```

During initialization and authentication, you can handle errors in the third parameter named `errorback` (an error callback). Your application would then have this structure:

``` javascript
visualize({
    auth : { ...
    }
}, function(){

    // your application logic

}, function(err){

    // handle all initialization and authentication errors here

})
```

## Catching Search Errors

One way to handle search errors is to specify an error handler as the second parameter of `run`:

``` javascript
new ResourcesSearch({
    server:"http://localhost:8080/jasperserver-pro",
    folderUri: "/public",
    recursive: false
})).run( usefulFunction, function(error){

    alert(error);

}))
```

Another way to handle search errors is to specify a function as the third parameter of `run`. This function is an `always` handler that runs every time when operation ends.

``` javascript
new ResourcesSearch({
    server:"http://localhost:8080/jasperserver-pro",
    folderUri: "/public",
    recursive: false
})).run(usefulFunction, errorHandler, function(resultOrError){

    alert(resultOrError);

}))
```

## Validating Search Properties

You can also validate the structure of the search properties without making an actual call to the search function:

``` javascript
var call = new ResourcesSearch({
    server:"http://localhost:8080/jasperserver-pro",
    folderUri: "/public",
    recursive: false
}));

var error = call.validate();

if (!error){
    // valid
} else {
    // invalid, read details from error
}
```

## Catching Report Errors

To catch and handle errors when running reports, define the contents of the `err` function as shown in the following sample:

``` javascript
visualize({
    auth : { ...
    }
}, function(v){

    var report = v.report({
        error: function(err){
            // invoked once report is initialized and has run
        }
    });

    report
        .run()
        .fail(function(err){
            // handle errors here
        });

)
```

To catch and handle errors when running reports, define the contents of the `err` function as shown in the following sample:

``` javascript
jrio.config({
    ...
});
jrio(function(jrioClient) {

    var report = jrioClient.report({
        error: function(err){
            // invoked once report is initialized and has run
        }
    });

    report
        .run()
        .fail(function(err){
            // handle errors here
        });

)
```

## Catching Input Control Errors

Catching and handling input control errors is very similar to handling report errors. Define the contents of the `err` function that gets invoked in error conditions, as shown in the following sample:

``` javascript
visualize({
    auth : { ...
    }
}, function(v){

    var ic = v.inputControls({
        error: function(err){
            // invoked once input control is initialized
        }
    });

    inputControls
        .run()
        .fail(function(err){
            // handle errors here
        });

)
```

## Validating Input Controls

You can also validate the structure of your input controls without making an actual call. However, the values of the input controls and their relevance to the named resource are not checked.

``` javascript
var ic = new InputControls({
    server: "http://localhost:8080/jasperserver-pro",
    resource: "/public/my_report",
    params: {
        "Country_multi_select":["Mexico"],
        "Cascading_state_multi_select":["Guerrero", "Sinaloa"]
    }
});

var error = ic.validate();

if (!error){
    // valid
} else {
    // invalid, read details from error
}
```
