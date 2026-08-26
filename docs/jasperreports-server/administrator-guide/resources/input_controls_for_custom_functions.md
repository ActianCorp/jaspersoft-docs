---
title: Input Controls with Custom Functions
description: Input Controls with custom functions in JasperReports Server are user-defined components that allow you to filter or provide specific input for reports or dashboards. It provides advanced user...
---

# Input Controls with Custom Functions

Input Controls with custom functions in JasperReports Server are user-defined components that allow you to filter or provide specific input for reports or dashboards. It provides advanced user interface elements that go beyond the basic, built-in types to collect parameters from the user before running a report.

You can provide an custom expression using a subset of DomEL or call custom JavaScript/Groovy functions defined in the `/WEB-INF/custom_functions/` directory.

To create an input control with custom functions:

1.  Follow steps 1 through 8 in the [Input Controls](input_controls.md) section.

2.  In the **Display Settings** section, select the custom input control options in:

    -   **Enable/Disable Input Control &gt; Conditional**
    -   **Show/Hide Input Control &gt; Conditional**

    !!! note

        For more information, see the Input Controls with Custom Expressions section in the JasperReports Server User Guide.

3.  Call the custom Javascript/Groovy functions defined in the `WEB INF/custom_functions` directory:

    -   HasAnyRoles('ROLE_SUPERUSER')

    -   startsWith(Country,'M')

    -   contains(Country, 'ca')

    Following are examples of the `contains.js` and `contains.groovy` custom functions defined in the `/WEB-INF/custom_functions` directory.

    1.  `contains.js`

        ``` text
        function contains(ctx, str, substring) {
            return str.includes(substring);
        }
        ```

    2.  `contains.groovy`

        ``` text
        static def contains(Expando ctx, str, substring) {
            return (str as String).contains(substring as String)
        }
        ```
