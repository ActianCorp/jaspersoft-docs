---
title: Setting up AWS ECR
description: This deployment of Jaspersoft IO At-Scale modules uses the Amazon Elastic Container Registry (AWS ECR) to hold the container images. This section covers the steps for uploading your docker images to...
---

# Setting up AWS ECR

This deployment of Jaspersoft IO At-Scale modules uses the Amazon Elastic Container Registry (AWS ECR) to hold the container images. This section covers the steps for uploading your docker images to AWS ECR.

!!! warning

    Before proceeding, make sure you have fully configured your modules and have built the final images, as described in [“Building Docker Images” on page 1](../dockerimages/intro_modules.md).

1.  Open the Amazon ECR web console at <https://console.aws.amazon.com/ecr/repositories> and create one repository for each image you want to upload. Usually, the repositories have the same name as the corresponding modules:

- jrio-manager
- jrio-reporting
- jrio-export
- jrio-rest
- jrio-client (optional)

After creating each repository, record the URL that is given for accessing it, for example:

`123456789000.dkr.ecr.us-east-1.amazonaws.com/jrio-manager`

1.  Starting with the first module, in this case jrio-manager, perform the Docker login to its AWS ECR repository with the following command:

```
aws ecr get-login-password --region us-east-1 | docker login --username AWS
--password-stdin 123456789000.dkr.ecr.us-east-1.amazonaws.com/jrio-manager
```

The login is valid for over an hour, giving you time to perform the following steps. If you are interrupted, you may need to perform the Docker login command again.

1.  Find the Docker ID of that module's image:

```
docker images | grep jrio-manager
jrio-manager           3.0           57cbe0cd4e9f        2 days ago          320MB
```

1.  Use that Docker ID and tag it to the corresponding AWS ECR repository with the following command:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>docker tag 57cbe0cd4e9f 123456789000.dkr.ecr.us-east-1.amazonaws.com/jrio-manager:1.8.0-redis</code></pre></td>
</tr>
</tbody>
</table>

You can give your Docker images a tag such as 1.8.0-redis in this example, but you will need this tag during installation as well.

1.  Push the selected image to the AWS ECR repository with the following command:

```
docker push 123456789000.dkr.ecr.us-east-1.amazonaws.com/jrio-manager:1.8.0-redis
```

1.  Repeat these steps for each of the modules in order to login, tag, and push each image to its corresponding AWS ECR repository.
