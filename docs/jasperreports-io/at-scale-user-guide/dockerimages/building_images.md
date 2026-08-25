---
title: Building Docker Images
description: "After all of your configurations and customizations have been made, you can build Docker images for the modules. Go to the folder where jrio-manager-docker and the other modules are located and run..."
---

# Building Docker Images

After all of your configurations and customizations have been made, you can build Docker images for the modules. Go to the folder where jrio-manager-docker and the other modules are located and run the following commands:

1.  If you have not already done so, install the Docker command-line app to run Docker commands. You can download the Docker app for Mac, Windows, and Linux from <https://docs.docker.com/get-docker/>.
2.  If you plan to use minikube and not the remote Docker registry, before building the images you must proxy all docker commands to the local minikube docker registry with the following:

``` text
eval $(minikube docker-env)
```

1.  Build the docker image for each of the modules. In the following commands, X.X represents a docker image tag according to your own naming scheme, for example `jrio-reporting:3.0` or `jrio-reporting:production2`:

``` text
docker build -t jrio-reporting:X.X ./jrio-reporting-docker
docker build -t jrio-export:X.X ./jrio-export-docker
docker build -t jrio-rest:X.X ./jrio-rest-docker
docker build -t jrio-manager:X.X ./jrio-manager-docker
docker build -t jrio-client:X.X ./jrio-client-docker
```

1.  Verify that all images were built and stored in the local repo:

``` text
docker images | grep jrio
```

When all images have been built, follow the deployment procedures in the next chapter.
