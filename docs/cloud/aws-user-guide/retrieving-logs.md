---
title: Retrieving Logs
description: 1. SSH into your instance using your AWS private key and the username ec2-user.
---

# Retrieving Logs

To retrieve logs:

1.  SSH into your instance using your AWS private key and the username `ec2-user`.

    1.  To follow the logs, run this command:

        `tail -f /var/log/jasperserver/jasperserver.log`

    2.  To dump log content, run this command:

`cat /var/log/jasperserver/jasperserver.log`
