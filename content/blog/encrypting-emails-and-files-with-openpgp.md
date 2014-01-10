title: Encrypting emails and files with OpenPGP
date: 2013-05-26 12:58
comments: false
categories: encryption openPGP
---
This was originally written for a blog I co-run with my sister, over at nesasio.com (hence the domain in the screenshots). Actively writing to a single blog is hard enough, let alone multiple. Oh well, here's this post.

Have you ever wanted to make sure nobody else saw an email or file except who you wanted? Have you ever wanted to feel like a super spy? Well, through the magic of math (and it is very close to magic!), a system called OpenPGP makes that possible!

<!-- more -->

Without getting too detailed, OpenPGP and the toolset we will use - GNU Privacy Guard (GPG) uses a type of encryption called "asymmetric" as opposed to symmetric. Symmetric encryption uses the same key for scrambling and unscrambling a message. Asymmetric encryption used two different keys- a public key and private key, each with different purposes.

Let's figure out what we need to send secret messages. Because of long-standing traditions, encryption scenarios refer to two characters: Alice and Bob. Alice is you, and Bob is who you want to talk to. Let's look at the process we need to follow to safely get secrets to Bob, using a paint metaphor.

<center>
![](/images/openPGPTutorial/500px-Diffie-Hellman_Key_Exchange.gif)
</center>
We will be working on Windows 7, but the process will likely be similar for all versions of Windows, both forward and past.
<h2><strong>Installation and creating your keypair</strong></h2>
<h4>Step 1: the common paint</h4>
First, we need to get the GPG tools! The download can be found at http://gpg4win.org/download.html. We will be using Gpg4win 2.1.0, the most recent stable release. Once downloaded, install it! The defaults should be fine for our purposes. On the screen labeled "Defined trustable root certificate", check to skip configuration. This is related to another encryption type, and will not affect us. You can view the README if you wish.

After install, you should see a program called Kleopatra. This is the graphical user interface (GUI) that makes it easier to work with GPG keys and various operations related to GPG. Launch it.

<h4>Step 2: your secret color</h4>
Once Kleopatra is open, it will look fairly empty and boring. We need to create a keypair! Choose File -&gt; New Certificate, and select "Create a personal OpenPGP key pair".

<center>
![](/images/openPGPTutorial/Email1.png)
</center>

You will be prompted for name, email, and a comment should you choose one. These can be anything, so you can use your real name, a fake name, or any bit of text you like! If you want to make a "professional" key pair, it is recommended to use your full, real name. For now, I will create a key pair for this site!


<center>
![](/images/openPGPTutorial/Email2.png)
</center>

The next screen is verifying the information you entered. If it looks right, hit create key. 
Now we have a little work to do. Think of a good, complicated password. I would recommend following xkcd 936:

<center>
![](https://sslimgs.xkcd.com/comics/password_strength.png)
</center>

Enter your password (twice, to make sure you didn't fat finger it), and your key pair will be created!

<center>
![](/images/openPGPTutorial/Email3.png)
</center>

<h2><strong>Encrypting with your new keypair</strong></h2>

<center>
![](/images/openPGPTutorial/Email4.png)
</center>

With your newly created keypair, you have generated your secret color. We have the mixture of step 3, and need to send our mixture to someone else to do the rest of the steps; to create a common secret. You have to get someone else's mixture - in this case, Bob's blueish mix he made on step 3. Bob can be anyone, Bob is your intended recipient. The recipient could be a friend following this tutorial, or <a href="http://www.gpg4win.org/doc/en/gpg4win-compendium_13.html#sec_publishPerEmail">the GPG robot known as Adele</a>.

For this tutorial, we will talk to Adele.

Computers, handy things they are, can make our mixture sending, scrambling, and unscrambling easier for us. To that end, we will use the email program Thunderbird. Download it here: <a href="https://www.mozilla.org/en-US/thunderbird/">https://www.mozilla.org/en-US/thunderbird/</a> The standard defaults will do just fine. Launch Thunderbird after the install finishes.

You can make Thunderbird the default client for email, newsgroups, and feeds if you so choose. These choices will not affect the tutorial.

<center>
![](/images/openPGPTutorial/Email5.png)
</center>

Thunderbird, as a way of making money, offers the ability to buy a new email address, of which Mozilla, the people who make Thunderbird, get a little cut. For now, we will skip this and use an existing email.

<center>
![](/images/openPGPTutorial/Email6.png)
</center>

Thunderbird is pretty clever here, and should be able to figure out the correct settings for your email address, if you use any sizeable mail service. Hit done, and Thunderbird will retrieve your mail.

<center>
![](/images/openPGPTutorial/Email7.png)
</center>

 Now that we have our email, we need to add the encryption part! In an attempt to look snazzy, Thunderbird hides the menu bar by default. Press the ALT key, and select Tools -&gt; Add-ons. In the search box in the upper right, type in "enigmail", and the first option should be the right one. Hit install, and restart Thunderbird after it finishes.

<center>
![](/images/openPGPTutorial/Email8.png)
</center>

Now we have all the software we need, so now it's time to use it! Press the "Write" button, and let's send an email to Adele!

<center>
![](/images/openPGPTutorial/Email9.png)
</center>

Before we send the email, we have to tell Enigmail to send our mixture to Adele. Assuming you used the same email in your keypair (your secret color) as you did when setting up Thunderbird, it should be smart enough to find the correct key / secret color.

<center>
![](/images/openPGPTutorial/Email10.png)
</center>

Make sure "Sign Message" is checked, then send your email! Your passphrase box will pop up, to make sure you are who should really be using your secret color. Enter your passphrase, and the mail will go out.

<center>
![](/images/openPGPTutorial/Email11.png)
</center>

In your reply, there will be an important bit of information- Adele's public key - her mixture. At the top of the Thunderbird window, hit "Decrypt", and import her public key.

Now, compose a new email to Adele, but this time, in the OpenPGP menu, check both Encrypt and Sign! And we're done! For anyone that isn't a robot, repeat the process. Send them a signed message, have them reply with a message that they signed, and then sign and encrypt all emails between the pair of you!

Here's the decrypted version of the email:

<center>
![](/images/openPGPTutorial/Email12.png)
</center>

and the scrambled version!

<center>
![](/images/openPGPTutorial/Email13.png)
</center>

<h1>What about files?</h1>
We already did the hard work with generating and exchanging our keys, so files are pretty simple to work with!

First, I've made this super-secret treasure map I only want Adele to see!

<center>
![](/images/openPGPTutorial/File1.png)
</center>

Right click on the file in Windows Explorer and select "Sign and Encrypt"

<center>
![](/images/openPGPTutorial/File2.png)
</center>

After some thinking, the Sign and Encrypt wizard from Kleopatra will appear.

<center>
![](/images/openPGPTutorial/File3.png)
</center>

Next, select who you want to encrypt it to. I'll encrypt it to Adele, as I already have her public key handy.

<center>
![](/images/openPGPTutorial/File4.png)
</center>

If I try to continue, Kleopatra gives me this warning:

<center>
![](/images/openPGPTutorial/File5.png)
</center>

While this can be handy in some circumstances, let's encrypt it to myself also.

<center>
![](/images/openPGPTutorial/File6.png)
</center>

Next, select who to sign as. I only have my own private key (secret color), so that seems like the best choice.

<center>
![](/images/openPGPTutorial/File7.png)
</center>

Once that's done, it will process the file(s) you set to be signed and encrypted.

<center>
![](/images/openPGPTutorial/File8.png)
</center>

Since I chose to save the unscrambled file after I made the scrambled one, my folder now looks like this:

<center>
![](/images/openPGPTutorial/File9.png)
</center>

Now, the secretTreasure.png.gpg file can only be opened by Adele, and myself. However, she's a robot, and doesn't do file-handling yet. 

While this is by no means a complete or comprehensive OpenPGP lesson, this is enough to get you up and running, and passing encrypted emails and files back and forth between your friends. The neat part about the key exchange (the paint color exchange) is that the public keys (the mixtures) can be shared openly! As long as your secret key (secret color) stays secret, the system will be (relativley) secure!
If you are interested in more, <a href="https://en.wikipedia.org/wiki/Public-key_encryption">I would recommend Wikipedia as a starting point. </a>There is lots of documentation and articles on public key encryption, especially OpenPGP.</p>
