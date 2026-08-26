---
title: Jaspersoft OLAP in a Cluster
description: "Jaspersoft OLAP (On Line Analytical Processing) is a module of JasperReports Server that uses different data schemas, queries, and views to perform interactive data analysis such as slicing,..."
---

# Jaspersoft OLAP in a Cluster

Jaspersoft OLAP (On Line Analytical Processing) is a module of JasperReports Server that uses different data schemas, queries, and views to perform interactive data analysis such as slicing, drill-down, and drill-through. As with JRXML and JasperReports, all of the analysis schemas, MDX queries, and analysis views are stored in the repository and accessible from any node of the cluster. Therefore, the basic configuration of Jaspersoft OLAP will run without modification in a cluster.

However, Jaspersoft OLAP is composed of two parts: an XML/A client that displays data and an XML/A provider or server that retrieves and processes the data. As described in the Jaspersoft OLAP User Guide, these two parts can run on separate instances of JasperReports Server. Different behaviors result depending on how define the XML/A connection in a cluster:

-   In the default case, the definition of the XML/A provider points to the `localhost`, so the same node that receives the user request will both perform the analysis and display it.

-   You can change the definition of the provider so that it points to the URL of the load balancer for the cluster. In this case, the node that receives the user request will ask another node to retrieve the data for it, and the results will be sent back to the first node for display.

!!! note

    Because of the extra communication and connections, whether this configuration increases performance depends on your overall cluster load. If you have lots of analysis users at the same time, the load will be uniformly high, and there will be no benefit to calling the XML/A provider on a node that is equally busy. In fact, the extra overhead may impact performance, in particular if the connection loops back to the same node.

    On the other hand, if your nodes are occasionally idle or if your load balancer detects real-time load on each node, this configuration will spread the analysis load and optimize performance for all users.

-   You can set the connection to the URL of a specific XML/A provider. This could be a dedicated instance of JasperReports Server running Jaspersoft OLAP that's not connected to the cluster. You would need to size this instance to handle your expected analysis load and possibly implement two nodes as a cluster for availability. The advantage of having a dedicated XML/A provider instance is that it would centralize the cache for XML/A connections, thereby increasing cache hits.

Factors such as the size of your data and the ratio of JasperReports load to OLAP load can help you determine how to configure your XML/A connections in a cluster. If you don’t perform much analysis, use the default configuration with `localhost` for your connections. If you have many analysis requests to the same data, a dedicated instance of Jaspersoft OLAP could provide a central cache and increase performance. Remember that connection behavior is determined by the XML/A connection defined in the repository, not by the nodes.

For simplicity, we recommend that every XML/A connection be configured the same way, so that XML/A connections are uniform across the cluster. However, if you have advanced analysis needs, you might benefit from having different behaviors for different XML/A connections. How to determine and configure optimal Jaspersoft OLAP performance in a cluster is beyond the scope of this document.
