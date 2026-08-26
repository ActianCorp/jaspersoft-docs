---
title: Configuration for Repository files
description: "A new configuration is available to control and define the behavior of the \"Open\" repository option. The \"Open\" option supports the following three different behaviors:"
---

# Configuration for Repository files

A new configuration is available to control and define the behavior of the "Open" repository option. The "Open" option supports the following three different behaviors:

-   **Open file**: Opens the file in a browser.
-   **Download file**: Downloads the file by browser instead of opening the file.
-   **Open or Download file depending on file type**: The browser decides what action needs to be taken, depending on the file type. If the browser allows opening an embedded PDF file then it opens in the browser, else it downloads the file.

To configure the Open action of the file in the repository:

1.  Open the configuration file `…/WEB-INF/jasperserver-servlet.xml` for editing.

2.  Locate `<property name="whitelistDefaultOrInlineContent">` in the file. The following is the list of supported file types:

    ``` xml
    <list>
           <value>pdf</value>
           <value>xls</value>
           <value>xlsx</value>
           <value>docx</value>
           <value>rtf</value>
           <value>csv</value>
           <value>odt</value>
           <value>ods</value>
           <value>pptx</value>
           <value>json</value>
           <value>txt</value>
    </list>
    ```

    If the type of file that you have selected to open is found in the list `whitelistDefaultOrInlineContent` (see above list), then JasperReports Server allows the browser to decide whether it can open or download the file. If there is no tool available in the browser to open the file, then the browser downloads the file. Any other file type (which is not present in the above list) is always downloaded when the Open option is chosen.

    !!! note

        To be compatible with the previous implementation, we added the `forceInlineContent` (**deprecated**) property to provide the ability to instruct the browser to open those files.

        However, please note that the file type still has to be whitelisted by `whitelistDefaultOrInlineContent` (effectively, which means you have to add a file type twice in the configuration).
