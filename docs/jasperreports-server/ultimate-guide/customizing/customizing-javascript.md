---
title: Customizing JavaScript Source Code
description: The JavaScript source code is customized to improve performance.
---

# Customizing JavaScript Source Code

The JavaScript source code is customized to improve performance.

To customize the JavaScript source code

1.  Create a working directory where you can extract sources from the JasperReports Server source bundle Zip file (`TIB_js-jrs_<version>_src.zip`).
2.  Download and install node.js from <http://nodejs.org/>.
3.  Install yarn (version 1.22.x is required).
4.  Run the following commands to install node modules.

-   `cd jasperserver-ui/pro`

    -   `yarn install`

        1.  Make your changes to the JavaScript source code.
        2.  Run the following commands to build the final bundled static assets.

    -   `cd jasperserver-ui/pro/jrs-ui-pro`

    -   `yarn run clean`

    -   `yarn run build`<br>
        Bundled static assets will be placed in the `jrs-ui/build/overlay/scripts` folder.

1.  Back up the `scripts` folder of your JasperReports Server instance deployment.<br>
    For example, `<tomcat>/webapps/jasperserver-pro/scripts` folder, when Apache Tomcat is used.
2.  Delete the content of the `scripts` folder of your JasperReports Server instance deployment.<br>
    For example, `<tomcat>/webapps/jasperserver-pro/scripts` folder.
3.  To deploy bundled static assets (build result) to the JasperReports Server instance, copy the content of the `jrs-ui-pro/build/overlay/scripts` folder to the `scripts` folder of your JasperReports Server instance deployment.<br>
    For example, `<tomcat>/webapps/jasperserver-pro/scripts` folder.

!!! note

    Visualize.js will be built as part of the build process of JavaScript source code. Therefore, there is no separate build process for Visualize.js while starting JasperReports Server 10.0.0.<br>
