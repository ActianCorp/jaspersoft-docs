---
title: API Reference - resourcesSearch
description: The resourcesSearch function performs searches in the repository to find content that can be displayed by visualize.js.
---

# API Reference - resourcesSearch

The `resourcesSearch` function performs searches in the repository to find content that can be displayed by visualize.js.

This chapter contains the following sections:

-   [Search Properties](#search-properties)
-   [Search Functions](#search-functions)
-   [Finding Resources](#finding-resources)
-   [Reusing a Search Instance](#reusing-a-search-instance)
-   [Reusing Search Results](#reusing-search-results)
-   [Discovering Available Types](#discovering-available-types)

## Search Properties

The properties structure passed to the `resourcesSearch` function is defined as follows:

``` json
{
    "type": "object",
    "properties": {
        "server": {
            "type": "string",
            "description": "Url to JRS instance."
        },
        "q": {
            "type": "string",
            "description": "Query string. Search for occurrence in label or description of resource."
        },
        "folderUri": {
            "type": "string",
            "description": "Parent folder URI.",
            "pattern": "^/\\w*(/\\w+)*$"
        },
        "types": {
            "type": "array",
            "description": "Type of resources to search.",
            "items": {
                "type":"string",
                "enum": [
                    "folder", "dataType", "jdbcDataSource", "awsDataSource", "jndiJdbcDataSource",
                    "virtualDataSource", "customDataSource", "beanDataSource", "xmlaConnection",
                    "listOfValues", "file", "reportOptions", "dashboard", "adhocDataView",
                    "query", "olapUnit", "reportUnit", "domainTopic", "semanticLayerDataSource",
                    "secureMondrianConnection", "mondrianXmlaDefinition", "mondrianConnection",
                    "inputControl"
                ]
            }
        },
        "offset": {
            "type": "integer",
            "description": "Pagination. Index of first resource to show.",
            "minimum": 0
        },
        "limit": {
            "type": "integer",
            "description": "Pagination. Resources count per page.",
            "minimum": 0
        },
        "recursive": {
            "type": "boolean",
            "description": "Flag indicates if search should be recursive."
        },
        "sortBy": {
            "type": "string",
            "description": "Field to sort on.",
            "enum": [
                "uri",
                "label",
                "description",
                "type",
                "creationDate",
                "updateDate",
                "accessTime",
                "popularity"
            ]
        },
        "accessType": {
            "type": "string",
            "description": "Filtering by type of access, e.g. what was done with resource.",
            "enum": [
                "viewed",
                "modified"
            ]
        },
        "showHiddenItems": {
            "type": "boolean",
            "description": "Flag indicates if hidden items should present in results."
        },
        "forceTotalCount": {
            "type": "boolean",
            "description": "If true, Total-Count header is always set (impact on performance),
                            otherwise - in first page only"
        }
    },
    "required": ["server"]
}
```

## Search Functions

The `resourcesSearch` function exposes the following functions:

``` javascript
define(function () {

    /**
     * Constructor. Takes context as argument.
     * @param contextObj - map of properties.
     */
    function ResourcesSearch(contextObj);

    /**
     * Get/Set 'q' parameter of the query
     * @param contextObj - map of properties.
     * @returns this if 'value' sent to the method,
     *          otherwise returns current value of the parameter
     */
    ResourcesSearch.prototype.q= function(value);

    /**
     * Get/Set 'folderUri' parameter of the query
     * @param value - new value, optional
     * @returns this if 'value' sent to the method,
     *          otherwise returns current value of the parameter
     */
    ResourcesSearch.prototype.folderUri= function(value);

    /**
     * Get/Set 'type' parameter of the query
     * @param value - new value, optional
     * @returns this if 'value' sent to the method,
     *          otherwise returns current value of the parameter
     */
    ResourcesSearch.prototype.type= function(value);

    /**
     * Get/Set 'offset' parameter of the query
     * @param value - new value, optional
     * @returns this if 'value' sent to the method,
     *          otherwise returns current value of the parameter
     */
    ResourcesSearch.prototype.offset= function(value);

    /**
     * Get/Set 'limit' parameter of the query
     * @param value - new value, optional
     * @returns this if 'value' sent to the method,
     *          otherwise returns current value of the parameter
     */
    ResourcesSearch.prototype.limit= function(value);


    /**
     * Get/Set 'recursive' parameter of the query
     * @param value - new value, optional
     * @returns this if 'value' sent to the method,
     *          otherwise returns current value of the parameter
     */
    ResourcesSearch.prototype.recursive= function(value);
    /**
     * Get/Set 'sortBy' parameter of the query
     * @param value - new value, optional
     * @returns this if 'value' sent to the method,
     *          otherwise returns current value of the parameter
     */
    ResourcesSearch.prototype.sortBy= function(value);

    /**
     * Get/Set 'accessType' parameter of the query
     * @param value - new value, optional
     * @returns this if 'value' sent to the method,
     *          otherwise returns current value of the parameter
     */
    ResourcesSearch.prototype.accessType= function(value);

    /**
     * Get/Set 'showHiddenItems' parameter of the query
     * @param value - new value, optional
     * @returns this if 'value' sent to the method,
     *          otherwise returns current value of the parameter
     */
    ResourcesSearch.prototype.showHiddenItems= function(value);

    /**
     * Get/Set 'forceTotalCount' parameter of the query
     * @param value - new value, optional
     * @returns this if 'value' sent to the method,
     *          otherwise returns current value of the parameter
     */
    ResourcesSearch.prototype.forceTotalCount= function(value);

    return ResourcesSearch;
});
```

## Finding Resources

The following code example shows how to perform a search and store the results in a variable:

``` javascript
// Populate the repository list
JRSClient.resourcesSearch({
// server: serverUrl,
folderUri:"/public/Samples",
recursive:true,
types:["reportUnit", "dashboard"],
success:listRepository,
error:function (err)
{ alert(err); }

});
```

The next two examples show different ways of handling results after making a simple repository search in the Public folder.

``` javascript
new ResourcesSearch({
    server:"http://localhost:8080/jasperserver-pro",
    folderUri: "/public",
    recursive: false
})).run(function(resourceLookups){
    // results here
});
var search = v.resourcesSearch({
    folderUri: "/public",
    recursive: false,
    success: function(repo) {
        console.log(repo.data()); // resourceLookups
    }
});
```

You can also specify the `runImmediately:false` parameter so that you can set up the search in the first call, and run it later in a separate call. In the following code sample, the first statement builds a query but makes no request to the server, and the second statement actually sends the request, which executes the query.

``` javascript
var query = v.resourcesSearch({
    server:"http://localhost:8080/jasperserver-pro",
    folderUri: "/public",
    recursive: false,
    runImmediately : false
}));

query.run().done(function(results))
```

## Reusing a Search Instance

If you make multiple searches, for example in different folders, you can create a function to do that using the `ResourcesSearch` function.

``` javascript
var folderContentQuery = new ResourcesSearch({
    server:"http://localhost:8080/jasperserver-pro",
    recursive: false
}));

// call 1
folderContentQuery.folderUri("/uri1").run(doSomethingWithResultFunction);
...
// call 2 after some time
folderContentQuery.folderUri("/uri2").run(doSomethingWithResultFunction);
```

## Reusing Search Results

Code example:

``` javascript
var call = new ResourcesSearch({
    server:"http://localhost:8080/jasperserver-pro",
    folderUri: "/public",
    recursive: false
})).run(function(resourceLookups){
    // data() available here
});
// at this point call.data() will return null until the run callback is called.
call.data() === null // -> true

.....
// if some data was obtained earlier, it accessible via data()
var resourceLookups = call.data();
```

## Discovering Available Types

You can write code to discover and display the types that can be searched and types of sorting that can be specified.

``` javascript
visualize({
    auth: {
        name: "jasperadmin",
        password: "jasperadmin",
        organization: "organization_1"
    }
}, function (v) {

    buildControl("Resources types", v.resourcesSearch.types);
    buildControl("Resources search sort types", v.resourcesSearch.sortBy);

});
function buildControl(name, options) {

        function buildOptions(options) {
            var template = "<option>{value}</option>";
            return options.reduce(function (memo, option) {
                return memo + template.replace("{value}", option);
            }, "")
        }

    console.log(options);

    if (!options.length){
        console.log(options);
    }

    var template = "<label>{label}</label><select>{options}</select><br>",
        content = template.replace("{label}", name)
                .replace("{options}", buildOptions(options));

    $("#container").append($(content));
}
```
