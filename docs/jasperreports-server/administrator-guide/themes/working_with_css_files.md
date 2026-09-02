---
title: Working With CSS Files
description: This section is not a CSS tutorial but rather a collection of tips and tricks for working with the CSS that makes up the themes in JasperReports Server. This section focuses on how to test the themes...
---

# Working With CSS Files

This section is not a CSS tutorial but rather a collection of tips and tricks for working with the CSS that makes up the themes in JasperReports Server. This section focuses on how to test the themes you develop and match the CSS to its behavior in the JasperReports Server UI. There are many different editors for CSS and tools for testing it, so the recommendations in this section are just one way of developing a theme.

## Theme Development Workflow

The major choice to make when developing a theme is whether to use simple theme overrides or to duplicate and modify theme files, as described in section [CSS Priority Scheme and Custom Overrides](how_themes_work.md). Usually, the extent of your modifications determines which method to use.

Once you have made that determination, you are ready to create your theme. The main steps in a theme development workflow are as follows:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Step</p></th>
<th><p>Reference</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><ol>
<li>Download the default theme so you have a copy of the files and CSS rules that you want to modify.</li>
</ol></td>
<td><p><a href="creating_themes.md">Downloading and Uploading Theme ZIP Files</a></p></td>
</tr>
<tr>
<td><ol>
<li>Create your new CSS rules, CSS files, and image files.</li>
</ol></td>
<td><p><a href="#firefox-web-developer-tools">Firefox Web Developer Tools</a></p></td>
</tr>
<tr>
<td><ol>
<li>Upload your new files to a test platform, and activate the theme or place them in an active theme.</li>
</ol></td>
<td><p><a href="creating_themes.md">Creating Theme Folders and File Resources</a></p></td>
</tr>
<tr>
<td><ol>
<li>Verify your changes wherever they occur in the UI.</li>
</ol></td>
<td><p><a href="#test-platform">Test Platform</a></p></td>
</tr>
<tr>
<td><ol>
<li>Repeat <span>Step 2</span> through <span>Step 4</span> for all your changes until the theme is finalized.</li>
</ol></td>
<td></td>
</tr>
<tr>
<td><ol>
<li>Deploy your theme to your users.</li>
</ol></td>
<td><p><span> <a href="administering_themes.md">Setting the System Theme</a> or <a href="administering_themes.md">Setting an Organization Theme</a></span></p></td>
</tr>
</tbody>
</table>

## Firefox Web Developer Tools

To help you find, view, and modify CSS rules in Step 2 above, you can use the web developer tools in the Mozilla Firefox browser. In particular, the Page Inspector tool displays the HTML and CSS rules of web pages as you browse. It has a dynamic interface that lets you select an element on the web page, and it displays the specific CSS rules that apply to the element. It also allows you to modify those rules in the browser memory and immediately see the effect on the web page.

The web developer tools are ideal for modifying themes in JasperReports Server. Once you locate the pages and elements that you want to modify, you can prototype your changes directly within the tool. For example, you can see overall effect of changing a color or modifying the spacing.

If you are implementing your theme through custom overrides, you can copy the CSS rules from the tools directly into the overrides_custom.css file. Firefox displays the entire rule from its original file, so the copy overrides it exactly. If you are modifying other files from the default theme, the Page Inspector shows you the filename and line number of the rule, so that you can easily find it in your copy of the file.

And when you are testing a theme that uses overrides, the Page Inspector displays both the active CSS rule from `overrides_custom.css` and the original rule in the regular theme file of the inherited theme. The original rule is displayed in strike-through, so you can easily tell which rule is active and which rule it overrides, according to the CSS priority scheme.

For more information, see the Firefox Page Inspector tool [overview](https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector/UI_Tour) and [documentation](https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector).

## Test Platform

When you upload a theme and make it active, it is immediately visible to every user in the organization, or in the case of a system theme, to every user on the server. Even editing or uploading a file into an active theme is reflected immediately in the user interface. Because developing a theme requires many iterations of uploading, activating, and testing CSS rules, you shouldn't develop themes on a production server.

In the simplest case, you can develop and test your themes before putting your JasperReports Server into production. As you test your server during the deployment, you can develop your themes without impacting real users.

For multi-organization deployments that are in production, you can test on your production server as long as you create a test organization. The test organization inherits from the system theme, creating a very realistic test environment where you can see how your theme overrides the inherited theme. Make sure your test organization reflects your real organizations, for example having OLAP views if your real organizations perform OLAP analysis. This can help you test your theme with the elements of the user interface that your organization users see the most.

For single-organization deployments that don't have a license to create organizations, you can test your themes on a second installation of the server. For example, you could download the evaluation copy of JasperReports Server and install it on the same computer where you develop the theme. This lets you see how your theme appears either as a system theme or in the default organization. As in the case of the test organization, test your theme with all the server features, for example the Ad Hoc Editor, Dashboard Designer, input controls on reports, scheduling, and the like.

When your theme is well-tested and nearly complete, you should test it on the production server. Upload your theme to the Themes folder where you intend to deploy it, but do not activate it. Log in as a test user and add the following parameter to any URL, for example the home page URL:

``` text
&theme=<theme-name>
```

This activates your theme for the test user on all pages that you access until the user session times out. This allows you to navigate the entire application and see the effect of your theme in the production environment, without affecting other users.

!!! note

    To set the theme back to the default append the &theme parameter to the URL with the string default (`&theme=default`). This is especially useful if a problem with the current theme has inadvertently disabled any functionality.

On each of these test platforms, look at the user interface generated by your theme with the same browsers and browser versions that your users have. If you see errors, you can still use the Firefox web developer tools to look at the CSS rules that are involved, even if the errors do not show up in Firefox. When testing your theme, look at its effect across all pages and dialogs of JasperReports Server. Your test organization and test users should access all the features of the server to view the user interface under all conditions.
