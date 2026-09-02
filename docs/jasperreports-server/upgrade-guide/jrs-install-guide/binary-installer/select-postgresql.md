---
title: Selecting a PostgreSQL Configuration
description: "JasperReports Server requires a database. The installer is pre-configured to run with the PostgreSQL database. You may use any of the following two options:"
---

# Selecting a PostgreSQL Configuration

JasperReports Server requires a database. The installer is pre-configured to run with the PostgreSQL database. You may use any of the following two options:

-   bundled PostgreSQL

-   existing PostgreSQL (deselect the **Bundled PostgreSQL** option)

## Choosing the Bundled PostgreSQL

If you install the bundled PostgreSQL, the installer puts PostgreSQL onto your system. The default PostgreSQL port is 5432. If port 5432 is in use, the installer prompts you to pick an alternate port.

The installer sets the PostgreSQL administrator password to **postgres** and creates a PostgreSQL database user with administrator privileges and the credentials **jasperdb/password**.

If you install the bundled PostgreSQL, the installer puts PostgreSQL onto your system. The default PostgreSQL port is 5432. If port 5432 is in use, the installer increments the port number by one until it finds an open port.

The installer sets the PostgreSQL administrator password to **postgres**.

The following table summarizes the parameters set during installation of the bundled PostgreSQL:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Parameter</p></th>
<th><p>Default Value and Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Binary Directory</p></td>
<td><p>The directory where the PostgreSQL and pgAdmin binaries are located.</p></td>
</tr>
<tr>
<td><p>Port</p></td>
<td><p>The port number PostgreSQL uses (default is 5432). Choose an alternate port if 5432 is in use.</p></td>
</tr>
<tr>
<td><p>IP or Host Name</p></td>
<td><p>The IP address or name of the machine where PostgreSQL is installed. The default value is 127.0.0.1.</p></td>
</tr>
<tr>
<td><p>PostgreSQL Administrative Password</p></td>
<td><p><span>Password of the database administrative user: <span>password</span>. </span></p>
<p>Password of the <span>postgres</span>administrative user.</p>
<p>The installer cannot handle special characters at the end of a password string. Incompatible characters include: &amp; ; $</p></td>
</tr>
<tr>
<td><p>Database User Name</p></td>
<td><p>The user name is hard coded. The default value is <strong>jasperdb</strong>. The installer creates this user to connect to the JasperReports Server database.</p></td>
</tr>
<tr>
<td><p>Database User Password</p></td>
<td><p>The password is hard coded. The default value is <strong>password</strong>. The installer uses this password for the jasperdb user.</p></td>
</tr>
<tr>
<td><p>Additional notes for Linux</p></td>
<td><p>If your Linux installation does not have a locale setting that supports UTF-8 encoding, your bundled PostgreSQL instance is initialized using a temporary locale (<code>--locale=C</code>). This allows the PostgreSQL initdb to succeed with the desired UTF-8 database encoding.</p></td>
</tr>
</tbody>
</table>

## Choosing an Existing PostgreSQL on a Local Host

If you choose to use an existing PostgreSQL database, then you are prompted for the location of PostgreSQL and the port to use. If you have an instance of PostgreSQL installed locally, accept the default, which is 127.0.0.1, the localhost. Accept the default location for the PostgreSQL \\bin directory, or click **Browse** to select another location. You are also be prompted for the default administrative account password of the PostgreSQL administrative user. The database administrative user account name **postgres** is used by default. Enter the database administrative user password and click **Enter**.

## Choosing an Existing PostgreSQL

If you choose to use an existing PostgreSQL database, then you are prompted for the location of PostgreSQL. If you have an instance of PostgreSQL installed locally, accept the default, which is 127.0.0.1, the localhost. Accept the default location for the PostgreSQL \\bin directory, or click **Browse** to select another location. You are also prompted for the default administrative account password of the PostgreSQL administrative user. The database administrative user account name **postgres** is used by default. Enter the database administrative user password and click **Enter**.

!!! note

    If the installer displays with the following error message: FATAL: password authentication failed for user postgres, then try re-entering the administrative password for your PostgreSQL database.

The following table summarizes the parameters set during the installation of an existing PostgreSQL.

| Defaults Used | Hard-coded Default Values Used or Created |
|----|----|
| PostgreSQL Administrative User Name | postgres - The default administrative database user. |
| jasperserver Database User Name | jasperdb - The installer creates this database user to connect to the jasperserver database. |
| jasperserver Database User Password | password - The installer creates this password for the jasperdb database user. |

!!! warning

    To improve system security, Jaspersoft recommends that you change the default password for jasperdb as soon as possible. To change the jasperdb connection password in JasperReports Server, edit: `<js-install>/apache‑tomcat/``jasperserver`` ``-pro`` /META-INF/context.xml`. (And delete:` <js-install>/apache-tomcat/conf/Catalina/localhost/``jasperserver`` ``-pro`` .xml`, if it exists.) Then make the same change in PostgreSQL using pgAdmin or psql.

## Using an Existing PostgreSQL on a Remote Host

If you are installing on a remote instance of PostgreSQL, then you need to have the PostgreSQL client tools on your local machine. The client tools version should match the version of your remote PostgreSQL. You can check the version of the PostgreSQL instance by entering this command on the computer where it is installed:

`psql --version`

or

`<path-to-postgresql-bin-folder>/psql --version`

For instance: `C:/Jaspersoft/PostgreSQL/9.0/bin/psql --version`

To verify that, you can connect to the target remote PostgreSQL from the local installation machine

-   Using your local PostgreSQL client tools, enter this command:

`psql -U postgres -h <remote-host> -d postgres `

or

`<path-to-postgresql-bin-folder>/psql -U postgres -h <remote-host> -d postgres`

You might also need to enable connections as described below.

## Enabling Connections to a Remote Host

On most platforms, the default PostgreSQL installation does not allow remote connections for security reasons. You need to enable remote connections as described in this documentation:

-   The PostgreSQL configuration documentation is on the PostgreSQL website.

-   The \\docs directory of your PostgreSQL installation.

To enable connections from the installation machine to the remote PostgreSQL server

1.  Locate the following PostgreSQL host-based authentication (hba) configuration file on the remote PostgreSQL server instance:

    Windows: `C:\Program Files\PostgreSQL\X.X\data\pg_hba.conf` (where X.X is the version number)

    Linux: `/var/lib/pgsql/data/pg_hba.conf`

2.  Add the IP address of your local JasperReports Server installation machine to this file. For example, to allow the local installation machine with address 192.168.12.10 to connect to the PostgreSQL server, add this entry to the pg_hba.conf file:

    `host all 192.168.12.10/32 trust`

3.  Allow TCP/IP connections to the remote PostgreSQL server instance by making the following change to the postgresql.conf file on the remote machine:

    From: `listen_addresses = 'localhost`'

    To:` listen_addresses = '*' `

4.  Restart PostgreSQL.

5.  Using your local PostgreSQL client tools, verify that you can connect to the target remote PostgreSQL from the local installation machine, as described in [Using an Existing PostgreSQL on a Remote Host](#using-an-existing-postgresql-on-a-remote-host).
