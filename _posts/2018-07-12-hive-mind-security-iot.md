---
layout: post
title: Hive mind, no, not aliens, we are talking about hardware!
author: terceranexus6
image:
  feature: banners/header.jpg
tags: iot seguridad ubiquitous-computing
---

<img src="{{ site.url }}/assets/images/dev.to/alien.gif" style="display: block; margin: 0 auto;">

It's been a long time since my security sprint publications I took some vacations in order to further studying, work and practice a bit more about some security areas I've been working on. My lasts efforts have been laid over distributed systems and how to apply security in ubiquitous networks. I aim to write a larger paper about this, but for now I'd love to share a sneak of the possibilities surrounding this interesting topic.

## Divide to conquer!

**Ubiquitous computing** is leading us to a brand new relationship between users and technology. Step by step we are forgetting about technology surrounding us and focusing in our goals, and this could means also forgetting about the risk. Security is a main concern in every system and internet of things is uncovering a new horizons of risks, for this I’m investigating about attack response and prevention using low cost hardware in ubiquitous Networks, inspired by a paper [1], I recently found.

The main point of using a decentralized model is to both allowing to use *low-cost* hardware, as the security is in the model and not the devices and to make attacks more difficult. Not having a centralized point, makes every target *equally relevant*, and designing a fast attack is way harder. In the model we should consider interconnected nodes that communicate to each other and the message exchanging mush be signed before adding it to the common log.

Using an interconnected network of sensors that sends and receives information, sharing the state content in a common memory log, and randomly checking on the neighbor nodes, would allow a fast attack detection, even considering the false positives. If an area is considered “*contaminated*”, the rest of the nodes can be banned to sign the exchange of information in order to **control and suffocate the attack**.

Using *evolutionary computation* it’s even possible to determine the steps that were made in an area to be considered contaminated and prevent a second attack of the same type.

This prevention and response model could be victim of false nodes that communicate to the rest the area is not contaminated and injecting mistaken content in the network, though.

## Ready? Attack!

Let's say we have two main kind of possible attacks, passive and active. Passive attacks are performed by spy nodes that catch relevant information in the network, or in any case make the communication slower but doesn't inject mistaken information into the network, which is considered active. Both can perform together to contaminate the whole network, but the work should be carefully build in order to prevent suffocation or isolation. Beware, shitty drawings coming!

<img src="{{ site.url }}/assets/images/dev.to/x753o0sngjtj85u31yln.jpg" style="display: block; margin: 0 auto;">

In the picture, there's a network with 3 different areas that could perfectly be sensors in a house. All the nodes have a common log of the "transactions" between each others, which have as tokens information of time and content. A range of normal content and response time are supposed to be preset. In the first transaction T1 (A -> B) aims to be a normal, healthy communication. any of the connected nodes which are from the A1 can randomly sign it, and witness the state of the communication. In T2, Not only more nodes are implicated (A1 and A2), but also I wanted to show a false positive, which is considered and alerted, but not labelled as a main contamination. in T3, some new friends are implicated: \*, ♥ (active attackers) and ☾ (passive attacker). the influence of ☾ (and other possible passive attackers in other nodes) makes the ♥ sign first the contaminated communication between \* and F. If this attack is successful, it will be added to the log as a healthy communication. *Yikes!*

Even though, the communication is decentralized, so creating a relevant attack implies a combination of timing and resources that should be orchestrated in order to not alert the healthy nodes, which is highly difficult as the transactions are randomly activated. Not impossible, in any case.

I'm still investigating and doing trials, for this I'm using basic open hardware such as arduino nano devices with simple sensors, so they can work concurrently and check their neighbors. Network simulation is also a great cheaper option but what can I say, I love hardware.

I will post some code in an open repo as soon as I have a nice performance working, but I'd love to hear your thoughts and opinions about this!

*\[1\]: 1. Ajith Abraham, Rafael Falcon, Mario Koeppen.: Computational Intelligence in Wireless Sensor Networks, 978-3-319-47715-2.*

*Also written in: [https://dev.to/terceranexus6/hive-mind-security-in-distributed-iot-3p45](https://dev.to/terceranexus6/hive-mind-security-in-distributed-iot-3p45)*
