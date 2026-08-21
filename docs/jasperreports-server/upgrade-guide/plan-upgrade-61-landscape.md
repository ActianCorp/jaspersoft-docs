---
title: Changes in 6.1 That May Affect Your Upgrade
description: "The look and feel of the JasperReports Server web interface has been redesigned to modernize the application's appearance. To accomplish this, markup and styles have been modified. As a result of..."
---

# Changes in 6.1 That May Affect Your Upgrade

## Changes to Themes

The look and feel of the JasperReports Server web interface has been redesigned to modernize the application's appearance. To accomplish this, markup and styles have been modified. As a result of these modifications, custom themes developed for the previous interface need to be updated for the new interface.

The following table lists the changes made to the user interface and describes some of the steps necessary to update custom themes in overrides_custom.css. The main changes are in the banner, body, footer, and login page. The changes to the login page are extensive. Instead of attempting to update an existing login page, you should reimplement the login page in the new default theme.

For information on developing new themes, see the JasperReports Server Administrator Guide and the JasperReports Server Ultimate Guide.

<table>
<caption><p>Updating Themes in JasperReports Server 6.1</p></caption>
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
<td><p>Banner</p></td>
<td><p><code>.banner</code><br />
<br />
Give custom value to <code>height</code></p></td>
<td><p>containers.css</p></td>
<td><p>Default value:<br />
height: 32 px</p></td>
</tr>
<tr>
<td><p>Body</p></td>
<td><p><code>#frame</code><br />
<br />
Set custom <code>top</code> and <code>bottom</code> values that position the body of the application between the banner and footer without overlap</p></td>
<td><p>containers.css</p></td>
<td><p>Default value:<br />
top: <span>32 px</span><br />
bottom: <span>17 px</span></p>
<p>This value needs to be equal to or greater than the height of <code>.banner</code></p>
<p>The bottom position needs to be adjusted only if the height of the footer is changed</p></td>
</tr>
<tr>
<td><p>Banner<br />
Logo</p></td>
<td><p><code>#logo</code><br />
<br />
Give custom values to height and width that match the dimensions of your logo</p>
<p>Adjust margins around the logo if needed</p></td>
<td><p>theme.css</p></td>
<td><p>Default values:</p>
<p>height: <span>22 px</span><br />
width: <span>176 px</span></p>
<p>margin-top: <span>6 px</span><br />
margin-right: <span>4 px</span><br />
margin-bottom: 0<br />
margin-left: <span>8 px</span></p></td>
</tr>
<tr>
<td><p>Banner<br />
Main Navigation</p></td>
<td><p><code>.menu.primaryNav.wrap</code><br />
<br />
Set height and line-height to 1 px shorter than <code>.banner</code></p></td>
<td><p>containers.css</p></td>
<td><p>height: <span>31 px</span><br />
line-height: <span>31 px</span></p></td>
</tr>
<tr>
<td><p>Banner<br />
Main Navigation Home icon</p></td>
<td><code>.menu.primaryNav #main_home.wrap &gt; .icon</code>
<p>Set the height to be the same as .banner</p>
<p>Set values for width and background-position to fit your image.</p></td>
<td><p>containers.css</p></td>
<td><p>height: <span>32 px</span></p>
<p>width: <span>14 px</span><br />
background-position: 0 <span>-164 px</span><br />
background-position: 0 <span>-163 px </span>(<span>IE8-9</span>)</p></td>
</tr>
<tr>
<td><p>Banner<br />
Main Navigation<br />
Item arrow icon</p></td>
<td><code>.menu.primaryNav .node &gt; .wrap &gt; .icon</code>
<p>Set height to your desired value, with the maximum value being the same height measurement as the .banner element.</p>
<p>Set background-position and width to a value that properly displays the default or your custom image.</p></td>
<td><p>containers.css</p></td>
<td><p>height: 32 px</p>
<p>background-position: left <span>-79 px</span><br />
width: <span>11 px</span></p></td>
</tr>
<tr>
<td><p>Banner<br />
Main Navigation<br />
Item arrow icon</p></td>
<td><p><code>.menu.primaryNav .wrap.over </code><br />
<code>.menu.primaryNav .wrap.pressed</code></p>
<p>Set background-position to a value that properly displays the default or your custom image.</p></td>
<td><p>containers.css</p></td>
<td><p>background-position is not explicitly defined. The value is cascaded from <code>.menu.primaryNav .node &gt; .wrap &gt; .icon</code></p>
<p>This only needs to be adjusted if you want a different color disclosure indicator for the pressed and over states of the main menu links.</p></td>
</tr>
<tr>
<td><p>Banner<br />
Search container</p></td>
<td><code>#globalSearch.searchLockup</code>
<p>Set the margin-top to a desired value that will vertically center it within the banner.</p></td>
<td><p>controls.css</p></td>
<td><p>margin-top: <span>5 px</span></p></td>
</tr>
<tr>
<td><p>Banner<br />
Metadata</p></td>
<td><code>#metalinks li</code>
<p>Set the line-height to the desired value that will vertically center it within the banner.</p></td>
<td><p>themes.css</p></td>
<td><p>line-height: <span>20 px</span></p></td>
</tr>
<tr>
<td><p>Footer</p></td>
<td><p><code>#frameFooter</code></p>
<p>Set the height if you want it to be anything other than the default value.</p></td>
<td><p>containers.css</p></td>
<td><p>height: <span>17 px</span></p></td>
</tr>
<tr>
<td>Login page</td>
<td colspan="3"><p>Reimplement in a new theme.</p></td>
</tr>
</tbody>
</table>
