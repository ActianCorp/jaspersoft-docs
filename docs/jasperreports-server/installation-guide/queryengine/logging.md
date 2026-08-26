---
title: Logging and Debugging
description: There are several ways to collect and analyze logs from the Ad Hoc workers running in Kubernetes. These logs are useful in case certain Ad Hoc views are causing errors. Setting log levels and...
---

# Logging and Debugging

There are several ways to collect and analyze logs from the Ad Hoc workers running in Kubernetes. These logs are useful in case certain Ad Hoc views are causing errors. Setting log levels and searching for log messages can help debug the cause.

Log levels using Log4j2 can be set in values.yaml or using the following command line:

``` text
helm --set logging.level=DEBUG
```

## Aggregate to File

The scalable query engine can use Fluentd to collect logs from all running workers and make them available on the machine where JasperReports Server is running. By default, the scalable query engine uses one `fluentd` instance per physical node (or virtual machine) for collecting log messages in text format from the workers in Kubernetes. There are then two possible ways to access the logs:

-   Fluentbit on each physical node or VM forwards text logs to the Fluentd aggregator, and aggregate logs can be viewed on the same machine as JasperReports Server.

-   Fluentbit is set to JSON format on each physical node or VM and accessed directly by Elasticsearch and Kibana (ELK) to view logs. Alternatively, you can use ELK to view the aggregate text log file in the first case.

First you should download the Fluentd package with the following commands:

``` text
git clone <br>
  --depth 1 <br>
  --filter=blob:none <br>
  --no-checkout <br>
  https://github.com/fluent/fluentd-kubernetes-daemonset/tree/master/docker-image/v1.11/debian-s3  <br>
;
mv debian-s3 docker-fluentd-file
cd docker-fluentd-file
git checkout master -- d1
```

To enable the Fluentd aggregator set `logging.enabled=true` and configure the `fluentd.*` properties in values.yaml.

## Elasticsearch Kibana (ELK)

Elasticsearch is an analytics engine from distributed sources, Kibana is a graphing package for Elasticsearch, and together they can be used to access logs from the Ad Hoc workers.

Jaspersoft does not support for Elasticsearch and Kibana, only a basic configuration for demonstration and a collector (Fluentd).

1.  Configure the `elasticsearch.*` properties in values.yaml.

2.  Install Kibana with the following command:

    ``` text
    helm install kibana elastic/kibana --set service.type=NodePort --set resources.requests.memory=1Gi
    ```

    Note that the resources value (1Gi) is an example that should be modified for your own usage. The Kibana index pattern is `scalable-adhoc-<ReleaseName>-*`, where &lt;ReleaseName&gt; is the helm release name.

3.  The default output format is text. If you want to log directly to ELK, you can set the output format to JSON with the following helm setting:

`--set logging.layout=json`

Depending on the log driver being used, JSON output may require you to configure merging and indexing on Kubernetes. It is also possible to use ELK for the visualization of text output from the Fluentd aggregator.

The JSON output may require you to configure merging and indexing on K8s (depending on the log driver used). The main use case would be to configure the Scalable Query Engine to log directly to ELK. For more information, see <https://docs.fluentbit.io/manual/pipeline/outputs>.
