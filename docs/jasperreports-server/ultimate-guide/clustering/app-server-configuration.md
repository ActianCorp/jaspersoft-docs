---
title: Sample Configurations
description: "The app server usually manages the user session for a web application and is responsible for the policies that allow the session to be replicated in a cluster environment. However, you must also..."
---

# Sample Configurations

The app server usually manages the user session for a web application and is responsible for the policies that allow the session to be replicated in a cluster environment. However, you must also configure parts of JasperReports Server for repository and session replication, including the Ehcache component.

!!! note

    This section describes how to configure JasperReports Server for session replication. To configure your application server, see the documentation for your application server. For additional information, see the "Configuration for Session Persistence" section in the JasperReports Server Administrator Guide.

This section describes two levels of replication for JasperReports Server:

-   Ehcache replication only: The repository cache handles the folder structure and saved reports, and speeds up repository access in a given instance of JasperReports Server. Changes to permissions and folders are cached on the server where they occur, but they can take one to two minutes to be written to the repository database. To maintain performance and avoid collisions, you should configure Ehcache replication whenever you have multiple JasperReports Server instances that share a single repository. Ehchache replication can be configured independently of session replication.

-   Partial session replication for failover: Partial session replication shares, based on Ehcache replication, shares additional information about the logged-in users and allows for failover without requiring re-authentication. If you configure this, you must first configure Ehcache replication.

## EhCache Replication

The repository cache in JasperReports Server is implemented internally via the Ehcache component. Edit the Ehcache configuration files as described below to replicate the repository cache among all instances that share a single repository. You do not have to configure a cluster for cache replication.

There are several replication mechanisms available:

-   Remote Method Invocation (RMI): The simplest and fastest cache distribution mechanism. Use RMI distribution if your cluster runs on your own real or virtual computers, as long as their addresses will not change. You cannot use RMI distribution if your cluster is hosted in a cloud, such as with Amazon Redshift, because the IP addresses of the nodes may change. RMI distribution relies on IP multicast, which you must set up.

-   Java Message Services (JMS): It can provide cache distribution for nodes in a cloud where IP addresses may change. Jaspersoft provides a configuration for using the [Apache ActiveMQ JMS Server](http://activemq.apache.org/). You must first install and configure ActiveMQ on one of the computers in your cluster.

On each node, you must edit the following cache configuration files. Make sure to uncomment only one of the options provided in each file:

-   Ehcache for Hibernate: Edit the `/WEB-INF/classes/ehcache_hibernate.xml` file. (Once the file is fully configured, copy it to `/WEB-INF/ehcache_hibernate.xml`.)

-   Ehcache: Edit the `<web-app>/WEB-INF/ehcache.xml` file.

    To configure JasperReports Server nodes for repository cache replication

    1.  If you are using RMI distribution, you must make sure that the subnet that contains all the nodes is configured to allow IP multicasting.

    2.  For all distribution mechanisms, comment out the section marked "NO CLUSTERING" in both files as follows. By default, this section is uncommented. For example, in the ehcache_hibernate.xml, comment out the "NO CLUSTERING" section as follows:

        ``` text
        <!-- *********************   NO CLUSTERING   ******************** -->
            <!-- START
            <cache name="defaultRepoCache"
                maxElementsInMemory="100000"
                statistics="false"
                eternal="true"
                overflowToDisk="false"
                timeToIdleSeconds="36000"
                timeToLiveSeconds="180000"
                diskExpiryThreadIntervalSeconds="120"
                diskPersistent="false"/>
            END -->
        <!-- ******************* END of NO CLUSTERING ******************* -->
        ```

    3.  (RMI only) To configure the nodes for RMI distribution:

        1.  Uncomment the RMI section in `<web-app>/WEB-INF/classes/ehcache_hibernate.xml` and `<web-app>/WEB-INF/ehcache.xml` on each node.
        2.  Set the RMI properties for your IP multicast.
        3.  Configure `CacheManagerPeerListenerFactory` with different ports in `<web-app>/WEB-INF/classes/ehcache_hibernate.xml` and `<web-app>/WEB-INF/ehcache.xml`. The port should be the same across all nodes. For example, you might set the `port` property as follows:

    -   `port=40001` in `<web-app>/WEB-INF/classes/ehcache_hibernate.xml` on all nodes

        -   `port=40011` in `<web-app>/WEB-INF/ehcache.xml` on all nodes

            1.  You must also add the hostname property with the value of the real IP address, in this example, 123.45.6.701. Add the `hostName` property to the `cacheManagerPeerListenerFactory`, right before the `port`. This specifies the real IP address of the host, as shown in the example above.

                The following example shows the beginning of the RMI section of one of the files:

                ``` text
                <!-- ======== RMI ======  -->
                   <cacheManagerPeerProviderFactory
                        class="net.sf.ehcache.distribution.RMICacheManagerPeerProviderFactory"
                        properties="peerDiscovery=automatic,multicastGroupAddress=228.0.0.1,
                        multicastGroupPort=4446,timeToLive=32"/>
                    <cacheManagerPeerListenerFactory
                        class="net.sf.ehcache.distribution.RMICacheManagerPeerListenerFactory"
                        properties="hostName=123.45.6.701,port=40001,socketTimeoutMillis=120000"/>

                    ...

                <!-- ========= END OF RMI ======= -->
                ```

            2.  (JMS only) For JMS distribution:

                1.  Install the JMS server on one computer in your cluster.
                2.  Uncomment the JMS section in `<web-app>/WEB-INF/classes/ehcache_hibernate.xml` and `<web-app>/WEB-INF/ehcache.xml` on each node.
                3.  Set the `providerURL` properties in both files to the address of your JMS server, for example 123.45.6.701. There are several `providerURL` properties to set in each file, only the first one is shown in the code example below.
                4.  If you do not use the default values for `replicationTopicBindingName` and `topicBindingName`, make sure that these names are different for the two different files.

            For example, you might set these properties as follows:

        -   `myName1` in `<web-app>/WEB-INF/classes/ehcache_hibernate.xml` on all nodes.

        -   `myName2` in `<web-app>/WEB-INF/ehcache.xml` on all nodes.

``` text
<!-- ========= JMS =============  -->

    <cacheManagerPeerProviderFactory
        class="net.sf.ehcache.distribution.jms.JMSCacheManagerPeerProviderFactory"
        properties="initialContextFactoryName=com.jaspersoft.jasperserver.api.
        engine.replication.JRSActiveMQInitialContextFactory,
        providerURL=tcp://123.45.6.701:61616,
        replicationTopicConnectionFactoryBindingName=topicConnectionFactory,
        replicationTopicBindingName=ehcacheAcl,
        getQueueConnectionFactoryBindingName=queueConnectionFactory,
        getQueueBindingName=ehcacheQueueAcl,
        topicConnectionFactoryBindingName=topicConnectionFactory,
        topicBindingName=ehcacheAcl"
        propertySeparator=","/>


   ...

<!-- ======= END OF JMS ======= -->
```

1.  On each node, edit the file `<web-app>/META-INF/context.xml`. Locate the `Manager pathname` near the end, and comment it out as follows:

    ``` text
      <!-- <Manager pathname="" />  -->
    ```

2.  Copy the correctly configured `<web-app>/WEB-INF/classes/ehcache_hibernate.xml` file to `<web-app>/WEB-INF/ehcache_hibernate.xml` on each node.

3.  If you are only configuring cache replication, restart or redeploy JasperReports Server on each node. If you also want partial session replication, complete the additional configurations below before restarting.

## Additional Configurations for Partial Session Replication

If you want to configure partial session replication/failover, first set up repository cache replication as described in [Repository Cache Replication](#ehcache-replication), then make the additional changes described in this section.

On each node, edit *all* of the following three files as described below for your chosen distribution mechanism. You should make the same additional changes in all of them. Make sure to uncomment only one of the options provided in each file:

-   `<web-app>/WEB-INF/ehcache_hibernate.xml`
-   `<web-app>/WEB-INF/classes/ehcache_hibernate.xml`
-   `<web-app>/WEB-INF/ehcache.xml`

!!! note

    Partial session replication, which is based on UDP (User Datagram Protocol), is not available for Amazon Web Services.

To configure JasperReports Server nodes for partial session replication

1.  Make sure that the subnet that contains all the cluster nodes is configured to allow IP multicasting. This is usually required by the app server for replication, and it's also required by JasperReports Server's Ehcache component when using RMI distribution in a cluster environment.

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

3.  On each node of the cluster, enable session replication in your app server or web container. For example, to enable session replication on Apache Tomcat 9.x, edit the file `<tomcat>/conf/server.xml` as follows.

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
