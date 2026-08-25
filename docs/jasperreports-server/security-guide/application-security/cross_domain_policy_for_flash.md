---
title: Defining a Cross-Domain Policy for Flash
description: "JasperReports Server can be configured to use Flash for advanced Fusion-based charts such as gauges and maps. For security reasons, a Flash animation playing in a web browser is not allowed to access..."
---

# Defining a Cross-Domain Policy for Flash

JasperReports Server can be configured to use Flash for advanced Fusion-based charts such as gauges and maps. For security reasons, a Flash animation playing in a web browser is not allowed to access data that resides outside the exact web domain where the SWF originated.

As a result, even servers in subdomains cannot share data with a server in the parent domain unless they define a cross-domain policy that explicitly allows it. The file `crossdomain.xml`, located at the root of the server containing the data, determines which domains can access the data without prompting the user to grant access in a security dialog. Therefore, the server containing the data determines which other servers may access the data.

The following `crossdomain.xml `sample allows access from only the example domain or any of its subdomains. This example says the server with this file trusts only example.com to use its data.

``` xml
<?xml version="1.0" ?>
    <!DOCTYPE cross-domain-policy SYSTEM
        "http://www.macromedia.com/xml/dtds/cross-domain-policy.dtd">

    <cross-domain-policy>
        <allow-access-from domain="example.com" />
        <allow-access-from domain="*.example.com" />
    </cross-domain-policy>
```

Behind a firewall, servers and users often refer to other computers in the same domain without using the domain name. Flash considers this a different domain and blocks access to data unless the computer name is given in the policy.

``` xml
    <cross-domain-policy>
        <allow-access-from domain="myserver.example.com" />
        <allow-access-from domain="myserver" />
    </cross-domain-policy>
```

When using web services, use the `allow-http-request-headers-from` element so that actions encoded in the request header are allowed. The following example allows standard requests and web service requests from any subdomain of example.com.

``` xml
    <cross-domain-policy>
        <site-control permitted-cross-domain-policies="master-only"/>
        <allow-access-from domain="*.example.com"/>
        <allow-http-request-headers-from domain="*.example.com" headers="*"
            secure="true"/>
    </cross-domain-policy>
```

For a description of all possible properties, see the [cross-domain policy file specification](http://www.adobe.com/devnet/articles/crossdomain_policy_file_spec.html).

To define a cross-domain policy for Flash-based reports, create a file such as the one above on the server containing the data being accessed. Be sure to place the `crossdomain.xml` file at the root of the filespace being served. For example, if you use Apache Tomcat, place your files in the following locations:

| File | Location |
|----|----|
| `crossdomain.xml` | `<website-B-tomcat-dir>/webapps/ROOT/crossdomain.xml` |
| XML data (\*.xml) | `<website-B-tomcat-dir>/webapps/ROOT/<any-dir>/*.xml` |
| Flash component (\*.swf) | `<website-A-tomcat-dir>/webapps/<appname>/<any-dir>` |

For more information o configuring the server to use Flash to render advanced charts, see the JasperReports Server Administrator Guide.
