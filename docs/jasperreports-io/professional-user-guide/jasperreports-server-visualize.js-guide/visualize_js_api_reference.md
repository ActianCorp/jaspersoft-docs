---
title: API Reference - Visualize.js
description: "The JavaScript API exposed through Visualize.js allows you to embed and dynamically interact with reports. With Visualize.js, you can create web pages and web applications that seamlessly embed..."
---

# API Reference - Visualize.js

The JavaScript API exposed through Visualize.js allows you to embed and dynamically interact with reports. With Visualize.js, you can create web pages and web applications that seamlessly embed reports and complex interaction. You can control the look and feel of all elements through CSS and invent new ways to merge data into your application. Visualize.js helps you make advanced business intelligence available to your users.

# JavaScript API Reference - jrio.js

The JavaScript API exposed through jrio.js allows you to embed reports into your web pages and web applications. The embedded elements are fully interactive, either through the UI or programmatically. Users navigate their data in the context of your app, and you can dynamically compute, update, or render the jrio.js elements to create seamless interaction. You can use JavaScript frameworks for layout and control the look and feel of all elements through style sheets (CSS).

With the JavaScript API, you can invent new ways to merge data into your application, and make advanced business intelligence available to your users.

This chapter contains the following sections:

- Requesting the Visualize.js Script

- Contents of the Visualize.js Script

- Usage Patterns

- Testing Your JavaScript

- Changing the Look and Feel

- Cross-Domain Security

- Serving Visualize.js from a CDN

Each function of Visualize.js is then described in the following chapters:

- [API Reference - login and logout](../../../jasperreports-server/visualize-js-guide/authenticating.md)

- [API Reference - resourcesSearch](../../../jasperreports-server/visualize-js-guide/searching_the_repository.md)

- [API Reference - reports](displaying_reports.md)

- [API Reference - inputControls](../../../jasperreports-server/visualize-js-guide/input_controls.md)

- [API Reference - dashboard](../../../jasperreports-server/visualize-js-guide/displaying_dashboards.md)

- [API Reference - Errors](handling_errors.md)

The last chapters demonstrate more advanced usage of Visualize.js:

- [API Usage - Report Events](report_events.md)

- [API Usage - Report Hyperlinks](hyperlinks.md)

- [API Usage - Interactive Reports](interactive_reports.md)

- [Visualize.js Tools](../../../jasperreports-server/visualize-js-guide/visualize_js_tools.md)

This chapter contains the following sections:

- Loading the jrio.js Script

- Configuring the JasperReports IO Client

- Usage Patterns

- Testing Your JavaScript

- Changing the Look and Feel

Each function of the JasperReports IO JavaScript API is then described in the following chapters:

- [JavaScript API Reference - report](displaying_reports.md)

- [JavaScript API Reference - Errors](handling_errors.md)

The last chapters demonstrate more advanced usage of the JasperReports IO JavaScript API:

- [JavaScript API Usage - Report Events](report_events.md)

- [JavaScript API Usage - Hyperlinks](hyperlinks.md)

- [JavaScript API Usage - Interactive Reports](interactive_reports.md)

## Loading the jrio.js Script

The script to include on your HTML page is named jrio.js. It is located on your running instance of the JasperReports® IO JavaScript API distribution, which is available for download and can be deployed in your hosting web application. Later on your page, you also need a container element to display the report from the script.

```
<!-- Provide the URL to jrio.js -->
<script src="http://bi.example.com:8080/jrio-client/optimized-scripts/jrio/jrio.js"></script>
...
<!-- Provide a container for the report -->
<div id="reportContainer"></div>
```

The content of jrio.js is `type='text/javascript'`, but that is the default so you usually don't need to include it.

## Requesting the Visualize.js Script

The script to include on your HTML page is named visualize.js. It is located on your running instance of JasperReports® Server. Later on your page, you also need a container element to display the report from the script.

```
<!-- Provide the URL to visualize.js -->
<script src="http://bi.example.com:8080/jasperserver-pro/client/visualize.js"></script>
...
<!-- Provide a container for the report -->
<div id="container"></div>
```

The content of visualize.js is `type='text/javascript'`, but that is the default so you usually don't need to include it.

You can specify several parameters when requesting the script:

| Parameter | Type or Value | Description |
|----|----|----|
| `userLocale` | locale string | Specify the locale to use for display and running reports. It must be one of the locales supported by JasperReports Server. The default is the locale configured on the server. |
| `logEnabled` | true\|false | Enable or disable logging. By default, it is enabled (true). |
| `logLevel` | debug\|info\|warn\|error | Set the logging level. By default the level is error. |
| `baseUrl` | URL | The URL of the JasperReports Server that will respond to visualize requests. By default, it is the same server instance that provides the script. |

The following request shows how to use script parameters:

```
<script src="http://bi.example.com:8080/jasperserver-pro/client/
             visualize.js?userLocale=fr&logLevel=debug"></script>
```

## Configuring the JasperReports IO Client

Loading the jrio.js script as above gives you access to the JasperReports IO JavaScript API in your web page.

But this JasperReports IO client-side API needs to be configured to point to an existing JasperReports IO REST reporting service URL which delivers the actual reports output to be displayed on the current page, the location of the API scripts (either optimized or non-optimized) and UI theme.

This is achieved by calling the `config()` function on the jrio object made available globally on the page by the loading of the jrio.js script:

```
jrio.config({
    server : "http://bi.example.com:8080/jrio",
    scripts : "http://bi.example.com:8080/jrio-client/optimized-scripts",
    theme: {
        href: "http://bi.example.com:8080/jrio-client/themes/default"
    },
    locale: "en_US"
});
```

You can specify several parameters when requesting the script:

| Parameter | Type or Value | Description |
|----|----|----|
| `server` | URL | The URL to the JasperReports IO service that responds to the report generating REST requests. This parameter is required. |
| `scripts` | URL | The URL to the folder containing the JasperReports IO JavaScript API files, either in optimized or non-optimized format. This parameter is required. |
| `theme` | URL | The URL to the folder containing the JasperReports IO JavaScript UI theme files. |
| `locale` | locale string | Specify the locale to use for display and running reports. It must be one of the locales supported by JasperReports IO. The default is the locale configured on the server. This parameter is required. |
| `logEnabled` | true\|false | Enable or disable logging. By default, it is disabled (false). |
| `logLevel` | debug\|info\|warn\|error | Set the logging level. By default the level is error. |

!!! note

    The `server`, `scripts`, and `locale` parameters are required. The jrio object may produce errors if they are not set.

The scripts making up the JasperReports IO JavaScript API are available in two formats: optimized and non-optimized. They are placed in separate folders in the JasperReports IO JavaScript API distribution under `/optimized-scripts` and `/scripts` subfolders respectively.

If you notice undesirable side-effects when including the JasperReports IO JavaScript library, change the client configuration to use the optimized scripts to provide better protection, also known as encapsulation. For example, the JasperReports IO JavaScript API functions might interfere with collapse functions on your menus. Non-optimized scripts are preferred when you want to perform some runtime debugging for the JavaScript code.

If you want to used the optimized jrio.js script, use the following URL to load it: `<script src="http://bi.example.com:8080/myapp/jriojsapi/optimized-scripts/jrio/jrio.js"></script>`

If you want to use the non-optimized jrio.js script, you will have to use all of the following scripts:

```
<script src="http://bi.example.com:8080/myapp/jriojsapi/scripts/bower_components/requirejs/require.js"></script>
<script src="http://bi.example.com:8080/myapp/jriojsapi/scripts/require.config.js"></script>
<script src="http://bi.example.com:8080/jrio-client/scripts/jrio/loader/jasper.js"></script>
<script src="http://bi.example.com:8080/jrio-client/scripts/jrio/jrio.js"></script>
<script>
    require.config({
        baseUrl: "http://bi.example.com:8080/myapp/jriojsapi/scripts"
    });
</script>
```

## Contents of the Visualize.js Script

The Visualize.js script itself is a factory function for an internal JrsClient.

```
/**
 *  Establish connection with JRS instance and generate
 *  ready to use client
 *  @param {Object} properties - configuration to connect to JRS instance
 *  @param {Function} callback - optional, successful callback
 *  @param {Function} errorback - optional, invoked on error
 *  @param {Function} always - optional, invoked always
 */
function visualize(properties, callback, errorback, always)

/**
 *  Store common configuration, to share them between visualize calls
 *  @param {Object} properties - configuration to connect to JRS instance
 */
function visualize.config(properties);
```

You write JavaScript in a callback that controls what the client does. The following code sample shows the functions of the JrsClient that are available to you:

```
{    /**
     * Perform authentification with provided auth object
     * @param auth {object}  - auth properties
     */
    login : function(auth),

    /**
     * Destroy current auth session
     */
    logout : function(),

    /**
     * Create and run report component with provided properties
     * @param properties {object}  - report properties
     * @returns {Report} report - instance of Report
     */
    report : function(properties),

    /**
     * Create and run controls for provided controls properties
     * @param properties {object}  - input controls properties
     * @returns {Options} inputControls instance
     *
     */
    inputControls : function(properties),

    /**
     * Create and run resource search component for provided properties
     * @param properties {object}  - search  properties
     * @returns {Options} resourcesSearch instance
     *
     */
    resourcesSearch : function(properties)
}
```

These functions are described in the remaining API reference chapters.

## Usage Patterns

After configuring the JasperReports IO client object, you write the callback that will execute inside this client provided by jrio.js.

```
jrio.config({
    server : "http://bi.example.com:8080/jrio",
    scripts : "http://bi.example.com:8080/myapp/jriojsapi/optimized-scripts",
    theme: {
        href: "http://bi.example.com:8080/myapp/jriojsapi/themes/default"
    },
    locale: "en_US"
});
jrio(function(jrioClient) {
    jrioClient.report({
        resource: "/samples/reports/highcharts/HighchartsChart",
        container: "#reportContainer",
        error: function(err) {
            alert(err);
        },
    });
});
```

After specifying the authentication information, you write the callback that will execute inside the client provided by visualize.js.

```
visualize({
    server: "http://bi.example.com",
    auth: {
        name : "joeuser",
        password: "joeuser"
    }
}, function(v){

    //'v' is a client to JRS instance under  "http://bi.example.com"
    //session established for joeuser/joeuser

    var report = v.report(...);

}, function(err){
    alert(err.message);
});
```

The following sample shows how to use the always callback:

```
visualize({
    server: "http://bi.example.com",
    auth: {
        name : "joeuser",
        password: "joeuser"
    }
    }).always(function(err, v) {

        if (err) {
        alert(err.message);
        return;
        }

    v.report(); // use v here

});
```

As of JasperReports Server 7.9, the server can provide the code to embed any report, dashboard, or Ad Hoc view. This means you can browse your server's repository, choose the dashboard or Ad Hoc View that you want to embed, preview it, and then select the ![js Viewer icon EmbedCode](../assets/images/js-Viewer-icon-EmbedCode.png) icon in the toolbar to view the sample code. For more information, see:

- [Getting the Embed Code for a Report](displaying_reports.md)
- [Getting the Embed Code for a Dashboard](../../../jasperreports-server/visualize-js-guide/displaying_dashboards.md)
- [Getting the Embed Code for an Ad Hoc View](../../../jasperreports-server/visualize-js-guide/ad_hoc_views.md)

## Testing Your JavaScript

As you learn to use Visualize.js the JasperReports IO JavaScript API and write the JavaScript that embeds your reports into your web app, you should have a way to run and view the output of your script.

In order to load Visualize.js jrio.js, your HTML page containing your JavaScript must be accessed through a web server. Opening a static file with a web browser does not properly load the iframes needed by the script.

One popular way to view your Visualize.js JasperReports IO output, is to use the [jsFiddle](https://jsfiddle.net/) online service. You specify your HTML, JavaScript, and optional CSS in 3 separate frames, and the result displays in the fourth frame.

Another way to test your JavaScript is to use the app server bundled with JasperReports Server. If you deploy the server from the installer with the Apache Tomcat app server, you can create an HTML file at the root of the server web app, for example:

`<js-install>/apache-tomcat/webapps/jasperserver-pro/testscript.html`

Another way to test your JavaScript is to use the app server bundled with JasperReports IO. If you deploy the server from the installer with the Jetty web application server, you can create an HTML file at the root of one of the web apps shipped with it by default, for example:

`<jrio-install>/jrio/webapps/jrio-docs/testscript.html`

Write your HTML and JavaScript in this file, and then you can run Visualize.js by loading the file through the following URL:

`http://mydomain.com:8081/jasperserver-pro/testscript.html`

Write your HTML and JavaScript in this file, and then you can run jrio.js by loading the file through the following URL:

`http://mydomain.com:8081/jrio-docs/testscript.html`

## Changing the Look and Feel

When you create a web application that embeds Visualize.jsJasperReports IO content, you determine the look and feel of your app through layout, styles, and CSS (Cascading Style Sheets). Most of the content that you embed consists of reports and dashboards that you create in JasperReports Server with JasperReports IO or Jaspersoft® Studio, where you set the appearance of colors, fonts, and layout to match your intended usage.

But some Visualize.jsJasperReports IO JavaScript API elements also contain UI widgets that are generated by the server in a default style, for example the labels, buttons, and selection boxes for the input controls of a report. In general, the default style is meant to be neutral and embeddable in a wide range of visual styles. If the default style of these UI widgets does not match your app, there are two approaches described in the following sections:

- Customizing the UI with CSS: You can change the appearance of the UI widgets through CSS in your app.
- Customizing the UI with Themes: You can redefine the default appearance of the UI widgets in themes on the server.

### Customizing the UI with CSS

The UI widgets generated by the server have CSS classes and subclasses, also generated by the server, that you can redefine in your app to change their appearance. To change the appearance of the generated widgets, create CSS rules that you would add to CSS files in your own web app. To avoid the risk of unintended interference with other CSS rules, you should define your CSS rules with both a classname and a selector, for example:

```
#inputContainer .jr-mInput-boolean-label {
    color: #218c00;
}
```

To change the style of specific elements in the server's generated widgets, you can find the corresponding CSS classes and redefine them. To find the CSS classes, write the JavaScript display the UI widgets, for example input controls, then test the page in a browser. Use your browser's code inspector to look at each element of the generated widgets and locate the CSS rules that apply to it. The code inspector shows you the classes and often lets you modify values to preview the look and feel that you want to create. For more information, see [Embedded Input Control Styles](../../../jasperreports-server/visualize-js-guide/input_controls.md).

### Customizing the UI with Themes

You can redefine the default appearance of the UI widgets in themes on the server.

Themes are CSS in the JasperReports IO JavaScript API. The UI widgets in JasperReports IO elements are generated on the server and their look and feel is ultimately determined by themes.

The UI widgets in Visualize.js elements are generated on the server and their look and feel is ultimately determined by themes. Themes are CSS files defined for organizations, and thus appearances are determined by the user credentials submitted by your Visualize.js instance. Certain visual properties of the UI widgets embedded in your app by Visualize.js can be modified by changing themes on the server. For more information about themes, see the JasperReports Server Administrator Guide.

However, not all properties of a UI widget can be modified through themes. If you want to create a fully custom visualization, you might need to access raw data through the Visualize.js APIs and write your own elements and CSS to display them. For more information, see [Exporting Data From a Report](displaying_reports.md).

## Cross-Domain Security

After developing your web application and embedding Visualize.js, you will deploy it to your users through some web domain, for example `bi-enabled.myexample.com`. For testing, JasperReports Server accepts Visualize.js requests from any domain, and your web app will display embedded reports and dashboards. However, once you go into production, you should add security and make sure that the server responds only to Visualize.js requests from your web app. This is called cross-site request forgery (CSRF) protection.

JasperReports Server includes a configurable whitelist of domains, and it only responds to Visualize.js requests from those domains. Add your web domain to this whitelist, and no other web apps on malicious domains can access your server. In addition to whitelisted domains, JasperReports Server always responds to requests that originate from the same domain as the server itself.

To configure the cross-domain whitelist

1.  Log in as system administrator (`superuser`).
2.  Select **Manage \> Server Settings** then **Server Attributes**.
3.  The server attribute named `domainWhitelist` contains a regular expression that matches allowed domains. Set it as follows:
    - When your Visualize.js web app is on another domain, such as in this example, create a regular expression to match the protocol, domain name and port numbers. You can also match multiple subdomains or several port numbers as in this example:<br>
      `domainWhitelist = http://*.myexample.com:80\d0`<br>
      The server translates this simplified expression into the proper regular expression `^http://.*\.myexample\.com:80\d0$`. If you want to avoid the translation, put `^ $` around your value.
    - When your Visualize.js web app is on the same domain as your JasperReports Server set the value to \<blank\> (no value) so that no other domain has access:<br>
      `domainWhitelist = <blank>`<br>
    - It is also possible to limit the domains accessing the JasperReports Server for each organization. For advanced configuration details, see the section on cross-domain whitelists in the JasperReports Server Security Guide.

For more information about setting attributes see the JasperReports Server Administrator Guide.

### Cross-Site Errors

Even when the domain whitelist is configured, some browsers may limit cross-site access for security reasons. In particular, the Safari browser often blocks access to the Visualize.js script because it uses third-party cookies to enable cross-site access.

There are several workarounds in this case:

- Use a different browser. Other browsers may allow access when Safari does not. However, in the future, other browsers may also begin to restrict access to third-party cookies that enable cross-site access.
- Use a proxy to make JasperReports Server appear to be on the same domain as your website. If you have already embedded Visualize.js in a cross-site way, changing to proxying will require changes to your environment (implementing and configuring a proxy service) and to your application.
- Use the same domain but different sub-domains for your application and JasperReports Server, for example:
  - www.myapp.com for your application
  - jaspersoft.myapp.com for JasperReports Server serving the Visualize.js script

When accessing JasperReports Server application resources from another domain, Chrome will treat it as a CORS request. To make this work, both applications (requestor and JasperReports Server) should communicate via HTTPS protocol:

- Server should use HTTPS.
- Client-side application should also use HTTPS.
- For XMLHttpRequest, you need to set *withCredentials=true*

JasperReports Server will send *Secure;HttpOnly Cookies* attributes.

The Chrome browser accepts cookies only with these attributes (ignoring `Path=/jasperserver-pro`, so it works for CORS requests).

### Enabling Private Network Access

When private network access is blocked for AJAX calls from public networks, you can enable private network access by configuring JasperReports Server to send an Access-Control-Allow-Private-Network: true header back to the browser.

To enable private network access

1.  Find `tomcat/webapps/jasperserver-pro/WEB-INF/applicationContext-security-web.xml`.
2.  Find `<bean id="corsProcessor" class="com.jaspersoft.jasperserver.api.security.csrf.JSCorsProcessor">`
3.  In that bean under `<property name="headerUrlPatterns">`, uncomment:

```
<entry key="Access-Control-Allow-Private-Network">
    <util:list>
        <value>.*</value>
    </util:list>
</entry>
```

1.  And under `<property name="headerValues">`, uncomment:

```
<<entry key="Access-Control-Allow-Private-Network">
    <util:list>
        <value>true</value>
    </util:list>
</entry>
```

Note that in the property `headerUrlPatterns`, you can set regex which will decide to which URL requests these headers should be set, by default there is `.*` which means that this header will be set for every request.

## Serving Visualize.js from a CDN

This feature allows you to serve Visualize.js scripts from the static host or a CDN.

### Setup

To set up:

1.  Copy the following folder: `<tomcat>/webapps/jasperserver-pro/scripts/visualize/` (or if you are building Visualize from the source code: `<jasperserver-ui>/pro/jrs-ui-pro/build/overlay/scripts/visualize/`) to the location which will be used as a static resources source.
2.  Set up your static resources server or CDN to serve content of this folder.

### Using Visualize.js from a CDN

Assumptions:

- The content of the visualize.js folder described above is available at the following URL: `https://somehost.com/visualize`
- The JasperReports Server instance is available at the URL: `https://jrshost.bi/jasperserver-pro`

The following sample shows how to use static Visualize.js:

```
<script src="https://somehost.com/visualize/visualize.js"></script>
 <div id="container"></div>
<script>
  visualize({
    publicPath: "https://somehost.com/visualize/",
    server: "https://jrshost.bi/jasperserver-pro",
    auth: {
      name: "superuser",
      password: "superuser"
    }
  }, function (v) {
    v.dashboard({
      resource: "/public/Samples/Dashboards/1._Supermart_Dashboard",
      container: "#container",
      error: function (e) {
        console.log(e);
      }
    });
  });
</script>
```

- **publicPath**: this property MUST be present if Visualize.js scripts are served from some separate server (not from JRS instance). Its value should be the URL where folder described in a Set Up section. Value should ends with /
- **server**: this property is mandatory when Visualize.js scripts are served from separate server.

You cannot use URL parameters to configure Visualize.js when it is served from a separate server. So in the above example, this will not work: `https://somehost.com/visualize/visualize.js?baseUrl=https://jrshost.bi/jasperserver-pro`

#### How to Avoid Using publicPath

If you are building Visualize.js from the source code, it is possible to hardcode the value of the publicPath property into the Visualize.js scripts during the build, so that the **publicPath** property becomes optional.

To do this, build Visualize.js from the source code (you should set up your build environment by reading the README.md in the source code):

1.  Create `.env.loca`l file in `<jasperserver-ui>/pro/jrs-ui-pro` folder.
2.  Add the following lines to this file:

```
WEBPACK_INCLUDE_CONFIGS=visualize
WEBPACK_PUBLIC_PATH=https://somehost.com/visualize/
```

1.  Build:

```
cd <jasperserver-ui>/pro/jrs-ui-pro
yarn run build
```

1.  Use build result from this folder `<jasperserver-ui>/pro/jrs-ui-pro/build/overlay/scripts/visualize/` to serve Visualize.js.

#### Serving CSS from a CDN

Visualize.js requires a special CSS which is loaded by default from the JRS instance (which is configured by server property).

This allows you to use the themeability feature because the CSS is loaded after authentication process, so the loaded CSS respects the logged in user theme.

But sometimes you might want to serve CSS from the static server (CDN).

Assuming that the CSS is accessible at this url: `https://somehost.com/visualize/css`, then the following CSS files should be accessible:

`https://somehost.com/visualize/css/jasper-ui/jasper-ui.css`

`https://somehost.com/visualize/css/jquery-ui/jquery-ui.css`

`https://somehost.com/visualize/css/dashboard/canvas.css`

`https://somehost.com/visualize/css/panel.css`

`https://somehost.com/visualize/css/webPageView.css`

`https://somehost.com/visualize/css/pagination.css`

`https://somehost.com/visualize/css/menu.css`

`https://somehost.com/visualize/css/simpleColorPicker.css`

`https://somehost.com/visualize/css/notifications.css`

In this case, use the following configuration to use custom CSS files:

```
visualize({
//... other config props
theme: {
href: "https://somehost.com/visualize/css"
}
}, function (v) {
//.....
});
```
