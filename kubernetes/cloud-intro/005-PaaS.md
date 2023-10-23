## PaaS 
#### Platform as a Service (PaaS) is a cloud service model representing a class of cloud computing services that allow users to develop, run, and manage applications while concealing the tasks involved in the management of the underlying infrastructure. With PaaS, users are able to concentrate their efforts on building their applications, which is a great benefit to developers.

Users have a choice between managed and self-managed PaaS solutions. Managed PaaS solutions are hosted by cloud computing providers like Amazon AWS, Microsoft Azure, Google Cloud Platform (GCP), IBM Cloud, and Oracle Cloud, while an on-premises PaaS can be deployed as a self-managed solution, using a platform such as Red Hat OpenShift.

PaaS can be deployed on top of IaaS, or, independently on VMs, bare-metal servers, and containers.

Infrastructure as a Service is the backbone of all other cloud services, providing computing resources. After the provisioning of the computing resources, other services are set up on top.
## Examples:
### Amazon EC2 Elastic Compute Cloud
```
Amazon Web Services (AWS) is one of the leading cloud services providers. Its cloud services, whether Platform, Software, DB, Containers, Serverless, Machine Learning, to name a few, rely heavily on its Infrastructure. Part of Amazon's Infrastructure as a Service (IaaS) model is the Amazon Elastic Compute Cloud (Amazon EC2) service. Amazon EC2 service allows individual users and enterprises alike to build a reliable, flexible, and secure cloud infrastructure for their applications and workloads on Amazon's platform. AWS offers an easy to use Console, which is a web interface for cloud resources management.

Amazon EC2 instances are in fact Virtual Machines. When provisioning EC2 instances on the AWS infrastructure, we are provisioning VMs on top of hypervisors that run directly on Amazon's physical infrastructure. In addition to the web console, AWS also offers a command line interface (CLI), a tool to manage resources scriptically if necessary. 

At the heart of Amazon EC2 service, are various type-1 hypervisors, such as Xen, KVM, and Nitro (a newer KVM-based lightweight hypervisor that delivers close to bare-metal performance).

Although Amazon EC2 is a paid service, new users are encouraged to try the AWS platform for free through AWS Free Tier offerings. While not all of its services qualify for the free tier, the ones that are available for free do come with some limitations. Several such services are offered under short-term Free Trials, others are offered for 12 months free, while a third group of services may be Always free to all users. The three types of free offerings have been designed to encourage users to take advantage of the free tier offerings to become familiar with the most popular services the AWS platform has to offer.
```
### Azure Virtual Machine:
```
Microsoft Azure is a leading cloud services provider, with products in different domains, such as compute, web and mobile, data and storage, Internet of Things (IoT), and many others. The Azure Virtual Machine service allows individual users and enterprises alike to provision and manage compute resources, both from a web Portal or the Azure Cloud Shell, a flexible command line utility configurable to use either Bash or PowerShell.

Azure cloud services are enabled by the Azure Hypervisor, a customized version of Microsoft Hyper-V type-1 hypervisor. The Azure Hypervisor promises high efficiency, performance, and scalability over a small footprint thanks to the optimization of the custom Hyper-V hypervisor coupled with its tight integration with the physical infrastructure. 

The Azure Virtual Machine is a paid service, however, the Azure free account offering aims to attract new users and encourage them to explore the cloud services the Azure platform has to offer. Between an initial credit limited to the first 30 days following the opening of the free account, popular services free for 12 months, and a set of always free services, users have several options enabling them to become familiar with the most popular services the Azure cloud platform has to offer.
```
### Google Compute Engine:
```
Google Cloud Platform (GCP) is one of the leading cloud services providers. Its infrastructure is the foundation for all other cloud services, whether Platform, Software, Containers, Serverless, Artificial Intelligence, Machine Learning, to name a few. Part of Google's Infrastructure as a Service (IaaS) model is the Compute Engine service. Google Compute Engine (GCE) service allows individual users and enterprises alike to build a reliable, flexible, and secure cloud infrastructure for their applications and workloads on Google's platform. GCP offers an easy to use Console, which is a web interface for cloud resources management.

GCE instances are in fact Virtual Machines. When provisioning GCE instances on the GCP infrastructure, we are provisioning VMs on top of hypervisors that run directly on Google's physical infrastructure. In addition to the web Console, GCP also offers a command line interface (CLI), a tool to manage resources scriptically if necessary. 

GCE services are enabled by the KVM type-1 hypervisor, running directly on Google's physical infrastructure and allowing for VMs to be launched with Linux and Windows guest Operating Systems.

GCE is a paid service, however, new users are encouraged to try the GCP platform for free through the GCP Free Tier offering. The Free Tier offers new users a chance to become familiar with the most popular services the Google Cloud Platform has to offer with the help of short-term initial free credits and several products that are always free within predefined usage limits.
```
![KVM](images/KVM.png "KVM")