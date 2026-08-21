---
title: Administrator Login
description: "Administrators log in on the standard login page, using the following default passwords:"
---

# Administrator Login

Administrators log in on the standard login page, using the following default passwords:

|                     |                                                  |
|---------------------|--------------------------------------------------|
| System admin:       | user ID `superuser` and password `superuser`     |
| Organization admin: | user ID `jasperadmin` and password `jasperadmin` |

!!! warning

    For security reasons, always change the default administrator password<span>s</span> immediately after installing JasperReports Server. For instructions, see <a href="../management/managing_users.md">Editing a User</a>.

For more information about options on the Login page and logging in with multiple organizations, see the JasperReports Server User Guide.

The first time you log in as an administrator, you may be prompted to opt-into the Heartbeat program. You should also set the administrator passwords and email.

Failed login attempts can disable an account. The number of remaining attempts is displayed after a failed login.

It is recommended to create a second system admin (with custom name) in case a `superuser` gets locked out, you will need to edit the db table to unlock. See **Creating a System Administrator**.

Refer to the [Enabling a Locked User](../management/managing_users.md) topic for information on how to unlock a user account. Refer to the JasperReports Server Security Guide for information on how to disable or configure the setting (enabled by default).

## JasperReports Server Heartbeat

When you log into JasperReports Server for the first time after installation, administrators may be prompted to opt into the server's [Heartbeat](http://www.jaspersoft.com/heartbeat) program. It reports specific information to Jaspersoft about your implementation: the operating system, JVM, application server, database (type and version), and JasperReports Server edition and version number. By tracking this information, we can build better products that function optimally in your environment. No personal information is collected.

To opt into the program, click **OK**. To opt out, clear the check box then click **OK**.

## Administrator Email

After logging in for the first time, you should set the email on the `superuser` and `jasperadmin` accounts to your email address. In rare cases, the server may notify you by email about issues with your license.

!!! warning

    This is also a good time to change the default passwords on the<span>`superuser` and</span>`jasperadmin` account<span>s</span>.

To set the email and passwords on the administrator accounts, edit the user account information as described in [Editing a User](../management/managing_users.md).
