---
title: Sample Configurations
description: "The app server usually manages the user session for a web application and is responsible for the policies that allow the session to be replicated in a cluster environment. However, you must also..."
---

# Sample Configurations

The app server usually manages the user session for a web application and is responsible for the policies that allow the session to be replicated in a cluster environment. However, you must also configure parts of JasperReports Server for repository and session replication, including the Infinispan component.

!!! note

    This section describes how to configure JasperReports Server for session replication. To configure your application server, see the documentation for your application server. For additional information, see the "Configuration for Session Persistence" section in the JasperReports Server Administrator Guide.

This section describes two levels of replication for JasperReports Server:

-   Infinispan replication only: The repository cache handles the folder structure and saved reports, and speeds up repository access in a given instance of JasperReports Server. Changes to permissions and folders are cached on the server where they occur, but they can take one to two minutes to be written to the repository database. To maintain performance and avoid collisions, you should configure Infinispan replication whenever you have multiple JasperReports Server instances that share a single repository. Infinispan replication can be configured independently of session replication.

-   Partial session replication for failover: Partial session replication shares, based on Infinispan replication, shares additional information about the logged-in users and allows for failover without requiring re-authentication. If you configure this, you must first configure Infinispan replication.

## Infinispan Replication

The repository cache in JasperReports Server is implemented internally via Infinispan. Infinispan uses JGroups as its cluster transport layer to replicate the repository cache among all instances that share a single repository. You do not have to configure a separate broker or message server for cache replication.

### To configure JasperReports Server nodes for repository cache replication

#### Scenario A
This recommended path is used for a fresh JasperReports Server installation on each cluster node. The buildomatic tool automatically places all required Infinispan and JGroups files.

1 - Edit the `default_master.properties` file.
  
   a. Open `<js-install>/buildomatic/default_master.properties`.
   b. Set Enable clustered Infinispan cache:
    ``` text
    appCacheType=infinispan-embedded
    networkType=tcp
    ```
2 - Run `gen-config`.

From the buildomatic directory, run `./js-ant.sh clean-config gen-config`.

This command reads `default_master.properties` and generates all configuration files, including:

  - Placing Infinispan XML files into `WEB-INF/`.
  - Placing JGroups XML files into `WEB-INF/classes/`.
  - Resolving the `${infinispan.application.main.network.cfg.path}` and related placeholders in the Infinispan config files to point to the correct JGroups stack file `(jgroups-tcp.xml)` based on the `networkType` value.
  
3 - Configure JGroups

After `gen-config`, open each JGroups configuration file in `<webapp>/WEB-INF/classes/`. The files are:

  - `jgroups-tcp.xml`
  - `jgroups-hibernate-main-tcp.xml`
  - `jgroups-hibernate-audit-tcp.xml`
  - `jgroups-hibernate-profiling-tcp.xml`
  
In each file, locate the JS_JDBC_PING element and verify the `datasource_jndi_name` matches your `Tomcat/application` server JNDI datasource name. The default value is `jdbc/jasperserver`.

  ```
   <com.jaspersoft.ji.cache.JS_JDBC_PING
   datasource_jndi_name="jdbc/jasperserver"
   info_writer_sleep_time="1000"
   info_writer_max_writes_after_view="3"
   remove_all_data_on_view_change="false"/>
    ```

If your JNDI name differs, update it in all four files.
JasperReports Server uses a custom `JS_JDBC_PING` protocol (an extended version of JGroups standard JDBC_PING). Each node writes its address into the shared database on startup and reads the addresses of other nodes from the same table. This enables automatic node discovery without multicast or static IP lists.

4 - Configure bind address and port (if needed).

By default, JGroups auto-detects the bind address by checking network interfaces in order: `eth1, eth0, en0,` and finally any `SITE_LOCAL` address.

The default bind ports in Jgroup files are 7800, 7810, 7820 and 7830.

Ensure port 7800, 7810, 7820, and 7830 (or your chosen ports) is open in firewall rules between all cluster nodes.

5 -  Repeat on each node.

Perform steps 1 through 4 on each cluster node. The `dbHost` and `appCacheType` must be identical on all nodes.

6 - Start the cluster.

Start Tomcat on each node sequentially. 
On startup, each node registers itself in the
shared database via `JS_JDBC_PING` and joins the Infinispan cluster.

#### Scenario B - Existing Installation
Use this path when JasperReports Server is already deployed and running. Run the `cleanconfig` 
and `gen-config` commands to overwrite your existing WEB-INF configuration. To avoid this, manually copy only the Infinispan and JGroups files.

1 - Copy Infinispan config files to `<webapp>/WEB-INF/`.
Copy the following files from the buildomatic source to `<webapp>/WEB-INF/`:

Source: `<js-install>/buildomatic/conf_source/cache/infinispanembedded/`

Destination: `<webapp>/WEB-INF/`

Files to copy:
```
data-snapshots-infinispan-configs.xml
local-only-infinispan-configs.xml
main-infinispan-configs.xml
```
Destination: `<webapp>/WEB-INF/`
    

2 - Copy JGroups and Infinispan files to `<webapp>/WEB-INF/classes/`.

Copy the following files from the buildomatic source to `<webapp>/WEB-INF/classes/`:

Source: `<js-install>/buildomatic/conf_source/cache/infinispanembedded/`

Destination: `<webapp>/WEB-INF/classes/`

Files to copy:
```
audit-hibernate-infinispan-configs.xml
hibernate-infinispan-configs.xml
jgroups-hibernate-audit-tcp.xml
jgroups-hibernate-main-tcp.xml
jgroups-hibernate-profiling-tcp.xml
jgroups-tcp.xml
profiling-hibernate-infinispan-configs.xml
```
Destination: `<webapp>/WEB-INF/classes/`   

3 - Resolve JGroups stack-file paths in Infinispan config files.

When `gen-config` is NOT run, the placeholder variables in the Infinispan config files are NOT resolved automatically. You must replace them manually with the literal JGroups filename.

Open each of the following listed files and replace the placeholder with the actual JGroups filename as shown:

 a - `WEB-INF/main-infinispan-configs.xml`

Replace: `<stack-file name="app-jgroups"
path="${infinispan.application.main.network.cfg.path}"/>`
With: `<stack-file name="app-jgroups" path="jgroups-tcp.xml"/>`

 b - `WEB-INF/classes/audit-hibernate-infinispan-configs.xml`

Replace: `<stack-file name="hibernate-jgroups"
path="${infinispan.hibernate.audit.network.cfg.path}"/>`

With: `<stack-file name="hibernate-jgroups" path="jgroups-hibernate-audittcp.xml"/>`

 c - `WEB-INF/classes/hibernate-infinispan-configs.xml`

Replace: `<stack-file name="hibernate-jgroups"
path="${infinispan.hibernate.main.network.cfg.path}"/>`

With: `<stack-file name="hibernate-jgroups" path="jgroups-hibernate-maintcp.xml"/>`

d - `WEB-INF/classes/profiling-hibernate-infinispan-configs.xml`

Replace: `<stack-file name="hibernate-jgroups"
path="${infinispan.hibernate.profiling.network.cfg.path}"/>`

With: `<stack-file name="hibernate-jgroups" path="jgroups-hibernate-profiling-tcp.xml"/>`

The resulting JGroups sections appears as follows:

 -   `main-infinispan-configs.xml:`:

    ```
    <jgroups>
         <stack-file name="app-jgroups"path="jgroups-tcp.xml"/>
    </jgroups>
    ```
-   `audit-hibernate-infinispan-configs.xml:`:

    ```
    <jgroups>
         <stack-file name="hibernate-jgroups" path="jgroupshibernate-audit-tcp.xml"/>
    </jgroups>
    ```

-   `hibernate-infinispan-configs.xml:`:

    ```
    <jgroups>
         <stack-file name="hibernate-jgroups" path="jgroupshibernate-main-tcp.xml"/>
    </jgroups>
    ```
    -   `profiling-hibernate-infinispan-configs.xml:`:

    ```
    <jgroups>
         <stack-file name="hibernate-jgroups" path="jgroupshibernate-profiling-tcp.xml"/>
    </jgroups>
    ```

4 - Configure datasource_jndi_name in all JGroups files.

In each of the four JGroups XML files in `WEB-INF/classes/`, verify that `<datasource_jndi_name>` matches your JNDI datasource name:
```
jgroups-tcp.xml
jgroups-hibernate-main-tcp.xml
jgroups-hibernate-audit-tcp.xml
jgroups-hibernate-profiling-tcp.xml
```
Each file contains:
```
<com.jaspersoft.ji.cache.JS_JDBC_PING
    datasource_jndi_name="jdbc/jasperserver"
    .../>
```
If your JNDI datasource name is different, update it in all four files.

5 - Configure bind address and port.

Follow the steps in Scenario A, step 4, Configure bind address and port [Scenario A](#scenario-a) (if needed).
Repeat on each node.

Perform steps 1 through 5 on every cluster node. All nodes must have identical
Infinispan and JGroups configuration files.

6 - Start the cluster.

#####JGroups Configuration
All JGroups configuration files follow the same structure. Following are the key configurable elements:

-  Transport protocol (TCP)

    ```
    <TCP bind_addr="${JGROUPS_BIND_ADDR:match-interface:eth1,matchinterface: eth0,match-interface:en0,SITE_LOCAL}" bind_port="${JGROUPS_BIND_PORT:7800}"/>
    ```

    **Description:**

    -    `<bind_addr>`: The IP address this node listens on for cluster communication. Default auto-detects by trying eth1, eth0, en0, then any site-local address.

    -   `<bind_port>`: The TCP port for JGroups. Must be open in the firewall between all cluster nodes.

- Node discovery via shared database table (JS_JDBC_PING)

    ```
    <com.jaspersoft.ji.cache.JS_JDBC_PING
        datasource_jndi_name="jdbc/jasperserver"
        info_writer_sleep_time="1000"
        info_writer_max_writes_after_view="3"
        remove_all_data_on_view_change="false"/>
    ```
   **Description:**
    -    `<datasource_jndi_name>`: Specifies the JNDI name for the JasperReports Server database connection pool, which must match the datasource configured in Tomcat's `context.xml`. Cluster nodes use this shared database connection to discover each other by reading and writing to a shared database table.

    -   `info_writer_sleep_time`: Defines the frequency, in milliseconds, at which the cluster node writes its active status to the database. The default value is 1000ms.
    - `<remove_all_data_on_view_change>`: When enabled (`true`), automatically clears the cluster discovery table whenever a node joins or leaves the cluster. Leave this set to `false` unless explicitly instructed otherwise.

#####File Reference Summary
- Files in `WEB-INF/` (Infinispan application cache):

    - `main-infinispan-configs.xml`: Main app cache (ACL, engine, AdHoc, and so on)
    - `local-only-infinispan-configs.xml`: Local-only caches (not replicated)
    - `data-snapshots-infinispan-configs.xml`: Data snapshot cache
- Files in `WEB-INF/classes/` (JGroups stacks and Hibernate caches):
    - `jgroups-tcp.xml`: JGroups TCP stack for main app cache
    - `jgroups-hibernate-main-tcp.xml`: JGroups TCP stack for main Hibernate cache
    - `jgroups-hibernate-audit-tcp.xml`: JGroups TCP stack for audit Hibernate cache
    - `jgroups-hibernate-profiling-tcp.xml`: JGroups TCP stack for profiling Hibernate cache
    - `hibernate-infinispan-configs.xml`: Hibernate L2 cache config (main)
    - `audit-hibernate-infinispan-configs.xml`: Hibernate L2 cache config (audit)
    - `profiling-hibernate-infinispan-configs.xml` : Hibernate L2 cache config (profiling)

## Additional Configurations for Partial Session Replication

If you want to configure partial session replication/failover, first set up repository cache replication as described in [Repository Cache Replication](#infinispan-replication), then make the additional changes described in this section.


!!! note

    Partial session replication, which is based on UDP (User Datagram Protocol), is not available for Amazon Web Services.

To configure JasperReports Server nodes for partial session replication

1.  Make sure that the subnet that contains all the cluster nodes is configured to allow IP multicasting. This is usually required by the app server for replication.

2.  On each node of the cluster, edit the file `<web-app>/WEB-INF/web.xml` to make the following changes:

    1.  Locate the `ClusterFilter` that's given in comments and uncomment it as follows:

        ``` xml
            <filter>
                <filter-name>ClusterFilter</filter-name>
                <filter-class>com.jaspersoft.jasperserver.war.TolerantSessionFilter</filter-class>
            </filter>
        ```

    2.  Locate the corresponding mapping for the `ClusterFilter` and uncomment it as well. You must also uncomment the `<distributable>` element.

        ``` xml
            <filter-mapping>
                <filter-name>ClusterFilter</filter-name>
                <url-pattern>/*</url-pattern>
            </filter-mapping>
            <distributable/>
        ```

3.  On each node of the cluster, enable session replication in your app server or web container. For example, to enable session replication on Apache Tomcat 9.x, edit the `<tomcat>/conf/server.xml` file as follows.

    Add the `Cluster` definition within the `<Engine name="Catalina" defaultHost="localhost">` configuration. In this example, 123.45.6.701 is the IP address of the node being configured. This example uses Delta Manager, but you can also use Backup Manager:

    ``` xml
    <Cluster className="org.apache.catalina.ha.tcp.SimpleTcpCluster"
             channelSendOptions="8">
        <Manager className="org.apache.catalina.ha.session.DeltaManager"
                 expireSessionsOnShutdown="false"
                 notifyListenersOnReplication="true"/>
    <Channel className="org.apache.catalina.tribes.group.GroupChannel">
            <Membership className="org.apache.catalina.tribes.membership.
                McastService"
                        address="228.0.0.4"
                        port="45564" frequency="500"
                        dropTime="3000"/>
            <Sender className="org.apache.catalina.tribes.transport.
                ReplicationTransmitter">
                <Transport className="org.apache.catalina.tribes.
                    transport.nio.PooledParallelSender"/>
            </Sender>
            <Receiver className="org.apache.catalina.tribes.transport.
                nio.NioReceiver"
                      address="123.45.6.701" port="4000" autoBind="100"
                      selectorTimeout="5000" maxThreads="6"/>
            <Interceptor className="org.apache.catalina.tribes.group.
                interceptors.TcpFailureDetector"/>
            <Interceptor className="org.apache.catalina.tribes.group.
                interceptors.MessageDispatch15Interceptor"/>
        </Channel>

    <!--<Valve className="org.apache.catalina.ha.tcp.ForceReplicationValve"/>-->
        <Valve className="org.apache.catalina.ha.tcp.ReplicationValve" filter=""/>
        <Valve className="org.apache.catalina.ha.session.JvmRouteBinderValve"/>
        <ClusterListener className="org.apache.catalina.ha.session.ClusterSessionListener"/>
    </Cluster>
    ```

4.  Restart or redeploy JasperReports Server on each node.
