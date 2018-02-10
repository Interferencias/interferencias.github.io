---
layout: post
title: Security Sprint&#58 Week 9 - Privacy politics and the Internet
author: terceranexus6
image:
  feature: banners/header.png
tags: discuss security web w3c
---

By chance I discovered an old World Wide Web consortium (W3C) [project](https://www.w3.org/TR/P3P11/) that has been abandoned for a while. Platform for Privacy Preferences Project (**P3P**) is supposed to be a protocol which gives the opportunity to declare the intended usage of collected information of web browser users in specific pages, in order to make a standardized way of protecting user privacy. At first I thought this was a wonderful idea, and reminded me a lot of the cookies policies problems. This should be an example of syntax of statements for policy (taken from Web Privacy with P3P by Lorrie Faith Cranor, O'reilly):

```
<STATEMENT>
  <EXTENSION optional="no">
    <SAFE-HARBOR eu-applicable="yes"
     xmlns="http://www.example.com/P3P/safe-harbor/"/>
  </EXTENSION>
  <PURPOSE><current/></PURPOSE>
  <RECIPIENT><ours/></RECIPIENT>
  <RETENTION><stated-purpose/></RETENTION>
  <DATA-GROUP>
    <DATA ref="#user.home-info.postal"/>
  </DATA-GROUP>
</STATEMENT>
<STATEMENT>
  <EXTENSION optional="no">
    <SAFE-HARBOR eu-applicable="no"
      xmlns="http://www.example.com/P3P/safe-harbor/"/>
  </EXTENSION>
  <PURPOSE><current/><profiling/></PURPOSE>
  <RECIPIENT><ours/><other-recipient/></RECIPIENT>
  <RETENTION><indefinitely/></RETENTION>
  <DATA-GROUP>
    <DATA ref="#user.home-info.postal"/>
  </DATA-GROUP>
</STATEMENT>
```

As I read and found more and more documentation, and mostly reasons why this project stopped, I found a bunch of advantages and disadvantages surrounding the project and similar ones.

**Advantages?**

Privacy for the user, an standardized way of protecting information and making web surfing more secure. This kind of protocol could block any cookies that the user might not want on his computer! Tools like Privacy Badger could be directly implemented this way, not add-ons needed.

**Disadvantages?**

Apparently one of the main reasons this project was stopped was because it seemed "way too complicated" for the regular user. I found this weird enough to wrinkle my nose: Don't many things on computer development seem "complicated" by inexperienced eyes? Another concern is its use is not compulsory and by that the actual pages that would need blocking wouldn't use it. This seemed more reasonable to me.

Fortunately we have several user-friendly add-ons and programs to protect ourselves but even tho I think is sad such an idea died in the end. Some other similar projects raised in the last years but none of them seemed to succeed, or at least I haven't found them.

**What do you guys think about this kind of projects? Do you think it worths a try to create awareness on the internet about privacy using new protocols or you think other ways are more useful?**

*Also written in: [https://dev.to/terceranexus6/security-sprint-week-9-privacy-politics-and-the-internet-o71](https://dev.to/terceranexus6/security-sprint-week-9-privacy-politics-and-the-internet-o71)*
