---
title: Using Unicode Characters in Expressions
description: "You can use Unicode syntax to write non-Latin-based characters (such as Greek, Cyrillic, and Asian characters). For these characters, specify the Unicode code in the expression that identifies the..."
---

# Using Unicode Characters in Expressions

You can use Unicode syntax to write non-Latin-based characters (such as Greek, Cyrillic, and Asian characters). For these characters, specify the Unicode code in the expression that identifies the field text. For example, to print the Euro symbol, use the Unicode `\u20ac` character escape. The expression `\u20ac` is not simple text; it is a Java expression that identifies a string containing the € character.

!!! note

    If you use this character in a static text element, “\\u20ac” will appear. The value of a static field is not interpreted as a Java expression.
