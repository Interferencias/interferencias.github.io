---
layout: post
title: CA pairs creation
author: inversealien
image:
  feature: banners/header.png
tags: security english linux
---

I found a nice topic to write about: **CA pairs creation with openssl in Linux**. A digital certificate tells an application (a browser, for example) that a public key is owned by the one who calls it. This allows relying parties to rely upon signatures made to this public key. OpenSSL is a free and open-source cryptographic library that provides several command-line tools for handling digital certificates. So, for now we are working on `root` so first of all I suggest to `sudo -i` and then do the rest.

In this case we are working on a directory we are going to call 'ca' in root so first of all let's create it using `mkdir /root/ca` (remember we already did sudo -i, so be careful) and inside it let's create a bunch of directories we will find useful later. Also we are giving permissions (read+write+execute) to the owner. If you have doubts about chmod permissions in this article I suggest to check this amazing [chmod calculator](https://chmod-calculator.com/) I found. Finally I'm also creating an index.txt to keep track of signed certificates, a plain database.

```
cd /root/ca
mkdir certs crl newcerts private
chmod 700 private
touch index.txt
echo 1000 > serial
```

Now we should define the CA Root Configuration file, in which we should define different modules for openssl to read later. This is [the one](https://github.com/terceranexus6/SPSI/tree/master/normal) we are using. On [ca] which is compulsory, we indicate to follow the indications in [CA_default]. In [CA_default] we should point to the directory we already create (ca) and the rest of the directories we created inside it. In [policy_strict] and [policy_loose] we should define the policy for both root and intermediate (we will explain later) root CA. Like this, there are other modules to take care about, also some customized extensions we can call as commands with openssl later, in this case [v3_ca] and others, like [ usr_cert ] and [ server_cert ] for signing both un client or server cases or ocsp extension when signing the Online Certificate Status Protocol (OCSP) certificate.

Once our configuration file is completely defined, we might make sure it's on `/root/ca` and proceed to create the root key. You can use RSA or DSA, many examples shows RSA, so for creating a different option I'm gonna use DSA. For using DSA, we should create at first the parameters:

```
openssl dsaparam -out dsaparam.pem 4096
```

We are using 4096 because we will still be able to sign server and client certificates of a shorter length. And then, we can create the key:

```
openssl gendsa -aes256 -out private/ca.key.pem dsaparam.pem
```

We will be asked for a passphrase, once it's done let's take care of the permissions with `chmod 400 private/ca.key.pem`. 

For creating a root certificate, we check we are in `/root/ca` and then use openssl with `req`, which we previously defined in the configuration file. 

```
openssl req -config openssl.cnf -key private/ca.key.pem -new -x509 -days 7300 -sha256 -extensions v3_ca -out certs/ca.cert.pem
``` 

It will ask us a passphrase and some details for the certificate (name, state and such). Once it's done, let's go again with the permissions with `chmod 444 certs/ca.cert.pem`. For verifying the content, we can use `openssl x509 -noout -text -in certs/ca.cert.pem` and the output should show us algorithm, date, entity that signed the certificate, and the certificate itself. Boom!

And for better security we should create an intermediate certificate inside the `/root/ca` directory. For this, let's create a `/root/ca/intermediate` directory and then, inside it, let's create some more directories, like we did before with `/root/ca`

```
cd /root/ca/intermediate
mkdir certs crl csr newcerts private
chmod 700 private
touch index.txt
echo 1000 > serial
```
Next, is to `echo 1000 > /root/ca/intermediate/crlnumber` to keep track of certificate revocation lists. Now, as we did before we should take care of the configuration file, which is pretty like the one we already defined but changing the directories in [CA_default] for `/root/ca/intermediate` ones. 

```
[ CA_default ]
dir             = /root/ca/intermediate
private_key     = $dir/private/intermediate.key.pem
certificate     = $dir/certs/intermediate.cert.pem
crl             = $dir/crl/intermediate.crl.pem
policy          = policy_loose
``` 
Also the extension v3 name for v3_intermediate_ca. The modified version completed is [here](https://github.com/terceranexus6/SPSI/tree/master/intermediate).

Once we have this, we can create the intermediate key. Be careful to return to `/root/ca` for this. We will use a similar command as before, changing the path of the key for the one in `/intermediate/`.

```
openssl gendsa -aes256 -out intermediate/private/ca.key.pem dsaparam.pem

```
And, as always, taking care of the permissions with `chmod 400 intermediate/private/intermediate.key.pem`. For creating the intermediate certificate signing request (CSR), we should be in `/root/ca` and be careful to specify the CA configuration of `/intermediate/`, like this:

```
openssl req -config intermediate/openssl.cnf -new -sha256 -key intermediate/private/intermediate.key.pem -out intermediate/csr/intermediate.csr.pem
``` 
When asking for the details, don't forget to add in the _Common name_ the "intermediate tag", for example: "John Doe Intermediate CA". For creating the certificate, in `/root/ca`:

```
openssl ca -config openssl.cnf -extensions v3_intermediate_ca -days 3650 -notext -md sha256 -in intermediate/csr/intermediate.csr.pem -out intermediate/certs/intermediate.cert.pem
```
We give permissions with `chmod 444 intermediate/certs/intermediate.cert.pem` and then we should verify our work. For verifying the details we wrote:

```
openssl x509 -noout -text -in intermediate/certs/intermediate.cert.pem
```
And for verifying it against the root CA:

```
openssl verify -CAfile certs/ca.cert.pem intermediate/certs/intermediate.cert.pem
```
which should return an **OK** of everything went fine. Finally, we create a certificate chain file for letting the application check the CA against the root. 

```
cat intermediate/certs/intermediate.cert.pem \
      certs/ca.cert.pem > intermediate/certs/ca-chain.cert.pem
chmod 444 intermediate/certs/ca-chain.cert.pem
```
And, **tadaaah!** we are done! I'm still learning to Sign server and client certificates, which I hope to be the next step. Hope you guys found this part interesting! again, you can guys try RSA instead of DSA and other algorithms instead of aes. For example, **Camellia** is supposed to be as strong as AES, but less used in Europe due to default security settings in companies. I suggest to try different kinds of algorithms, just for fun!
