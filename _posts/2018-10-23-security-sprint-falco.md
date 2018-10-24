---
layout: post
title: Security Sprint - Falco
author: terceranexus6
image:
  feature: banners/header.jpg
tags: security docker linux
---

Hello again! Continuing with the security sprint articles, this week I'm going to talk about Falco. Nope! I'm not talking about the musician, I'm referring to an open source tool that allows us to monitor behavioral activity and detect anomalous activity in applications.

<img src="{{ site.url }}/assets/images/dev.to/falco_running.gif" style="display: block; margin: 0 auto;">

Some examples of anomalous detection are shell running inside a container in production, SQL injection attacks, rootkit’ed host, unauthorized process, write to non user-data directory, etc. An example of Falco rule is:

```
- macro: bin_dir
  condition: fd.directory in (/bin, /sbin, /usr/bin, /usr/sbin)

- macro: open_write
  condition: (evt.type=open or evt.type=openat) and evt.is_open_write=true and fd.typechar='f'

- macro: package_mgmt_binaries
  items: [dpkg, dpkg-preconfigu, rpm, rpmkey, yum, frontend]

- rule: Write below binary dir
  desc: an attempt to write to any file below a set of binary directories
  condition: bin_dir and evt.dir = < and open_write and not proc.name in (package_mgmt_binaries)
  output: "File below a known binary directory opened for writing (user=%user.name command=%proc.cmdline file=%fd.name)"
priority: WARNING
```

The most important part is the condition rule, a filter applied to each system call. The final output is a notification message using a mix of plain text and information from the event. We will see and example, but first, let's install Falco.

```
$ sudo -s
# mkdir /etc/falco
# cd /etc/falco
/etc/falco# curl https://raw.githubusercontent.com/katacoda-scenarios/sysdig-scenarios/master/sysdig-falco/assets/falco.yaml -o falco.yaml
/etc/falco# curl https://raw.githubusercontent.com/katacoda-scenarios/sysdig-scenarios/master/sysdig-falco/assets/falco_rules.yaml -o falco_rules.yaml
/etc/falco# touch /var/log/falco_events.log
```

`falco.yaml` configures the Falco service, `falco_rules.yaml` contains the threat detection patterns and `falco_events.log` will be used as the events log file. For mounting those...

```
# docker pull sysdig/falco
# docker run -d --name falco --privileged -v /var/run/docker.sock:/host/var/run/docker.sock -v /dev:/host/dev -v /proc:/host/proc:ro -v /boot:/host/boot:ro -v /lib/modules:/host/lib/modules:ro -v /usr:/host/usr:ro -v /etc/falco/falco.yaml:/etc/falco/falco.yaml -v /etc/falco/falco_rules.yaml:/etc/falco/falco_rules.yaml -v /var/log/falco_events.log:/var/log/falco_events.log sysdig/falco
```

Now, let's get back to the example. In the [official documentation](https://sysdig.com/blog/selinux-seccomp-falco-technical-discussion/#falco) it explains how the rule monitors file opens to identify attempts to open a file. I'm going to try the same on my own container using `docker`:

<img src="{{ site.url }}/assets/images/dev.to/yoq11lw5egy8i3gg5ak7.png" style="display: block; margin: 0 auto;">

After playing around a bit, let's `exit` and tail our log.

```
tail /var/log/falco_events.log
```

<img src="{{ site.url }}/assets/images/dev.to/uzqfauhl5j2mlqy3vyfw.png" style="display: block; margin: 0 auto;">

That's it! Falco throws an advise.

<img src="{{ site.url }}/assets/images/dev.to/3D88214031.gif" style="display: block; margin: 0 auto;">

Welp, now let's try another example, any process trying to write to a non data directory. After `curl https://raw.githubusercontent.com/katacoda-scenarios/sysdig-scenarios/master/sysdig-falco/assets/falco_rules_step4.yaml -o falco_rules.yaml` and restarting docker falco:

<img src="{{ site.url }}/assets/images/dev.to/dnjoat5r6uya8p2c1m0m.png" style="display: block; margin: 0 auto;">

So, that's it! For more information on using docker and falco, check this [tutorial](https://www.katacoda.com/courses/docker-security/sysdig-falco) where the yaml files I used are hosted.

Hope you guys enjoyed this week Security Sprint!

*Also written in: [https://dev.to/terceranexus6/security-sprint-falco-e0o](https://dev.to/terceranexus6/security-sprint-falco-e0o)*
