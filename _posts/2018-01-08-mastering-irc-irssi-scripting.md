---
layout: post
title:  Mastering IRC tool Irssi + scripting
author: terceranexus6
image:
  feature: banners/header.jpg
tags: chat vintage irc perl
---

I must confess I'm a big fan of 80's and 90's tech. I grew up admiring *cyberpunk* stuff, wore green lab goggles until I was fourteen and used computers since I was three. I enjoy learning the newest tool for the tech field and be up to date, but I have a natural attraction for the classics. I admire them for being the beginning of everything we have now, and that way **I just wanted to learn about IRC channels for fun**.

<img src="{{ site.url }}/assets/images/dev.to/ELzh4.jpg" style="display: block; margin: 0 auto;">

But then I discovered a rather interesting tool for managing IRC in Linux terminal that allows you to **load perl scripts** on the go. At first I thought I could emulate some classic communications with friends but apart from that I might could take advantage of the scripting magic.

First of all, here's what I'm using:

- Linux (in my case, debian jessie) terminal
- Freenode irc channel
- Irssi for Linux
- Perl, python, bash or whatever scripting

So first of all is downloading the tool:

```
sudo apt-get install irssi
```

Once `irssi` is installed execute it, only write `irssi` in the terminal. In the `[(status)]` command line you can choose a nickname different from the one in the terminal using the command `/SET nick yournickname` if you don't use this, it will automatically catch your username from the terminal. You can also set a proxy like this:

```
/SET use_proxy ON
/SET proxy_address <Proxy host address>
/SET proxy_port <Proxy port>
```

Once you are set up, it's time to connect. First of all connect to the Freenode:

```
/CONNECT Freenode
```

Once you are in (you should wait a bit) join your channel using `/join thenameofyourchannel`.

These are the basics for a fast set up. For more information about the networks just use `/help network` in `[(status)]` command line. The same goes with the channels `/help channels`. For listing any of those use `/list networks` or `/list channels`. Also there are some useful commands:

```
/help [command] - more information about a command
/eval ${whatever} - evaluates the given command, for example S - server N - username
/cat file_dir/file - the same as bash cat command
/exec - executes commands in the background like, ls
/cd - same as linux terminal
/alias name command - give alias to custom commands. useful with online roleplaying
/ping user - ping an user. Also a Channel.
```

And much more. Apart from this, you can **set an automatic perl command that launches when starting irssi**. For example if you want a personal greeting, you should write this:

```
#hello.pl
#special greeting

print "Hello there master, welcome again.\n";
```

And save it in `~/.irssi/scripts/autorun/`. If you want to execute it yourself, save it in `~/.irssi/scripts`, and in the `[(status)]` command line just use `/script load hello.pl`. But also, you can execute them in the channel using `/exec perl ~/.irssi/scripts/hello.pl`, and not just Perl, anything. I tried to launch a Flask app with it using **Python** command. Now, once you discovered this, you can create better scripts in perl or take the ones in [this repo](https://scripts.irssi.org/).

But! more interesting. The irssi saves a **log file** in `~/irclogs/$tag/$0.log` by default but you can change it using `/SET autolog_path ~/new_path/irclogs/$tag/$0.log`. And then I thought, hey what use could I get from these? Well, depending on your needs. For example you can create a script that checks the log and looks for certain words to work. For example, imagine you have a raspberry pi and install the irssi. You gets the script work in the background and open the irc channel. You leave the rpi and go away, next you connect to the irc anywhere and write the *magic word*.

Like this, you can go and play with all the options this has. Of course,let's not forget about **ALL the online role playing** options here...

**Anyway irssi is easy to use, flexible and fun.** I recommend you to try it!

*Also written in: [https://dev.to/terceranexus6/mastering-irc-tool-irssi--scripting-3jp6](https://dev.to/terceranexus6/mastering-irc-tool-irssi--scripting-3jp6)*
