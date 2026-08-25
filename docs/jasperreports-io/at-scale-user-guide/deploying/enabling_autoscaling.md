---
title: Enabling Autoscaling
description: "For the cluster to scale automatically based on load, it needs an autoscaler app installed and metrics to know the state of each node. Each of these features is installed in the following sections."
---

# Enabling Autoscaling

For the cluster to scale automatically based on load, it needs an autoscaler app installed and metrics to know the state of each node. Each of these features is installed in the following sections.

## Installing the Cluster Autoscaler

The cluster autoscaler is an app that monitors utilization in the cluster and is authorized to modify the node groups to fit the current load on your cluster.

This section relies on the Amazon document “Cluster Autoscaler” at:

<https://docs.aws.amazon.com/eks/latest/userguide/cluster-autoscaler.html>

Open that document in a separate tab and apply it as follows:

1.  Skip cluster creation using eksctl, because we already created our cluster.

2.  Skip the node group IAM policy, because we already created the EKSNodeInstanceRole.

3.  The autoscaling group tags should already be defined, but it is best to verify them.

    1.  Open the AWS Web console and locate your cluster.
    2.  Select your node group under your cluster.
    3.  Locate the autoscaling group created automatically for the node group.
    4.  Scroll down to Tags and confirm the following (where JRIOcluster is the cluster name):

    |                                       |       |
    |---------------------------------------|-------|
    | k8s.io/cluster-autoscaler/JRIOcluster | owned |
    | k8s.io/cluster-autoscaler/enabled     | true  |

4.  Perform all steps in the section “Deploy the Cluster Autoscaler” of the Amazon document. At the time of publication, the latest version of the autoscaler is 1.7.3, giving the final command as follows:

``` text
kubectl -n kube-system set image deployment.apps/cluster-autoscaler
cluster-autoscaler=us.gcr.io/k8s-artifacts-prod/autoscaling/cluster-autoscaler:v1.17.3
```

## Deploying the Kubernetes Metrics Server

The metrics server is needed to monitor the Kubernetes cluster and collect metrics from each node. The autoscaler uses these metrics to determine node utilization and trigger scaling the node group up or down. You must deploy the metrics server when using the autoscaler.

The metrics server is installed using the kubectl tool as follows:

1.  Run the following command to check if the metrics server is already installed:

    ``` text
    kubectl get deployment metrics-server -n kube-system
    ```

2.  If it is not already deployed, deploy the metrics server with the following command:

    ``` text
    kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.3.6/components.yaml
    ```

3.  Run the first command again to verify that the metrics server is installed:

``` text
kubectl get deployment metrics-server -n kube-system

NAME             READY   UP-TO-DATE   AVAILABLE   AGE
metrics-server   1/1     1            1           4m
```

This section is based in part on the Amazon document “Tutorial: Deploy the Kubernetes Dashboard (web UI)” at:

<https://docs.aws.amazon.com/eks/latest/userguide/dashboard-tutorial.html>

If you want to install the dashboard application to have a graphical view of your cluster, follow the remaining steps in that document.
