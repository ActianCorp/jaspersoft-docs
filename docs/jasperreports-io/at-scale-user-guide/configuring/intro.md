---
title: Configuring a Cluster in Kubernetes
description: This chapter explains how to configure and optimize a JasperReports IO At-Scale Kubernetes cluster.
---

# Configuring a Cluster in Kubernetes

This chapter explains how to configure and optimize a JasperReports IO At-Scale Kubernetes cluster.

A Kubernetes cluster is managed by the Helm chart that is shipped as part of the enterprise package. The Helm chart is in the following folder:

<table>
<tbody>
<tr>
<td>Folder</td>
<td colspan="2">jasperreports-io-at-scale-10.1.0/helm/</td>
</tr>
<tr>
<td rowspan="2">Contents</td>
<td>values.yaml</td>
<td>The Helm chart contains all the properties required for JasperReports IO At-Scale pods or services.</td>
</tr>
<tr>
<td>templates</td>
<td>Subfolder containing files for kubectl commands. These can only be installed through Helm, because the files use variables from the values.yaml file.</td>
</tr>
</tbody>
</table>
