---
title: Multiple Jobs and Alerts fail to Trigger at the Same Time
description: "When scheduling multiple jobs or alerts, the Scheduler and Alerting engine fails to run some of the jobs or alerts triggered during the same time, resulting in only a few jobs or alerts executing...."
---

# Multiple Jobs and Alerts fail to Trigger at the Same Time

When scheduling multiple jobs or alerts, the Scheduler and Alerting engine fails to run some of the jobs or alerts triggered during the same time, resulting in only a few jobs or alerts executing. This happens as these jobs or alerts have a recurrence set to be repeated every 1-2 min. The scheduler and alerting engine pick up the list of jobs to be run, and that list is checked every minute.

Every job or alert trigger is added to the queue because of the default misfire policy set as `SMART_POLICY`. Since every triggered job or alert has the same priority, even if the execution of first job is not complete within one minute, the next consequent execution task of the job or alert gets added to the queue and the list keeps increasing. Therefore, based on the number of jobs or alerts, the number of recurrent execution tasks keep getting configured.

To fix this behavior in `.../WEB-INF/js.quartz.base.properties`, set the following parameter:

``` properties
org.quartz.jobStore.misfireThreshold = 360000
```

After changing this parameter, restart the Tomcat server.

The default value of `org.quartz.jobStore.misfireThreshold` corresponds to 180 seconds. The time has been increased in milliseconds to complete all triggered jobs or alerts before the next consequent trigger of that job or alert has to be run.
