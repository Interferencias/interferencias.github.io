---
layout: post
title: Security Sprint&#58 Week 12 - What I learnt in a CTF
author: terceranexus6
image:
  feature: banners/header.jpg
tags: seguridad ctf hacking tools
---

For the ones who are not close to security related slang, **Catch The Flag** is an online hacking game that consist in hacking stego, web, network, etc in order to get passwords (the flags) and catch them all before the rest of the contestants. So through three days, I played one of those organized by my university, with a team mostly dedicated in Network and Forensic study. I won't be explaining all the process here, but I want to point out all the tools I used (most of them brand new for me) for solving the problems.

<img src="{{ site.url }}/assets/images/dev.to/mr_robot.gif" style="display: block; margin: 0 auto;">

* **tcpdump**: I already [wrote about this tool](https://dev.to/terceranexus6/security-sprint-week-2---choosing-a-nice-point-to-sniff-and-using-tcpdump-for-packet-analysis--e9) but I found it very useful this time too. It's a network scanning and processing tool that allowed me to find out a weird file in a network that actually contained the *flag*. When other tools were blocked by the system, this one remained. Yay! it's also a command line tool in linux, flexible and handful.

* **Nikto**: This is a very useful network scanning tool that unfortunately was blocked by the CTF system, but it might be useful in real life or other CTF's. it has a lot of options, including -e that looks for weird files. An example of a host scanning is `nikto -host {host}`.

* **nmap**: A classic network scanning tool. For example `nmap -v -sn {host}`.

* **Identify**: Helped me giving me information about and image, using a command such as `identify -verbose image.jpg`.

* **stegosolve**: As it names indicates, it's a tool that works specially for steganography. Actually what this program does can be done directly using **Gimp**. But it's faster this way. It plays with ganma colors of an image as well as the saturation. It's a java program so an example would be `java -jar stegosolve.jar image.png`.

* **Binwalk**: This is also for steganography, this tool can find binary files such as zip files or txt or another image, inside an image. I actually used **ghex** first and saw there was a "PK" in the translated hexadecimal, which means there's a ZIP inside it. But without Binwalk it would have been more difficult to catch it. It's posible using **dd** like `dd if=image.png bs=1 skip=the_line_in_decimal_where_PK_is of=foo.zip` but Binwalk is a better option: `binwalk -e image.png`, and it's done.

* **Volatility**: Last but not least, volatility is like pure magic. Is a powerful forensic tool that allows to look for clues in dump files.

Depending on the puzzles and the hacker, some other tools could be useful. In my case these are all framed in Debian Jessie GNU/Linux, and taking advance of the terminal, in which I feel more comfortable. Anyway, CTF's are good options for learning an there are tons of them on the Internet but beware! They're highly addictive.

*Also written in: [https://dev.to/terceranexus6/security-sprint-what-i-learnt-in-a-ctf-2nf3](https://dev.to/terceranexus6/security-sprint-what-i-learnt-in-a-ctf-2nf3)*
