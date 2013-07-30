title: "Dota 2 on Xubuntu 13.04"
date: 2013-06-20 00:50
comments: false
categories: linux games wine
---

***UPDATE*** Valve was awesome enough to do a native Linux port. [Get that version instead!](http://store.steampowered.com/app/570/)

Dota 2 is a really good game. Linux is really good. Out of the box, they don't play nice together. Let's fix that!

<!-- more -->

First, let's lay out the details.

I am running 

 * Xubuntu 13.04 Raring Ringtail
 * AMD Phenom(tm) II X4 970 Processor
 * Nvidia GTX 465 with 319.23 drivers
 * wine-1.6-rc2


and on all low settings I can easily get a solid 60 FPS in-game, with no dips. Your mileage may vary according to your hardware. 

## Drivers
First, we need the latest drivers from Nvidia (or ATI, depending on your card). The open source drivers are fine for day-to-day computing, but they don't handle games so well. A rather sexy fellow named Harold Hope made a delightful and very colorful script called [sgfxi](http://smxi.org/site/donations.htm) that makes installing your latest and greatest binary drivers very easy. Grab a root shell, and run
``` 
cd /usr/local/bin && wget -Nc smxi.org/sgfxi && chmod +x sgfxi
```

Now we need to get into a non-X shell. CTRL-ALT-F1 will do the job nicely. Log in, and run
```
sudo sgfxi
```
and follow the wizard. You may have to do this once or twice, to remove the old free-as-in-speech drivers before installing the binary drivers. It should be easy to follow.

## Getting Wine
Man, Wine has improved *so much* since I last messed with it around the Gutsy Gibon days. Let's add their PPA
```
sudo add-apt-repository ppa:ubuntu-wine/ppa && sudo apt-get update && sudo apt-get install wine winetricks
```
and wait for all the goodies to download.

After Wine is installed and situated, we will follow a modified/updated version of the writeup on [WineHQ](http://appdb.winehq.org/objectManager.php?sClass=version&iId=24458). 

Here's what we need to do:
```
WINEPREFIX=~/.wine_dota2/ winecfg
```
will set up a new bottle (haha wine puns) to be our Dota 2 machine. 
## Getting Steamy
Now, let's install Steam!
```
wget http://winetricks.org/winetricks
WINEPREFIX=~/.wine_dota2/ sh winetricks --no-isolate steam
```
Follow the wizard, let it update, and log into Steam. Download Dota 2, and add some launch options. Right click Dota 2 in the games list -> properties -> set launch options. These work for me:
```
-novid -console -noforcemaccel -forcemspd -useforcedmparms -high -nod3d9ex -nod3dx -noborder -gl
```
"-novid" disables the intro video. "-console" enables the console. "-noforcemaccel -forcemspd -useforcedmparms" disables mouse acceleration. "-high" starts the game with high CPU priority. "-nod3d9ex -nod3dx -gl" are video tweaks to make it run smoother. "-noborder" starts the game in a borderless window, making alt-tabbing out should the need occur much easier. 

It should be noted that with Wine wine-1.6-rc2 and the setup outlined above, I am not affected by any of the bugs on the [WineHQ page](http://appdb.winehq.org/objectManager.php?sClass=version&iId=24458). I'm not sure if that's luck of my hardware or improvements in Wine. There is some hitching when the game is loading things (hero selection, playing new sounds for the first time) but once everything is loaded up, the hitching disappears. Very playable, and not booting into Windows anytime soon!

I don't have comments on this blog because comments are for jerks and weirdos. Email me if you have questions or comments, and I will edit the post accordingly. glhf!