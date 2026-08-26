---
title: Creating Topics from Domains
description: "In some circumstances it is important to create a Topic based on the Domain and data settings you chose, but it's not always necessary. The main consideration is how reports based on the Domain-based..."
---

# Creating Topics from Domains

In some circumstances it is important to create a Topic based on the Domain and data settings you chose, but it's not always necessary. The main consideration is how reports based on the Domain-based view are used. The following table explains the choices.

| If you want to … | Then do this | Explanation |
|----|----|----|
| Create a single-use report from the Domain with your settings. | Click **Table**, **Chart**, or **Crosstab** after defining your settings in the Data Chooser, then format the view and create your report. | Your field selections appear in the Ad Hoc Editor and you can create views from them, but the settings themselves are not saved. |
| Run a report repeatedly as is or with prompting for new input, or make very similar reports in the Ad Hoc Editor. | Click **Table**, **Chart**, or **Crosstab** after defining your settings in the Data Chooser, then format and save the view in the Ad Hoc Editor. | After you save a view, users can create reports to be run from it repeatedly and be prompted for input each time if you defined unlocked filters. |
| Reuse your field, filter, and display settings on this Domain to create new views with different formatting. | After saving your settings as a Domain Topic in the Data Chooser, start a new view and choose your Domain Topic from the **Domains** tab. | Domain Topics are saved in JRXML format in the repository. They appear on the **Topics** tab when you start a view. |
| Be able to modify one or more of the settings you made in the Data Chooser wizard. | After saving your settings as a Domain Topic in the Data Chooser, find your Domain Topic in the repository and open it in the Domain Designer. | Domain Topics can be edited as described in Editing a Domain Topic. After you save your changes, you can create views based on the modified Domain Topic. |
| Create views from the same repository data source but with different Domain settings, such as derived fields and different joins to make new fields available in a report. | Edit the Domain and save it with a new name. Then start a new view and choose your data from the new Domain. | Domains provide advanced functionality such as table joins and derived fields based directly on a data source. Domains usually require administrator permissions to create and modify. |

!!! warning

    Ad Hoc views based on Domain topics may return duplicate data if Data Staging is enabled.

## Access Permissions in Domain Topics

If other users create reports from your Domain Topic-based view, and the Domain is configured for security, it's important to consider everyone’s access permissions. You might not have access to all of the fields in the Domain nor to all the data in those fields. There may be fields that can be seen only by other users, and in the fields that you can see, some data may be hidden from you. When you save the Domain as a Topic, only the fields that you selected appear in the Domain Topic. When you create a view from the Topic, only the data that you can access in those fields appears. When others create views from the Topic, they see only fields that they have permission to access. These rules also apply to the reports generated from these views.

For example, in a Domain, user Tomas can access fields B-C and data rows 1-3; Anita can access fields C-E and data rows 2‑5. Tomas uses the Data Chooser and saves a Domain Topic based on the Domain. When Tomas and Anita create reports from the same view, they see different combinations of fields and the data in them.

|                                           | Fields | Data    |
|-------------------------------------------|--------|---------|
| Tomas's report from his Domain Topic      | B C    | 1 2 3   |
| Anita’s report from the same Domain Topic | C      | 2 3 4 5 |

Even though Anita has permission to see more fields, they're not available to her because Tomas did not have access to them when he created the Domain Topic. However, Anita does have permission to see more data than Tomas, so when she creates a view, or opens or runs the report based on that view, she can see more rows than Tomas can when he views the report. See the JasperReports Server Security Guide for a technical explanation of data security for Domains.

## Saving Domain Settings as a Domain Topic

To save settings in the Data Chooser wizard as a Domain Topic

1.  While making selections in the Data Chooser, navigate to the **Save Topic** page.

2.  Enter a Topic name and description.<br>
    Do not change the location folder. Using the default /adhoc/topics folder makes the saved Domain Topic available in the **Ad Hoc Components &gt; Topics** folder when you select **Create &gt; Ad Hoc View**.

3.  If your data selections, filter definitions, and display settings are complete, click **Table**, **Chart**, or **Crosstab**.

    !!! note

        If settings are incomplete, navigate to the other pages to finish, then click **Table**, **Chart**, or **Crosstab**

The new Topic appears in the **Ad Hoc Components &gt; Topics** folder.

Because a Domain Topic is a type of report, it appears when the Search page is filtered to show reports:

## Editing a Domain Topic

You can modify a Domain Topic you created using the Data Chooser.

To edit the settings in a Domain Topic

1.  Select **View &gt; Repository** and search (or browse) for the Domain Topic you want to modify. Domain Topics are usually kept in the **Ad Hoc Components &gt; Topics** folder.

2.  Right-click the Domain Topic and select **Open in Designer** from the context menu. The Domain Topic opens in the Data Chooser wizard.

3.  Follow the guidelines in [Using the Data Chooser Wizard](adhoc-data-chooser.md) to edit the Domain Topic as needed.

4.  To save changes to the selected Domain Topic, click **Table**, **Chart**, **or Crosstab** on any page.

    !!! warning

        Use caution when editing Domain Topics that may have been used to create other views. Users relying on the Domain Topic might receive unexpected data or errors. It's safer to save changes as a new Domain Topic.

To save changes as a new Domain Topic, navigate to the Save as Topic page and enter identifying information for the new Topic, then click **Table**, **Chart**, **or Crosstab**.
