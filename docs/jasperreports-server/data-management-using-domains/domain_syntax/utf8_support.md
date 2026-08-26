---
title: UTF-8 Support in Domains
description: "JasperReports Server supports international characters in the database schema, for example in the table and column names. The server supports UTF-8 (8-bit Unicode Transformation Format) character..."
---

# UTF-8 Support in Domains

JasperReports Server supports international characters in the database schema, for example in the table and column names. The server supports UTF-8 (8-bit Unicode Transformation Format) character encoding as described in the Localization chapter in the JasperReports Server Administrator Guide.

If your database is properly configured and the appropriate fonts are available to your browser, the Domain Designer displays the international characters on the various tabs where table and column names appear. This means that your data architects can work in their native language within the Domain Designer.

!!! note

    As with all values from your reporting database, table and column names are not localizable. They can only be displayed in the Domain Designer as they appear in the database. You can, however, have localized labels for these table and column names, so that they appear in the Ad Hoc designer according to the user’s locale.

IDs have the following character restrictions:

-   All UTF-8 characters are allowed in IDs except for the following symbols, which will cause errors:

`().,"=!+-></:[]*|?$`

This limitation applies to table IDs in the database as well as user-created IDs in design files and in the Domain Designer.

-   The straight single quote (`'`, Unicode 0027) can appear in database table IDs but not in user-created IDs.
-   In general, the best practice is to use alphabet characters, not punctuation or arithmetic symbols, when creating Domains.
