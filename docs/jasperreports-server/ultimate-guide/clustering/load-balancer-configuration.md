---
title: Load Balancer Configuration
description: "This section gives two examples of load balancer configuration, Apache web server (httpd) and HAProxy. These sample configuration files are meant only as examples for testing."
---

# Load Balancer Configuration

This section gives two examples of load balancer configuration, Apache web server (httpd) and HAProxy. These sample configuration files are meant only as examples for testing.

## Apache HTTP Server Example

The following changes configure the [Apache HTTP server](http://httpd.apache.org/) (httpd) as a load balancer.

1.  Add following line to the end of the httpd.conf file:

```
Include conf/mod-jk.conf
```

1.  Create the following two files in the `/conf` folder of your `httpd` server.

- `mod-jk.conf`:

```
# Load mod_jk module
# Specify the filename of the mod_jk lib
LoadModule jk_module modules/mod_jk.so

# Where to find workers.properties
JkWorkersFile conf/workers.properties

# Where to put jk logs
JkLogFile logs/mod_jk.log

# Set the jk log level [debug/error/info]
JkLogLevel info

# Select the log format
JkLogStampFormat "[%a %b %d %H:%M:%S %Y]"

# JkOptions indicates to send SSK KEY SIZE
JkOptions +ForwardKeySize +ForwardURICompat -ForwardDirectories

# JkRequestLogFormat
JkRequestLogFormat "%w %V %T"

# Mount your applications
JkMount /* loadbalancer

# You can use external file for mount points.
# It will be checked for updates each 60 seconds.
# The format of the file is: /url=worker
# /examples/*=loadbalancer
#JkMountFile conf/uriworkermap.properties

# Add shared memory.
# This directive is present with 1.2.10 and
# later versions of mod_jk, and is needed for
# for load balancing to work properly
JkShmFile logs/jk.shm
#JkShmFile /var/log/httpd/mod_jk.shm

# Add jkstatus for managing runtime data
<Location /jkstatus>
 JkMount status
 Order deny,allow

 Allow from all
</Location>
```

- `workers.properties`:

```
# Define list of workers that will be used
# for mapping requests
worker.list=loadbalancer,status

# Define Node1
# modify the host as your host IP or DNS name.
worker.node1.port=8009
worker.node1.host=123.45.6.701
worker.node1.type=ajp13
worker.node1.lbfactor=1

# Define Node2
# modify the host as your host IP or DNS name.
worker.node2.port=8009
worker.node2.host=123.45.6.702
worker.node2.type=ajp13
worker.node2.lbfactor=1

# Load-balancing behaviour
worker.loadbalancer.type=lb
worker.loadbalancer.balance_workers=node1,node2
worker.loadbalancer.sticky_session=1
#worker.list=loadbalancer

# Status worker for managing load balancer
worker.status.type=status
```

## HAProxy Load Balancer Example

The following example is a configuration for the [HAProxy](http://www.haproxy.org/) load balancer. HAProxy is a high-performance, free and open source load balancer for Linux/x86 and Solaris/Sparc.

Edit the `/etc/haproxy.cfg` file as follows:

```
global
        log         127.0.0.1 local2 debug #log using syslog service on localhost
        maxconn     4096 # Total Max Connections. This is dependent on ulimit
        daemon

defaults
        mode        http
        maxconn     4096
        clitimeout  60000
        srvtimeout  30000
        contimeout  4000
        option      httpclose # Disable Keepalive
        log         global
        option      httplog

listen  farm 123.45.6.700:80
        mode http
        stats uri /haproxy #show haproxy colsole
        balance roundrobin
        cookie farmID insert #assign a farmID coockie to each client
        option httpclose
        option httpchk
        option forwardfor

        ## Define your servers to balance
        server node1 123.45.6.701:8081 cookie farmID_node1 check
        server node2 123.45.6.702:8081 cookie farmID_node2 check
```

## Troubleshooting

In some cases, when you are using a proxy or load balancer, your users may have problems with loading links and other resource files in hypermedia documents. This can occur when JasperReports Server generates links to a specific node instead of the host server.

For example, suppose you have a setup with a proxy host and two servers as follows:

|            |                                    |
|------------|------------------------------------|
| proxy_host | http://bi.example.com              |
| node 1     | http://node1:8080/jasperserver-pro |
| node 2     | http://node2:8080/jasperserver-pro |

When the user accesses http://bi.example.com, JasperReports Server forwards the user to the login page on the first available node, http://node1:8080/jasperserver-pro. After login, when the user accesses hypermedia, JasperReports Server generates links to hypermedia resources using the base http://node1:8080/jasperserver-pro instead of http://bi.example.com.

To resolve this, set the following in the /WEB-INF/js.config.properties file on all nodes:

deploy.base.url=http://bi.example.com
