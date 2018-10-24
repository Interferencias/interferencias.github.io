---
layout: post
title: Fun with secrets
author: terceranexus6
image:
  feature: banners/header.jpg
tags: security maths cryptography
---

Security in computer science is a huge point every individual and company. Communications (either between humans or human-network or whichever online communication) are susceptible to be sniffed or manipulated.

For example, using **http** instead of **https** is insecure (sometimes even tagged by your browser as untrustful) as information that goes through it is not encrypted and someone is able to impersonate your accounts with the collected data. This is why [https everywhere](https://www.eff.org/es/https-everywhere) and [privacy badger](https://www.eff.org/es/privacybadger) are recommended for secure browsing.

**But when we say "*encrypt*", what are we referring to?**

Back in the days when computers weren't a thing, cryptography already existed. Maths has always been there to protect our communications. Sometimes it was a letter, sometimes it was a note or a messenger, but there were tons of witty ways of hiding messages.

For example, the "*monoalphabetic substitution system*" is a bijective application

```
e: A -> A
```

Being A an alphabet an A* the chain aggregation over A with arbitrary length:

```
e: A* -> A*, [e(X0 X1 ...) = e(X0) e(X1)...]
```

An example of this is the Cesar cipher. This consist on cyclic displacement to the right, mathematically (with displacement = +3):

```
e: Z23 -> Z23, [e(x) = x+3 (mod 23)]
```

Note it's Z23 because Roman alphabet length = 23.

Unfortunately this method (that you might have used as a kid to pass notes) has a huge security hole: **letters Periodicity Analysis**. Let me explain myself. Every language has an already study that shows the periodicity a letter appears in such language. Even if the letters are mixed, if we take this numbers (in English, for example, most used letters are E or T) we can guess the message.

There's a similar cipher version called "*Polyalphabetic substitution system*". This system uses a keyword to cipher all the message. (It's like repeating monoalphabetic many times). Let me show you an example:

- our keyword is TUX
- and our message is HELP ME OBI WAN KENOBI

We have our alphabet tagged with numbers, like this:

<div class="bootstrap">
  <table class="table table-bordered table-striped table-hover table-condensed table-responsive">
  	<thead>
  		<tr>
  			<th>
  				A
  			</th>
  			<th>
  				B
  			</th>
  			<th>
  				C
  			</th>
  			<th>
  				...
  			</th>
  			<th>
  				X
  			</th>
  			<th>
  				Y
  			</th>
  			<th>
  				Z
  			</th>
  		</tr>
  	</thead>
  	<tbody>
  		<tr>
  			<td>
  				1
  			</td>
  			<td>
  				2
  			</td>
  			<td>
  				3
  			</td>
  			<td>
  				...
  			</td>
  			<td>
  				23
  			</td>
  			<td>
  				24
  			</td>
  			<td>
  				25
  			</td>
  		</tr>
  	</tbody>
  </table>
</div>

- So TUX is equal to 19,20,23
- And HELP ME OBI WAN KENOBI is equal to 7,4,11,15,12,4,14,1,8,22,0,13,10,4,13,14,1,8

Now we set the numbers in TUX in the message, like this:

<div class="bootstrap">
  <table class="table table-bordered table-striped table-hover table-condensed table-responsive">
  	<thead>
  		<tr>
  			<th>
  				H
  			</th>
  			<th>
  				E
  			</th>
  			<th>
  				L
  			</th>
  			<th>
  				P
  			</th>
  			<th>
  				M
  			</th>
  			<th>
  				E
  			</th>
  			<th>
  				O
  			</th>
  			<th>
  				B
  			</th>
  			<th>
  				I
  			</th>
  			<th>
  				W
  			</th>
  			<th>
  				A
  			</th>
  			<th>
  				N
  			</th>
  			<th>
  				K
  			</th>
  			<th>
  				E
  			</th>
  			<th>
  				N
  			</th>
  			<th>
  				O
  			</th>
  			<th>
  				B
  			</th>
  			<th>
  				I
  			</th>
  		</tr>
  	</thead>
  	<tbody>
  		<tr>
  			<td>
  				T
  			</td>
  			<td>
  				U
  			</td>
  			<td>
  				X
  			</td>
  			<td>
  				T
  			</td>
  			<td>
  				U
  			</td>
  			<td>
  				X
  			</td>
  			<td>
  				T
  			</td>
  			<td>
  				U
  			</td>
  			<td>
  				X
  			</td>
  			<td>
  				T
  			</td>
  			<td>
  				U
  			</td>
  			<td>
  				X
  			</td>
  			<td>
  				T
  			</td>
  			<td>
  				U
  			</td>
  			<td>
  				X
  			</td>
  			<td>
  				T
  			</td>
  			<td>
  				U
  			</td>
  			<td>
  				X
  			</td>
  		</tr>
  		<tr>
  			<td>
  				19
  			</td>
  			<td>
  				20
  			</td>
  			<td>
  				23
  			</td>
  			<td>
  				19
  			</td>
  			<td>
  				20
  			</td>
  			<td>
  				23
  			</td>
  			<td>
  				19
  			</td>
  			<td>
  				20
  			</td>
  			<td>
  				23
  			</td>
  			<td>
  				19
  			</td>
  			<td>
  				20
  			</td>
  			<td>
  				23
  			</td>
  			<td>
  				19
  			</td>
  			<td>
  				20
  			</td>
  			<td>
  				23
  			</td>
  			<td>
  				19
  			</td>
  			<td>
  				20
  			</td>
  			<td>
  				23
  			</td>
  		</tr>
  	</tbody>
  </table>
</div>

And now we add the value setted to the original value (in mod 25).

<div class="bootstrap">
  <table class="table table-bordered table-striped table-hover table-condensed table-responsive">
  	<thead>
  		<tr>
  			<th>
  				H
  			</th>
  			<th>
  				E
  			</th>
  			<th>
  				...
  			</th>
  			<th>
  				B
  			</th>
  			<th>
  				I
  			</th>
  		</tr>
  	</thead>
  	<tbody>
  		<tr>
  			<td>
  				7 + 19
  			</td>
  			<td>
  				4 + 20
  			</td>
  			<td>
  				...
  			</td>
  			<td>
  				1 + 20
  			</td>
  			<td>
  				8 + 23
  			</td>
  		</tr>
  		<tr>
  			<td>
  				A
  			</td>
  			<td>
  				Y
  			</td>
  			<td>
  				...
  			</td>
  			<td>
  				V
  			</td>
  			<td>
  				F
  			</td>
  		</tr>
  	</tbody>
  </table>
</div>

And so HELPMEOBIWANKENOBI = AYIIGBHVFPUKDYKHVF

This system is a little bit more complex but also vulnerable to periodicity analysis **if we know the keyword length**.

We also have Hill cipher, which consist in matrix cipher.

For example, we can cipher the word MATH, using the key matrix = ([32],[15])

- M,A = ([12],[0]) in the alphabet
- T,H = ([10],[7])

```
([32],[15])([12],[0]) = ([0],[12])
([32],[15])([10],[7]) = ([71],[54]) = ([35][18]) **in mod 36 (alphanumeric)**
```

So MATH = AM95

This system is way more secure than the others. There's also the so called transposition systems in which consist in changing the letters order (the periodicity analysis also fails here). For example:

<img src="{{ site.url }}/assets/images/dev.to/cryptography-from-demaratus-to-rsa-4-638.jpg" style="display: block; margin: 0 auto;">

This lasts were very used in the WW2, alongside One-time-pad and notebooks ciphers.

In general, there are certain rules a cryptosystem must follow. For example, the secret must be hidden with the algorithm and the power of this algorithm is in it's form, not the way the algorithm is hidden to the public. (This is the main problem some users have with privative cryptography). Most of the mathematical rules can be found in *[Communication theory of secrecy systems](http://pages.cs.wisc.edu/%7Erist/642-spring-2014/shannon-secrecy.pdf)* , a study by C.E. Shannon about the matter. Current ciphering works in bits, not letters, and latests cryptography studies are developing quantum cryptography, for the upcoming of quantum computers. This could mean a complete chaos for regular computer cryptography, and we shall be on guard!

On the mean time we can keep writing love notes and letter in basic cryptography. It is said that it worked with *Don Juan* , who made a woman fall in love with him after he deciphers a message she cipher with Vigenere.

*Originally written in: [https://dev.to/terceranexus6/fun-with-secrets-2p3](https://dev.to/terceranexus6/fun-with-secrets-2p3)*
