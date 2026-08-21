---
title: Implementation Suggestions
description: "The iReport plugin for JasperReports Server relies on the repository web service described in this document. If you use Java, Jaspersoft recommends that you familiarize yourself with the plugin’s..."
---

# Implementation Suggestions

The iReport plugin for JasperReports Server relies on the repository web service described in this document. If you use Java, Jaspersoft recommends that you familiarize yourself with the plugin’s source code, as it can help you understand how best to implement your own web services client. It is included in JasperReports Server Professional and Enterprise editions. It is also available in the [JasperReports Server source code](http://sourceforge.net/project/showfiles.php?group_id=162962) on SourceForge. In the source code, look for the plug-in files in this location: `jasperserver/jasperserver-ireport-plugin`. Download the ZIP file that contains the iReport plugin. In particular, this JAR can be very illuminating:

\<js-install\>\ireport\ireport\modules\com-jaspersoft-ireport-jasperserver.jar

Its dependencies, located in \<js-install\>\ireport\ireport\modules\ext, are:

- `js_activation-1.1.jar`
- `js_axis-1.4patched.jar`
- `js_commons-codec-1.3.jar`
- `js_commons-discovery-0.2.jar`
- `js_commons-httpclient-3.1.jar`
- `js_jasperserver-common-ws-3.5.0.jar`
- `js_jaxrpc.jar`
- `js_mail-1.4.jar`
- `js_saaj-api-1.3.jar`
- `js_wsdl4j-1.5.1.jar`

If necessary, you can marshal and unmarshal request and response objects by using the following classes:

- `com.jaspersoft.jasperserver.ws.xml.Marshaller`
- `com.jaspersoft.jasperserver.ws.xml.Unmarshaller`

If you use a development environment other than Java (such as .NET), you can easily generate a client from the WSDL.
