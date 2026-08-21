---
title: Configuring the Login Page for a Single-Organization Deployment
description: "Even for a single-organization deployment, the user needs to enter an external organization name on the login page. To make the organization field available on the login form, you need to set the..."
---

# Configuring the Login Page for a Single-Organization Deployment

Even for a single-organization deployment, the user needs to enter an external organization name on the login page. To make the organization field available on the login form, you need to set the `alwaysRequestOrgIdOnLoginForm` property in the `externalAuthProperties` bean to `true`.

Deployments with multiple organizations in the database always display a line for the organization ID on the login page.
