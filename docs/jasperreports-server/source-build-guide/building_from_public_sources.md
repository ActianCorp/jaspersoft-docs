---
title: Building From Public Sources
description: "Commercial customers can download the full commercial source code as described in the chapters above. However, approximately half the source code that makes up the full commercial source is actually..."
---

# Building From Public Sources

## Introduction

Commercial customers can download the full commercial source code as described in the chapters above. However, approximately half the source code that makes up the full commercial source is actually open source that's always available for browsing and checkout.

Open source users and commercial users might find it useful to checkout and build directly from the Subversion repository available online.

## Checkout and Build Public Source Code

You can check out the JasperReports Server public source code here:

http://code.jaspersoft.com/svn/repos/jasperserver

Here is an example checkout command:

`svn checkout --username anonsvn --password anonsvn`

http://code.jaspersoft.com/svn/repos/jasperserver/tags/lastReviewed-trunk jasperserver

In this example, `tags/lastReviewed-trunk` represents the most current successfully built version of the source that's been reviewed by the Jaspersoft QA team.

This wiki article on the Jaspersoft Community Site covers the steps for building the public source code:

http://community.jaspersoft.com/wiki/building-jasperreports-server-source-code

## Browse Public Source Code

To browse the public source code, go to this page and look for the "Browse Source Code" link:

http://community.jaspersoft.com/project/jasperreports-server
