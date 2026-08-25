---
title: Using a Redis Cluster
description: "By default, JasperReports IO At-Scale uses the redis module to deploy a single redis pod. Redis is a data store used by JRIO to queue report requests and to hold report output. In applications with..."
---

# Using a Redis Cluster

By default, JasperReports IO At-Scale uses the `redis` module to deploy a single `redis` pod. Redis is a data store used by JRIO to queue report requests and to hold report output. In applications with high demand, Redis can become a bottleneck for requests. Therefore, an option for high-performance needs is to deploy Redis as a separate cluster and configure JRIO to use it instead of its own `redis` pod.

To implement a Redis cluster, first you need to deploy and configure the cluster itself. Then you need to configure the JasperReports IO At-Scale modules before building the Docker images. Finally, you need to configure the JRIO Helm Chart before deploying the JRIO cluster.

## Deploying a Redis Cluster

The Redis cluster is separate from the JasperReports IO At-Scale product: you must obtain and install Redis from a third-party source. Jaspersoft has tested JasperReports IO At-Scale with the Redis cluster and Helm chart available from Bitnami, specifically the Redis 6.0.7-debian-10-r0 image, and the examples in this section are based on their product:

<https://github.com/bitnami/charts/tree/master/bitnami/redis-cluster><br>
<https://bitnami.com/stack/redis-cluster/helm>

After downloading the Redis cluster, download the values-production.yaml file from the Bitnami GitHub repo:

<https://github.com/bitnami/charts/blob/master/bitnami/redis-cluster/values-production.yaml>

Edit the values-production.yaml file as follows:

| Property | Description |
|----|----|
| `cluster.nodes` | The number of nodes in the Redis cluster. Jaspersoft has successfully tested with the default of 6 nodes. |
| `cluster.replicas` | The number of Redis replicas, tested with the default of 1. |
| `usePassword` | Set to `true`. |
| `password` | Set your password for accessing Redis from JasperReports IO At-Scale, for example `mypassword`. |

Deploy the Bitnami Redis cluster with the additional values-production.yaml file using the following command:

``` text
helm install redis bitnami/redis-cluster --values values-production.yaml
```

The cluster name is right after the word install in the helm command. In this example, the cluster name is `redis`. The cluster name is used in the redis service name in the JRIO modules configuration, in the format `<cluster-name>-redis-cluster`. Therefore, the service name for this cluster is `redis-redis-cluster`.

If you need to delete the Redis cluster, use the following command where `redis` is the `<cluster-name>`:

``` text
helm delete redis
```

However, Helm does not delete redis volumes, so before you create a new Redis cluster, check the persistent volume claims (pvc) and delete them individually as shown in the following example. There is one volume for each node, so 6 in our example:

``` text
redis_ha> kubectl get pvc | grep redis
redis-data-redis-redis-cluster-0 Bound pvc-e715109e-e0df-4a80-a38b-3449a2bd142a 8Gi RWO gp2 2d17h
redis-data-redis-redis-cluster-1 Bound pvc-0f9a9fda-b3d0-46c0-b2c1-13f202637212 8Gi RWO gp2 2d17h
redis-data-redis-redis-cluster-2 Bound pvc-53121613-929e-467e-b607-b0bec6ee75e4 8Gi RWO gp2 2d17h
redis-data-redis-redis-cluster-3 Bound pvc-963d458d-fffa-4bca-bc5c-f4cb21f39373 8Gi RWO gp2 2d17h
redis-data-redis-redis-cluster-4 Bound pvc-84bc2600-48c7-4eb5-93ef-08b02c01a74b 8Gi RWO gp2 2d17h
redis-data-redis-redis-cluster-5 Bound pvc-17db9ab9-44af-4d69-b422-ba9c0da507a1 8Gi RWO gp2 2d17h

redis_ha> kubectl delete pvc redis-data-redis-redis-cluster-0 redis-data-redis-redis-cluster-1
 redis-data-redis-redis-cluster-2 redis-data-redis-redis-cluster-3
 redis-data-redis-redis-cluster-4 redis-data-redis-redis-cluster-5
persistentvolumeclaim "redis-data-redis-redis-cluster-0" deleted
persistentvolumeclaim "redis-data-redis-redis-cluster-1" deleted
persistentvolumeclaim "redis-data-redis-redis-cluster-2" deleted
persistentvolumeclaim "redis-data-redis-redis-cluster-3" deleted
persistentvolumeclaim "redis-data-redis-redis-cluster-4" deleted
persistentvolumeclaim "redis-data-redis-redis-cluster-5" deleted
```

## Configuring JRIO Modules for a Redis Cluster

Before building the Docker images, you have to configure the JasperReports IO At-Scale modules to use your Redis cluster instead of the built-in Redis module. Edit the following files:

jrio-export-docker/jrio/redis-config.yaml<br>
jrio-manager-docker/jrio/redis-config.yaml<br>
jrio-reporting-docker/jrio/redis-config.yaml<br>
jrio-rest-docker/jrio/WEB-INF/redis-config.yaml

Change the configuration as follows, using the Redis service name and password set in the previous examples:

``` yaml
clusterServersConfig:
 password: "mypassword"
 nodeAddresses:
 - "redis://redis-redis-cluster:6379"
codec: !<org.redisson.codec.SerializationCodec>
```

The Redis service name format is `<cluster-name>-redis-cluster`.

Now you can build the JRIO Docker images and put them into the Docker registry, as described in [Building Docker Images](building_images.md).

## Configuring JRIO Helm Chart for a Redis Cluster

Before deploying your JasperReports IO At-Scale cluster, you must configure its Helm chart to use the Redis cluster. Make sure the jasperreports-io-at-scale-10.1.0/helm/values.yaml file uses the new images built after updating with the Redis cluster service.

Delete the following files that are no longer needed:

jasperreports-io-at-scale-10.1.0/helm/templates/redis-deployment.yaml<br>
jasperreports-io-at-scale-10.1.0/helm/templates/redis-service.yaml

Then edit the following files:

jasperreports-io-at-scale-10.1.0/helm/templates/jrio-manager-deployment.yaml<br>
jasperreports-io-at-scale-10.1.0/helm/templates/jrio-reporting-deployment.yaml<br>
jasperreports-io-at-scale-10.1.0/helm/templates/jrio-export-deployment.yaml<br>
jasperreports-io-at-scale-10.1.0/helm/templates/jrio-rest-deployment.yaml

In each of them, replace the Redis connection and initialization script with the following:

``` yaml
initContainers:
 - name: redis-connection
   image: alpine:3.11.6
   command: ['sh', '-c', "until nc -vz redis-redis-cluster 6379; do echo waiting for redis; sleep 2; done; echo connected to redis"]
```

Now you can proceed with [Configuring the Helm Chart](../configuring/helm_chart.md) and [Deploying a Cluster in AWS EKS](../deploying/intro.md).
