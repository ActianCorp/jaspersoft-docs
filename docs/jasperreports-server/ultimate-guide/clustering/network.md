---
title: Network
description: "Finally, consider the availability and quality of your network. How remote are your users and how do they connect to the cluster?"
---

# Network

Finally, consider the availability and quality of your network. How remote are your users and how do they connect to the cluster?

The two main concerns about your network are:

-   Network availability and capacity affects the cluster's availability and scalability. If you have strict availability requirements, you may need redundant network connections from different providers. For scalability and performance requirements, your network needs to handle the load of the planned maximum number of users, or have plans to scale the network along with the number of users.

-   Network bandwidth can affect server load by slowing down individual connections. JasperReports Server can generate multiple large documents simultaneously that are sent to the web browser or API clients. Network capacity (megabytes per second) is critical to being able to deliver these generated documents in reasonable time. The slower the network, the more load on the servers generating the report documents, as they'll take longer to deliver the same content, and potentially lead to more simultaneous report requests.
