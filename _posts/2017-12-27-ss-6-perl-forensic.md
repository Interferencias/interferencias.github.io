---
layout: post
title: Security Sprint&#58 Week 6 - Perl, forensic and new limits
author: terceranexus6
image:
  feature: banners/header.jpg
tags: forensic scripting security perl
---

Again my weekly security sprints arrives in late, but I hope *not too late* as this time, I'm experimenting with dangerous new horizons, such as [Perl](https://dev.to/jj/introduction-to-grammars-with-perl6-75e) and **Forensics**. I approached to Perl with respect and, yes why not saying it, *fear*. First of all everyone, except my [cloud computing teacher](https://dev.to/jj), warned me about the complexity of this language. Anyway I tried to made it the easy way, and searched for help in an [already prepared script for security](https://github.com/fwaeytens/dnsenum/blob/master/dnsenum.pl) I found on GitHub. The script is quite clear and organized which helped me to both learn perl and study security applications with it. For example, for doing a basic monitoring getting hosts' addresses:

```
# (1) get the host's addresses
printheader ("Host's addresses:\n");
my $res = Net::DNS::Resolver->new(  tcp_timeout => $timeout,
                    udp_timeout => $timeout,
                    defnames => 0);

$res->nameservers($dnsserver) if $dnsserver;

my $packet = $res->query($domain);
if ($packet) {
    foreach my $rr (grep { $_->type eq 'A' } $packet->answer) {
        printrr($rr->string);
        xml_host($rr);
        push @results, $rr->address
            if $rr->name =~ /$domain$/;
    }
}
elsif ($verbose) {
    warn " ", $domain ," A query failed: ", $res->errorstring, "\n";
}
```

The `my $res = Net::DNS::Resolver->new(...)` creates a brand new variable called res which has the definition described in (...). After defining it, it creates a packet variable which is equal to the domain of the dns, and pass through a filter in which, if the packet is successfully catched, creates a string which saves an specific type of packets ('A' in this case). Once this part is understood, the rest are quite similar, for example in the second option, which gets the name servers, it says:

```
foreach my $rr (grep { $_->type eq 'NS' } $packet->answer) {
        #...
    }
```

Or maybe, we can encounter a slightly different parts, such as the scrapping:

```
if ($scrap) {
    printheader ("Scraping ".$domain." subdomains from Google:\n");
    my @tmp = googlescraping();
    if (scalar @tmp) {
        #print STDOUT "\n Performing nslookups:\n";
        launchqueries(\&nslookup, map { $_ .= '.'.$domain } @tmp);
    }
}
```

In which it gets the current domain and scrap subdomains from Google.Scalar forces `@tmp` to be interpreted in scalar context and returns the lenght of it. In this case if the return is true, a query for nslookup is launched, using a translation to `@tmp` in to the corresponding characters.

<img src="{{ site.url }}/assets/images/dev.to/perl_camel.jpg" style="display: block; margin: 0 auto;">

In any case this script is highly customizable and contains all the basic elements required for packet analyzing.

After investigating about perl for security scripting, I also took some time in Forensics. For that, I bought [this book](https://www.packtpub.com/networking-and-servers/learning-network-forensics), apart from other things. The basic goals of forensic is to investigate an already corrupted system, due to an exploit taking advantage of a vulnerability. The steps for a programmer to build a malware are:

- Reconnoiter (identify potential targets)
- External information gathering (vulnerability identification)
- Target penetration (malware comes into play)
- Privilege escalation (the malware steps up)
- Persistence (the malware tries to build a stable performance and tries to stay in the system at all cost)

Malware analysis involves capturing a sample of the malware and performing a static or dynamic analysis on it (a common test in CTF games) but forensic involves analyzing an already compiled sample and performing reversing engineering in order to understand what the malware was supposed to do.

<img src="{{ site.url }}/assets/images/dev.to/107230875-56a1e28c3df78cf7726f9c57.jpg" style="display: block; margin: 0 auto;">

To perform Forensic investigation, we should perform "TAARA" methodology. TAARA stands for:

<img src="{{ site.url }}/assets/images/dev.to/7pfexofecj1pshwkmylm.jpg" style="display: block; margin: 0 auto;">

- **Trigger**: study the context of the compromised system/network in order to determine if anything is *weird*. For example, the books says "*Multiple outbound connections from an internal host in a short span of time could indicate a compromised host being used to attack the external systems*". Also Communications with block listed malicious IP addresses or URLs could mean the host is compromised.
- **Acquire**: This part is complicated for the expert, which should take special care of the national law regarding compromising data or essential information. Also the work of analyzing the evidence should not change the evidence itself as it's an important part of the case. Once the data is acquired a deduction effort should be made, Had sensitive data been successfully collected? Was The attacker technically savvy and quite aware of the security perimeter? all of this.
- **Analyze**: This is probably the slower part, in which the sensitive data we already acquired must be studied, for example querying **WHOIS** in suspicious IPs. In this part, a covert image of both the memory and media of the print server is made and preserved.
- **Report**: YAY! Documentation, we all love that, don't we? Yes, our investigation must be properly written, it should basically be **clear, concise and purposeful**. It must have Introduction, information available and assumptions, investigations, findings, and action taken.
- **Act**: It happened once, it's natural; it happens twice, it's a mistake. Once we already knew what happened, the team should focus on incident response. Which artifacts exist that can help us identify such an incident in the future? How can the future investigations improve?

This is pretty much everything I learned this week, I hope you guys found it interesting. I wish to use it in a national catch the flag event I signed in recently.

**What are your favorite security scripting languages? Did you performed a forensic investigation before?**

*Also written in: [https://dev.to/terceranexus6/security-sprint-week-6---perl-forensic-and-new-limits-2eci](https://dev.to/terceranexus6/security-sprint-week-6---perl-forensic-and-new-limits-2eci)*
