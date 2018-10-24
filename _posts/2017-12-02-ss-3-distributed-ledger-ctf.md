---
layout: post
title: Security Sprint&#58 Week 3 - Distributed Ledger system and our first Catch The Flag training
author: terceranexus6
image:
  feature: banners/header.jpg
tags: bitcoins hacking network security
---

Friday was such an intense day regarding to security. First of all I started investigating for a class assignment about **Distributed Ledger** (as in [Bitcoin](https://dev.to/terceranexus6/bitcoins-d00) system) applied to other things such as energy industry, communication and similar. A distributed ledger is a database held and updated independently by each participant (or node) in a large network. The lacking of central authority makes individual nodes process every transaction, and update the ledger again (for every node).

<img src="{{ site.url }}/assets/images/dev.to/giphy.gif" style="display: block; margin: 0 auto;">

I found this deeply interesting and started investigating about *Ethereum* as its [documentation](https://www.ethereum.org/) provides a guide on coding to [create your own cryptocurrency](https://www.ethereum.org/token) or a [democracy on the blockchain](https://www.ethereum.org/dao), which I found really cool, I just got very excited and decided to experiment with all of this. Specially the democracy system can help me develop something interesting to deploy in class and show my own ideas about distributed ledger systems (gasp). This, for example, is a basic template for a contract in ethereum:

```
contract MyToken {
    /* This creates an array with all balances */
    mapping (address => uint256) public balanceOf;

    /* Initializes contract with initial supply tokens to the creator of the contract */
    function MyToken(
        uint256 initialSupply
        ) {
        balanceOf[msg.sender] = initialSupply;              // Give the creator all initial tokens
    }

    /* Send coins */
    function transfer(address _to, uint256 _value) {
        require(balanceOf[msg.sender] >= _value);           // Check if the sender has enough
        require(balanceOf[_to] + _value >= balanceOf[_to]); // Check for overflows
        balanceOf[msg.sender] -= _value;                    // Subtract from the sender
        balanceOf[_to] += _value;                           // Add the same to the recipient
    }
}
```

Anyway I have a month or so to develop my project, and I hope I'll be able to share something interesting before next year. Apart from distributed ledger investigation, I've also met with the Network and Forensic research group this week and we started learning about tools we can use in different security puzzles and catch the flag events. We solved (alongside other hacking groups) a couple of funny examples.

<img src="{{ site.url }}/assets/images/dev.to/iVHfwLc.gif" style="display: block; margin: 0 auto;">

We started solving [this puzzles](http://forensicscontest.com/puzzles) that you might also be interested in solving. In the [first](http://forensicscontest.com/2009/09/25/puzzle-1-anns-bad-aim) puzzle "Ann’s Bad AIM" we are security experts trying to catch an spy in a company. In this case, the analyzed network is given to us using a .pcap file, which we opened with [Wireshark](https://www.wireshark.org/) (I personally also used [tcpdump](https://dev.to/terceranexus6/security-sprint-week-2---choosing-a-nice-point-to-sniff-and-using-tcpdump-for-packet-analysis--e9) to save it in a log and read it on my own terminal, which I find comfortable) and it was a lot of fun, even if we had to stop in the middle for that day. If you are brave enough, there are even Perl options for the solution. One of our members, for example, discovered a "*Here’s the secret recipe… I just downloaded it from the file server. Just copy to a thumb drive and you’re good to go >:-)*" message in the pcap file, using some filters, and we learned about the magic number of a file. [Magic numbers](https://en.wikipedia.org/wiki/List_of_file_signatures) are hex signatures used to identify or verify the content of a file. This is very useful for Network System Monitoring. I suggest, for further hex analysis, using **GHEX** (in Linux). To better manage our work, we will deploy our common stuff using Docker.

Our main option is to use [this framework](https://github.com/CTFd/CTFd) with Docker using `docker-compose up -d,` which already provides an easy deployment option. There's an already very complete guide on using this framework with Docker [here](https://medium.com/@rkkautsar/how-docker-helps-me-manage-a-capture-the-flag-competition-7af303c1de2), I'll personally also try homemade Docker deployment without the framework (as I like to control my own stuff) but for now it's a wonderful option.

To sum up, I have exciting things to work with for the next weeks, and I can't wait to share the development of everything. **Do you guys ever tried to solve a CTF puzzle game?** Have you ever tried to experiment with cryptocurrency related development? any tips on it?

*Originally written in: [https://dev.to/terceranexus6/security-sprint-week-3---distributed-ledger-system-and-our-first-catch-the-flag-training-dpj](https://dev.to/terceranexus6/security-sprint-week-3---distributed-ledger-system-and-our-first-catch-the-flag-training-dpj)*
