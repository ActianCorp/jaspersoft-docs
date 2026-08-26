---
title: Security
description: "JasperReports IO provides security for your web applications and reports through a protection domain used by the Java security manager. A protection domain defines the security permissions, public..."
---

# Security

JasperReports IO provides security for your web applications and reports through a protection domain used by the Java security manager. A protection domain defines the security permissions, public keys, and URI for a group of JasperReports IO components, such as report expressions and repository JAR files. You can customize the permissions using the `<jrio-install>/jrio/security.policy` file.

JasperReports IO comes with a preconfigured protection domain that by default gives users all permissions to the files for:

-   The Java Virtual Machine.

-   The web application server.

-   The JasperReports IO reporting service web applications.

    The preconfigured protection domain restricts users' permissions to the following:

-   Repository JARs.

-   Report expressions.

The following shows the preconfigured protection domain settings in the `security.policy` file:

``` sql
grant codeBase "file:${java.home}/lib/-" {
permission java.security.AllPermission;
};
grant codeBase "file:${java.home}/lib/ext/-" {
    permission java.security.AllPermission;
};
grant codeBase "file:${user.dir}/jetty/-" {
    permission java.security.AllPermission;
};
grant codeBase "file:${user.dir}/jrio/webapps/-" {
    permission java.security.AllPermission;
};
//permissions for JRIO repository jars
    grant codeBase "file:/__jrio/repository/jars/" {
//permission java.security.AllPermission;
};
//permissions for JR reports
grant codeBase "file:/__jrio/repository/reports/";
```

This default configuration restricts a user's ability to pass parameters within the path of a report. You can edit the protection domain to customize the security permissions for JasperReports IO to meet your security needs.

More details about the syntax of the `security.policy` file and what permissions are available can be found in the [Java Security documentation](https://docs.oracle.com/javase/8/docs/technotes/guides/security/spec/security-specTOC.fm.html).

The protection domain and the Java security manager for used by JasperReports IO are not active when you first install the reporting service. To activate the security manager and protection domain, edit the start script in the `<jrio-install>` directory to uncomment the following:

``` text
-Djava.security.manager -Djava.security.policy=jrio/security.policy
```

The Java security manager and protection domain is active when you start the web application server.
