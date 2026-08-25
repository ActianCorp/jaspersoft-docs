---
title: Stopping and Restarting Tomcat
description: To stop and restart Tomcat
---

# Stopping and Restarting Tomcat

To stop and restart Tomcat

1.  SSH into your instance using your AWS private key and the username `ec2-user`.

2.  Stop the Tomcat service using the following command:

    `sudo systemctl stop tomcat.socket`

3.  Restart the Tomcat service:

`sudo systemctl start tomcat.socket`
