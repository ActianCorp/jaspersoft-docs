---
title: Using the Bundle Editor
description: "The bundle editor has the following:"
---

# Using the Bundle Editor

The bundle editor has the following:

The Properties tab is shown by default. This tab displays the key editor on the left and the value editor on the right,

The key list shows the keys in alphabetical order. If you have created keys in a period-delimited format, the keys are nested.

Working area on the right. The contents of this area depend on the selection:

To create a base name and empty bundle files

1.  Go to **File \> New \> Other...** to open the New dialog.

2.  Select **Messages Editor \> ResourceBundle** and click **Next**.

    The ResourceBundle wizard is displayed.

3.  Set the following:

    - **Folder**: The folder where you want the resource bundle files. This can be in the current project or in another project in Jaspersoft Studio. Note that you can share bundles between projects.
    - **Base Name**: The base name for bundle files. Country and location codes are appended to this name. For this example, use SampleBundle.

4.  Choose the locales that you want. You can set a language (for example, French) or a language and location (for example, French (Luxembourg)). Note that the **\[Default\]** locale is automatically created. This example uses American English for the default locale.

    - To add a locale, select it from the **Choose or type a Locale** dropdown or enter the locale code in the **Lang.** box, then click **Add**. You may optionally enter a **Country** or **Variant**.
    - To remove a locale, select it in the list of **Selected locales** to the right and click **Remove**.

    If you are using the locale dropdown, you can type the first letter of a locale to jump to that letter in the list. When you select a locale, the code for the locale are entered in the boxes below the dropdown.

    For this example, select the French locale or type `fr` directly in the **Lang.** box.

5.  Click **Finish**.

The Resource Bundle editor is displayed. In addition, a separate properties file is created for each locale you specified, along with a default file.

This example uses American English for the default. To create a file for UK English, select English (United Kingdom) from the **Choose or type a Locale** dropdown, then click **Add**.

The bundle editor for your files opens to the **Properties** tab.

To add keys and values

The bundle editor lets you create keys on the left and then create values for each locale on the right.

You can use any naming convention for keys that you choose. However, if you use periods (.) to separate categories or levels, additional tools in the bundle editor help you organize and view them. The list of keys on the left lets you do the following:

- The entry bar at the top lets you search for keys. It shows all keys that begin with the same letters that you enter. You cannot search for the middle or end of a key.
- Shows period-separated items in a tree.
- Shows period-separated items in a list.
- In tree view, expands the tree.
- In tree view, collapses the tree.
- The entry bar at the bottom lets you enter a new key name. Type the key that you want and then click **Add**.

For this example, enter the following keys:

1.  Type `titleband.title` in the **Add** entry bar at the lower left of the bundle editor and click **Add**.
2.  Enter `field.lastname` and click **Add**.
3.  Enter `field.firstname` and click **Add**.

Each key you create is added to the list of keys.

Editing a key/value pair

You can view or edit all the values corresponding to a single key.

1.  Click a key in the key panel on the left.

    The value (if any) for each language bundle is shown.

2.  To add or edit values, click in an entry box and edit your text. To edit a different value, click in the entry box for the locale you want.

3.  To save your changes, use **Ctrl-S** or select **File \> Save**.

Editing properties files

You can directly edit a property file as a text file.

1.  Open the Default property file for editing:

    - Click the file name in the right-hand panel
    - OR: Click the Default tab at the bottom of the bundle editor.

    The file opens and displays the keys with blank values.

2.  Type the values that you want for the default:

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><div class="language-properties highlight"><pre><code><span class="na">field.firstname</span><span class="o">=</span><span class="s">First Name</span>
<span class="w">    </span><span class="na">field.lastname</span><span class="o">=</span><span class="s">Last Name</span>
<span class="w">    </span>
<span class="na">titleband.title</span><span class="o">=</span><span class="s">Title</span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

3.  Click the French tab and edit it as follows:

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><div class="language-properties highlight"><pre><code><span class="na">field.firstname</span><span class="o">=</span><span class="s">Prénom</span>
<span class="w">    </span><span class="na">field.lastname</span><span class="o">=</span><span class="s">Nom de famille</span>
<span class="w">    </span>
<span class="na">titleband.title</span><span class="o">=</span><span class="s">Titre</span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

4.  Click the tab English (United Kingdom).

5.  Edit the 4th line to read `field.lastname = Surname`

    !!! note

        If you do not add a value for a given key, the report uses the value in the default file.

6.  To return to the main view, click the **Properties** tab at the bottom of the bundle editor.
