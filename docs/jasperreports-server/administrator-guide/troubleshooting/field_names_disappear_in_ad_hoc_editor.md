---
title: Field Names Disappear in Ad Hoc Editor
description: Some fields with international characters in their display names disappear when the field is dragged into the canvas of the Ad Hoc Editor. This is caused by non-Unicode characters used in the field...
---

# Field Names Disappear in Ad Hoc Editor

Some fields with international characters in their display names disappear when the field is dragged into the canvas of the Ad Hoc Editor. This is caused by non-Unicode characters used in the field name in the JRXML underlying the selected Topic.

To make the international characters appear in Ad Hoc view field labels, use the resource bundle mechanism:

1.  Create a resource bundle (`*.properties`) and associate each of your field labels with a unique key. Use Unicode escape sequences such as `\u0153` for the œ character to insert international characters in your label values.
2.  Use the `$R` syntax in the Topic to specify the appropriate key for the label of each desired field.
3.  Upload the resource bundle as a resource of the Topic.

When you open the Topic in the Ad Hoc Editor, the labels are displayed correctly from the resource bundle.

This method has the advantage that you can create a resource bundle for each language the Topic needs to support, and users see the labels for the locale they set in their browser.

For more information about localizing JasperReports Server, see [Localization](../localization/localization_intro.md).
