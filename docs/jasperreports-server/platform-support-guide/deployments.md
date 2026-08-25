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
<li>25.x+</li>
<li>27.x</li>
</ul></td>
<td><p>Certified</p></td>
<td><p>Certified</p></td>
</tr>
<tr>
<td><p>Kubernetes</p></td>
<td><ul>
<li>1.34+</li>
</ul></td>
<td><p>Certified</p></td>
<td><p>Certified</p></td>
</tr>
</tbody>
</table>

Jaspersoft products are compatible with various deployment platforms that support Docker and Kubernetes engines. For example, the compatibility has been confirmed on platforms such as AWS ECS, AWS EKS, Azure EKS, and Openshift. While these platforms have been tested and verified, Jaspersoft products can also be deployed on other platforms that work with Docker and Kubernetes engines.

Detailed information on Docker or Kubernetes deployments can be found in the Jaspersoft Docker Repository, accessible at <https://github.com/Jaspersoft/js-docker/tree/main>.

## Supported Docker Images

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th><p>Image</p></th>
<th><p>JasperReports Server</p></th>
<th><p>JasperReports IO Pro</p></th>
<th><p>JasperReports IO At-Scale</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>eclipse-temurin-17-alpine</p></td>
<td></td>
<td><p>Certified</p></td>
<td><p>Certified</p></td>
</tr>
<tr>
<td><p>tomcat:10.1.55-jdk21-temurin</p>
<p>tomcat:10.1.55-jdk17-temurin</p></td>
<td>Certified</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td><p>tomcat:10-jdk21-corretto</p>
<p>tomcat:10-jdk17-corretto</p></td>
<td>Certified</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td><p>eclipse-temurin:21-jdk-noble</p>
<p>eclipse-temurin:17-jdk-noble</p></td>
<td>Certified, required for buildomatic image</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td><p>amazoncorretto:21-al2023-jdk</p>
<p>amazoncorretto:17-al2023-jdk</p></td>
<td>Certified, required for buildomatic image</td>
<td> </td>
<td> </td>
</tr>
</tbody>
</table>
