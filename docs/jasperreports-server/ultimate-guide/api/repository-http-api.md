---
title: Repository HTTP API
description: "The HTTP interface provides an easy way to implement the API for accessing repository objects. However, the HTTP interface can't be embedded the way the web services and Visualize.js APIs can be in..."
---

# Repository HTTP API

The HTTP interface provides an easy way to implement the API for accessing repository objects. However, the HTTP interface can't be embedded the way the web services and Visualize.js APIs can be in non-Jaspersoft applications. Rather, the HTTP interface is used primarily as shortcuts or entry points to commonly used features or content. Typically, the HTTP interface is accessed programmatically by generating the URL that returns HTML that displays either the desired object (in the case of report execution and repository URLs) or the content of repository objects (such as report output in the form of content resources).

As shown in the following examples, the major entry points are:

-   flow.html

-   dashboard/\*\*

-   olap/\*\*

-   fileview/\*\*

!!! note

    The examples in this section are generalized to describe both the community and commercial editions of JasperReports Server. For simplicity, this section refers to the deployment context generically.

    For example:

    -   `http://<host>:<port>/<context>/flow.html?_flowId=searchFlow&folderUri=/public/Samples/Reports`
    -   `http://<host>:<port>/<context>/flow.html?_flowId=searchFlow&folderUri=/public/Samples/Reports`

    With the default deployments, the `<context>` refers to:

    -   `jasperserver-pro` in the commercial editions
    -   `jasperserver` in the community project

## General Parameters

The following parameters can be used for any URL that points to a JasperReports Server web page. The parameters are specified as standard HTTP GET parameters (that is, they are in the form `name=value` and are separated by ampersands (&)). For dashboard URLs in JasperReports Server 6.0 and 6.0.1, general parameters must be placed before the \# sign.

!!! warning

    If the server is hosted by Tomcat 8.5.x and higher, you need to encode all pipe symbols (\|, encoded as %7C) in the parameter to make the parameter URL-safe. For example, the format for a user in an organization would be `j_username=userID%7CorgID`.

-   `userlocale`: It specifies the locale of the user. It can be added to the startup URI, as in this example:

    `http://localhost:8080/jasperserver-pro/login.html?userLocale=en_US`

-   `j_username` and `j_password`: Pass these credentials to authenticate a user with the server. The user name must correspond to a valid user, and `j_password` must be the user password (in clear text).

    If you use a commercial edition and host more than one organization, the organization ID or alias must be passed along with the user ID as part of the `j_username` parameter. The format for a user in an organization is `j_username=userID|orgID`.

    If the credential parameters are not present, no authenticated server session exists, and the server is not configured to use automatic authentication (such as Single Sign-on), the server prompts the user for a username and a password, then redirects the user to the requested page. These authentication parameters let the user skip the login page and directly access a specific page.

-   `theme`: specifies a theme to use for the JasperReports Server interface. Once a theme has been set, it remains the default until the user log out, the session ends, or another theme is set.

-   `decorate`: `decorate=no` removes the page headers, footers, and borders from the requested page. Page titles are not removed. The default is `decorate=yes`.

-   `sessionDecorator`: `sessionDecorator=no` removes the page headers, footers, and borders from the JasperReports Server user interface for the entire user session. Once `sessionDecorator` has been set (`yes` or `no`), the setting remains the default until the user log outs, the session ends, or `sessionDecorator` is called again. As with `decorate`, page titles are not removed.

!!! note

    You can also remove decorations using a custom theme. See [1.0.1, “Using Themes to Remove Branding,” on page 1](../customizing/themes-removing-branding.md) for more information.

## Executing ReportUnits

The following sections provide examples and details about URLs that execute reports.

### Simple Report Execution

The HTTP interface can execute and export reports within the JasperReports Server web application.

The following example calls a report with no parameters and exports to the default format (HTML):

The URL is:

``` text
http://<host>:<port>/<context>/flow.html?_flowId=viewReportFlow&
reportUnit=/public/Samples/Reports/SalesByMonthReport
```

This is the simplest possible report execution URL. The following section explains more advanced options.

### Passing ReportUnit Execution Parameters

Reports support the following types of parameters:

-   General parameters supported by all URLs, such as `theme` or `userLocale`.

-   Reserved report parameters such as `output` or `reportLocale`.

-   Input control parameters, described in [1.1.4, “Input Control Parameters for Reports and Dashboards,” on page 1](#input-control-parameters-for-reports-and-dashboards).

The following example executes the same report as the previous section, but also passes `7` as an input control parameter and exports to PDF instead of HTML:

``` text
http://<host>:<port>/<context>/flow.html?_flowId=viewReportFlow
&reportUnit=/public/Samples/Reports/SalesByMonthReport&startMonth=7&output=pdf
```

Note the URL parameters:

-   `&startMonth=7` indicates that the value 7 should be passed to the input control called startMonth. The report returns data starting in July.

-   `&output=pdf` indicates that the output should be generated in PDF format.

If the report parameter supports multiple values, you can specify them using the ampersand (&); for example:

``` text
http://<host>:<port>/<context>/flow.html?_flowId=viewReportFlow&reportUnit=
/reports/SalesbyState&country=US&country=Canada&output=pdf
```

The report execution parameters can either be reserved parameters the server uses to determine the general attributes of the report execution, or arbitrary parameters that correspond to the report’s input controls/parameters. The parameters are specified as standard HTTP GET parameters (in `name=value` form and separated by ampersands (&)).

### Reserved Report Parameters

The following reserved report parameters are recognized by JasperReports Server:

-   `reportUnit`: specifies the URI of the report unit in the repository.
-   `output` (optional): specifies the output format. Values for this parameter are keys for the report exporters configured in the server. By default, the server recognizes the following output types: `pdf` for PDF, `xls` for Excel (Paginated), `xlsNoPag` for Excel, `xlsx` for XLSX (Paginated), `xlsxNoPag` for XLSX, `rtf` for RTF, `csv` for CSV and `swf` for the Flash report viewer. When this parameter is not specified, the default format is HTML displayed in the report viewer.
-   `reportLocale`: specifies the locale where the report should be executed. A locale is passed as code consisting of a lower-case two letter ISO-639 language code, followed by an optional upper-case two letter ISO-3166 country code and a locale variant, separated by underscore (the format is identical to the standard Java locale programmatic names).
-   `pageIndex` (optional): specifies the initial page to be displayed when launching the target report. The page index is 1-based. If a negative page index or a page index greater than the number of pages in the report is used, the report opens at the first page. This parameter is effective only for HTML output.
-   `anchor` (optional): specifies the name of an anchor from the target report at which the report should open. If an anchor with the specified name is not found in the report, the first page of the report is shown. The parameter is effective only when `pageIndex` is not specified and when the output is HTML.

## Executing Dashboards

As of JasperReports Server 6.0, dashboards do not use the flow.html entry point used by Spring Web Flow. Instead, they use an updated dashboard entry point.

!!! note

    If you are working with legacy dashboards created in versions before 6.0, these dashboards work similar to reports.

The following example opens a dashboard for viewing:

``` text
http://<host>:<port>/<context>/dashboard/viewer.html#/public/Samples/Dashboards/1._Supermart_Dashboard
```

To open a dashboard for editing, call the Dashboard Designer:

``` text
http://<host>:<port>/<context>/dashboard/designer.html#/public/Samples/Dashboards/1._Supermart_Dashboard
```

!!! note

    The dashboard Resource URL must go after the hash sign (#). This syntax supports faster page refreshing. When you save a new or existing dashboard, only the URL segment after the hash sign is reloaded.

### Passing Dashboard Execution Parameters

-   Dashboards support the following types of parameters:

    General parameters supported by all URLs, such as `theme` or `userLocale`.

-   The reserved dashboard parameters `viewAsDashboardFrame` and `dashboardResource`

-   Input control parameters, described in [1.1.4, “Input Control Parameters for Reports and Dashboards,” on page 1](#input-control-parameters-for-reports-and-dashboards).

As of JasperReports Server 6.1, you can use non-authentication parameters before or after the hash sign (#). However, if you place general parameters after the hash sign, then on Dashboard Viewer load, the parameters are moved before the hash sign and the page is redirected to the resulting URL. The authentication parameters `j_username` and `j_password` cannot be redirected; they must appear before the hash sign.

For example, suppose you enter the following URL:

``` text
http://<host>:<port>/<context>/dashboard/viewer.html?theme=pods_summer#/public/Samples/Dashboards/1._Supermart_Dashboard&userLocale=de&country=Mexico
```

When you go to the Dashboard Viewer, you are redirected as follows:

``` text
http://<host>:<port>/<context>/dashboard/viewer.html?theme=pods_summer&userLocale=de&country=Mexico
#/public/Samples/Dashboards/1._Supermart_Dashboard
```

### Reserved Dashboard Parameters

The following reserved dashboard parameters are available:

-   `viewAsDashboardFrame` (optional): displays the dashboard without any decoration. This setting is similar to decorate=no, but hides the dashboard viewer toolbar in addition to the page headers, footers, and borders. You can use `viewAsDashboardFrame` when you embed your dashboard in another webapp. For example:

``` text
http://<host>:<port>/<context>/dashboard/viewer.html?viewAsDashboardFrame=true#/public/MyDashboard
```

-   `dashboardResource` (optional, deprecated): supports earlier versions of JasperReports Server dashboard execution URLs. Use only for backwards compatibility.

``` text
http://<host>:<port>/<context>/dashboard/viewer.html?dashboardResource=/public/MyDashboard
```

When your application uses this format, JasperReports Server automatically redirects it to the new dashboard viewer format. For example, the URL above would be redirected to:

`http://<host>:<port>/<context>/dashboard/viewer.html#/public/MyDashboard`

## Input Control Parameters for Reports and Dashboards

In addition to the standard parameters, report and dashboard execution URLs can contain parameters that provide values for input controls/parameters. The URL parameter names must match the name of the corresponding input control. The values used for such URL parameters depend on the type of input control:

-   For filters or simple single value input controls, the value is a URL parameter value:

    -   If the type of the input control is text, the URL parameter value is directly used as the input control value.
    -   If the type of the input control is numeric, the URL parameter value is the numerical value formatted according to standard rules, using a period (.) as the decimal separator.
    -   If the type of the input control is date or date/time, the URL parameter value is the date/time value formatted as described in the jasperserver_config\_&lt;locale&gt;.properties file for the current locale. See the *JasperReports Server Administrator Guide* for more information on formatting date and time. The following table shows the formats for the default locale.

    | Input Control Type | URL Parameter Format    | Example             |
    |--------------------|-------------------------|---------------------|
    | date.format        | yyyy-MM-dd              | 2021-06-28          |
    | datetime.format    | yyyy-MM-dd 'T' HH:mm:ss | 2021-06-28T13:45:22 |
    | time.format        | HH:mm:ss                | 13:45:22            |

-   For Boolean (check box) input controls, the URL parameter value is either `true` or `false`.

-   For input controls that refer to a static list of values, the URL parameter value is the key/value of the list entry. For example, to select the first value in a list called `ListInput`, use the parameter `&ListInput=1`.

-   For input controls that rely on a query, the URL parameter value corresponds to the query key/value column. For example, to set a query-based control to the value `l_meade`, use the parameter `&QueryInput=lmeade`.

-   For multi-value input controls, multiple occurrences of the same URL parameter can be used. For example, `parameter=value1&parameter=value2&parameter=value3`.

-   You can use the following special values for input controls:

    -   no value: when a string parameter is called with no value, it finds all instances where the string is empty, for example, `&Country=`. When the database result set does not include an empty string value, this URL input is ignored.

    -   `~NULL~`: finds NULL value. For example, `&Address=~NULL~` returns all records with a NULL address. When the database result set does not include any NULL values, this URL input is ignored.

    -   `~NOTHING~`: depends on the form of the input control:

        -   For an input control that supports multi-selection, `~NOTHING~` clears the current selection and resets the input control to all values. (The generated SQL query in this case is 0=0, which essentially omits the filter.) For example, consider a multi-value input control named MultiInput. By default, this parameter is a list of two values. To override this list of values with another set of two values, you could use the parameter `&MultiInput=item1&MultiInput=item2`, where `item1`and `item2` are the overriding list values. To override the default with an empty list, use the parameter `&MultiInput=~NOTHING~`.
        -   For a single-select, non-mandatory input control, `~NOTHING~` selects --.
        -   For a single-select, mandatory input control, `~NOTHING~` selects the default value.

If the parameter values included in a report or dashboard execution URL are not valid (for example, if a required parameter is missing or a parameter value is not valid), the user is prompted with the input controls so they can correct the values.

## Linking to Content

The HTTP interface can return generated content saved to the repository in PDF, HTML, Excel, or RTF format.

The following example links to a PDF file stored in the repository:

``` text
http://<host>:<port>/<context>/fileview/fileview/public/Samples/Reports/05._Accounts_Report.pdf
```

## Viewing Resources in the Repository

The following example displays all resources saved in the /public/Samples/Reports folder in the repository:

``` text
http://<host>:<port>/<context>/flow.html?_flowId=searchFlow&folderUri=/public/Samples/Reports
```

The following example displays all resources of the type `olapview` (analysis view) saved in all folders in the repository:

``` text
http://<host>:<port>/<context>/flow.html?_flowId=olapViewListFlow
```
