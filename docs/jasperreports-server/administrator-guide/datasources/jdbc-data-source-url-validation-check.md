---
title: JDBC Data Source URL Validation Check
description: "When you create a JDBC data source, the URL that gets generated automatically after adding the hostname, port, and database name has to pass the validation rules defined in the following..."
---

# JDBC Data Source URL Validation Check

When you create a JDBC data source, the URL that gets generated automatically after adding the hostname, port, and database name has to pass the validation rules defined in the following `applicationContext-settings.xml` validation configuration file.

``` text
<!-- This configuration is optional and can be commented out to disable any data source url validation -->
    <bean class="com.jaspersoft.jasperserver.remote.resources.validation.JdbcDataSourceUrlValidationSettings">
        <!--
            Validation pattern that forbids whitespace url. Ignores data source's that allow whitespaces (for example any SQL Server driver).
            To allow (disallow) whitespace you need to set property "allowSpacesInDbName" to "true" ("false") for a concrete data source.
            Please check "jdbcBasicConnectionMap" and "jdbcTibcoConnectionMap" beans in the "applicationContext-webapp.xml" file.
         -->
        <property name="forbidWhitespacesPattern" value="#{ dataSourcePatterns.getOrDefault('forbidWhitespacesPattern', '^jdbc:([^\s])+$') }"/>
        <!-- Uncomment for an additional validation that can be extended to prevent passing malicious url patterns -->
        <!--
        <property name="commonUrlPattern" value="^(?i)(?![\w\W]*(java\.|javascript))[\w\W]*$"/>
        -->
        <property name="jdbcConnectionMap" ref="jdbcConnectionMap"/>
    </bean>
```

This `applicationContext-settings.xml` file contains the following checks:

-   [URL Space Check](#url-space-check): The `forbidWhitespacesPattern` checks if a data source URL has whitespaces or not.
-   [URL String Check](#url-string-check): The `commonUrlPattern` checks if the URL matches the pattern.

!!! note

    By default, the `forbidWhitespacesPattern` is ENABLED. To disable whitespace validation, you can uncomment it.

    The `forbidWhitespacesPattern` pattern is IGNORED for all data sources when `allowSpacesInDbName` in `jdbcBasicConnectionMap` and `jdbcTibcoConnectionMap` is set to `true`.

## URL Space Check

This is the first check. It is taken care of by the following property, which verifies if the URL has a whitespace or not, some drivers allow it and some do not allow it.

``` text
 <!--
            Validation pattern that forbids whitespace url. Ignores data source's that allow whitespaces (for example any SQL Server driver).
            To allow (disallow) whitespace you need to set property "allowSpacesInDbName" to "true" ("false") for a concrete data source.
            Please check "jdbcBasicConnectionMap" and "jdbcTibcoConnectionMap" beans in the "applicationContext-webapp.xml" file.
         -->
        <property name="forbidWhitespacesPattern" value="#{ dataSourcePatterns.getOrDefault('forbidWhitespacesPattern', '^jdbc:([^\s])+$') }"/>
```

Check `jdbcBasicConnectionMap` and `jdbcTibcoConnectionMap` beans in the `applicationContext-webapp.xml` file to set the following property:

-   If `allowSpacesInDbName` is set to `true`, then whitespace in database name is allowed and `forbidWhitespacesPattern` is ignored.

-   If `allowSpacesInDbName` is set to `false`, then `forbidWhitespacesPattern` regex is applied, which does not allow whitespace in the complete JDBC URL.

## URL String Check

The URL string is validated in this check. To enable it, you can uncomment the following property for an additional validation that can be extended to prevent passing malicious URL patterns.

By default, it checks if the URL does not contain keywords like "java" and "javascript", thus preventing any Java package or any Javascript malicious code from being used in the data source URL.

``` xml
<property name="commonUrlPattern" value="^(?i)(?![\w\W]*(java\.|javascript))[\w\W]*$"/>
```

!!! note

    The `commonUrlPattern` property is global for all data sources and is DISABLED by default.

You can extend it by adding more keywords using keyword regexp construction, for example:

-   The following keyword regexp prevents select keyword.

    ``` text
    ^(?i)(?![\w\W](java\.|javascript|select))[\w\W]$
    ```

-   The following keyword regexp additionally prevents any .sql file from being used.

    ``` xml
    <property name="commonUrlPattern" value="^(?i)(?![\w\W](java\.|javascript*|select|\.sql*))[\w\W]$"/>
    ```
