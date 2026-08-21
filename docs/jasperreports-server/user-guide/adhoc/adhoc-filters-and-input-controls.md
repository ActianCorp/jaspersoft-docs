---
title: Using Filters and Input Controls
description: "JRXML Topics, Domains, and OLAP connections use different mechanisms for screening the data they return:"
---

# Using Filters and Input Controls

JRXML Topics, Domains, and OLAP connections use different mechanisms for screening the data they return:

- JRXML Topics can contain Parametrized queries. The parameters can be mapped to input controls that allow users to select the data they want to include.
- Domains (and Domain Topics) can be filtered by selecting fields in the Domain and specifying comparison values. The filters can be configured for users to select the data to include.
- Within the Domain design, filters based on conditions can also be defined; these filters are not displayed in the Report Viewer when the report runs.
- OLAP connections rely on XML schemas to filter the data in an underlying transactional database. Input controls are never generated directly from the OLAP schema.

You can define filters in the Ad Hoc Editor regardless of whether you are working with data from a Domain, Topic, or OLAP connection. Such filters can be helpful in improving the view's initial performance by reducing the amount of data the view returns by default. For more information, see [Input Controls and Filters Availability](adhoc-filters-availibility.md). To prevent users from seeing the full dataset, you can also use input controls in a JRXML Topic or filters defined in the Domain design, which can be hidden from end users.

If you want to return different data to different users of the same view, define data-level security based on a user roles and profile attributes. This is available for reports based on a Domain, Domain Topic, or OLAP client connection. For more information, refer to the Jaspersoft OLAP User Guide.

Input controls and filters interact seamlessly. For example, you can create filters in an Ad Hoc view that gets data from a JRXML Topic that includes input controls.

The server refreshes the editor against both the filters and the input controls. Because some combinations of input controls and filters don’t return data, this can result in an empty view.

!!! note

    If the result set is empty, check for an incompatible combination of filters and input controls, such as a standard filter (set to Mexico against a Country field) and a **Keep Only** filter (set to Canada against a Country field), or an incorrectly-defined advanced filter expression (data must meet all criteria in multiple filters, rather than meeting criteria in a subset of those filters). See [Advanced Filtering](adhoc-filters.md) for information on advanced filter expressions.

In rare cases, filters can conflict with view parameters, and you’ll need to rename the field causing the conflict by editing the JRXML file. Refer to the Jaspersoft Studio User Guide for more information about editing JRXML files.

For more information about:

- JRXML Topics and input controls, see [Adding Input Controls](../repo-upload-reports/repo-adding-input-controls.md).
- Domain Topic filters, see [Creating Topics from Domains](adhoc-create-topic-from-domain.md).
- Localizing input control prompts and lists of values, see [Localizing Reports](../repo-upload-reports/repo-localizing-reports.md).
