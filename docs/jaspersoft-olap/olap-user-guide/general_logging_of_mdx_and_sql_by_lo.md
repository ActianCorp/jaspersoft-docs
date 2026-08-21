---
title: General Logging of MDX and SQL by log4j
description: Jaspersoft OLAP’s fundamental logging is controlled through log4j settings. log4j’s statement logging occurs in the mondrian.mdx and mondrian.sql log4j categories. These categories log the statements...
---

# General Logging of MDX and SQL by log4j

Jaspersoft OLAP’s fundamental logging is controlled through log4j settings. log4j’s statement logging occurs in the `mondrian.mdx` and `mondrian.sql` log4j categories. These categories log the statements and how long they ran. The SQL log also records the number of results returned in the result set.

To log your MDX and SQL queries, edit the `/WEB-INF/log4j.properties` file and uncomment these lines:

``` bash
#log4j.logger.mondrian.mdx=debug, jasperanalysis
#log4j.logger.mondrian.sql=debug, jasperanalysis
```

To log all possible Mondrian debugging information, add this line to the `log4j.properties` file:

``` properties
log4j.logger.mondrian=debug
```

Adding this property also ensures that Jaspersoft OLAP logs all SQL and MDX queries.

To log the SQL generated when users drill-through to the underlying transactional data, add this line to the `log4j.properties` file:

``` properties
log4j.logger.jasperanalysis.drillthroughSQL=DEBUG,jasperanalysis
```

!!! note

    You can also use JasperReports Server’s audit Domains and reports to log user activity. For more information, refer to the JasperReports Server Administrator Guide.
