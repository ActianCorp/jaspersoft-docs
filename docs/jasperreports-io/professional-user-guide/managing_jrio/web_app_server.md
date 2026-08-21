---
title: Web Application Server
description: The JasperReports IO reporting service is deployed in a Java web application on an Eclipse Jetty web server included with JasperReports IO. You can create a web application with interactive reports...
---

# Web Application Server

The JasperReports IO reporting service is deployed in a Java web application on an Eclipse Jetty web server included with JasperReports IO. You can create a web application with interactive reports and the web application server handle all HTTP requests from users. The web application server is located in the `<jrio-install>/jetty` directory. For information on the Eclipse Jetty web server, see the [Jetty documentation](https://www.eclipse.org/jetty/documentation/current/).

On JasperReports IO, there are two scripts in the `<jrio-install>` directory to start and stop the Eclipse Jetty server and the JasperReports IO reporting service. The script to start the web application server is `start.bat` for Windows and `start.sh` for Mac OS and Linux, and the stop script is `stop.bat` for Windows and `stop.sh` for Mac OS and Linux.

## Configuring the Web Application Server

The start script specifies several startup configuration parameters for the server that can be changed to better suit your needs.

### Java Virtual Machine Heap Memory

There are two parameters for specifying the amount of heap memory allocated to the JasperReports IO reporting service's Java web application when it starts up. The `-Xms<size>` parameter specifies the initial heap memory size for the web application and the `-Xmx<size>` parameter specifies the maximum heap memory size. The following examples show an initial heap memory size of 256 MB and a maximum size of 512 MB:

**Linux:** `./jre/bin/java -Xms256m -Xmx512m -jar ./jetty/start.jar`

**Windows:** `jre\bin\java -Xms256m -Xmx512m -jar jetty\start.jar`

**Mac OS:** `./jre/Contents/Home/bin/java -Xms256m -Xmx512m -jar ./jetty/start.jar`

### Web Application Server Port

By default, the web application server starts on port 8080, but if this port is already in use on your host machine, you can edit the start script to change the following setting to another port number:

`-Djetty.http.port=8080`

### Web Application Server Stop Port and Stop Key

The start and stop scripts define the stop port and stop key settings required for stopping the web application server. The stop port is the number of the port on the host machine that listens for termination requests and the stop key is a key that must be the port of the stop request. These settings must match in both scripts for the web application server to shut down properly. The following is an example of the stop port and key settings:

`-DSTOP.PORT=8989 -DSTOP.KEY=st0p_J3Tty`

## Web Application

When the web application server is running, the user's web browser accesses the HTML files in the `<jrio-install>/repository/ROOT` folder when they open `http://<jrio>:8080` in their browser. You can store the files for your web application in this folder or create an `index.html` file to redirect the user's browser to a web application in another directory. For example, the sample `index.html` in the directory that was created during installation redirects the user's browser to `http://<jrio>:8080/jrio-docs`, where the sample web application that comes with JasperReports IO is installed.
