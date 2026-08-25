---
title: Planning for Localization
description: Creating and editing translation files for Domains can be a complicated process that often happens incrementally. The best strategy for you depends on your deployment. The following sections describe...
---

# Planning for Localization

Creating and editing translation files for Domains can be a complicated process that often happens incrementally. The best strategy for you depends on your deployment. The following sections describe a common workflow that is useful for most situations.

Each label and description in the Domain has an internationalization key that names a property in a properties file, and the value of that property is the translated string for the item.

In the Domain Designer, the name of the internationalization keys are defined by the **Label Key** and **Descriptions Key** properties on each set and item on the **Data Presentation** tab. By default, these properties are blank. You can name the keys in any way you want, as long as each key is unique among all keys within the Domain. However, because keys are used in a Java properties file, they may only use characters from the ISO Latin-1 set, digits, and underscores (\_).

You can create and edit the properties file in any text editor. Some editors provide syntax highlighting for editing properties files. There are also Java translation editors that manage all of the properties files together, allowing you to translate in parallel and find missing keys and missing translations.

## Designing a Domain for Localization

1.  If you know you will be translating, create your labels and descriptions in a properties file instead of in the Domain Designer. This makes it easier to create and edit additional properties files in the future. You can do this even if you are not translating at this time. See [Property Values](properties_file_syntax.md) for more information on evaluation order of values.

    !!! note

        If you have no current need for translation, you can create your labels and descriptions within the Domain Designer. If you later need to translate, you can create key names and properties file as you need them.

2.  Decide whether you want to explicitly assign keys for each element, or if you want to use generated keys.

3.  If you are using generated keys, give the data islands and sets in your presentation meaningful **ID**s. It is easier to work with keys such as `ACCOUNTS_MASTER.ACCOUNTS.LABEL` rather than `JOINTREE_1.SET1.ACCOUNTS.LABEL`.

## Overview of Localizing a Domain

1.  Once you have finalized the naming of the keys or **ID**s, use the **download the template** link on the **Locale** tab in the Domain Designer to generate a file with the keys you want. See [Downloading the Bundle Template](creating_locale_bundles.md) for more information.

2.  Using the downloaded file as a starting point, create a file with blank values as a template for your properties files. If you did not explicitly define any labels or definitions, the values in the downloaded file are blank. If you have explicitly defined values, you need to remove them to create a file with blank values.

3.  Make sure to save a properties file with blank values or the default locale bundle as a template for future translations.

4.  Create a master file with the strings for your base locale. Set this as the default properties file.

    !!! note

        Make sure to create a default properties file. If every file has a locale code in the filename, the values will not appear for users in unsupported locales.

        If you prefer, you can define labels and descriptions in the Domain Designer, which display in unsupported locales. However, this makes it harder to create and maintain a blank version of the properties file.

5.  For each additional locale you want to support, copy the blank file and change the `_<locale>` designator to create a basis for the translated file. For information about file naming, see [Properties File Names](creating_locale_bundles.md).

6.  Use specialized software or a translation service to create the Java localization properties files for each locale you want to support.

7.  Use the **Locales** tab in the Domain Designer to attach the properties files to the Domain, as described in [Adding Locale Bundles to a Domain](adding_locale_bundles.md).

8.  Make sure to save a blank properties file or the default locale bundle as a template for future translations.
