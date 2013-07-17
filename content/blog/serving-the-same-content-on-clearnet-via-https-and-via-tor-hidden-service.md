title: "Serving identical content on HTTPS and Tor hidden service"
date: 2013-07-03 21:52
comments: false
categories: encryption tor mod_rewrite apache
---
I recently came into an interesting problem- I wanted to serve the same website over the clearnet (the regular internet) using *only* HTTPS, and serve that same content over a Tor hidden service. I assume you have at this point a web server installed (I like Apache) that will successfully serve HTTPS exclusively, but need to add the Tor.

<!-- more -->

1. Install Tor. You will want to use [the Tor Project's repos](https://www.torproject.org/download/download-unix.html.en) to make sure you have the most up-to-date version.

2. Edit your torrc. It is likely at /etc/tor/torrc. Uncomment the following lines:

        HiddenServiceDir /var/lib/tor/hiddenService/
        HiddenServicePort 80 127.0.0.1:80
    
    and/or adjust them accordingly. If you have Apache listening on 443 (for HTTPS) and 80, you should be set with this config.

3. Restart Tor to apply new settings. In Debian Wheezy: 

        sudo /etc/init.d/tor restart
        
4. Get your hostname

        sudo cat /var/lib/tor/hiddenService/hostname
    
    should be a string of characters followed by ".onion".

5. Backup your private key

        sudo cp /var/lib/tor/hiddenService/privateKey /root
    
6. Adjust your public html folder to move users based on their requested site

    1. Enable mod_rewrite (if not already)
        
            sudo a2enmod rewrite    
        
    2. Edit (on a default Debian Wheezy apache install) /var/www/.htaccess and add:
                
            RewriteEngine On
            RewriteCond %{HTTP_HOST} !^youronionaddress.onion$
            RewriteCond %{HTTPS} !on
            RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI}
        
7. Test it out!

The .htaccess does the following:

1. Is the user not requesting the .onion? (Tor hidden services get confused when you talk HTTPS to them)

2. Is HTTPS not on? (If they don't want the .onion, and HTTPS isn't on, we should turn it on!)

3. If conditions 1 and 2 are met:

3. Send them back to whatever address they requested, but with HTTPS.

Granted this does NOT hide the location of your webserver, but it will allow Tor users to save precious exit node bandwidth by staying inside the Tor network. This is especially neat because changes made on the clearnet will be reflected on the hidden service side, and vice versa.  