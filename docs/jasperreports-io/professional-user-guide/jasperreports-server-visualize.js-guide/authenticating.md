---
title: API Reference - login and logout
description: The initialization of the script sets the authentication method and credentials that you want to use for accessing JasperReports Server. You can then use the login and logout functions to manage...
---

# API Reference - login and logout

The initialization of the script sets the authentication method and credentials that you want to use for accessing JasperReports Server. You can then use the `login` and `logout` functions to manage multiple user sessions.

This chapter contains the following sections:

-   Authentication Properties
-   Authentication Functions
-   Login With Plain Text Credentials
-   Login With SSO Token
-   Logging Out
-   Login With Hooks
-   UI for Login/Logout
-   UI for Login/Logout With SSO Token
-   Sharing Credentials Between Calls
-   Using Visualize.js Without Authentication

## Authentication Properties

The properties argument to the visualize function has all the fields for specifying various authentication methods.

``` json
{
    "allOf": [
        {
            "$ref": "BIComponentSchema.json"
        },
        {
            "type": "object",
            "description": "Authentication Properties",
            "properties":{
                "url": {
                    "type" : "string",
                    "description": "Jasper Reports Server deployment URL"
                },
                "name": {
                    "type" : "string",
                    "description": "Name of the user to authenticate"
                },
                "password": {
                    "type" : "string",
                    "description": "Password of the user to authenticate"
                },
                "organization": {
                    "type": ["string", "null"],
                    "description": "Organization of the user to authenticate"
                },
                "locale": {
                    "type": "string",
                    "description": "Default user locale to use for this session. Can be overridden for particular user action"
                },
                "timezone": {
                    "type": "string",
                    "description": "Default user timezone to use for this session. Can be overridden for particular user action"
                },
                "token" : {
                    "type": "string",
                    "description": "SSO authentication token. If present, then all the rest parameters are ignored"
                },
                "preAuth" : {
                    "type": "boolean",
                    "description": "Pre authentication enabled flag. If true, then authentication request is sent to base JRS URL, otherwise to {baseUrl}/j_spring_security_check"
                },
                "tokenName" : {
                    "type": "string",
                    "description": "SSO authentication token name. Use this parameter to override default SSO token parameter name"
                },
                "loginFn": {
                    "type": "function",
                    "description": "A function to process login"
                },
                "logoutFn": {
                    "type": "function",
                    "description": "A function to process logout"
                }
            },
          "required": ["url"]
        }
    ]
}
```

## Authentication Functions

The Authentication module has functions for logging in and logging out.

``` javascript
define(function () {
    /**
     * @param {Object} properties - authentication properties
     * @constructor
     */
    function Authentication(properties)

    /**
     * Performs JRS login using current Authentication instnce properties.
     * @param {Function} callback - optional, invoked in case successful logout
     * @param {Function} errorback - optional, invoked in case of failed logout
     * @param {Function} always - optional, invoked always
     * @return {Deferred} dfd - login deferred
     */
    Authentication.prototype.run= function(callback, errorback, always);

    /**
     * Performs JRS authentication.
     * @param {Object} properties - mandatory, contain all the required properties for the authentication
     * @param {Function} callback - optional, invoked in case successful login
     * @param {Function} errorback - optional, invoked in case of failed login
     * @param {Function} always - optional, invoked always
     * @return {Deferred} dfd - authentication deferred
     */
    Authentication.prototype.login= function(properties, callback, errorback, always);
    /**
     * Performs JRS logout. Session is dropped.
     * @param {Function} callback - optional, invoked in case successful logout
     * @param {Function} errorback - optional, invoked in case of failed logout
     * @param {Function} always - optional, invoked always
     * @return {Deferred} dfd - logout deferred
     */
    Authentication.prototype.logout= function(callback, errorback, always);
    return Authentication;
});
```

There are several ways to set the user credentials, based on your environment.

## Login With Plain Text Credentials

Use the methods of the Authentication module to set the credentials and perform login and logout operations.

``` javascript
var authentication = new Authentication({
    name:"JoeUser",
    password:"supersecret",
    organization:"organization_1"
    locale: "en",
    timezone: "Europe/Helsinki"
});
authentication.run();
...
authentication.logout();
```

Alternatively, you can specify the username, password, organization (if required), and optional parameters in the `auth` property of the visualize object itself.

``` javascript
visualize({
    auth: {
        name: "JoeUser",
        password: "supersecret",
        organization:"organization_1",
        timezone: "Europe/Helsinki"
    }
}, function (v) {
    ...
}, function () {
    alert("Unexpected error!");
});
```

## Login With SSO Token

If you have single-sign-on (SSO) implemented and have configured JasperReports Server to use it, you can specify the SSO token in the Authentication module or Visualize.js. This example shows a token from a Central Authentication Service (CAS) server.

``` javascript
var authentication = new Authentication({
token: "ST-40-CZeUUnGPxEqgScNbxh9l-sso-cas.prod.jaspersoft.com",
});
authentication.run();
```

Or:

``` javascript
visualize({
    auth : { token : "ST-40-CZeUUnGPxEqgScNbxh9l-sso-cas.prod.jaspersoft.com"}
}, function (v){
    alert("You are now logged into JasperReports Server with your SSO token.");
    ...
}, function(err){
    alert(err.message);
});
```

Some SSO implementations require encoding, additional parameters, or both. For example, if your server is configured for pre-authentication, you could use the following example to authenticate from Visualize.js. Note that the encoded fields depend on the specifics of your pre-authentication configuration:

``` javascript
var t = encodeURIComponent("u=John|r=Ext_User|o=organization_1|pa1=USA|pa2=1");
visualize({
    auth: {
        token: t,
        preAuth: true,
        tokenName: "pp"
    }
}, function (v){
    ...
});
```

If you have configured token-based pre-authentication with WebLogic Server, there is one additional setting needed for authentication to work properly with Visualize.js. Edit the file `applicationContext-externalAuth-preAuth-mt.xml` in the JasperReports Server web app, and remove the comments (`<!-- -->`) on the following line:

``` text
<!-- <property name="welcomePage" value="/index.htm"/> -->
```

## Logging Out

To log out and destroy the current user session, call the logout function and optionally specify any action to take when done.

``` javascript
visualize({
    auth: {
        name: "jasperadmin",
        password: "jasperadmin",
    }
}, function (v) {

    ...

    //destroy session
    $("#logout").click(function () {
        v.logout().done(function () {
            alert("You are now logged out of JasperReports Server.");
        });
    });
});
```

## Login With Hooks

If you have external authentication providers, you can invoke their login and logout URLs. Again, there are two similar forms, one with the Authentication module, and one with the auth properties.

The functions you define for login and logout must return a deferred object and accept two arguments:

-   `properties`: An object that contains all the required authentication properties.
-   `request`: A request function your function can use to perform authentication from a website.

``` javascript
var authentication = new Authentication({
    name:"JoeUser",
    password:"supersecret",
    loginFn: function(properties, request){
        return request({url: "http://auth.example.com?username=" + properties.name + "&password=" + properties.password});
    },
    logoutFn: function(properties, request){
        return request({url: "http://auth.example.com/logout"});
    }
});
authentication.run();
...
authentication.logout();
```

Or:

``` javascript
visualize({
    auth: {
        name: "jasperadmin",
        password: "jasperadmin",
        loginFn: function (properties, request) {
            // Use a customLogin function to authenticate
            // It must be on the same domain: 'request' works only with JRS instance
            alert("Sending custom login request to 'http://bi.example.com/customLogin'");
            return request({
                url: "http://bi.example.com/customLogin?username=" + properties.name + "&password=" + properties.password
            });
        },
        logoutFn: function (properties, request) {
            // Use a customLogout function to destroy the session
            // It must be on the same domain: 'request' works only with JRS instance
            alert("Sending custom logout request to 'http://bi.example.com/customLogout'");
            return request({
                url: "http://bi.example.com/customLogout"
            });
        }
    }
}, function (v) {
    ...
});
```

## UI for Login/Logout

You can define IDs (`#name`) with listeners that perform login and logout functions. In your HTML, you can then assign these IDs to the appropriate buttons or links.

``` javascript
visualize(
    function(v){
        $("#selected_resource").change(function () {
            $("#container").html("");
            createReport($("#selected_resource").val(), v);
        });
        $("#login").click(function(){
            v.login(getAuthData()).done(function(){
                createReport($("#selected_resource").val(),v);
                showMessage(".success");
            }).fail(function(){showMessage(".error");});
        });
        $("#logout").click(function(){
            v.logout().done(function(){showMessage(".logout");});
        });
        $(':disabled').prop('disabled', false);
    }
);

//create and render report to specific container
function createReport(uri, v) {
    v("#container").report({
        resource: uri,
        error: function (err) {
            alert(err.message);
            }
     });
};

function showMessage(selector){
    $(".message").hide();
    $(selector).show();
};

function getAuthData(){
    return {name: $("#j_username").val(),
            password: $("#j_password").val(),
            organization:$("#orgId").val(),
            locale:$("#userLocale").val(),
            timezone:$("#userTimezone").val()
           }
};
```

## UI for Login/Logout With SSO Token

The code is slightly different if you have a login/logout UI and use SSO tokens. Note that the logout uses the `.always` event instead of `.done`.

``` javascript
visualize(
    function(v){
        $("#selected_resource").change(function () {
            $("#container").html("");
            createReport($("#selected_resource").val(), v);
        });
        $("#login").click(function(){
            v.login(getAuthData()).done(function(){
                createReport($("#selected_resource").val(),v);
                showMessage(".success");
            }).fail(function(){showMessage(".error");});
        });
        $("#logout").click(function(){
            v.logout().always(function(){showMessage(".logout");});
        });
        $(':disabled').prop('disabled', false);
    }
);

//create and render report to specific container
function createReport(uri, v) {
    v("#container").report({
        resource: uri,
        error: function (err) {
            alert(err.message);
            }
     });
};

function showMessage(selector){
    $(".message").hide();
    $(selector).show();
};

function getAuthData(){
    return {token: $("#token").val()};
};
```

## Sharing Credentials Among Calls

Use the `visualize.config` function to define and store authentication credentials. It uses the same `auth` structure as the `visualize` function. You can then create several containers with separate calls to `visualize`, using the common credentials.

``` javascript
visualize.config({
    auth: {
        name: "jasperadmin",
        password: "jasperadmin",
        organization:"organization_1",
        timezone: "Europe/Helsinki"
    }
});

visualize(function (v) {
    v("#container1").report({
        resource: "/public/Samples/Reports/06g.ProfitDetailReport",
        error: function (err) {
            alert(err.message);
        }
    });
});
visualize(function (v) {
    v("#container2").report({
        resource: "/public/Samples/Reports/State_Performance",
        error: function (err) {
            alert(err.message);
        }
    });
});
```

## Using Visualize.js Without Authentication

Internally, Visualize.js uses the REST API to authenticate and interact with the server. However, the REST client receives and reuses the JSESSIONID cookie that identifies it as authenticated, which is also the same cookie used in regular browser clients. Therefore, users who access the JasperReports Server web app UI and use the same browser to run a visualize.js client before their session expires do not need to authenticate in visualize.js.

If your visualize.js solution includes other browser windows or other authenticated REST calls, then you can simplify your visualize.js and remove the authentication:

``` javascript
// This assumes that authentification was made somehow prior
visualize(function (v) {

    //do what you usally do with 'v'
    console.log(v);

});
```
