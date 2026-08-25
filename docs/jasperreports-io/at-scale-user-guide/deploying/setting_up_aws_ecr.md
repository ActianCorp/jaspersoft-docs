---
title: Setting up AWS ECR
description: This deployment of JasperReports IO At-Scale modules uses the Amazon Elastic Container Registry (AWS ECR) to hold the container images. This section covers the steps for uploading your docker images...
---

# Setting up AWS ECR

This deployment of JasperReports IO At-Scale modules uses the Amazon Elastic Container Registry (AWS ECR) to hold the container images. This section covers the steps for uploading your docker images to AWS ECR.

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

2.  Starting with the first module, in this case jrio-manager, perform the Docker login to its AWS ECR repository with the following command:

    ``` text
    aws ecr get-login-password --region us-east-1 | docker login --username AWS
    --password-stdin 123456789000.dkr.ecr.us-east-1.amazonaws.com/jrio-manager
    ```

    The login is valid for over an hour, giving you time to perform the following steps. If you are interrupted, you may need to perform the Docker login command again.

3.  Find the Docker ID of that module's image:

    ``` text
    docker images | grep jrio-manager
    jrio-manager           3.0           57cbe0cd4e9f        2 days ago          320MB
    ```

4.  Use that Docker ID and tag it to the corresponding AWS ECR repository with the following command:

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><div class="language-text highlight"><pre><code>docker tag 57cbe0cd4e9f 123456789000.dkr.ecr.us-east-1.amazonaws.com/jrio-manager:1.8.0-redis</code></pre></div></td>
    </tr>
    </tbody>
    </table>

    You can give your Docker images a tag such as 1.8.0-redis in this example, but you will need this tag during installation as well.

5.  Push the selected image to the AWS ECR repository with the following command:

    ``` text
    docker push 123456789000.dkr.ecr.us-east-1.amazonaws.com/jrio-manager:1.8.0-redis
    ```

6.  Repeat these steps for each of the modules in order to login, tag, and push each image to its corresponding AWS ECR repository.
