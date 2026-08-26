---
title: Deploying the Cluster
description: "Now that everything is configured, the cluster has been created with a node group, and the images have been pushed to the ECR repository, we can finally start the cluster. This instantiates nodes..."
---

# Deploying the Cluster

Now that everything is configured, the cluster has been created with a node group, and the images have been pushed to the ECR repository, we can finally start the cluster. This instantiates nodes from the corresponding images according to the number of machines in the virtual private cloud.

!!! warning

    Before proceeding, make sure you have fully configured your Helm chart (values.yaml) and other cluster configuration files, as described in [Configuring a Cluster in Kubernetes](../configuring/intro.md).

1.  If you have not already done so, install the Helm command-line app to run Helm commands. You can download binaries or use package managers as described in <https://helm.sh/docs/intro/install/>.

2.  Go to the home directory of the JasperReports IO At-Scale distribution, by default jasperreports-io-at-scale-10.1.0/ where the helm folder is located, and run the following command:

    ``` text
    helm install JRIOcluster ./helm
    ```

    Where `JRIOcluster` is the name of your AWS EKS cluster.

3.  Verify that the cluster was deployed with the following command:

    ``` text
    helm list
    ```

4.  Then verify that all the nodes have started successfully:

    ``` text
    root@/opt> kubectl get all
    NAME                                 READY   STATUS    RESTARTS   AGE
    pod/jrio-client-88cc9485c-cjj5v      1/1     Running   0          68s
    pod/jrio-export-859b6dd55f-xnspz     1/1     Running   0          68s
    pod/jrio-manager-ccb7bf45d-qwkvb     1/1     Running   0          68s
    pod/jrio-reporting-66b7d7f74-7628p   1/1     Running   0          68s
    pod/jrio-rest-5475ddb958-cl5vq       1/1     Running   0          68s
    pod/redis-7c676c6-5qczq              1/1     Running   0          68s

    NAME                  TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)
    service/jrio-client   NodePort       10.100.235.226   <none>        8080:32629/TCP
    service/jrio-rest     LoadBalancer   10.100.11.180    [see below]   8080:31946/TCP
    service/kubernetes    ClusterIP      10.100.0.1       <none>        443/TCP
    service/redis         ClusterIP      10.100.169.121   <none>        6379/TCP

    NAME                             READY   UP-TO-DATE   AVAILABLE   AGE
    deployment.apps/jrio-client      1/1     1            1           68s
    deployment.apps/jrio-export      1/1     1            1           68s
    deployment.apps/jrio-manager     1/1     1            1           68s
    deployment.apps/jrio-reporting   1/1     1            1           68s
    deployment.apps/jrio-rest        1/1     1            1           68s
    deployment.apps/redis            1/1     1            1           68s

    NAME                                       DESIRED   CURRENT   READY   AGE
    replicaset.apps/jrio-client-88cc9485c      1         1         1       68s
    replicaset.apps/jrio-export-859b6dd55f     1         1         1       68s
    replicaset.apps/jrio-manager-ccb7bf45d     1         1         1       68s
    replicaset.apps/jrio-reporting-66b7d7f74   1         1         1       68s
    replicaset.apps/jrio-rest-5475ddb958       1         1         1       68s
    replicaset.apps/redis-7c676c6              1         1         1       68s
    ```

    After the cluster has been deployed, the only service with an external IP hostname is the jrio-rest service of type LoadBalancer. On AWS, it takes some time, you may need to wait a few minutes before the hostname appears, for example:

    a073e3faaa4b341c4ac637f6529bc45a-1698884248.us-east-1.elb.amazonaws.com on port 8080

5.  Finally, the load balancer security group has to be configured to allow incoming traffic from the JasperReports Server instance or from any other machine. Note that this will work properly only when a single AWS Availability Zone is configured; for multi-AZ another load balancer type should be used in the AWS EKS config. To enable incoming traffic:

    1.  In your AWS console, go to EC2 &gt; Load Balancers and find your load balancer. It will have the same name as the exposed Kubernetes service.
    2.  Select the load balancer, and locate the source security group in its description. Write down the ID of this group.
    3.  In the AWS console again, go to Security Groups, and find the security group with that ID. It should also have `k8s-elb` in its name.
    4.  Edit the Inbound rules for that security group, and open the port (8080 in this example) for your server instance or any other machine.
