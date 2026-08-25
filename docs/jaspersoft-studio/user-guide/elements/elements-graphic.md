---
title: Graphic Elements
description: Graphic elements like lines and shapes are used to make reports more attractive and readable. You can also add these by dragging them from the palette to the report editing area.
---

# Graphic Elements

Graphic elements like lines and shapes are used to make reports more attractive and readable. You can also add these by dragging them from the palette to the report editing area.

## Line

In Jaspersoft Studio, a line is defined by a rectangle for which the line represents the diagonal. By default, the foreground color is used as the default color and a 1-pixel-width line is used as the line style.

You can customize the look, style, and direction of the line in the element’s Properties view.

## Rectangle and Ellipse

The rectangle element is usually used to draw frames around other elements. By default, the foreground color setting is used and a normal one pixel width.

The ellipse is the only element that has no attributes specific to it. The ellipse is drawn in a rectangle that defines the maximum height and width. By default, the foreground color is used, and a normal 1-pixel-width line is used as line style. The background is filled with the background color setting if the element has not been defined as transparent.

## Images

An image is the most complex of the graphic elements. You can insert raster images (such as GIF, PNG and JPEG images) in the report, but you can also use an image element as a canvas object to render, for example, a Swing component, or to use some custom rendering code.

Dragging an image element from the Palette into the report editing area opens the **Create new image element** dialog. This is the most convenient way to specify an image to use in the report. Jaspersoft Studio does not save or store the selected image anywhere, it just uses the file location, translating the absolute path of the selected image into an expression to locate the file when the report is run. The expression is then set as the value for the `Image Expression` property.

You can add an image by explicitly defining the full absolute path of the image file in your expression. This is an easy way to add an image to the report, but, overall, it has a significant impact on the report’s portability, since the file may not be found on another machine (for instance, after deploying the report on a web server or running the report on a different computer).

## Padding and Borders

For the image and text elements you can visualize a frame or define a particular padding (the space between the element border and its content) for the four sides. Border and padding are specified by selecting the element in the report editing area, and using the Properties view.

In the Properties view, click the **Borders** option. This includes the following controls:

- Padding allows you to define padding widths for each of the four sides, or to apply the same value to all sides.
- Borders allow you to select their color, style, and width, as well as choose where it appears.

As always, all the measurements are shown in pixels.
