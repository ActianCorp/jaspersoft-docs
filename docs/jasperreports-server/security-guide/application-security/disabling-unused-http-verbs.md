---
title: Disabling Unused HTTP Verbs
description: It is a good idea to disable all unused HTTP verbs so they cannot be used by intruders.
---

# Disabling Unused HTTP Verbs

It is a good idea to disable all unused HTTP verbs so they cannot be used by intruders.

In the default JasperReports Server installation, the following HTTP verbs are not used, but they are allowed. To make it easier to disable the verbs, they are listed in a single block of code in `<js-webapp>/WEB-INF/web.xml`. As in the code immediately above, the URL pattern `/*` applies the security constraint to all access to the server, including web service requests.

!!! warning

    The list is commented out by default because it has not been exhaustively tested with all system configurations and platforms.

After uncommenting the security constraint, your final code should be like the following:

``` text
<!-- This constraint disables the listed HTTP methods, which are not used by JS -->
<security-constraint>
  <web-resource-collection>
    <web-resource-name>RestrictedMethods</web-resource-name>
      <url-pattern>/*</url-pattern>
      <http-method>HEAD</http-method>
      <http-method>CONNECT</http-method>
      <http-method>COPY</http-method>
      <http-method>LOCK</http-method>
      <http-method>MKCOL</http-method>
      <http-method>OPTIONS</http-method>
      <http-method>PATCH</http-method>
      <http-method>PROPFIND</http-method>
      <http-method>PROPPATCH</http-method>
      <http-method>SEARCH</http-method>
      <http-method>TRACE</http-method>
      <http-method>UNLOCK</http-method>
    </web-resource-collection>
</security-constraint>
```
