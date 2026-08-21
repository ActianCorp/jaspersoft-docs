---
title: LDAP Search for Multiple Organizations
description: "When you're authenticating users for one or more organizations in a commercial edition of JasperReports Server, the search parameters must be able to locate all users for all organizations for these..."
---

# LDAP Search for Multiple Organizations

When you're authenticating users for one or more organizations in a commercial edition of JasperReports Server, the search parameters must be able to locate all users for all organizations for these reasons:

- The mapping from LDAP user entries to organizations in the server requires the user entries to be in a hierarchical tree structure that mimics the intended organization hierarchy. You can't use attribute values or group membership in LDAP to define organizations.
- External authorization doesn't allow the user to enter an organization name. So the search must find the username among all organizations.

This has two implications:

1.  Your choice of pattern matching or search depends on the structure of user entries in LDAP. For example, if you have a small fixed number of organizations, you could match them with a pattern for each one, as follows:

||
||
||

```
      <property name="userDnPatterns"><list>
        <value>uid={0},ou=users,o=Finance</value>
        <value>uid={0},ou=users,o=HR</value>
        <value>uid={0},ou=users,o=Executive</value></list>
      </property>
```

But if you have a large number of organizations, or if the number or names of organizations can change, you need to search for every potential user. Depending on your LDAP structure, you may be able to specify a search base in `constructor-arg index="0"`; the example below doesn't have one.

```
<bean id="userSearch" class="com.jaspersoft.jasperserver.api.security.
      externalAuth.wrappers.spring.ldap.JSFilterBasedLdapUserSearch">
  <constructor-arg index="0"><value></value></constructor-arg>
  <constructor-arg index="1"><value>(uid={0})</value></constructor-arg>
  <constructor-arg index="2"><ref bean="ldapContextSource" /></constructor-arg>
  <property name="searchSubtree"><value>true</value></property>
</bean>
```

2.  You cannot implement external authentication for two users with the same login name in different organizations. LDAP supports this as long as the two users have distinct DNs, and JasperReports Server supports this for the default internal authentication. But during external authentication, organization mapping happens after user search, so the user search must return a single LDAP entry:

- Pattern matching stops at the first match based on the login name. As a result, only the user whose LDAP entry pattern is listed higher in the list can log in.
- Search returns more than one entry. As a result, login fails for both users with the same login name.
