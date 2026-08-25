---
title: Password History Validation
description: "The password history validation feature prevents the reuse of old or recycled passwords, reducing the risk of unauthorized account access. This helps in securing your account and protecting your data."
---

# Password History Validation

The password history validation feature prevents the reuse of old or recycled passwords, reducing the risk of unauthorized account access. This helps in securing your account and protecting your data.

When you change or reset your password, the system checks your new password against a securely saved history of your previous passwords. If you try to reuse a recent password, the system blocks the update and prompts you to choose a new password, displaying the following message: **New password must not match any of your recent passwords. Please choose a different password.**

Your organization's administrator determines exactly how many of your past passwords the system will remember before you can reuse them. They can change users and their corresponding password. If they try to reuse any of your recent passwords, the system blocks the update and prompts them to choose a new password, displaying the following message: **New password must not match any of user's recent passwords. Please choose a different password.**

!!! note

    If your organization has not enabled this feature, you will not experience these restrictions during password resets.

For more information, see the *Password History Validation* section in the JasperReports Server Administrator Guide.
