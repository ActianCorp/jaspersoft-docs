---
title: Launching JasperReports Server from Azure Marketplace
description: This section describes the requirements and steps for launching a Jaspersoft VM on Azure Marketplace.
---

# Launching JasperReports Server from Azure Marketplace

This section describes the requirements and steps for launching a Jaspersoft VM on Azure Marketplace.

Jaspersoft offers BYOL (Bring Your Own License) VM on Azure. Instructions in this section ensure that the right VM size is selected for your Jaspersoft deployment.

## Requirements for Single Instance BYOL VM

The following JasperReports Server features must be turned ON.

- **Chromium** - Export for dashboards and reports
- **Diagnostic** - Diagnostic report should be present and enabled
- Password change is enabled and prompts the user to change the password on the login page. For more information about changing the password, see [Configuring User Password Options](https://community.jaspersoft.com/documentation/tibco-jasperreports-server-administrator-guide/v60/configuring-user-password-options).

The following multi-tenant configurations are recommended:

- Only root organization is present.
- Superuser - activated and password auto-generated at VM creation time
- All other users disabled in JasperReports Server
- Encryption - default settings

The following Sample Data is available:

- Foodmart and SugarCRM database populated on VM
- All standard sample repository resources deployed

!!! info "Important"

    On the Azure Welcome Page (BYOL only available), users should update their passwords on the first login:<br>
    username:` superuser`<br>
    password: `<generated>`
