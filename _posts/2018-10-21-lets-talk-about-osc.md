---
layout: post
title: Let's talk about OSC
author: terceranexus6
image:
  feature: banners/header.jpg
tags: seguridad networking linux
---

Long time not see! It's been a while since I wrote about security over here, and I'd like to come back to my security sprints. This time, I'm talking about something I've been reading and studying about recently, Open Security Controller for open networking.

<img src="{{ site.url }}/assets/images/dev.to/OSC_logo.jpg.png" style="display: block; margin: 0 auto;">

A network controller is similar to a brain that can manage a network. It consists of multiple physical or virtual switches and routers. A network controller knows all endpoints in the network, and programs the underlying network devices to enable communication between endpoints.

Open Security Controller allow us to automates deployment of virtualized network security functions, such as vIPS (virtual intrusion prevention) or vNGFW (virtual next generation firewalls). The project itself is driven under the [Linux Foundation](https://www.linuxfoundation.org/).

It makes it possible to **separate duties between security admins and DevOps team**, allowing the security team to work independently. OSC fits in conceptually between the security managers and multiple virtualized environments (such as OpenStack, containers, SDN Controllers, orchestration engines...) and security functions. Although, OSC is not meant (of course) to substitute physical security appliances in datacenters, its aim is to include security in the diverse **virtualized environments**, exclusively. Those security functions are intended to be deployed to protect the assets contained in a security group.

Oh! The OSC counts with a GUI and an API which allow the security administrator to define policies. But anyway, let's take a look at the architecture provided by official documentation:

<img src="{{ site.url }}/assets/images/dev.to/osc_architecture_details.png" style="display: block; margin: 0 auto;">

As we can see, it works in conjunction with the SDN controller (implementing the SDN controller plugins to enable this integration), it doesn't replace it. Let's get to it.

For using OSC, we need communication to and from other services. SDN Controller to implement traffic redirection, Security Manager to enforce policies by applying security functions in a virtualized environmen. And now, this is where we get to [OpenStack](https://www.openstack.org/software/), as we need a virtualization provider. OpenStack is a cloud operating system

<img src="{{ site.url }}/assets/images/dev.to/overview-diagram.svg.png" style="display: block; margin: 0 auto;">

OpenStack's networking service includes standard security tools (see [OpenStack Mitaka release for more info](https://www.openstack.org/software/mitaka/)) but don't forget about our main point here, the OSC. Alternatively, OSC can be used in containarized workloads in [Kubernetes](https://kubernetes.io/) using a proxy to Kubernetes API.

For more information on this, take a look at the official [requirements](https://www.opensecuritycontroller.org/documentation/gettingstarted/requirements/). Once we are into this, we can perform protection of workloads on [Openstack or Kubernetes](https://www.opensecuritycontroller.org/documentation/tutorials/tutorials/). I'm still experimenting in [this last option](https://www.opensecuritycontroller.org/documentation/tutorials/k8s_workload/).

I hope you guys found useful learning about this tool.

Also, I leave a little concept help [over here](https://www.opensecuritycontroller.org/documentation/overviewandarchitecture/concepts/) ;)

*Also written in: [https://dev.to/terceranexus6/lets-talk-about-osc-2gbi](https://dev.to/terceranexus6/lets-talk-about-osc-2gbi)*
