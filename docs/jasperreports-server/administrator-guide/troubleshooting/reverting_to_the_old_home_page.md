---
title: Reverting to the Old Home Page
description: "Some older versions of JasperReports Server included a simpler home page than is now in vogue. If your installation or customizations require the old home page with the large buttons, you can specify..."
---

# Reverting to the Old Home Page

Some older versions of JasperReports Server included a simpler home page than is now in vogue. If your installation or customizations require the old home page with the large buttons, you can specify that the server use the old home page.

1.  Open the `.../WEB-INF/flows/homeFlow.xml` file.

2.  Locate the following line:

    ``` xml
    <view-state id="homeView" view="modules/home/home">
    ```

3.  Replace the view value as shown in the following sample:

    ``` xml
    <view-state id="homeView" view="modules/old_home/home">
    ```

4.  Restart the server or redeploy the JasperReports Server web app.
