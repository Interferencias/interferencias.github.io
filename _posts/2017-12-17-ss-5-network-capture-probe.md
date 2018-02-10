---
layout: post
title: Security Sprint&#58 Week 5 - Network Capture Probe with Raspberry
author: terceranexus6
image:
  feature: banners/header.png
tags: network nsm security english hacking raspberrypi
---

Recently something amazing was added in my university's library: you can ask not only for for books but also for electronic programming bundles such as Raspberry or Arduino kits. I decided to take a Raspberry Pi kit in order to make an experiment: a **network capture probe**.

<img src="{{ site.url }}/assets/images/dev.to/go7r450eu0ysx2uy09mr.jpg" style="display: block; margin: 0 auto;">

A network capture probe is a tool for network system monitoring that allows you to capture traffic in real-time. I learned about this technique not long ago when I met a guy who was wearing one of those in his bag everywhere using his Raspberry Pi, neat, eh?. Now I want to try the same...

I downloaded the latest version of [Raspbian](https://downloads.raspberrypi.org/raspbian_latest) , burnt a 8GB MicroSD, installed [Etcher](https://etcher.io/), installed the Raspbian ISO in the card using Etcher, and connecting the RPI to a screen using HDMI. I also attached a keyboard and a mouse. I had a RPI screen too, so I also did some magic to adjust to it later, as well as the WiFi pin, but important things first. I must say I tried to download bro tool first, but I didn't have enough space to compile it in my 8GB card... _ups_.

Once I installed **Raspbian** I opened the terminal and installed tcpdump using `apt-get install tcpdump`, take care of the `sudo`, too. Why? I wrote an easy script to capture stuff using tcpdump. Here it is:

```
#!/bin/bash

eval namedir=$1
eval net=$2
count=0
number=5

mkdir $namedir
cd $namedir

while [ $count -lt 1000 ]
do

    tcpdump -A -w $count_.pcap -c $number -i $2
    echo "just captured $number packets"

done

```

<img src="{{ site.url }}/assets/images/dev.to/r7ad5rfjzgafiv3c3zmg.jpg" style="display: block; margin: 0 auto;">

It's a simple example, with many details to polish. In this case, the first parameter is the name of the directory, second is the name of the WiFi card. An option is `any` for any card. Anyway these are examples of the input:

```
# ./script.sh trial wlan0
# ./script.sh trial eth1
# ./script.sh trial any

```

An output inside the directory we created would be `0_.pcap 1_.pcap 2_.pcap` and so it goes. Each pcap will contain the ASCII (`-A`) information of five (`number=5`) packets. To read them, there's the `-r` tcpdump command. Another idea to make it prettier would be using `-D` command, which show the list of available interfaces, save it in a file and use the file in a `for` loop to save information. But I haven't tried it yet. Anyway is a fun toy to play with an a nice tool to practise Network System Monitoring in random networks. Be careful tho ;)

*Also written in: [https://dev.to/terceranexus6/security-sprint-week-5-network-capture-probe--a33](https://dev.to/terceranexus6/security-sprint-week-5-network-capture-probe--a33)*
