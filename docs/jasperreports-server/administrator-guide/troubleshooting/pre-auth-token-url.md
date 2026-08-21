---
title: Preauth Token Authentication URL Fails After Session Timeout
description: "On upgrading to JasperReports Server version 9.0, it was observed that the user is redirected to login page when preauth token authentication URL is clicked after session timeout or even when the..."
---

# Preauth Token Authentication URL Fails After Session Timeout

On upgrading to JasperReports Server version 9.0, it was observed that the user is redirected to login page when preauth token authentication URL is clicked after session timeout or even when the user logs out explicitly. If a pre-authentication token is used to access the home page or other resources, the browser returns a cached response. This prevents the request from reaching the backend for processing.

This behavior is confirmed by successfully issuing the request in a new incognito or private window, and the issue not being reproducible when the browser's *disable cache* option is enabled.

To resolve this issue, adding a new `headersRule` for pre-authentication token requests is recommended. This instructs the browser not to cache these specific requests.

In `applicationContext-webapp.xml`, insert a new bean at the beginning of the `headerRules` list within `resourceHTTPHeadersFilter`.

``` xml
<bean p:method="GET" p:urlPattern=".*\\?pp.*" class="com.jaspersoft.jasperserver.war.httpheaders.HeadersRule">
                <property name="headers">
                    <list>
                        <bean class="org.apache.http.message.BasicHeader">
                            <constructor-arg value="Cache-Control"/>
                            <constructor-arg value="no-cache, no-store, must-revalidate"/>
                        </bean>
                        <bean class="org.apache.http.message.BasicHeader">
                            <constructor-arg value="Pragma"/>
                            <constructor-arg value="no-cache"/>
                        </bean>
                        <bean class="org.apache.http.message.BasicHeader">
                            <constructor-arg value="Expires"/>
                            <constructor-arg value="0"/>
                        </bean>
                    </list>
                </property>
            </bean>
```

!!! note

    `pp` is the `principalParameter` defined in `proxyPreAuthenticatedProcessingFilter`.
