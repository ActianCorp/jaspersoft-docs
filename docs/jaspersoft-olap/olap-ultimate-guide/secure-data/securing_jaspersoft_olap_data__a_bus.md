---
title: "Securing Jaspersoft OLAP Data: A Business Case"
description: "CZS is an up-and-coming consumer electronics company with operations in the U.S. and Japan. CZS is used Jaspersoft OLAP to track sales data, such as sales revenue and operating cost."
---

# Securing Jaspersoft OLAP Data: A Business Case

CZS is an up-and-coming consumer electronics company with operations in the U.S. and Japan. CZS is used Jaspersoft OLAP to track sales data, such as sales revenue and operating cost.

CZS employs the following sales staff:

- Rita is the regional sales manager in the Western U.S. She uses the Sales Numbers Ad Hoc view to track quarterly sales trends in her region.
- Pete is a Sales Rep selling televisions in Northern California. He uses the same view to track his quarterly progress.
- Yasmin is a Sales Rep selling cell phones in Northern California. She uses the same view to track her quarterly progress.
- Alexi is the regional sales manager in Kansai, Japan. He uses the same view to track sales trends in his region.

CZS stores its data in MySQL database tables. The data is exposed by the Sales Numbers Ad Hoc view, which displays information about CZS's consumer electronics sales across the world. It is filtered according to each user’s role, geographical area, and product.

This chapter describes how CZS addressed their business case using Jaspersoft OLAP. It describes the specific steps CZS took to secure their data for users with certain roles and attributes.
