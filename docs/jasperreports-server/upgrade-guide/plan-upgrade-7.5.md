---
title: Changes in 7.5 That May Affect Your Upgrade
description: "In the 7.5 release, the Simba JDBC drivers for Spark and Impala have been updated. By default, the new release supports the new JDBC drivers, and the old drivers cannot be used. You should update..."
---

# Changes in 7.5 That May Affect Your Upgrade

## Driver Updates

In the 7.5 release, the Simba JDBC drivers for Spark and Impala have been updated. By default, the new release supports the new JDBC drivers, and the old drivers cannot be used. You should update your data sources to use the new driver. For more information, see the JasperReports Server Administrator Guide.

!!! warning

    The drivers have been replaced due to vulnerabilities from third-party libraries. Update your data sources to use the new drivers.

### Using the Old Impala Driver

If you want to continue using the Impala driver that was previously available from the community website, modify the install as described below.

Add the following files to the \<js-install\>/WEB-INF/lib directory:

- Curator-client-2.6.0.jar
- Curator-framework-2.6.0.jar
- Curator-recipes-2.6.0.jar
- Hive-metastore-1.2.2.jar
- Hive-service-1.2.2.jar
- Impala-jdbc4-1.0.44.1055.jar
- Libfb303-0.9.3.jar

If you do not add the files listed, data sources that use the old Impala driver causes errors when running reports that rely on them.

### Using the Old Spark Driver

If you want to continue using the Spark driver that was previously available from the community website, modify the install as described below.

Add the following files to the \<js-install\>/WEB-INF/lib directory:

- Curator-client-2.6.0.jar
- Curator-framework-2.6.0.jar
- Curator-recipes-2.6.0.jar
- Hive-metastore-1.2.2.jar
- Hive-service-1.2.2.jar
- Spark-jdbc4-1.1.1.1001.jar
- Libfb303-0.9.3.jar

If you do not add the files listed, data sources that use the old Spark driver causes errors when running reports that rely on them.

## Changes to the Jaspersoft MongoDB Query Language

The Jaspersoft MongoDB Query Language has been updated to reflect changes in the MongoDB driver:

- All aggregate commands must be updated to the new API-driven query syntax.

- All other command-driven queries (queries that use `runCommand`) are deprecated. If you want to use your queries in a future release, you should update them to the new syntax.

See the [language reference](http://community.jaspersoft.com/wiki/jaspersoft-mongodb-query-language) for more information.

## Encryption Keys

JasperReports Server 7.5 streamlines how it manages the encryption keys it uses to protect sensitive data inside and outside of the server. There is no more any need to configure the encryption keys because all keys are generated automatically during the installation and stored in a central keystore. The keys are used transparently whenever the server stores passwords internally or exports sensitive data. And as long as the same user performs the upgrade, the upgrade scripts have access to the same keys in the keystore.

The new keys are backward compatible with the default keys from previous servers. However, there are possible cases when you need to manage keys during an upgrade. For example, if you do not have access to the user who installed the 7.5 instance, you may not be able to access the keystore anymore.

If you are in this situation, you should plan your upgrade as follows:

1.  Before starting, back up your original 7.5 server.

2.  Then export everything from your running 7.5 server with the following command:

    ``` bash
    cd <js-install-7.5>/buildomatic
    js-export.sh --everything --output-zip js-7.5-export.zip --genkey
    ```

    This encrypts the export with the key that is displayed on the console output:

    ``` text
    Secret Key: 0xb1 0x44 0x72 0x0a 0xe9 0x5b 0x39 0xf5 0x87 0x5c 0xa9 0x1b 0x99 0x9d 0x14 0x4c
    Key Alias (UUID): 9e41cd54-31da-43aa-84c2-638a7d0b47b8
    ```

3.  Proceed with the upgrade and installation of the new server, but without migrating your data.

4.  Import the key into your upgraded server with the following command.

    ``` bash
    ./js-import.sh --input-key "0xb1 0x44 0x72 0x0a 0xe9 0x5b 0x39
                     0xf5 0x87 0x5c 0xa9 0x1b 0x99 0x9d 0x14 0x4c"
                   --keyalias 9e41cd54-31da-43aa-84c2-638a7d0b47b8
                   --keyalg AES --keypass NewKeyPassword
    ```

5.  Proceed with the migration of your data to the upgraded server, or manually import your catalog to the upgraded server. As the data is imported, it is decrypted with the given key, and re-encrypted with the server's new keys.

6.  Once the server is ready for production, back up your data and the new keystore once again.

    For more information and procedures for importing keys, see the JasperReports Server Security Guide.

## Theme Changes

The look and feel of the JasperReports Server web interface has been redesigned to modernize the application's appearance. To accomplish this, markup and styles have been modified. As a result of these modifications, custom themes developed for the previous interface need to be updated for the new interface. The main changes are in the banner, body, and home page.

The following table lists the changes made to the user interface, except for the changes to the home page. The changes to the home page are extensive. Instead of attempting to update an existing home page, you should reimplement the home page in the new default theme.

If you have not customized the user interface, these changes do not affect you.

### Banner

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th>Element</th>
<th>Classname and Modifications</th>
<th>File</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Banner</td>
<td><p><code>.banner</code></p>
<p>Changed <code>background-color</code>, <code>font-family</code> and <code>height</code>.</p></td>
<td>containers.css</td>
<td><p>Default value:</p>
<p><code>background-color: #062e79</code><br />
<code>font-family: source_sans_proregular</code><br />
<code>height: 40px</code></p></td>
</tr>
<tr>
<td>Body</td>
<td><p><code>#frame</code></p>
<p>Changed the <code>top</code> value to fit the body of the application between the banner and footer without overlap.</p></td>
<td>containers.css</td>
<td><p>Default value:</p>
<p><code>top: 40px</code><br />
</p></td>
</tr>
<tr>
<td>Banner Logo</td>
<td><p><code>#logo</code></p>
<p>Changed <code>width</code> and <code>height</code>.</p>
<p>Responsive behavior was added to the banner. There is now a breakpoint at which the logo shrinks in size (1100 px) and a breakpoint at which it becomes hidden (980 px).</p></td>
<td>theme.css</td>
<td><p>Default values:</p>
<p><code>height: 23px</code><br />
<code>width: 200px</code></p>
<p>Breakpoint from 981-1100 px:</p>
<p><code>width: 150px</code></p>
<p>980 px and below:</p>
<p><code>display: none</code></p></td>
</tr>
<tr>
<td>Banner Main Navigation home icon</td>
<td><p><code>.menu.primaryNav #main_home .wrap &gt; .icon</code></p>
<p>New sprites for <code>background-image</code>: one for standard-resolution displays and one for high-resolution displays.</p></td>
<td>containers.css</td>
<td><p>Default value:</p>
<p><code>background-image: url(images/banner_icons_sprite@1x.png)</code></p>
<p>High-resolution value:</p>
<p><code>background-image: url(images/banner_icons_sprite@2x.png)</code></p></td>
</tr>
<tr>
<td>Banner Main Navigation Item text</td>
<td><p><code>.menu.primaryNav .wrap</code></p>
<p>Enlarged <code>font-size</code>. Changed <code>height</code> and <code>line-height</code> to be 1 px shorter than <code>.banner</code>.</p></td>
<td>containers.css</td>
<td><p>Default values:</p>
<p><code>font-size: 14px</code><br />
<code>height: 39px</code><br />
<code>line-height: 39px</code></p></td>
</tr>
<tr>
<td>Banner Main Navigation Item arrow icon</td>
<td><p><code>.menu.primaryNav .node &gt; .wrap &gt; .icon</code></p>
<p>New sprites for <code>background-image</code>: one for standard-resolution displays and one for high-resolution displays. Changed <code>height</code> of icon container.</p></td>
<td>containers.css</td>
<td><p>Default values:</p>
<p><code>background-image: url(images/disclosure_icons_sprite@1x.png)</code><br />
height: <code>16 px</code></p>
<p>High-resolution value:</p>
<p><code>background-image: url(images/disclosure_icons_sprite@2x.png)</code></p></td>
</tr>
<tr>
<td>Banner Metadata container</td>
<td><p>#metalinks</p>
<p>Changed <code>height</code> to be 1 px shorter than <code>.banner</code>. Increased <code>margin-right</code> to accommodate search box.</p>
<p>With the addition of responsive behavior, the <code>margin-right</code> value changes at certain breakpoints to accommodate a smaller search box.</p></td>
<td>theme.css</td>
<td><p>Default values:</p>
<p>height: <code>39px</code><br />
margin-right: 270 px</p>
<p>Breakpoint from 821-1100 px:</p>
<p><code>margin-right: 200px</code></p>
<p>Breakpoint from 751-820 px:</p>
<p><code>margin-right: 140px</code></p></td>
</tr>
<tr>
<td>Banner Metadata text</td>
<td><p><code>#metalinks li</code></p>
<p>Enlarged <code>font-size</code>. Increased <code>line-height</code> to vertically center text in the banner.</p></td>
<td>theme.css</td>
<td><p>Default values:</p>
<p>font-size: <code>14 px</code><br />
line-height: <code>39 px </code></p></td>
</tr>
<tr>
<td>Banner Search container</td>
<td><p><code>#globalSearch.control.searchLockup</code></p>
<p>Increased <code>width</code> of container.</p>
<p>Responsive behavior was added to the banner. There are now breakpoints at which the search container shrinks in width and a breakpoint at which it becomes hidden.</p></td>
<td>controls.css</td>
<td><p>Default value:</p>
<p><code>width: 250px</code></p>
<p>Breakpoint from 821-1100 px:</p>
<p><code>width: 180px</code></p>
<p>Breakpoint from 751-820 px:</p>
<p><code>width: 100px</code></p>
<p>750 px and below:</p>
<p><code>display: none</code></p></td>
</tr>
<tr>
<td>Banner Search input wrapper</td>
<td><p><code>#globalSearch.control.searchLockup &gt; .wrap</code></p>
<p>Increased <code>height</code> of input wrapper.</p></td>
<td>controls.css</td>
<td><p>Default values:</p>
<p>height: 28 px</p></td>
</tr>
<tr>
<td>Banner Search input</td>
<td><p><code>#globalSearch.control.searchLockup &gt; .wrap &gt; input[type=text]</code></p>
<p>Responsive behavior was added to the banner. There are now breakpoints at which the search input shrinks in width and a breakpoint at which it becomes hidden.</p></td>
<td>controls.css</td>
<td><p>Default value:</p>
<p><code>width: 200px</code></p>
<p>Breakpoint from 821-1100 px:</p>
<p><code>width: 130px</code></p>
<p>Breakpoint from 751-820 px:</p>
<p><code>width: 80px</code></p>
<p>750 px and below:</p>
<p><code>display: none</code></p></td>
</tr>
<tr>
<td>Banner Search button icon</td>
<td><p><code>#globalSearch .button.search</code></p>
<p>New sprites for <code>background-image</code>: one for standard-resolution displays and one for high-resolution displays.</p></td>
<td>controls.css</td>
<td><p>Default value:</p>
<p><code>background-image: url(images/search_icons_sprite@1x.png)</code></p>
<p>High-resolution value:</p>
<p><code>background-image: url(images/search_icons_sprite@2x.png)</code></p></td>
</tr>
</tbody>
</table>

### Ad Hoc Designer

Extensive changes have been made to the look and feel of the Ad Hoc Designer. Although there are too many changes to document fully, the following table lists the basic elements that have changed.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th>Element</th>
<th>Classname and Modifications</th>
<th>File</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Page Title</td>
<td><p><code>#display &gt; .column.decorated &gt; .content &gt; .header</code></p>
<p>This element has been removed and replaced with the new <code>.pageHeader</code> element.</p></td>
<td>pages.css</td>
<td><br />
</td>
</tr>
<tr>
<td>Data and Filters Panel Headers</td>
<td><p><code>#designer .column.decorated &gt; .content &gt; .header</code></p>
<p>Removed bottom border, changed background-color, and increased <code>height</code>.</p></td>
<td>pageSpecific.css</td>
<td><p>Default values:</p>
<p><code>background-color: #d6d5d5</code><br />
<code>border-bottom: 0</code><br />
<code>height: 32px</code></p></td>
</tr>
<tr>
<td>Data and Filters Panel Headers Title Text</td>
<td><p><code>#designer .column.decorated &gt; .content &gt; .header &gt; .title</code></p>
<p>Changed <code>color</code> and <code>font-family</code>. Increased <code>font-size</code> and <code>line-height</code>.</p></td>
<td>pageSpecific.css</td>
<td><p>Default values:</p>
<p><code>color: #333333</code></p>
<code>font-family: source_sans_proregular</code><br />
<code>font-size: 15px</code><br />
<code>line-height: 32px</code></td>
</tr>
<tr>
<td>Panel Minimize Button</td>
<td><p><code>#designer .button.minimize</code></p>
<p>New sprites for <code>background-image</code>: one for standard-resolution displays and one for high-resolution displays. Changed <code>height</code> and <code>width</code>. Added a <code>background-color</code>.<br />
</p></td>
<td>pageSpecific.css</td>
<td><p>Default values:</p>
<p><code>background-color: #999999</code><br />
<code>background-image: url(images/disclosure_indicators_icons_sprite@1x.png)</code><br />
<code>height: 32px</code><br />
<code>width: 14px</code></p>
<p>High-resolution value:</p>
<p><code>background-image: url(images/disclosure_indicators_icons_sprite@2x.png)</code></p></td>
</tr>
<tr>
<td><p>Panel Options Button</p>
<p>Panel Section Options Button</p></td>
<td><p><code>.header &gt; .button.mutton,</code><br />
<code>#filter-container .title .button.mutton</code><br />
</p>
<p>New sprites for <code>background-image</code>: one for standard-resolution displays and one for high-resolution displays. Changed <code>height</code> and <code>width</code>.</p></td>
<td>pageSpecific.css</td>
<td><p>Default values:</p>
<p><code>background-image: url(images/disclosure_indicators_icons_sprite@1x.png)</code><br />
<code>height: 32px</code><br />
<code>width: 22px</code></p>
<p>.</p>
<p>High-resolution value:</p>
<p>background-image: url(images/disclosure_indicators_icons_sprite@2x.png)</p></td>
</tr>
<tr>
<td>Panel Section Headers</td>
<td><p><code>#designer #availableFields .dimension .header</code>,<br />
<code>#designer #availableFields .measure .header,</code><br />
<code>#level-container .pod-header,</code><br />
<code>#filter-container .header,</code><br />
<code>#expression-container .header</code><br />
</p>
<p>Changed <code>background-color</code> and <code>font-family</code>, increased <code>height</code>, and removed the bottom border.</p></td>
<td>pageSpecific.css</td>
<td><p>Default values:</p>
<p><code>background-color: #ebebeb</code><br />
<code>border-bottom: none</code><br />
<code>font-family: source_sans_proregular</code><br />
<code>height: 32px</code></p></td>
</tr>
<tr>
<td>Toolbar</td>
<td><p><code>#designer .toolbar</code></p>
<p>Increased <code>height</code>.</p></td>
<td>pageSpecific.css</td>
<td><p>Default values:</p>
<p><code>height: 32px</code></p></td>
</tr>
<tr>
<td>Toolbar Buttons</td>
<td><p><code>button.capsule</code></p>
<p>Increased <code>width</code>.</p></td>
<td>buttons.css</td>
<td><p>Default value:</p>
<p><code>width: 32px</code></p></td>
</tr>
<tr>
<td>Toolbar Buttons with down arrow</td>
<td><p><code>button.capsule.mutton</code></p>
<p>Increased <code>width</code>.</p></td>
<td>buttons.css</td>
<td><p>Default value:</p>
<p><code>width: 36px</code></p></td>
</tr>
<tr>
<td>Toolbar Button Icons</td>
<td><p><code>.button.capsule .indicator</code></p>
<p>New sprites for <code>background-image</code>: one for standard-resolution displays and one for high-resolution displays.</p></td>
<td>pageSpecific.css</td>
<td><p>Default values:</p>
<p><code>background-image: url(images/disclosure_indicators_icons_sprite@1x.png)</code><br />
</p>
<p>.</p>
<p>High-resolution value:</p>
<p><code>background-image: url(images/disclosure_indicators_icons_sprite@2x.png)</code></p></td>
</tr>
</tbody>
</table>

### Report Viewer

Changes have been made to the general look and feel of the Report Viewer. The following table lists the basic elements that have changed.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th>Element</th>
<th>Classname and Modifications</th>
<th>File</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Page Title</td>
<td><p><code>#reportViewer #reportViewFrame &gt; .content &gt; .header</code><br />
</p>
<p>This element has been removed and replaced with the new <code>.pageHeader</code> element.</p></td>
<td>pages.css</td>
<td><br />
</td>
</tr>
<tr>
<td>Toolbar</td>
<td><p><code>#reportViewer .toolbar</code></p>
<p>Increased <code>height</code>.</p></td>
<td>pageSpecific.css</td>
<td><p>Default value:</p>
<p><code>height: 32px</code></p></td>
</tr>
<tr>
<td>Toolbar Buttons Container</td>
<td><p><code>#reportViewer .toolbar &gt; .buttonSet</code></p>
<p>Increased <code>height</code>.</p></td>
<td>pageSpecific.css</td>
<td><p>Default value:</p>
<p><code>height: 31px</code></p></td>
</tr>
<tr>
<td>Toolbar Button Icons</td>
<td><p><code>#designer .toolbar .button .icon</code></p>
<p>New sprites for <code>background-image</code>: one for standard-resolution displays and one for high-resolution displays.</p></td>
<td>pageSpecific.css</td>
<td><p>Default values:</p>
<p><code>background-image: url(images/button_action_icons_sprite@1x.png)</code><br />
</p>
<p>.</p>
<p>High-resolution value:</p>
<p><code>background-image: url(images/button_action_icons_sprite@2x.png)</code></p></td>
</tr>
<tr>
<td>Options Panel Header</td>
<td><p><code>#reportViewer #inputControlsForm &gt; .content &gt; .header</code></p>
<p>Removed bottom border, changed background-color, and increased <code>height</code>.</p></td>
<td>pageSpecific.css</td>
<td><p>Default values:</p>
<p><code>background-color: #d6d5d5</code><br />
<code>border-bottom: 0</code><br />
<code>height: 32px</code></p></td>
</tr>
<tr>
<td>Options Panel Header Title Text</td>
<td><p><code>#reportViewer #inputControlsForm &gt; .content &gt; .header &gt; .title</code><br />
</p>
<p>Changed <code>color</code> and <code>font-family</code>. Increased <code>font-size</code> and <code>line-height</code>.</p></td>
<td>pageSpecific.css</td>
<td><p>Default values:</p>
<p><code>color: #333333</code></p>
<code>font-family: source_sans_proregular</code><br />
<code>font-size: 15px</code><br />
<code>line-height: 32px</code></td>
</tr>
<tr>
<td>Options Panel Minimize Button</td>
<td><p><code>#reportViewer #inputControlsForm .button.minimize</code><br />
</p>
<p>New sprites for <code>background-image</code>: one for standard-resolution displays and one for high-resolution displays. Changed <code>height</code> and <code>width</code>. Added a <code>background-color</code>.<br />
</p></td>
<td>pageSpecific.css</td>
<td><p>Default values:</p>
<p><code>background-color: #999999</code><br />
<code>background-image: url(images/disclosure_indicators_icons_sprite@1x.png)</code><br />
<code>height: 32px</code><br />
<code>width: 14px</code></p>
<p>.</p>
<p>High-resolution value:</p>
<p><code>background-image: url(images/disclosure_indicators_icons_sprite@2x.png)</code></p></td>
</tr>
</tbody>
</table>

### Dashboard Designer

Extensive changes have been made to the look and feel of the Dashboard Designer. Although there are too many changes to document fully, the following table lists the basic elements that have changed.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th>Element</th>
<th>Classname and Modifications</th>
<th>File</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Page Title</td>
<td><p><code>.column.decorated &gt; .content &gt; .header</code></p>
<p>This element has been removed and replaced with the new <code>.pageHeader</code> element.</p></td>
<td>pages.css</td>
<td><br />
</td>
</tr>
<tr>
<td>Available Content Panel Header</td>
<td><p><code>.dashboardDesigner .column.decorated &gt; .content &gt; .header</code></p>
<p>Removed bottom border, changed background-color, and increased <code>height</code>.<br />
</p></td>
<td>designer.css</td>
<td><p>Default values:</p>
<p><code>background-color: #d6d5d5</code><br />
<code>border-bottom: 0</code><br />
<code>height: 32px</code></p></td>
</tr>
<tr>
<td>Available Content Panel Header Title</td>
<td><p><code>#display.dashboardDesigner .column.decorated &gt; .content &gt; .header &gt; .title</code></p>
<p>Changed <code>color</code> and <code>font-family</code>. Increased <code>font-size</code> and <code>line-height</code>.</p></td>
<td>designer.css</td>
<td><p>Default values:</p>
<p><code>color: #333333</code><br />
<code>font-family: source_sans_proregular</code><br />
<code>font-size: 15px</code><br />
<code>line-height: 32px</code></p></td>
</tr>
<tr>
<td>Available Content Panel Minimize Button</td>
<td><p><code>.dashboardDesigner .button.minimize</code><br />
</p>
<p>New sprites for <code>background-image</code>: one for standard-resolution displays and one for high-resolution displays. Changed <code>height</code> and <code>width</code>. Added a <code>background-color</code>.<br />
</p></td>
<td>designer.css</td>
<td><p>Default values:</p>
<p><code>background-color: #999999</code><br />
<code>background-image: url(images/disclosure_indicators_icons_sprite@1x.png)</code><br />
<code>height: 32px</code><br />
<code>width: 14px</code></p>
<p>High-resolution value:</p>
<p><code>background-image: url(images/disclosure_indicators_icons_sprite@2x.png)</code></p></td>
</tr>
<tr>
<td>Available Content Panel Section Headers</td>
<td><p><code>.dashboardDesigner .dashboardSidebar .panel.collapsiblePanel &gt; .header</code><br />
</p>
<p>Removed bottom border and increased <code>height</code>. Changed <code>background-color</code> and <code>font-family</code>.</p></td>
<td>designer.css</td>
<td><p>Default values:</p>
<p><code>background-color: #ebebeb</code><br />
<code>border-bottom: none</code><br />
<code>font-family: source_sans_proregular</code><br />
<code>height: 32px</code></p></td>
</tr>
<tr>
<td>Available Content Panel Section Headers Title</td>
<td><p><code>.dashboardDesigner .dashboardSidebar .panel.collapsiblePanel &gt; .header &gt; .title</code></p>
<p>Changed <code>color</code>. Increased <code>font-size</code>, height, and <code>line-height</code>.</p></td>
<td>designer.css</td>
<td><p>Default values:</p>
<p><code>color: #333333</code><br />
<code>font-size: 13px</code><br />
<code>height: 32px</code><br />
<code>line-height: 33px</code></p></td>
</tr>
<tr>
<td>Available Content Panel Section Headers Toggle Button</td>
<td><p><code>.dashboardDesigner .collapsiblePanel &gt; .header &gt; .buttonIconToggle</code></p>
<p>New sprites for <code>background-image</code>: one for standard-resolution displays and one for high-resolution displays. Increased <code>height</code> and <code>width</code>.</p></td>
<td>designer.css</td>
<td><p>Default values:</p>
<p><code>background-image: url(images/disclosure_indicators_icons_sprite@1x.png)</code><br />
<code>height: 32px</code><br />
<code>width: 22px</code></p>
<p>.</p>
<p>High-resolution value:</p>
<p>background-image<code>: url(images/disclosure_indicators_icons_sprite@2x.png)</code></p></td>
</tr>
<tr>
<td>Available Content Panel Section Options Button</td>
<td><p><code>.header &gt; .button.mutton</code></p>
<p>New sprites for <code>background-image</code>: one for standard-resolution displays and one for high-resolution displays. Increased <code>height</code> and <code>width</code>.</p></td>
<td>containers.css</td>
<td><p>Default values:</p>
<p><code>background-image: url(images/disclosure_indicators_icons_sprite@1x.png)</code><br />
<code>height: 32px</code><br />
<code>width: 22px</code></p>
<p>.</p>
<p>High-resolution value:</p>
<p><code>background-image: url(images/disclosure_indicators_icons_sprite@2x.png)</code></p></td>
</tr>
<tr>
<td>Dashboard Canvas</td>
<td><p><code>.dashboardCanvas &gt; .content &gt; .body</code></p>
<p>Changed <code>background-color</code>.</p></td>
<td>canvas</td>
<td><p>Default values:</p>
<p><code>background-color: #ffffff</code></p></td>
</tr>
</tbody>
</table>
