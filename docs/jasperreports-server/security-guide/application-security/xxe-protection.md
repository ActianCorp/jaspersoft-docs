---
title: Protecting Against XML External Entity Attacks
description: "XML files are vulnerable to XML External Entity (XXE) attacks when they include a Document Type Definition (DTD) with a DOCTYPE declaration. Because of this risk, JasperReports Server checks for..."
---

# Protecting Against XML External Entity Attacks

XML files are vulnerable to XML External Entity (`XXE`) attacks when they include a Document Type Definition (`DTD`) with a `DOCTYPE` declaration. Because of this risk, JasperReports Server checks for `DOCTYPE` declarations. By default, this protection is disabled as the setting causes errors if the XML files are vulnerable to the attack. Consider enabling this setting if `XXE` attacks are a concern. For more information on this security issue, see [Wikipedia's article on XML External Entity Attack.](https://en.wikipedia.org/wiki/XML_external_entity_attack)

Before enabling the check, ensure that the XML files in your repository do not include DOCTYPE declarations.

To enable XXE protection:

1.  Identify and edit any XML file in the JasperReports Server repository that include a `DOCTYPE` declaration. Delete the declaration and update the JasperReport on the server. Since JasperReports Server does not support `DTDs` themselves, we recommend removing them entirely.
2.  Use a text editor to open the `.../WEB-INF/applicationContext.xml` file.
3.  Locate the `skipXXECheck` property and set it to `false`.
4.  Restart JasperReports Server.

# Protecting Against Clickjacking Attacks

JasperReports Server implements a mechanism to protect against clickjacking attacks. To enable this mechanism, edit the `applicationContext-security-web.xml` configuration file.

1.  Using a text editor, open the `applicationContext-security-web.xml` file (found in `<js-install>\apache-tomcat\webapps\jasperserver-pro\WEB-INF`).
2.  Locate the `antiClickJackingEnabled` property in the `webAppSecurityFilter` bean, and set it to `true`. Setting this property to true instructs JasperReports Server to include an X-Frame-Options header in every response.
3.  You can also set the `antiClickJackingOption` property to control the header value. Valid values are:

-   `DENY` - JasperReports Server does not load into any iframe.
-   `SAMEORIGIN` - JasperReports Server only loads into an iframe on a page in the same domain as JasperReports Server.
-   `ALLOW-FROM` - JasperReports Server only loads in a frame on a page specified in the `antiClickJackingUri` property.

1.  If you set the `antiClickJackingOption` property to `ALLOW-FROM`, also set the `antiClickJackingUri` property to a valid URI.
2.  Save the file and restart the server.

!!! note

    If you use iframes to embed JasperReports Server (including use of Visualize.js), set `antiClickJackingOption` to either:

    -   `SAMEORIGIN` (if the embedding host is on the same domain as JasperReports Server) or

    -   `ALLOW-FROM` (if the embedding host is on a different domain than JasperReports Server).

    If you use `ALLOW-FROM`, set the `antiClickJackingUri` property too.

Clickjack protection does not support cases in which multiple domains embed JasperReports Server.
