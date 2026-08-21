---
title: Accessibility
description: "Accessibility is the ability to access any application with ease. Websites, applications, tools, and technologies must be designed and developed in a way that makes it easy for everyone to use them...."
---

# Accessibility

Accessibility is the ability to access any application with ease. Websites, applications, tools, and technologies must be designed and developed in a way that makes it easy for everyone to use them. Accessibility enables people with special abilities to access, interact, and navigate through an application. This provides a better user experience and improves usability.

The main purpose of accessibility is to promote inclusivity among all users, including users with special abilities.

Organizations are keen to integrate accessibility. There are international guidelines of compliance that must be followed for web accessibility including:

- Web Content Accessibility Guidelines (WCAG) 2.1 also known as ISO/IEC 40500

- Country-based accessibility guidelines, such as 508c in the U.S.A.

Voluntary Product Accessibility Template (VPAT) is a template used to document the product's conformance with accessibility standards and guidelines.

For JasperReports Server, WCAG 2.1 level A and level AA are implemented. Assistive technology such as, screen reader and voice recognition systems, are used to access the application. In addition, keyboard navigation is made easier for the ease of use while not using a mouse.

WCAG is implemented on the **Login, Home, Repository, Library, and Search Result** pages. The field that must be entered first, on any of these pages, is focused on and the control is already available on that field. You can use the **Tab** key, arrow keys, **Enter** key and the **Shift + Tab** keys, on the keyboard, to navigate around the page.

There are a few limitations of accessibility in JasperReports Server, including:

- **Library**:

  - Non-text elements are not read by the NonVisual Desktop Access (NVDA) screen reader.

  - Unable to navigate to the **Favorite** icon using the keyboard.

- **Repository**:

  - While navigating from **Folder \> Add Folder**, the dialog name is not tagged as a heading.

  - Unable to navigate to the **Favorite** icon using the keyboard.

- **Favorites**:

  - **Favorite** button is not accessible using the **Tab** and arrow keys.

  - Interactive role missing for list items.

- **Search Results**:

  - Labels missing for the expandable/collapsible buttons in the **Filter** section.

  - Interactive role missing for list items in the **Filter** section.

- **Login** and **Home**:

  - Footer content overlaps at 400%.

- Repository tree, List, and Toolbar:

  - The screen reader does not provide the status message after selecting the Cut, Copy, and Paste options.

- The **End** button on the keyboard does not move focus to the last cell or last row where infinite scrolling is used.

- Touchscreen devices and mobile devices do not support accessibility.

- The **Favorite** icon is the last element read by the screen reader on each Repository List row, even though it is the first element.

## Report Exporter and Viewer

In addition, when the reports are embedded in other applications, it is the HTML output produced by the JasperReports Library HTML exporter which is displayed there. The report exporter is enhanced to introduce semantic information in the output, so that the screen reader can understand the information in the report.

For images in the report, it is mandatory to include an alternate text for the screen reader to understand and read it out. For the tables in the report, the screen reader first introduces the report, reading out the number of rows and columns. It then follows it up by reading out the information in the table.
