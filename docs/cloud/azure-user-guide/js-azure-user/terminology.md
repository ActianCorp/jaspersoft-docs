---
title: Microsoft Azure Terminology
---

# Microsoft Azure Terminology

| Term | Description |
|----|----|
| Account | An account that is used to access and manage an Azure subscription. It is often referred to as an Azure account although an account can be an existing work, school, a personal Microsoft account, or an Office 365 user name and password. |
| API App | Another name for App Service app. |
| App Service App | The compute resources that Azure App Service provides for hosting a website or web application, web API, or mobile app backend. App Service apps are also referred to as App Services, web apps, API apps, and mobile apps. |
| Availability Set | A collection of virtual machines that are managed together to provide application redundancy and reliability. An availability set ensures that at least one virtual machine is available during a planned or unplanned maintenance event. |
| Azure Classic Deployment Model | One of two deployment models used to deploy resources in Azure (the new model is Azure Resource Manager). Some Azure services support only the Resource Manager deployment model, some support only the classic deployment model, and some support both. The documentation for each Azure service specifies which models they support. |
| Azure Command-line Interface (CLI) | A command-line interface that can be used to manage Azure services from Windows, macOS, and Linux. Some services or service features can be managed only via PowerShell or the CLI. |
| Azure PowerShell | A command-line interface to manage Azure services via a command line from Windows PCs. Some services or service features can be managed only via PowerShell or the CLI. |
| Azure Resource Manager Deployment Model | One of the two deployment models used to deploy resources in Microsoft Azure (the other is the classic deployment model). Some Azure services support only the Resource Manager deployment model, some support only the classic deployment model, and some support both. The documentation for each Azure service specifies which models they support. |
| Fault Domain | The collection of virtual machines in an availability set that can possibly fail at the same time. An example is a group of machines in a rack that share a common power source and network switch. In Azure, the virtual machines in an availability set are automatically separated across multiple fault domains. |
| Geo | A defined boundary for data residency that typically contains two or more regions. The boundaries may be within or beyond national borders and are influenced by tax regulation. Every geo has the at least one region. Examples of geos are Asia Pacific and Japan. Also called geography. |
| Geo-replication | The process of automatically replicating content such as blobs, tables, and queues within a regional pair. |
| Image | A file that contains the operating system and application configuration that can be used to create any number of virtual machines. In Azure, there are two types of images: VM image and OS image. A VM image includes an operating system and all disks attached to a virtual machine when the image is created. An OS image contains only a generalized operating system with no data disk configurations. |
| Limits | The number of resources that can be created or the performance benchmark that can be achieved. Limits are typically associated with subscriptions, services, and offerings. |
| Load Balancer | A resource that distributes incoming traffic among computers in a network. In Azure, a load balancer distributes traffic to virtual machines defined in a load-balancer set. A load balancer can be internet-facing, or it can be internal. |
| Mobile App | Another name for App Service App. |
| Offer | The pricing, credits, and related terms applicable to an Azure subscription. |
| Portal | The secure web portal is used to deploy and manage Azure services. |
| Region | An area within a geo that does not cross-national borders and contains one or more data centers. Pricing, regional services, and offer types are exposed at the regional level. A region is typically paired with another region, which can be up to several hundred miles away. Regional pairs can be used as a mechanism for disaster recovery and high availability scenarios. Also referred to as location. |
| Resource | An item that is part of your Azure solution. Each Azure service enables you to deploy different types of resources, such as databases or virtual machines. |
| Resource Group | A container in the Resource Manager that holds related resources for an application. The resource group can include all of the resources for an application, or only those resources that are logically grouped. You can decide how you want to allocate resources to resource groups based on what makes the most sense for your organization. |
| Resource Manager Template | A JSON file that declaratively defines one or more Azure resources and that defines the dependencies between the deployed resources. The template can be used to deploy the resources consistently and repeatedly. |
| Resource Provider | A service that supplies the resources you can deploy and manage through Resource Manager. Each resource provider offers operations for working with the resources that are deployed. Resource providers can be accessed through the Azure portal, Azure PowerShell, and several programming SDKs. |
| Role | A means for controlling access that can be assigned to users, groups, and services. Roles are able to perform actions such as create, manage, and read on Azure resources. |
| Service Level Agreement (SLA) | The agreement describes Microsoft’s commitments for uptime and connectivity. Each Azure service has a specific SLA. |
| Shared Access Signature (SAS) | A signature that enables you to grant limited access to a resource, without exposing your account key. |
| Storage Account | An account that gives you access to the Azure Blob, Queue, Table, and File services in Azure Storage. The storage account name defines the unique namespace for Azure Storage data objects. |
| Subscription | A customer's agreement with Microsoft that enables them to obtain Azure services. The subscription pricing and related terms are governed by the offer chosen for the subscription. |
| Tag | An indexing term that enables you to categorize resources according to your requirements for managing or billing. When you have a complex collection of resources, you can use tags to visualize those assets in the way that makes the most sense. For example, you could tag resources that serve a similar role in your organization or belong to the same department. |
| Update Domain | The collection of virtual machines in an availability set that are updated at the same time. Virtual machines in the same update domain are restarted together during planned maintenance. Azure never restarts more than one update domain at a time. Also referred to as an upgrade domain. |
| Virtual Machine | The software implementation of a physical computer that runs an operating system. Multiple virtual machines can run simultaneously on the same hardware. In Azure, virtual machines are available in a variety of sizes. |
| Virtual Machine Extension | A resource that implements behaviors or features that either help other programs work or provide the ability for you to interact with a running computer. For example, you could use the VM Access extension to reset or modify remote access values on an Azure virtual machine. |
| Virtual Network | A network that provides connectivity between your Azure resources that are isolated from all other Azure tenants. An Azure VPN Gateway lets you establish connections between virtual networks and between a virtual network and an on-premises network. You can fully control the IP address blocks, DNS settings, security policies, and route tables within a virtual network. |
| Web App | Another name for App Service App. |
