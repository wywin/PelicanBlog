Title: Rubustat - the Raspberry Pi Thermostat
Date: 2013-10-01 16:48
Slug: rubustat-the-raspberry-pi-thermostat
Categories:

It's been some time since I actually wrote a blog post. Mostly because I have had nothing original to write, and partially because school keeps me busy. Let's change that!

I figured I would do a proper writeup on one of my summer projects - the Rubustat.

##Disclaimer

While I enjoy programming and enjoyed making this project immensely, I make no claims that I am good at programming. High level Pythoners may wish to look away. However, the only way to get better is practice, right?

##The inspiration

While at home for the summer, the existing thermostat in the house was acting up. It wouldn't keep programmed settings, the display was a cheap LCD that was losing contrast, and it was generally an annoyance. Having ordered a couple Pis earlier in the summer (because why not, it's a $40 computer!), I quickly began researching the potential of a Raspberry Pi thermostat.

####Of course, someone already did it.

As is typically the case on the internet, someone had already implemented my idea, and was selling products. [Nich Fugal](http://makeatronics.blogspot.com) had done exactly what I planned - [hooked up an RPi to his thermostat](http://makeatronics.blogspot.com/2013/04/raspberry-pi-thermostat-hookups.html). Handily enough, he offers the schematics and parts list he used! He also makes and [sells pre-made boards](http://makeatronics.blogspot.com/2013/06/24v-ac-solid-state-relay-board.html) for easy solder-and-go purposes!

However, I found his [software](http://makeatronics.blogspot.com/2013/04/thermostat-software.html) implementation lacking, but admittedly functional.

##The project

<center>
![](/images/thumbnails/ubustat/rubustathookups_regular.jpg)<br>
The controller board (left) and thermometer (right) crammed into the GPIO ribbon cable
<br>
I soldered the connector on the PCB backwards. Oops!
</center>

While Nich did most of the hard work hardware wise, I knew I could improve the software. While I am by no means a web developer, I am halfway handy with Python, and Flask fulfilled my purposes well enough. Let's go through my amateur-at-best design process!

###The name

Being a huge fan of lazy portmanteaus, I knew it had to be something raspberry related. The genus of the common raspberry is Rubus, so the name "Rubustat" practically made itself.

###The daemon

The daemon was originally based on a straight copy of Nich's [software](http://makeatronics.blogspot.com/2013/04/thermostat-software.html). However, I found it to be a tad unstable, and used more external bash calls than I liked. While his use of outdoor temperature to determine heating vs cooling is clever, the primary user of the end product (my dad) preferred more manual control.

After some extended debugging, I found that it was difficult to cleanly kill off my daemon (which at this point was a endless while loop). I instead opted to use a daemon class written by [Sander Marechal](http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/) which worked better. To fully stabilize/debug the daemon, I had to add stale PID checks.

In it's final version, the daemon handles the GPIO pins, sqlite logging (initially to make fancy graphs, but the thermometer I ended up using wasn't precise enough to make any graphs except ones that look like sawteeth), email error reporting (implemented because one of the alligator clips fell off on the temporary hardware and the house got outstandingly warm), and monitoring of the status file to know what temperature and mode to be in.

I also got to learn the word "hysteresis", so that's fun.

###The web UI

<center>
![](/images/thumbnails/ubustat/phoneui_regular.png) <br>
Firefox for Android on a Galaxy Note<br>
<br>
![](/images/thumbnails/ubustat/desktopui_regular.png)
<br> Firefox on Windows
</center>
<br>
This is primary reason the project was created. We could get any number of cheap, difficult-to-control thermostats, or we could get any of a slightly smaller number of expensive, web-enabled thermostats. The beauty of this project is we got a cheap, web-enabled thermostat! You don't have to learn how to program the schedules! I doesn't even have the ***ability*** to run schedules! (feature forthcoming?)

The web UI looks like a hot pile of garbage. More importantly, however, is it a **functional** hot pile of garbage. I don't have much exciting to say about this interface. It writes directly to the status file, which is in turn read by the daemon and adjusts the GPIO pins accordingly.

The reason the interface is so dang big is because I have no idea how to do reactive design, and the idea was for the UI to be mobile-friendly. In a very inelegant way, it is mobile-friendly. I did however implement [fastclick](https://github.com/ftlabs/fastclick) so it feels like you're poking a button rather than a Slowbro.

Another in the line of features inspired by catastrophic failure is the daemon status section. I felt rather silly when the web UI started without the daemon, so the adjustments made would have no effect. While playing with this functionality, I included the GPIO statuses above that, the colors corresponding to the LEDs on the physical board.

###The wrap up

I took *no* security precautions in the code itself. If you make a Rubustat of your own ***DO NOT*** expose the RPi to the outside internet. It is a dreadful idea. It works just fine when confined to the LAN.

I'm actually pretty pleased with how this thing turned out. While it is by no means particularly pretty or elegant, it gets the job done, and doesn't catch fire. That's a success in my book.

If you want to look over the source or run it yourself, hit the [Github repo](https://github.com/wywin/Rubustat).