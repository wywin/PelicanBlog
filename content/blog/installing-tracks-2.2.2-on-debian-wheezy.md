Title: Installing Tracks 2.2.2 on Debian Wheezy
Date: 2013-07-30 10:59
Slug: installing-tracks-2-2-2-on-debian-wheezy
Categories: apache ruby
status: draft
---
This is a chronicle of my first Ruby on Rails deployment, and the things I learned while doing so. It is likely straight-forward and obvious for Rails vets, but hopefully this will help people who just want to host and use the great tool that is [Tracks](http://getontracks.org/) without too much hassle. 

Assumed: apache2, mysql (you [can use sqlite3](https://github.com/TracksApp/tracks/blob/v2.2.2/doc/installation.textile#decide-on-a-database) but I won't cover that here)
optional: php5, phpmyadmin

First, let's create a database and user for Tracks to use.
I used phpmyadmin here because its easiest for me, but you can do it as you see fit.

```
CREATE USER 'tracks'@'localhost' IDENTIFIED BY '***';

GRANT USAGE ON * . * TO 'tracks'@'localhost' IDENTIFIED BY '***' WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0 ;

CREATE DATABASE IF NOT EXISTS `tracks` ;

GRANT ALL PRIVILEGES ON `tracks` . * TO 'tracks'@'localhost';
```

Switch into a root shell with 
```
sudo -s
```
for the remainder of the install process.

We need some packages, so let's install them:

```
apt-get install curl unzip libxslt-dev libxml2-dev libmysql-ruby libmysqlclient-dev libcurl4-openssl-dev apache2-threaded-dev libapr1-dev libaprutil1-dev
```

Tracks works best with Ruby 1.9.3, so we will use Ruby Version Manager (RVM) to install it. 

```
\curl -L https://get.rvm.io | bash
source /etc/profile.d/rvm.sh
rvm requirements
rvm install 1.9.3
```

Verify 
```
which ruby
``` 
and
```
which gem
```

both point to 
```
/usr/local/rvm/rubies/ruby-1.9.3-p448/bin/ruby
```
or similar.

Now we have Ruby all situated, it's time to get Tracks.
In /root run:
```
wget https://github.com/TracksApp/tracks/zipball/v2.2.2
mkdir /srv/tracks
unzip v2.2.2 -d /srv/tracks
```
Now Tracks is unzipped and ready to be configured.
```
cd /srv/tracks
gem install bundler
bundle install
gem install passenger
/usr/local/rvm/gems/ruby-1.9.3-p448/bin/passenger-install-apache2-module
```

append to /etc/apache2/apache2.conf
```
LoadModule passenger_module /usr/local/rvm/gems/ruby-1.9.3-p448/gems/passenger-4.0.10/buildout/apache2/mod_passenger.so
PassengerRoot /usr/local/rvm/gems/ruby-1.9.3-p448/gems/passenger-4.0.10
PassengerDefaultRuby /usr/local/rvm/wrappers/ruby-1.9.3-p448/ruby
PassengerDefaultUser www-data
```
RailsBaseURI
bundle exec rake db:migrate RAILS_ENV=production
bundle exec rake assets:precompile
