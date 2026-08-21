---
title: Software Configuration
description: "Once you have the server hardware to handle your user load, you need to determine the optimal software configuration for your nodes. This includes:"
---

# Software Configuration

Once you have the server hardware to handle your user load, you need to determine the optimal software configuration for your nodes. This includes:

- JVM settings to optimize processor and memory use.

- Application server settings, mostly to provide connection pooling.

- JasperReports Server settings.

Server settings can help optimize performance based on the types and number of reports that you expect users to run:

- Data policies in Ad Hoc can help speed up Domain-based reports

- Cache settings in Ad Hoc can boost performance when there are many users accessing the same data.

- Query limits (for Ad Hoc reports and for JasperReports) can help prevent slow responses when users request huge data sets during peak times.

- Custom virtualization settings can help servers deal with large reports (greater than 300 pages).

For JVM setting to optimize performance, see the JasperReports Server Installation Guide. For details about query limits, data policies, and cache settings, see the chapter on configuration in the JasperReports Server Administrator Guide.

Also turning off features such as auditing and logging can improve performance in highly-loaded machines. For more information, see the chapter on server diagnostics in the JasperReports Server Administrator Guide.
