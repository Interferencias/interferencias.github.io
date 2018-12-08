---
layout: post
title: Network Security Monitoring with bro
author: terceranexus6
image:
  feature: banners/header.jpg
tags: tutorial linux seguridad networking
---

Recently I've been studying about Network Security. For a year, I've been using ettercap for pentesting and investigation, I even wrote a [Lex app](https://github.com/terceranexus6/proyecto_lex) for it, but recently I've found a tool which is pretty similar but way better, logs are pretty organized and have better commands. I must say I will be using linux, there are options for network monitoring in Windows, but I'm not going to talk about them in this article.

First of all, network security monitoring allow us to detect and respond to intrusions. The range of the NSM data is:

- **Full content**: all the information that cross the network
- **Extracted content**: high level data stream, such as images and such.
- **Session data**: Record of the conversation between two nodes (this is the logs that bro generates and the part that I will be focusing).
- **Transaction data**: Similar to session data, but focusing on understanding the request an replies.
- **Statistical data**: Traffic resulting from various aspects of an activity.
- **Metadata**: Studying further the data results of the monitoring and understanding them.
- **Alert data**: Intrusion detection.

And now I'm introducing Bro tool. Bro it's pretty easy to install. After downloading and opening the directory on the terminal, we can read the INSTALL instructions simply doing `cat INSTALL` , but it's a classic "`./configure, cmake, make`". If you have a problem, you should check if your network is wlan0, if not, change it. This took me a while to figure out.

Once we installed it, we go to the directory where we saved it. In my case, it's /usr/local/bro but wherever. in the .../bro/bin you shoul see a lot of executables. We will be focusing on broctl, sudo that thing! `sudo ./broctl`.

You should see something like this:

```
Welcome to BroControl 1.7

Type "help" for help.

[BroControl] >
```

Now we are starting. on the bro terminal we will write `start` that will start the scanning.

```
[BroControl] > start
starting bro ...
[BroControl] >
```

In another terminal we locate again our bro directory and then we go to .../bro/logs. We should see a log with the date and a directory called current. We are gonna check current (`cd current`). In that directory we should find a lot of directories, but we are going to center in `http.log`. The directories are zipped so first we are using `sudo gunzip *.log.gz` to unzip them. now lets `cat http.log`.

There we can see a lot of information divided in paragraphs. We should clearly see the GET requests in the network. If, for example, we enter [www.testmyids.com](http://www.testmyids.com/) in the browser, and doing again the `cat http.log` thing, it should allow us to clearly see the request for a favicon failed. A nice tip would be watching the x509.log directory, too. It contains information about the certificates of the places visited, which tell us the users are entering twitter, facebook, google... etc.

When we want to stop we only write "stop" in the bro terminal

```
[BroControl] > stop
stopping bro ...
```

There are [plenty more commands](https://www.bro.org/sphinx/components/broctl/README.html) for bro that will be useful for us to check. You could spend a while analizing all the data, and I assure you, you can get conclussions easily due to it's well organized system.

*Originally written in: [https://dev.to/terceranexus6/network-security-monitoring-with-bro](https://dev.to/terceranexus6/network-security-monitoring-with-bro)*
