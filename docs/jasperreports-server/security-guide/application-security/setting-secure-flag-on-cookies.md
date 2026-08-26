---
title: Setting the Secure Flag on Cookies
description: "JasperReports Server uses cookies in several ways:"
---

# Setting the Secure Flag on Cookies

JasperReports Server uses cookies in several ways:

-   `userTimezone` and `userLocale` to store user settings.
-   Other UI settings such as **Recently Viewed Resources** and **Popular Resources** on the **Home** page and **Data Source** page history. The cookie names for those resources are `homePageRecentlyViewedResourcesExpandableListState`, `homePagePopularLinksExpandableListState`, and `DataSourceControllerHistory`.

The JSESSIONID cookie is managed by the application server, so its security setting depends on your app server configuration.

Jaspersoft does not set the secure flag on these cookies because we do not want to force you to use secure connections. If you want all cookies to be secure, you must customize the source files that create the cookies. This requires the source code distribution and recompiling and building the server app, as described in the JasperReports Server Source Build Guide.

To customize JasperReports Server so cookies are sent only via secure connections:

1.  For the time zone and locale cookies, open the following file to edit:

    `jasperserver-war-jar\src\main\java\com\jaspersoft\jasperserver\war\UserPreferencesFilter.java`

2.  Locate the following code in two locations, one for each cookie, and add the middle line to both:

    ``` text
    cookie.setMaxAge(cookieAge);
    cookie.setSecure(true); /* requires HTTPS */
    ...
    httpOnlyResponseWrapper.addCookie(cookie);
    ```

    For more information, see the JavaDoc for the [setSecure](https://jakarta.ee/specifications/platform/10/apidocs/jakarta/servlet/http/cookie#setSecure(boolean)) method on the `javax.servlet.http.Cookie` class.

3.  For the cookies set in JavaScript (`homePageRecentlyViewResourcesExpandableListState` and `homePagePopularLinksExpandableListState`), edit the `jasperserver-ui/pro/jrs-ui-pro/src/home/util/cookie.ts` file.

4.  Locate the following code:

    ``` properties
    document.cookie = Object.keys(opt).reduce((cookie, key) => {
                let result = `${cookie}; ${key}`;
                const optionValue = opt[key];
                if (optionValue !== true) {
                    result += `=${optionValue}`;
                }

                return result;
            }, `${name}=${encodeURIComponent(value)}`);
    ```

    Modify the code as follows:

    ``` properties
    document.cookie = Object.keys(opt).reduce((cookie, key) => {
                let result = `${cookie}; ${key}`;
                const optionValue = opt[key];
                if (optionValue !== true) {
                    result += `=${optionValue}`;
                }

                return result;
            }, `${name}=${encodeURIComponent(value)}`) + ";secure;";
    ```

5.  Edit the `jasperserver-ui/ce/jrs-ui/src/util/utils.common.js` file.

6.  Locate the following line:

    ``` text
    return _.template('{{- name}}={{- value}}; expires={{- expires}}; path=/;')
    ```

    Modify the line as follows:

    ``` text
    return _.template('{{- name}}={{- value}}; expires={{- expires}}; path=/;secure;')
    ```

7.  To redeploy the JavaScript files, you need to optimize and implement them as described in the section "Customizing JavaScript Files" in the JasperReports Server Ultimate Guide. The optimized scripts are the ones that are served by JasperReports Server by default.

8.  Recompile, rebuild, and redeploy the JasperReports Server application.

    This acts only on the cookies. Providing a secure connection is up to the client application, usually by configuring and establishing an HTTPS connection, as described in [Using SSL in the Web Server](using-ssl-in-web-server.md). If no secure connection is established, the cookies with the secure flag will not be sent and user settings will not take effect.
