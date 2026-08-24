---
title: Jaspersoft Studio Source Build
description: This document describes how to compile and run the Jaspersoft® Studio Professional edition from the sources file.
---

# Jaspersoft Studio Source Build

This document describes how to compile and run the Jaspersoft® Studio Professional edition from the `sources` file.

!!! note

    Version 10.1 is used as an example, but the details are also valid for newer versions.

## Zip Package Contents

The zip package named `js-jss_10.1.0_sources.zip` contains the following items:

- `jrePackages` folder: Contains compressed files of the JRE version shipped with Jaspersoft Studio (required during the build).

- `playwrightPackages` folder: Contains compressed files of the Playwright version shipped with Jaspersoft Studio (required during the build and runtime).

- `sources` folder: Contains the source code of the Jaspersoft Studio Professional version.

- `targetRepoE436-10.1.0.zip` : Contains the target repository that can be used for both compiling in the Eclipse and building via Maven Tycho.

- `js-jss_10.1.0_license.txt` file: The current license file.

## Setting Up Eclipse and Your Workspace

To set up Eclipse and Workspace:

1.  Download the latest version of Eclipse from the website: <http://www.eclipse.org/>.<br>
    Normally, the Jaspersoft® developers use the **Eclipse IDE for a RCP and RAP developers** version.

As of the time this document's creation, Eclipse 2025-09 (version 4.37) was the most recent release.

1.  Choose a blank workspace when starting Eclipse instance.
2.  Configure the proper Java Virtual Machine (JVM) for compiling Jaspersoft Studio source code:

<!-- -->

1.  Select **Eclipse \> Preferences \> Java \> Installed JREs**. Make sure that Java 21 is in the list of items. This is because the Jaspersoft Studio source code is compatible with version 21, also the final product runs on version 21. Therefore, it is better to set it up properly (<https://adoptium.net/download/>). You could also utilize the JRE artifact that is included in the `jrePackages` folder.

![configuration installedJREs](../assets/images/configuration_installedJREs.png)

1.  Select **Eclipse \> Preferences \> Java \> Installed JREs \> Execution Environment**. Select the best compatible JVM for each execution environment (that is, Java 21).

![configuration executionEnvironments](../assets/images/configuration_executionEnvironments.png)

1.  Select **Eclipse \> Preferences \> Java \> Compiler**. Change the **Compiler compliance level** to 21. The code base is compatible with Java 21.

![configuration compilerSettings](../assets/images/configuration_compilerSettings.png)

1.  Configure the proper target platform for compiling Jaspersoft Studio source code:

<!-- -->

1.  Select **Eclipse \> Preferences \> Plug-in Development \> Target Platform**.
2.  Add a new platform starting from the **Nothing** option, then add the `targetRepoE436-10.1.0` directory containing the plug-ins and features that are the foundation for the Jaspersoft Studio platform.

![configuration targetPlatform](../assets/images/configuration_targetPlatform.png)

1.  Select the newly created platform to compile the sources.

![configuration targetPlatformSelected](../assets/images/configuration_targetPlatformSelected.png)

1.  Import the existing projects from the *sources* folder:

<!-- -->

1.  Select **File \> Import**.
2.  Select **Import (wizard) \> General \> Existing Projects into Workspace**.

![import sourceprojects](../assets/images/import_sourceprojects.png)

1.  Configure the wizard to point to the location of the downloaded `sources` directory, then click **Finish**. It is recommended to copy the projects directly into the dedicated workspace to avoid modifying the original ones.

!!! note

    Once the import operation ends, you see the automatic build triggered.

## Setting Up Run/Debug Configuration of Jaspersoft Studio

To run/debug a version of the Jaspersoft Studio runtime from the development environment, you can create a run/debug configuration:

1.  Select **Run \> Debug Configurations \> Eclipse Application \> New** from the menu.
2.  Enter the name and select `com.jaspersoft.studio.pro.rcp.product` for **Run a product** option.
3.  Set the **Execution environment** to the Java 21 version.

![debugconfiguration tab1](../assets/images/debugconfiguration_tab1.png)

1.  You can add the additional arguments and configuration parameters in the **Arguments** tab. You can also replicate the actual final product configuration using the information in the `jaspersoftstudiopro.product` file. The following example is based on the 10.1.0 configuration:

```
-Xms128m
-Xmx2048m
--add-modules=ALL-SYSTEM
--add-exports=java.xml/com.sun.org.apache.xml.internal.serialize=ALL-UNNAMED
--add-opens=java.desktop/sun.java2d=ALL-UNNAMED
--add-opens=java.base/java.io=ALL-UNNAMED
--add-opens=java.base/java.lang=ALL-UNNAMED
--add-opens=java.base/java.nio=ALL-UNNAMED
-Dfile.encoding=UTF-8
-Djava.net.preferIPv4Stack=true
-Djavax.xml.soap.MessageFactory=com.sun.xml.messaging.saaj.soap.ver1_1.SOAPMessageFactory1_1Impl
-Djavax.xml.soap.SOAPFactory=com.sun.xml.messaging.saaj.soap.ver1_1.SOAPFactory1_1Impl
-Djavax.xml.soap.SAAJMetaFactory=com.sun.xml.messaging.saaj.soap.SAAJMetaFactoryImpl
-Djavax.xml.soap.SOAPConnectionFactory=com.sun.xml.messaging.saaj.client.p2p.HttpSOAPConnectionFactory
-Dplaywright.cli.dir=/tmp/temp_building/playwright-1.50.0-macosx-x64/driver/mac
-Dlog4j.configurationFile=file:/tmp/temp_building/sources/jaspersoft-studio-pro-repo/aggregator.pro/ant-scripts/rootfiles/log4j2.xml
-XstartOnFirstThread
```

![debugconfiguration tab2](../assets/images/debugconfiguration_tab2.png)

The `playwright.cli.dir` is added to specify the location of the Playwright installation that will be used for the HTML PRO component.

The final Jaspersoft Studio product will not require this, since the library is bundled as part of the build process.

1.  (Optional) On the Plug-ins tab, disable the option **Validate Plug-ins automatically prior to launching** to avoid the warning message associated with plug-ins/fragments/features for multiple operating systems.
2.  Click **Debug** to launch the Jaspersoft Studio runtime.

## Creating Products from Jaspersoft Studio Sources

To test the way the final product looks after export, you can leverage Maven Tycho to build Jaspersoft Studio sources.

!!! note

    - All the source projects must be in one single folder, for example, it could be the Eclipse workspace or you may copy the projects into a new dedicated folder.
    - To build the Jaspersoft Studio Professional project use the `aggregator.pro` project as main location.

1.  Make sure you have correctly installed Maven.
2.  Set up Maven properly using any of these methods.

**Method 1**

1.  Configure your Maven `settings.xml` file. You can start from the following sample `settings.xml` file:

```
<settings>
    <profiles>
        <profile>
            <id>JSSProfile</id>
            <repositories>
                <repository>
                  <id>central</id>
                  <name>jaspersoft-repo</name>
                  <url>https://jaspersoft.jfrog.io/jaspersoft/jaspersoft-repo</url>
                </repository>
            </repositories>
            <properties>
                <!-- Local Repository with the target platform for building -->
                <targetplatform.repo>/tmp/temp_building/targetRepoE436-10.1</targetplatform.repo>
                <!-- JRE files location -->
                <jre.packages.location>/tmp/temp_building/jrePackages</jre.packages.location>
                <!-- Playwright artifacts location -->
                <playwright.packages.location>/tmp/temp_building/playwrightPackages</playwright.packages.location>
            </properties>
        </profile>
    </profiles>
    <activeProfiles>
        <activeProfile>JSSProfile</activeProfile>
    </activeProfiles>
</settings>
```

1.  In the `aggregator.pro` project folder, run the following command.

```
$ mvn clean package
```

**Method 2**: In the `aggregator.pro` folder, provide all the details in one single command:

```
  mvn clean package <br>
-Dmaven.repo.remote=https://jaspersoft.jfrog.io/jaspersoft/jaspersoft-repo <br>
-Dtargetplatform.repo=/tmp/temp_building/targetRepoE436-10.1 <br>
-Djre.packages.location=/tmp/temp_building/jrePackages <br>
-Dplaywright.packages.location=/tmp/temp_building/playwrightPackages
```

1.  When the build is completed, you can retrieve the product artifacts from the following location:

```
<FULLWORKSPACE_PATH>/com.jaspersoft.studio.pro.rcp.product/target/products/ com.jaspersoft.studio.pro.rcp.product/
```

`FULLWORKSPACE_PATH` is the location where all the sources are located including an Eclipse workspace folder.

1.  To properly package the previously created raw artifacts, perform the following steps:

<!-- -->

1.  Select the subfolder `ant-scripts` from `aggregator.pro` project as a current location.
2.  Run the following command using ANT:

```
ant -buildfile packageRawDistributions.xml -Djre.packages.location=/tmp/temp_building/jrePackages -Dplaywright.packages.location=/tmp/temp_building/playwrightPackages
```

1.  The zipped artifacts are found in the `product/dist` project subfolder.

### Additional information

For any further information, contact the Jaspersoft Studio team.
