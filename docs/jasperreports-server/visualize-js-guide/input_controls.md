---
title: API Reference - inputControls
description: "The inputControls function prepares and displays the input controls, also known as the filters, of a report. Your users interact with the controls to submit input when running reports."
---

# API Reference - inputControls

The `inputControls` function prepares and displays the input controls, also known as the filters, of a report. Your users interact with the controls to submit input when running reports.

Visualize.js supports much simpler input controls that are rendered directly by the server. All you need to do is specify the report resource and a container destination, and the server generates the UI interface that allows the user to select or enter values. You can then change the appearance of the input controls through CSS as necessary.

The previous mechanism of creating your own input control structures in JavaScript is still available to create custom input control interfaces. When creating custom input controls, your code can retrieve the input control data and generate your own input control UI interface.

This chapter contains the following sections:

- Input Control Properties
- Input Control Functions
- Embedding Input Controls
- Handling Input Control Events
- Resetting Input Control Values
- Embedded Input Control Styles
- Custom Input Controls

## Input Control Properties

The properties structure passed to the `inputControls` function is defined as follows:

``` json
{
    "type": "object",
    "properties": {
        "server": {
            "type": "string",
            "description": "Url to JRS instance."
        },
        "resource": {
            "type": "string",
            "description": "URI of resource with input controls.",
            "pattern": "^/[^/~!#\\$%^|\\s`@&*()\\-+=\\[\\]:;\"'<>,?/\\|\\\\]+(/[^/~!#\\$%^|\\s`@&*()\\-+=\\[\\]:;\"'<>,?/\\|\\\\]+)*$"
        },
        "params": {
            "type": "object",
            "description": "Parameters for input controls.",
            "additionalProperties": {
                "type": "array"
            }
        },
        "container": {
            "oneOf": [{
                "type": "object",
                "additionalProperties" : true,
                "description": "DOM element to render report to"
            }, {
                "type": "string",
                "description": "CSS selector for container to render report to."
            }]
        }
    },
    "required": ["server", "resource"]
}
```

## Input Control Functions

The `InputControls` function exposes the following functions:

``` javascript
define(function () {

    /**
     * Constructor. Takes properties as argument.
     * @param properties - map of properties.
     */
    function InputControls(properties);

    /**
     * Get/Set 'resource' property - URI of resource with input controls.
     * @param value - new value, optional
     * @returns this if 'value' sent to the method,
     *          otherwise returns current value of the parameter
     */
    InputControls.prototype.resource = function(value);

    /**
     * Get/Set 'params' property - Parameters for input controls.
     * @param value - new value, optional
     * @returns this if 'value' sent to the method,
     *          otherwise returns current value of the parameter
     */
    InputControls.prototype.params = function(value);

    /**
     * Attaches event handlers to some specific events.
     * New events overwrite old ones.
     * @param {Object} events - object containing event names as keys
     *                          and event handlers as values
     * @return {InputControls} input controls - current InputControls
     *                                          instance (allows chaining)
     */
    Report.prototype.events = function(events);

    /**
     * Reset input controls current state.
     * @param {Function} callback - optional, invoked in case successful export
     * @param {Function} errorback - optional, invoked in case of failed export
     * @param {Function} always - optional, optional, invoked always
     * @return {Deferred} dfd
     */
    Report.prototype.reset = function();

    return InputControls;
});
```

## Embedding Input Controls

When you display and use input controls, the server generates the UI widgets for all of the input controls of a report; you specify the container where you want to embed them.

If desired, it is still possible to generate your own UI widgets for each input control, as done in some previous versions; see Custom Input Controls. Previously written JavaScript that created custom input controls still work.

In the simplest embedding case, you specify the URI of the report resource and a container. Only the input controls for the designated report are embedded in the container. The input controls appear on your page as standard selection boxes and drop-down selectors that the user can interact with and choose new values. The following example shows the HTML and corresponding JavaScript:

``` html
<script src="http://localhost:8080/jasperserver-pro/client/visualize.js"></script>
<div id="inputContainer"></div>

visualize({
    auth: { ...
    }
}, function (v) {
    var inputControls = v.inputControls({
        resource: "/public/Samples/Reports/Cascading_Report_2_Updated",
        container: "#inputContainer",
        error: function (err) {
            console.error(err);
        }
    });

});
```

Of course, you can add styles to determine the shape and placement of your input controls container, as shown in the following CSS sample. If you wish to change the appearance of the embedded controls *within* the container, see Embedded Input Control Styles.

``` bash
#inputContainer {
  width: 300px;
  padding-left: 50px;
}
```

The following is a more realistic example that shows how to embed both the report and its input controls into separate containers on your page. The page also provides a button to run the report after the user has made changes to input controls:

``` html
<script src="http://localhost:8080/jasperserver-pro/client/visualize.js"></script>
<script type='text/javascript' src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<div id="inputContainer" style="width:300px"></div>
<button id="run">
Run
</button>
<div id="reportContainer"></div>
```

The JavaScript embeds the report and the input controls in their respective containers, then it handles the button click to read the current values of the input controls (called `parameters` in this instance) and run the report using those values:

``` javascript
var inputControls="";
visualize({
    auth: { ...
    }
}, function(v) {
    var resourceUri = "/public/Samples/Reports/ProfitDetailReport";
    //render report from resource
    var report = v.report({
        resource: resourceUri,
        container: "#reportContainer"
    });

    //render input controls from resource
    inputControls= v.inputControls({
        resource: resourceUri,
        container: "#inputContainer",
        error: function(err) {
            console.error(err);
        },
        success: function(data) {
            console.log(data)
        }
    });

    //run report again using paramaters from input control
    $("#run").click(
        function(){
            console.log(inputControls.data().parameters)
            inputControls.run(null, function(e));
        var params = inputControls.data().parameters;
        report.params(params).run()
    });
});
```

In most cases, your input controls will come from the same report that you are running. As in the example above, the URI for the report and the input controls is the same report resource. However, it is possible to use input controls from a different report, as long as the values from those input controls are compatible with the target report. Because input controls are ultimately used to create the query that fetches data for a report, the input controls of one report are compatible with another report if they are based on the same data source or Domain. For example, you might have two or more reports based on the same data source and embed the input controls from only one of them. You could then use the one set of input controls to update all of the reports simultaneously.

## Handling Input Control Events

Because the input controls are separate from the report, events provide a way for you to make them work together or provide additional information. The `inputControls` instance generates a change event after the user interactively sets or selects a new input control value using the UI widgets.

The most common use is to listen for input control change events in order to run the associated report with the new input control values. In this example, the HTML sample has the report and input controls containers side by side in a row (styles or CSS not shown):

``` html
<script src="http://localhost:8080/jasperserver-pro/client/visualize.js"></script>
<div class="container">
  <div class="row">
    <div class="col-lg-6">
      <div id="reportContainer"></div>
    </div>
    <div class="col-lg-6">
      <div id="inputContainer"></div>
    </div>
  </div>
```

Then, the JavaScript embeds the report and the input controls in their respective containers and adds a listener for change events. If there is no error, the input control values (called `params` in this instance) are taken from the event and used to run the report again. This is a very common pattern when using input controls:

``` javascript
visualize({
    auth: { ...
    }
}, function (v) {

    var resourceUri = "/public/Samples/Reports/Cascading_Report_2_Updated";

    var report = v.report({
        resource: resourceUri,
        container: "#reportContainer"
    });

     var inputControls = v.inputControls({
        resource: resourceUri,
        container: "#inputContainer",
        events: {
            change: function(params, error){
            if (!error){
                report.params(params).run();
            }
          }
        }
    });
});
```

Another use for change events is to update other parts of your page based on the value of an input control. Such a mechanism could be used to update the title above a report, after the report is updated with a change of input controls.

In the following example, the change event triggers an update to text that displays the current value of an input control. The HTML has a placeholder for the text:

``` html
<script src="http://localhost:8080/jasperserver-pro/client/visualize.js"></script>

<div id="inputContainer"></div>

<div  id="myText" >
    <span>Selection: </span>
    <strong id='output'></strong>
</div>
```

The CSS hides the text at first:

``` bash
#inputContainer {
    width:200px;
}

#myText {
   display:none
}
```

And the JavaScript catches the input control change event, then extracts the value of a given parameter to display it:

``` javascript
visualize({
    auth: {...
    }
}, function (v) {
    v.inputControls({
        container: "#inputContainer",
        resource: "/public/Samples/Reports/06g.ProfitDetailReport",
        error: function (err) {
            alert(err);
        },
        events: {
            change : function(params) {
                $("#myText").show();
                $("#output").text(params['ProductFamily'].join(', '));
            }
        }
    });
});
```

The change event can also be used to check whether the input controls entered by the user passed validation checks. Validation is defined on the server and ensures that values entered by the user are of the expected type or within a given range. The following example shows an event handler that checks the validation result:

``` javascript
        events: {
            change : function(state, validationResult) {
              if (validationResult) {
                console.log(validationResult)
              } else {
                console.log(state)
              }
            }
        }
```

## Resetting Input Control Values

`inputControls` provides a function to reset all input control values to their default values. When the reset function is invoked, the display of the input controls refreshes to show their default values, that is, the initial state of the input controls before the user made any changes.

The following example has buttons to run the report and also to reset input controls. The HTML sample has the containers and buttons that are needed:

``` html
<script src="http://localhost:8080/jasperserver-pro/client/visualize.js"></script>
<script type='text/javascript' src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<div id="inputContainer" style="width:300px"></div>
<button id="run">
Run
</button>
<button id="reset">
Reset
</button>
<div id="reportContainer"></div>
```

The corresponding JavaScript invokes the reset function when the button is clicked, and then it runs the report as well again:

``` javascript
var inputControls="";
visualize({
    auth: { ...
    }
}, function(v) {
    var resourceUri = "/public/Samples/Reports/ProfitDetailReport";
    //render report from resource
    var report = v.report({
        resource: resourceUri,
        container: "#reportContainer"
    });

    //render input controls from resource
    inputControls= v.inputControls({
        resource: resourceUri,
        container: "#inputContainer",
        error: function(err) {
            console.error(err);
        },
        success: function(data) {
            console.log(data)
        }
    });

    function runReport(){
        console.log(inputControls.data().parameters)
        inputControls.run(null, function(e));
        var params = inputControls.data().parameters;
        report.params(params).run()
    }

    //run report again using paramaters from input controls
    $("#run").click(runReport);

    //reset parameters in input controls then run report again
    $("#reset").click(
        function(){
            console.log("Params before reset: ", inputControls.params())
            inputControls.reset().done(runReport);
    });

});
```

## Embedded Input Control Styles

With the embedded input controls, the server generates all of the UI widgets within your container. These UI widgets all have a standard look and feel that is controlled by CSS also generated by the server. If you wish to change the appearance of the generated input controls, you can add your own CSS with the proper class names.

In the following simple example, the HTML has a container and the JavaScript uses it for the input controls:

``` html
<script src="http://localhost:8080/jasperserver-pro/client/visualize.js"></script>
<div id="inputContainer" style="width:300px"></div>

visualize({
    auth: {
        name: "superuser",
        password: "superuser"
    }
}, function (v) {
    var inputControls = v.inputControls({
        resource: "/public/viz/Adhoc/Ad_Hoc_View_All_filters_Report",
        container: "#inputContainer",
        error: function (err) {
            console.error(err);
        }
    });
});
```

The following CSS will change the text color of the label of the boolean input control:

``` bash
#inputContainer .jr-mInput-boolean-label {
    color: #218c00;
}
```

The following list shows the CSS base classes and secondary class names for the labels of each kind of input control embedded by the server. Use these in your CSS rules as shown in the example above to change the appearance of your labels.

``` bash
#inputContainer .jr-mInputControlBoolean .jr-mInput-boolean-label
#inputContainer .jr-mInputControlSingleValueText .jr-mInput-label
#inputContainer .jr-mInputControlSingleValueDate .jr-mInput-label
#inputContainer .jr-mInputControlSingleValueTime .jr-mInput-label
#inputContainer .jr-mInputControlSingleValueDatetime .jr-mInput-label
#inputContainer .jr-mInputControlSingleValueNumber .jr-mInput-label
#inputContainer .jr-mInputControlSingleSelect .jr-mInput-label
#inputContainer .jr-mInputControlMultiSelect .jr-mInput-label
#inputContainer .jr-mInputControlSingleSelectRadio .jr-mInput-label
#inputContainer .jr-mInputControlMultiSelectCheckbox .jr-mInput-label
```

If you want to change the style of other elements in the server's embedded input control UI, you can find the corresponding CSS classes and redefine them. To find the CSS classes, write the JavaScript to embed your input controls, then test the page in a browser. Use your browser's code inspector to look at each element of the generated input controls and locate the CSS rules that apply to it. The code inspector shows you the classes and often lets you modify values to preview the look and feel that you want to create.

## Custom Input Controls

In the sections above, the UI widgets for embedded input controls are generated by the server and displayed in a given container. An alternate way to create input controls for your reports in visualize.js is to retrieve the input control values and analyze their structure so you can create your own UI widgets. These are called custom input controls.

Custom input controls require more JavaScript coding, and might be specific to a given report's input controls. In addition, handling cascading input controls is more complex and requires you to listen for change events that update the input control structure. The following sections explain how to implement custom input controls.

### Input Control Structure

The data() for InputControls is an array of InputControl objects, with the structure shown in this example:

``` json
[
  {
    "id":"Cascading_name_single_select",
    "label":"Cascading name single select",
    "mandatory":"true",
    "readOnly":"false",
    "type":"singleSelect",
    "uri":"repo:/reports/samples/Cascading_multi_select_report_files/Cascading_name_single_select",
    "visible":"true",
    "masterDependencies": {
      "controlId": [
        "Country_multi_select",
        "Cascading_state_multi_select"
      ]
    },
    "slaveDependencies":null,
    "validationRules": [
      {
        "mandatoryValidationRule" : {
          "errorMessage" : "This field is mandatory so you must enter data."
        }
      }
    ],
    "state": {
      "uri": "/reports/samples/Cascading_multi_select_report_files/Cascading_name_single_select",
      "id": "Cascading_name_single_select",
      "value": null,
      "options": [
        {
          "selected": false,
          "label": "A & U Jaramillo Telecommunications, Inc",
          "value": "A & U Jaramillo Telecommunications, Inc"
        }
      ]
    }
  },
  ....
]
```

### Fetching Input Control Data

The data being output here has the input control structure shown in the previous section:

``` javascript
visualize(function(v){
    var ic = v.inputControls({
        resource: "/public/ReportWithControls",
        success: function(data) {
           console.log(data);
        }
    });
});
```

This example shows an alternate way of fetching input controls:

``` javascript
(new InputControls({
    server: "http://localhost:8080/jasperserver-pro",
    resource: "/public/my_report",
    params: {
        "Country_multi_select":["Mexico"],
        "Cascading_state_multi_select":["Guerrero", "Sinaloa"]
    }
})).run(function(inputControlsArray){
    // results here
})
```

### Creating Input Control Widgets

This example retrieves the input controls of a report and parses the structure to create drop-down menus of values for each control:

``` javascript
visualize({
    auth: {
        name: "superuser",
        password: "superuser"
    }
},function(v) {

    v.inputControls({
        resource: "/public/Samples/Reports/16g.InteractiveSalesReport",
        success: function (controls) {
            controls.forEach(buildControl);
        },
        error: function (err) {
            alert(err);
        }
    });

    function buildControl(control) {

        function buildOptions(options) {
            var template = "<option>{value}</option>";
            return options.reduce(function (memo, option) {
                return memo + template.replace("{value}", option.value);
            }, "")
        }

        var template = "<label>{label}</label><select>{options}</select><br>",
            content = template.replace("{label}", control.label)
                .replace("{options}", buildOptions(control.state.options));

        $("#container").append($(content));
    }
});
```

### Cascading Input Controls

In order to implement cascading input controls, you must implement a change listener on the parent control and use it to trigger an update on the dependent control:

``` javascript
var reportUri = "/public/Samples/Reports/Cascading_Report_2_Updated";

visualize({
    auth: {
        name: "superuser",
        password: "superuser"
    }
}, function (v) {
    var inputControls = v.inputControls({
        resource: reportUri,
        success: renderInputControls
    });

    var report = v.report({ resource: reportUri, container: "#container" });

    $("#productFamilySelector").on("change", function() {
        report.params({ "Product_Family": [$(this).val()] }).run();
    });
});
function renderInputControls(data) {
    var productFamilyInputControl = _.findWhere(data, {id: "Product_Family"});
    var select = $("#productFamilySelector");
    _.each(productFamilyInputControl.state.options, function(option) {
        select.append("<option " + (option.selected ? "selected" : "") + " value='" +
                        option.value + "'>" + option.label + "</option>");
    });
}
```

Associated HTML:

``` html
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script src="http://underscorejs.org/underscore-min.js"></script>
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>
<select id="productFamilySelector"></select>
<div id="container"></div>
```

### Reusing Input Control Instances

Input controls are meant to be dynamic and modified by users. By using the `inputControls.params` function, you can update the values of input controls and then update the corresponding report.

``` javascript
var inputControls = new InputControls({
    server: "http://localhost:8080/jasperserver-pro",
    resource: "/public/my_report"
});

// call 1
inputControls.params({ "Country_multi_select": ["Mexico"] }).run(doSomethingWithResultFunction);
...
// call 2 after some time
inputControls.params({ "Country_multi_select": ["USA"] }).run(doSomethingWithResultFunction);
```

### Reusing Input Control Data

You can store the data from the `inputControls` function and access the data() structure at a later time:

``` javascript
var call = (new InputControls({
    server: "http://localhost:8080/jasperserver-pro",
    resource: "/public/my_report"
})).run(function(inputControlsArray){
    // data() available here
});

// at this point call.data() will return null until the run callback is called.
call.data() === null // -> true
...
// if some data was obtained earlier, it accessible via data()
var inputControlsArray = call.data();
```
