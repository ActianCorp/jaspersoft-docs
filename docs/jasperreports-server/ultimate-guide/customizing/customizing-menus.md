---
title: Customizing Menus
description: "A very common customization is the removal, addition, or restriction of access to the main menu of JasperReports Server. Although you can remove access to the main menu items by simply hiding the..."
---

# Customizing Menus

A very common customization is the removal, addition, or restriction of access to the main menu of JasperReports Server. Although you can remove access to the main menu items by simply hiding the menu elements with CSS in a theme, as described in [1.0.1, “Hiding UI Elements,” on page 1](themes-hiding-ui-elements.md), users can bypass this restriction. Customizing the menu structure is more robust, more secure, and lets you fine tune the functionality available to users. In particular, you can restrict access to menus based on roles, so users see different menu choices depending on their roles.

The mechanism that implements the main menu is called the actionModel, and it's defined in a set of `actionModel-*.xml` files in the `<js-webapp>/WEB-INF/` folder. The action model is a way to represent menus, sub-menus, and menu items in XML, giving each item an action when selected, as well as optional role-based restriction. The actionModel is also used to define context menus on folders and resources listed on repository browse and search pages.

The actionModel represents the structure of the menus through the structure of the XML. When pages are processed, the actionModel converts the XML into the JavaScript that generates menus.
