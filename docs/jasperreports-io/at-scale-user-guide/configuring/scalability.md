---
title: Configuring Scalability
description: "The scalability configuration defines how the cluster can scale up or down depending on different metrics, usually memory, and CPU usage."
---

# Configuring Scalability

The scalability configuration defines how the cluster can scale up or down depending on different metrics, usually memory, and CPU usage.

The Kubernetes scheduler relies on data from the Metrics system server that is usually installed manually in the Kubernetes cluster. The scheduler monitors the cluster nodes on which the pods are running and sends aggregated values to the Kubernetes control plane. These values are averaged between pods and reported at 10 to 30-second intervals. Therefore, the cluster sometimes does not react to an increased workload immediately, at least not until the next metric reporting interval.

To scale up by starting a new pod, the Kubernetes control plane must know if there are enough resources on the node where it can start the new pod. That is, it must know if there is enough memory and CPU available for the memory and CPU requested by the new pod. This is why each pod should have its resource requests and limits defined in a deployment configuration file.

To configure scalability, set the resource requests and limits in the values.yaml file, as described in [Configuring the Helm Chart](helm_chart.md).

The `cpuRequest` and `memoryRequest` values are the minimum amount of resources for the pod to start inside a node, and the `cpuLimit` and `memoryLimit` are the maximum that Kubernetes can give to that pod. A pod will never get more resources than the `*Limit` settings, but it is possible for it to use less than defined in the `*Request` settings. For more information about resource usage, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits).

Helm also has scalability settings in the following files, but Jaspersoft recommends using the settings in values.yaml:

jasperreports-io-at-scale-10.1.0/helm/templates/jrio-\<module\>-deployment.yaml

For example, the contents of the jrio-reporting-deployment.yaml file are as follows:

``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jrio-reporting
  labels:
    jrio.app: jrio-reporting
spec:
  replicas: {{ default 2 .Values.jrioReporting.replicas }}
  selector:
    matchLabels:
      jrio.app: jrio-reporting
  template:
    metadata:
      labels:
        jrio.app: jrio-reporting
    spec:
      containers:
      - name: jrio-reporting
        image: {{ default "jrio-reporting" .Values.jrioReporting.dockerImage}}:{{ required "The .Values.jrioReporting.dockerTag is required!" .Values.jrioReporting.dockerTag }}
        resources:
          limits:
            cpu: 1000m
            memory: 1Gi
          requests:
            cpu: 500m
            memory: 512Mi
      restartPolicy: Always
```
