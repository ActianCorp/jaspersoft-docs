---
title: Deployments
description: "The following platforms are supported on:"
---

# Deployments

The following platforms are supported on:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th><p>Platform</p></th>
<th><p>Version</p></th>
<th><p>JasperReports Server</p></th>
<th><p>JasperReports IO At-Scale</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Docker</p></td>
<td><ul>
<li>20.10.x</li>
<li>23.0</li>
<li>24.0</li>
<li>27.x</li>
</ul></td>
<td><p>Certified</p></td>
<td><p>Certified</p></td>
</tr>
<tr>
<td><p>Kubernetes</p></td>
<td><ul>
<li>1.29+</li>
</ul></td>
<td><p>Certified</p></td>
<td><p>Certified</p></td>
</tr>
</tbody>
</table>

Jaspersoft products are compatible with various deployment platforms that support Docker and Kubernetes engines. For example, the compatibility has been confirmed on platforms such as AWS ECS, AWS EKS, Azure EKS, and Openshift. While these platforms have been tested and verified, Jaspersoft products can also be deployed on other platforms that work with Docker and Kubernetes engines.

Detailed information on Docker or Kubernetes deployments can be found in the Jaspersoft Docker Repository, accessible at <https://github.com/TIBCOSoftware/js-docker>.

## Supported Docker Images

| Image | JasperReports Server | JasperReports IO Pro | JasperReports IO At-Scale |
|----|----|----|----|
| eclipse-temurin-17-alpine |  | Certified | Certified |
| tomcat:10.1.43-jdk17-temurin | Certified |   |   |
| tomcat:10-jdk17-corretto | Certified |   |   |
| eclipse-temurin:17-jdk-noble | Certified, required for buildomatic image |   |   |
