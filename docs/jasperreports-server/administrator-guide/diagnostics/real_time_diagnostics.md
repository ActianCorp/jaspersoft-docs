---
title: Real-Time Diagnostics
description: "JasperReports Server's full instrumentation provides real-time diagnostic information such as memory use, concurrently running reports, cache statistics, and much more. Whereas auditing and..."
---

# Real-Time Diagnostics

JasperReports Server's full instrumentation provides real-time diagnostic information such as memory use, concurrently running reports, cache statistics, and much more. Whereas auditing and monitoring provide a historical record of events on the server, diagnostics display the current status of the server and its Java Virtual Machine (JVM) environment.

For example, you can use the diagnostic information to adjust your JVM settings. This helps to optimize memory based on the size of typical datasets in your Ad Hoc cache. As diagnostic data is available through a Topic, you can create Ad Hoc views. This Ad Hoc view helps you to analyze your server performance and identify performance bottlenecks before they happen.

The diagnostic feature relies on the Java Management Extensions (JMX) industry standard to gather run-time data and expose it to other management interfaces. JasperReports Server implements several JMX elements:

- New JMX-managed beans used to gather and hold diagnostic data such as the number of concurrent reports.
- Its own JMX agent, like a server that responds to JMX requests and exposes the information from the managed beans.
- Connections to existing JMX-managed beans in other components such as Ehcache to include their diagnostic data.
- Connections to other JMX agents such as JVM agent to gather system diagnostics.

For more information about JMX, see <http://docs.oracle.com/javase/tutorial/jmx/>.

There are two ways to use diagnostic data from JasperReports Server:

- If you have an external management console that can connect to a JMX agent, then you can use it to connect to the server's JMX agent. You will probably also want to connect to the JVM's JMX agent. You can then view the real-time diagnostic data from JasperReports Server integrated with the data from your other servers in your management console. Management consoles often offer further functionality like thresholds and alarms you can set on data from any JMX-managed bean.
- We provide a custom data source within the server that collects the same information from the managed beans in the server and in the JVM. You can then create JasperReports that access this data source and present this diagnostic data in a report that suits your needs. We also provide a report and an Ad Hoc Topic to demonstrate this.
