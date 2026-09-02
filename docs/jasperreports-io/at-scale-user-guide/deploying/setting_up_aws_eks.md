---
title: Setting Up AWS EKS
description: This section describes the tools and settings that you need to create a cluster resource on Amazon Elastic Kubernetes Service (AWS EKS). It relies on the Amazon document “Getting started with the AWS...
---

# Setting Up AWS EKS

This section describes the tools and settings that you need to create a cluster resource on Amazon Elastic Kubernetes Service (AWS EKS). It relies on the Amazon document “Getting started with the AWS Management Console” located at:

<https://docs.aws.amazon.com/eks/latest/userguide/getting-started-console.html>

Open that document in a separate tab and refer to it when mentioned here.

## Installing the AWS CLI

In order to create and interact with your cluster, you need an Amazon AWS account and the tools to access the service. The AWS CLI is a command-line application to send commands to your AWS resources.

Follow the instructions in the Amazon document to download and install the AWS CLI for your platform (Linux, Mac, or Windows). When done, test the tool by invoking it with the `--version` option.

``` text
root@/opt/jrs/jrio>aws --version
aws-cli/2.0.36 Python/3.7.4 Darwin/19.6.0 exe/x86_64
```

## Configuring AWS Credentials

In order for the AWS CLI tool to have access to your AWS resources, you must give it your AWS Access Key and Secret Key. These can be found on the AWS website as follows:

1.  Log into the AWS website either with your Federated User using your principal AWS credentials or with your AWS access key and secret key.
2.  Goto AWS Identity and Access Management (IAM), and acknowledge the warnings.
3.  Click Users on the left, then select your username.
4.  Select the Security Credentials Tab, and choose Create New Access Key.

Follow the instructions in the Amazon document to run the `aws configure` command and enter the keys when prompted. The AWS CLI tool stores your input in its configuration files located in the .aws folder:

``` text
root@/root/.aws>cat credentials
[default]
aws_access_key_id = <YOURACCESSKEYEXAMPLE>
aws_secret_access_key = <wJalrXUtnFEMI/K7MDENG/YOURSECRETKEYEXAMPLE>

root@/root/.aws>cat config
[default]
region = us-east-1
output = json
```

## Installing kubectl

You also need the kubectl command-line tool to manage the Kubernetes cluster you will deploy on AWS EKS. Follow the instructions in the Amazon document to download and install the kubectl tool for your platform (Linux, Mac, or Windows).

## Creating a Cluster Role

Using AWS Identity and Access Management (IAM), you need to create an IAM role that can be passed to the Kubernetes cluster once it is deployed within AWS EKS. Kubernetes can use this role to access other AWS services and perform actions on your behalf, for example to start new nodes.

Follow the instructions in the Amazon document to create an IAM role for the cluster using the AWS Management Console.

After you have created the role, you can configure the AWS CLI to use this role. Edit the .aws/config file to add the Amazon Resource Name (ARN) for the role. In the following example, the number 132456789000 is your 12-digit AWS user ID that appears in your AWS resource names and URLs.

``` text
[default]
region = us-east-1
output = json
role_arn = arn:aws:iam::123456789000:role/eksClusterRole
source_profile = default
```

Verify that the role is being applied to your AWS CLI commands by running the following command:

`aws sts get-caller-identity`

In the configuration above, the AWS CLI tool will use the cluster role for every command. If you wish to use the tool with other services, you should define the role in a separate profile that you use only with cluster commands. For more information, see the Amazon guide for AWS CLI roles:

<https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html>

## Creating a Virtual Private Cloud

An AWS EKS cluster runs in a Virtual Private Cloud (VPC) with at least two subnets. In this step, you will use Amazon CloudFormation to define and configure a VPC with its subnets.

Jaspersoft recommends having your JasperReports Server in a VPC with public access and the Kubernetes cluster nodes in a private subnet. For more information, see [Deploying JasperReports Server](deploying_the_cluster.md).

Follow the instructions in the Amazon document to create a VPC with public and private subnets for your Amazon EKS cluster.

Before you log out, look at the CloudFormation output tab and record the VPC ID, subnets IDs, and security group ID that has `ControlPlane` in the name.

## Creating the Cluster

When you create an AWS EKS cluster, you use the AWS cluster web console to define the cluster parameters using the VPC created in the previous section. This step creates an empty cluster with Kubernetes, the images are pushed and depolyed in later steps.

Follow the instructions in the Amazon document to create your Amazon EKS cluster.

Use the following information during the procedure:

-   Choose a name for your cluster, and be aware that it can't be changed later. The examples in this guide use the name `JRIOcluster`.
-   The cluster service role is the one created in [“Creating a Cluster Role” on page 1](#creating-a-cluster-role), for example `eksClusterRole`.
-   No encryption is needed, click Next.
-   Select the VPC ID that you recorded at the end of the previous section.
-   Verify that all the subnet IDs from the previous section are included.
-   Verify that the security group ID is the one from the previous section that includes the control plane.
-   The cluster enpoint access has been verified to work with the Public option. If you prefer to make this private, you can experiment with setting a CIDR range or selecting the Private option, but you may need further configuration.
-   No logging or monitoring is needed.
-   Cluster creation takes some time, wait until the status becomes Active.

## Updating kubectl

Now that you have an active but empty AWS EKS cluster, connect your local kubectl tool to the cluster. To do this, use the AWS CLI tool to create the kubeconfig file needed by the kubectl tool.

Follow the instructions in the Amazon document to create a kubeconfig file.

The command uses the name of the cluster that you defined in the previous section, for example:

``` text
aws eks --region us-east-1 update-kubeconfig --name JRIOcluster
```

Verify that the configuration works with the following command:

``` text
kubectl get svc
```

## Create Compute

Now that you have an empty cluster defined, and a control plane to manage it, this step defines the compute nodes that can be instantiated in the cluster.

Follow the instructions in the Amazon document to create compute with managed nodes.

Use the following information during the procedure:

-   Create a role for the nodes in the IAM console as described. This document uses the name EKSNodeInstanceRole.

-   There is no need for a launch template.

-   On the compute and scaling configuration page:

    -   AMI (Amazon Machine Image): the only supported option is Amazon Linux (Intel based), not GPU nor ARM.
    -   Disk size: select the default.
    -   Node group scaling: specify reasonable values, they can be changed later.

-   On the networking page, select all the subnets you defined in the VPC. Machines in the same VPC are all able to see each other, but only the ones that have public subnets will have access to the Internet.

-   An SSH key pair is needed only if you want to ssh to one of the nodes. In most cases this is not needed because the node lifecycle is managed via Kubernetes, and most work can be performed using kubectl.

After you create the managed node group, wait until they are in the ready state, as given by the following command:

``` text
kubectl get nodes --watch
```
