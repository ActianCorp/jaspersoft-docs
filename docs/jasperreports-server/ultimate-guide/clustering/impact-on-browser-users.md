---
title: Impact on Browser Users
description: "Thanks to partial session replication, a node failure has no impact on most users. If they're browsing the repository or scheduling a report, they won't even notice when failover to another node..."
---

# Impact on Browser Users

Thanks to partial session replication, a node failure has no impact on most users. If they're browsing the repository or scheduling a report, they won't even notice when failover to another node occurs. A node failure mainly affects interactive sessions where the user has unsaved work, such as in the Ad Hoc Editor and Dashboard Designer. In those cases, users are redirected to the home page on the new node, and they may need to re-create a report or dashboard, but they won't lose any critical functionality or data.

The following table lists the elements of the user session that cannot be replicated and explains the impact of failover on a user.

| Non-Replicated Session Element | Interactive Feature Impacted upon Failover |
|----|----|
| State of Ad Hoc fields and data | The Ad Hoc editor display consists of fields placed in the canvas and the various filters and mode settings that determine what values are displayed, as well as visualizations such as table columns, crosstabs, and charts. These items are displayed with data from the data source. Upon failover, the state and data in the Ad Hoc editor cannot be restored, so any unsaved changes are lost. |
| State of Dashboard designer | The Dashboard designer displays reports and controls in a grid layout. Upon failover, the contents and state of the canvas cannot be restored, so any unsaved changes are lost. |
| JasperPrint object from running a report | Reports in the report viewer rely on the JasperPrint object for pagination and exporting in other formats. Upon failover, reports in the report viewer cannot be restored, and any unsaved changes such as interactive sorting and filtering are lost. |
| State of the Domain designer | The Domain designer is a set of tabs for defining the tables, joins, filters, calculated fields, and default names for the fields of a Domain. Upon failover, the changes made in the Domain designer tabs cannot be restored and any unsaved changes are lost. |
| OLAP viewer state | The OLAP viewer lets you explore the dimensions and values in an OLAP cube by changing the MDX expression that defines the view. Upon failover any unsaved view is lost and would need to be created again through the same transformations (slicing and dicing). |
| Administration dialogs (when creating or editing an organization, user, or role) | Any information entered in an administration dialog is lost if it was not submitted before node failure. |

For example, when a node fails during interaction with the Ad Hoc editor, the user is redirected by the load balancer to another node, which like all nodes, has only the partially replicated user session. Because it does not have the state of the user's Ad Hoc changes, it cannot save or even display the work started on the failed node. In this event, the interactive work is lost, and users see an error message on the new node. Upon acknowledging the message, users are redirected to the home page.

The standard precaution against lost work is for users to save their work at regular intervals or significant milestones. Both the Ad Hoc Editor and the Dashboard Designer let users save their current view as a report or dashboard that can be opened to the same state. Work the user explicitly saves is stored in the shared repository and can be reopened in the new session on the new node. This includes any resources created, moved, or saved for any Save or Save As operation that completes before a failure.

For all cases not listed in the table above, work in progress is preserved upon failover, and the user can continue to work immediately on the new node. For example, if the user was searching the repository at the time of failure, all parts of the session needed for search are replicated. So the user can continue interacting with search results immediately on the new node – usually without even noticing there was a failure.

Also, information for the following dialogs are part of the replicated session, and are successfully transferred to a new node in case of a failover:

- Repository permissions dialog

- Add folder dialog

- Add resource dialogs, including adding or editing a data source, JasperReport, and other repository objects

- Copy, cut, and pasting resources in the repository

- Scheduling a report
