---
title: Configuring Services
description: "Services that are exposed by your cluster must be defined as type LoadBalancer when deployed in the cloud, that is when you have multiple nodes that scale up and down. When deployed in local setups..."
---

# Configuring Services

Services that are exposed by your cluster must be defined as type `LoadBalancer` when deployed in the cloud, that is when you have multiple nodes that scale up and down. When deployed in local setups such as Minikube or when you know the IP address of the node, exposed services must be defined as `NodePort`.

For JasperReports IO At-Scale, there is one service that is potentially exposed in different situations:

-   jrio-rest: Required for a production deployment when using a JasperReports Server repository, because all communication is performed through the REST API.

To expose the jrio-rest module in a production cluster, update the service configuration file jasperreports-io-at-scale-10.1.0/helm/templates/jrio-rest-service.yaml as follows:

``` yaml
apiVersion: v1
kind: Service
metadata:
  name: jrio-rest
  labels:
    jrio.app: jrio-rest
spec:
  type: LoadBalancer [or NodePort for Minikube]
  ports:
  - name: "8080"
    port: {{ default 8080 .Values.jrioRest.servicePort }}
    targetPort: 8080
  selector:
    jrio.app: jrio-rest
```

In this example, port 8080 is the port on which the service will listen for requests.

If you are deploying the demonstration app in the jrio-client module, make the same change to the jasperreports-io-at-scale-10.1.0/helm/templates/jrio-client-service.yaml file.
