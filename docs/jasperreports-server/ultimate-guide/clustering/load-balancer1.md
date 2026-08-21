---
title: Load Balancer
description: "Determine whether you need a dedicated hardware load-balancer or if a basic software load-balancer will meet your requirements. You should also specify the load-balancing techniques you'll use, such..."
---

# Load Balancer

Determine whether you need a dedicated hardware load-balancer or if a basic software load-balancer will meet your requirements. You should also specify the load-balancing techniques you'll use, such as round-robin, load-based, or some other configuration. If the load balancer communicates with the nodes to optimize traffic, specify how this happens.

Much of the load balancer requirement is based on the size and complexity of your cluster. A small cluster of two to three nodes can use a software load-balancer with a simple algorithm. But if you have many nodes or a few powerful nodes with high traffic, you need a dedicated load-balancer for the cluster.

If you have very strict performance requirements and need to closely monitor the load across the cluster, you may need a load-based balancer that communicates with the nodes. The trade-offs for these advanced load-balancing techniques are more maintenance and a more complex configuration on each node.

And finally, if the cluster is intended to scale over time, the load balancer must be able to handle more incoming traffic and more cluster nodes.
