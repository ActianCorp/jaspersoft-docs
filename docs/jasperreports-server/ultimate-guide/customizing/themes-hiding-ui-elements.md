---
title: Hiding UI Elements
description: "Setting the parameter display:none; is a convenient way to hide any element through the CSS. If you set display:none; as an override, the corresponding element is not rendered in the browser. You can..."
---

# Hiding UI Elements

Setting the parameter `display:none;` is a convenient way to hide any element through the CSS. If you set `display:none;` as an override, the corresponding element is not rendered in the browser. You can use `display:none;` alone or in addition to other CSS parameters.

!!! warning

    The hidden element still exists in the HTML transmitted to browsers, so don't use this parameter to hide sensitive information. For example, if you hide a menu item, a user with the FireBug plug-in to Firefox can remove the `display:none;` attribute to reveal the menu and use it. For a more secure way to remove menu items, see [Restricting Access by Role](restricting-access-by-role.md).

The following example shows how to use this parameter to remove the logo or the search box from the UI.

To remove the logo and/or the search box

1.  Edit a theme or create one.
2.  If necessary, copy the `overrides_custom.css` file from the default theme to the main folder of your theme.
3.  Do one or both of the following:

-   Remove the logo. Edit the `overrides_custom.css` file and add the following CSS rules:

    ``` bash
    #logo {
      display:none;
    }
    ```

    -   Remove the search box. Edit the overrides_custom.css file and add the following CSS rules:

``` text
.searchLockup {
display: none
}
```

1.  Upload and activate the new theme with your image and CSS file, then click your browser’s **Refresh** button.

You can also use this attribute to hide the footer in the UI. For instructions on changing the text in the footer, see [Editing decorator.jsp for Rebranding](customizing-ui-with-sitemesh.md).

To remove the footer

1.  In your `overrides_custom.css` file, add the following CSS statement to hide the footer:

    ``` bash
    #frameFooter {
        display: none;
    }
    ```

2.  Save and upload your `overrides_custom.css` file to your theme.
