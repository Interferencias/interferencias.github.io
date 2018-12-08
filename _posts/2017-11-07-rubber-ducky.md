---
layout: post
title: Rubber Ducky
author: terceranexus6
image:
  feature: banners/header.jpg
tags: ducky hack seguridad
---

You might have heard about the technique of Ducky debugging in which you tell a rubber ducky your dev problems and then you know how to solve them, but this is not the case, we are talking about *nasty* duckies here, not cute problem solvers ones.

Regardless the name, Rubber Ducky is the name of a hacking injection device that consist in a pen drive and a micro SD. The pack itself also comes with the case, and a couple of USB adapters.

<img src="{{ site.url }}/assets/images/dev.to/1_LxlmHycPbysH9w3ezFnEzw.jpeg" style="display: block; margin: 0 auto;">

The device imitates the human keyboard input, “Humans use keyboards. Computers trust humans” prays the motto. The process is simple, in the micro SD we save a program called “inject.bin” that we previously generated based in a code. We connect the micro SD in the duck and connect the code in the targeted computer, then it will make its magic.

<img src="{{ site.url }}/assets/images/dev.to/1_0dFQs9g3YLSiy64yxBN_4Q.jpeg" style="display: block; margin: 0 auto;">

Not long ago a friend of mine described hackers as some kind of magicians. They do their thing and no one knows how they do it, there’s a trick behind the curtain and you feel far away from knowing the truth. The trick in this case is fully documented on the [GitHub Wiki](https://github.com/hak5darren/USB-Rubber-Ducky/wiki), which explains how to write the code that afterwards will be encoded.

This is the official Command Breakdown

```
DELAY x — Delay in milli-secs
STRING xyz — types following characters
GUI — Windows Menu Key
GUI r — Windows Run box
COMMAND — OSX Command Key
UP | UPARROW — Up Key
DOWN | DOWNARROW — Down Key
LEFT | LEFTARROW — Left Key
RIGHT | RIGHTARROW — Right Key
CAPS |CAPSLOCK — Capslock Key
ENTER — Return/Enter key
SPACE — Spacebar
REPEAT x — Repeat previous command X times.
```

You can even use some (but not all) two or three key-combinations:

```
SHIFT-ENTER
CTRL-ALT-DEL
ALT-F4
```

With this and some knowledge of the Operating System we will be injecting the duck in, should be enough to make the easiest steps. Of course the responsibility of your actions are totally under you, this device could be used as a tester, as a social engineering companion or as a weapon. That’s up to you.

*Originally written in: [https://dev.to/terceranexus6/rubber-ducky-293](https://dev.to/terceranexus6/rubber-ducky-293)*
