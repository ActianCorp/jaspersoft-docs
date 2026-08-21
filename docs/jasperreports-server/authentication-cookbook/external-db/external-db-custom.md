---
title: Adding a Custom Processor
description: "To create custom code to run on the server after the user has been authenticated, you can create a custom processor and add it to the processors list for the externalUserProcessors property of the..."
---

# 1.1 Adding a Custom Processor

To create custom code to run on the server after the user has been authenticated, you can create a custom processor and add it to the processors list for the `externalUserProcessors` property of the `externalDataSynchronizer` bean. For example, you can add a processor that calls code to automatically create a user home folder for the authenticated user. See [Creating a Custom Processor](../advanced-topics/creating-custom-processor.md).
