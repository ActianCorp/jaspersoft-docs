---
title: Docker Configuration
description: The first step of installing the Scalable Query Engine is to configure and build the Docker images of the worker pods.
---

# Docker Configuration

The first step of installing the Scalable Query Engine is to configure and build the Docker images of the worker pods.

In the git project, jaspersoft-containers/Docker/scalableQueryEngine/ contains the following files and folders:

| File or Folder | Description |
|----|----|
| `Dockerfile` | The main installation script for the Scalable Query Engine. |
| `.env` | Environment variables for building the Docker images, see the next section. |
| `Dockerfile.drivers` | Script that copies the supported JDBC Drivers from JasperReports Server to the Scalable Query Engine. |
| `docker-compose.yaml` | Compose file to orchestrate the Scalable Query Engine, its drivers, and the redis services. |
| `scripts` | Folder containing scripts for the Scalable Query Engine. |
| `resources/drivers` | Folder created by scripts with a copy of the JDBC drivers. |
| `resources/keystore` | Folder where you place a copy of the JasperReports Server keystore. |
| `resources/properties` | Folder containing properties files for the Scalable Query Engine. |

## Configuring the Docker Images

Before building the Docker images, edit the .env file to specify the following properties:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>JASPERREPORTS_SERVER_</code><br />
<code>VERSION</code></p></td>
<td><p>JasperReports Server release version (must be 10.1.0 or higher).</p></td>
</tr>
<tr>
<td><p><code>SCALABLE_QUERY_ENGINE_</code><br />
<code>IMAGE_NAME</code></p></td>
<td><p>Name for the Docker image, <code>scalable-query-engine</code> by default.</p></td>
</tr>
<tr>
<td><p><code>SCALABLE_QUERY_ENGINE_</code><br />
<code>DRIVER_IMAGE_NAME</code></p></td>
<td><p>Name for the JDBC drivers Docker image, <code>scalable-adhoc-drivers</code> by default.</p></td>
</tr>
<tr>
<td><p><code>SCALABLE_QUERY_ENGINE_DRIVER_IMAGE_TAG</code></p></td>
<td><p>Docker tag for the Scalable Query Engine image, 10.1.0 by default.</p></td>
</tr>
<tr>
<td><p><code>SCALABLE_QUERY_ENGINE_IMAGE_TAG</code></p></td>
<td><p>Docker tag for the Scalable Query Engine Drivers image, 10.1.0 by default.</p></td>
</tr>
<tr>
<td><p><code>JDK_BASE_IMAGE</code></p></td>
<td><p>Docker image certified for the version of JasperReports Server being deployed, either <code>eclipse-temurin:17-jdk-noble </code>for Ubuntu or <code>amazoncorretto:17-al2023-jdk</code> for Amazon Linux 2023</p></td>
</tr>
<tr>
<td><p><code>ks</code></p></td>
<td><p>Path to the server's <code>.jrsks</code> keystore file, usually <code>/etc/secrets/keystore</code>.</p></td>
</tr>
<tr>
<td><p><code>ksp</code></p></td>
<td><p>Path to the server's <code>.jrsksp</code> keystore properties file, usually <code>/etc/secrets/keystore</code>.</p></td>
</tr>
<tr>
<td><p><code>RELEASE_DATE</code></p></td>
<td><p>Release date of the JasperReports Server version, for example Month-Day, Year when using 10.1.0.</p></td>
</tr>
</tbody>
</table>

## Building the Docker Images

The recommended way to build the Docker images for the Scalable Query Engine is to use `docker-compose` command as follows:

```
cd <js-install>/jaspersoft-containers/Docker/scalableQueryEngine
docker-compose build
```

If there is an error such as "requested access to the resource is denied," then run the following commands:

```
sudo gpasswd -a $USER docker
newgrp docker
```

Alternatively, you can also build the Docker images with the following commands:

```
cd <js-install>
docker build -t scalable-query-engine:<docker-tag>
             -f jaspersoft-containers/Docker/scalableQueryEngine/Dockerfile .
docker build -t scalable-query-engine-drivers:<drivers-tag>
             -f jaspersoft-containers/Docker/scalableQueryEngine/Dockerfile.drivers .
```

## Deploying with Docker Alone (Optional)

If you want to install the Ad Hoc worker with Docker alone, the deployment is simpler, but you do not have the advantages of a cluster managed through Kubernetes. If you want to deploy with Kubernetes and Helm charts, skip this section and go to [Deploying on Kubernetes](kubernetes.md).

1.  Edit the file `docker/application.properties` to make any necessary configuration. In particular, any JNDI data source to be used in Ad Hoc views and reports needs to be configured in this properties file.

<!-- -->

1.  Copy your server's keystore and keystore properties files to `<js-install>/jaspersoft-containers/Docker/scalableQueryEngine/resources/keystore`. The keystore files must be same that JasperReports® Server used when creating its repository database.

2.  Navigate to the `<js-install>` directory and run the following command:

    ``` text
    docker network create jrs_default
    docker-compose up -d scalable-query-engine
    ```

    You can check that the worker is running at:

    `<worker_ip>:8081/actuator/health.`

3.  Configure your JasperReports Server instance as described in [Configuring JasperReports Server](configuring_jrs.md), then restart your server.

    Once your server and query engine are running, you can test a dashboard that contains an Ad Hoc view. After it runs, you can check the worker logs with the following command on the server:

    ``` text
    docker logs scalable-query-engine/8.0.0
    ```
