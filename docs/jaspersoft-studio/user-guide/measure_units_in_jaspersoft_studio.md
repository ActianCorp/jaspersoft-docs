---
title: Units of Measure
description: "Jaspersoft Studio can handle many units of measure, including pixels, centimeters, millimeters, and inches. To accomplish this, we included a measure component in Jaspersoft Studio. This component..."
---

# Units of Measure

Jaspersoft Studio can handle many units of measure, including pixels, centimeters, millimeters, and inches. To accomplish this, we included a measure component in Jaspersoft Studio. This component looks like a standard text box with a place to enter a measure unit to the right of the value.

This component can handle a different measure unit for each field, if needed.

## Configuration

You can set two preferred (default) units of measure, one at the field level, the other at the report level. The report level unit is used wherever there is not a preferred field unit of measure. The report's default unit of measure is the pixel.

To change the report level unit

1.  Select **Window &gt; Preferences** to open the Preferences window (**Eclipse &gt; Preferences** on Mac).
2.  Expand **Jaspersoft Studio** and select **Report Designer**.
3.  Use the **Default Unit** drop-down menu to select one of the following units of measure:

-   Pixels

    -   Inches
    -   Millimeters
    -   Centimeters

## Changing the Field Unit of Measure

To change a field's local unit of measure select the field, double-click the unit of measure in the Properties view, and select a supported unit from the pop-up menu:

|  |
|----|
| ![Updating a field's measure unit](assets/images/Updating%20a%20field%27s%20measure%20unit.png) |
| *Figure 1 Updating a field's measure unit* |

## Alias and Auto-complete

Jaspersoft Studio has included alias and auto-complete services for units of measure. The following table shows your options.

| Unit       | Accepted Values                |
|------------|--------------------------------|
| centimeter | centimeter, centimeters, cm    |
| millimeter | millimeter, millimeters, mm    |
| pixel      | pixel, pixels, px              |
| inch       | inch, inches, " (double quote) |

Enter a value and begin typing a unit of measure. Auto-complete lists the matching-supported values for you to choose from.

## Approximations

Even though Jaspersoft Studio handles many units of measure, JasperReports works only with pixels. So pixels are the only unit allowed in the project file. Jaspersoft Studio approximates measurements and converts them to pixels. For example, 5 cm is converted to the nearest whole-number value in pixels. In this case the 5 centimeters is converted to 139 pixels (approximately 4.97 cm).
