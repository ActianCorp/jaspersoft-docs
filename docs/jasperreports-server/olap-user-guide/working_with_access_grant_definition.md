---
title: Working with Access Grant Definitions
description: "This section describes functionality that can be restricted by the software license for JasperReports Server. If you do not see some of the options described in this section, your license may..."
---

# Working with Access Grant Definitions

!!! info "Important"

    This section describes functionality that can be restricted by the software license for JasperReports Server. If you do not see some of the options described in this section, your license may prohibit you from using them. To find out what you are licensed to use, or to upgrade your license, contact Jaspersoft.

An access grant definition is an XML structure that specifies a user’s access rights to different parts of the data defined by an OLAP schema. The access grant definition specifies access rights based on roles. Users with a given role have the access rights granted to that role. An access grant definition can also refer to attributes that control access through properties defined for specific users, organizations, and server instances. This allows you to use variable substitution to create simple, flexible access grants.

This section includes:

- [Overview of Data-level Access Using AGXML Schemas](overview_of_data_level_access_using_.md)

- [Sample Access Grant Definition](sample_access_grant_definition.md)

- [Uploading an Access Grant Schema](uploading_an_access_grant_schema.md)

- [Working with Attributes](working_with_profile_attributes.md)

- [Best Practices for Designing Access Control](best_practices_for_designing_access_.md)

!!! note

    AGXML depends on Jaspersoft’s underlying OLAP engine, and as such only applies to data accessed by a local OLAP client connection (that is, a Mondrian connection). To restrict data accessed via XML/A, define your security in the remote host serving your data; for example, attach an AGXML schema to a Mondrian connection exposed by an XML/A source.
