---
title: Performing LDAP User Search
description: You need to set up the search parameters for locating your users in the LDAP directory. The goal is to locate a single user entry that validates the password given during the login process. The LDAP...
---

# Performing LDAP User Search

You need to set up the search parameters for locating your users in the LDAP directory. The goal is to locate a single user entry that validates the password given during the login process. The LDAP entry located by the user search is later used to map roles and organizations.

One of the most common problems in configuring LDAP for JasperReports Server is setting up the correct search parameters to locate the users you want to map. LDAP is a rich and complex structure, with many possible variations, and LDAP directories tend to grow in complexity over time. To successfully map your users from LDAP to JasperReports Server, you need to understand the directory server tree structure of your LDAP server. Be aware that branches can be password protected and a single keyword can be used in different ways in different contexts. It can be helpful to use an open-source LDAP browser, like Apache Directory Server/Studio or JXplorer, to view and navigate your LDAP directory while troubleshooting LDAP user search problems.

!!! warning

    Each time a user logs in, their roles and status are updated via your chosen method and synchronized with the internal jasperserver database. If you want to disable an external user or modify their external roles, you must do so in your LDAP directory.

## Configuring JSBindAuthenticator

The sample files use an unnamed bean of the `JSBindAuthenticator` class to encapsulate search parameters for finding users in the LDAP directory.

There are two ways to configure `JSBindAuthenticator` to locate users:

- Configure the `userDnPatterns` property in the `JSBindAuthenticator` bean to match RDN patterns based on the login name provided by the user. Use this method if the login name appears in the DN of your user entries and your user entries are in a fixed branch of your LDAP directory. See [Specifying userDnPatterns Parameters](ldap-userdnpatterns-parameters.md) for more information.

!!! note

    Matching patterns is faster because it checks for a DN only in the LDAP directory, instead of a searching all users. However, it's less flexible. `userDnPatterns` is not included in the sample files by default.

- Configure the `userSearch` helper bean to perform a search for the login name provided by the user. Use this method if the login name is the value of an attribute that doesn't appear in the RDN, or if your user entries are located in a more complex structure. See [Specifying userSearch Parameters](ldap-usersearch-parameters.md) for more information.

You can configure pattern matching and login name search at the same time. Patterns are matched first, and login name search is done only if no match is found.

To find a user, `JSBindAuthenticator` takes the login name entered into JasperReports Server and attempts to find the correct user in the LDAP directory using bind authentication, as follows:

1.  Using the specified pattern matching or search for the login name, find a candidate user entry.

!!! note

    The LDAP username for this candidate does not have to be the JasperReports Server login name. If they are different, the user in JasperReports Server is assigned the login name given during the login process, and not the LDAP username.

2.  Attempt to log into the LDAP server using the candidate LDAP username with the login password.
3.  A successful bind indicates that the right user was found.

## Alternative to Bind Authentication

Bind authentication with the `JSBindAuthenticator` bean is the default behavior when configuring Spring Security for LDAP authentication. But Spring Security provides an alternate authentication method based on password comparison:

1.  Use the administrator credentials in the `ldapContextSource` bean to log into the LDAP server.
2.  Find a candidate user entry.
3.  Retrieve the candidate’s password attribute and compare it to the login password, or send the login password for comparison by the LDAP server.

The alternate authentication method is implemented by Spring Security in the `PasswordComparisonAuthenticator` class. Configuring Spring Security with this class is beyond the scope of this guide. For more information, see the Spring Security documentation and Javadoc.
