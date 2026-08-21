---
title: Changing Colors and Fonts
description: "Changing colors, fonts, size, and spacing throughout the UI is very simple using themes. However, creating a complete theme that modifies all aspects of the UI involves changing many CSS rules and..."
---

# Changing Colors and Fonts

Changing colors, fonts, size, and spacing throughout the UI is very simple using themes. However, creating a complete theme that modifies all aspects of the UI involves changing many CSS rules and re-creating multiple images of buttons and window decorations.

To provide an example of theme customizations, the sample data installed with JasperReports Server includes three alternate themes: easy_access, pods_summer, and jasper_dark. You can activate a theme to see its effect and download its files to see how it works.

![js Customization PodsSummerTheme](../assets/images/js-Customization-PodsSummerTheme.png)

*Figure 1: Menu bar in the Sample Theme pods_summer*

Like most small-scale customizations, the pods_summer theme uses a single `overrides_custom.css` file and several files for images and sprites. The image files have the same names as those in the default theme, so when the theme is activated, they automatically replace the default images.

Sprites are image files that contain multiple images. The CSS rules that reference them give a vertical and horizontal offset for reading an individual image from the file. For icon sprites, the images often reflect the various icon states, such as enabled, disabled, mouse-over, and pressed. When customizing the theme images, having multiple images in one file is helpful because it allows you to work with many related images together in an image editor, instead of dealing with numerous files. For example, you can easily change the color hue for all buttons in a sprite file at the same time.
