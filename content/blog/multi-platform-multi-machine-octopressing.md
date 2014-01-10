title: Multi-platform, multi-machine Octopressing
date: 2013-04-29 07:40
comments: false
categories: octopress multi-platform
---
Moving to Octopress was a bit of a challenge. Moving from the centralized, easy-to-manage Wordpress ecosystem to the distributed git-managed Octopress was a kick in the head. After acciedently and repeatedly overwriting my own posts and configurations, I decided to clear up the problem once and for all. 

Blogging on Octopress from  multiple machines, without doing it a *very* specific way, does bad, bad things to the blog. To rectify this, I make some scripts to treat the repo as the authoritative copy. 

<!-- more -->

Get latest version from repo
============================
Before starting to work I run this:
``` bash
#!/bin/bash
git fetch
git reset --hard origin/source
git pull origin source
cd ./_deploy
git fetch
git reset --hard origin/master
git pull origin master
cd ..
```
or on Windows:
```
call git fetch origin
call git reset --hard origin/source
call git pull origin source
cd ./_deploy
call git fetch origin
call git reset --hard origin/master
call git pull origin master
cd ..
```

to effectively mirror the existing stuff on the repo, destroying(!) any unpushed changes on my current machine.

After writing a post, page, or otherwise updating the site
==========================================================

``` bash
#!/bin/bash
rake generate
git add .
git commit -m "updating via script!"
git push origin source
rake deploy
```
or on Windows
```
call rake generate
call git add .
call git commit -m "updating via script on Windows!"
call git push origin source
call rake deploy
```

This will cleanly and nicely regenerate the static html, and update both the source and site in the repo. 

Setting up a computer to blog from for the first time
=====================================================
``` bash
$ git clone git@github.com:username/username.github.com.git
$ cd username.github.com
username.github.com$ git checkout source
username.github.com$ mkdir _deploy
username.github.com$ cd _deploy
username.github.com/_deploy$ git init
username.github.com/_deploy$ git remote add origin git@github.com:username/username.github.com.git
username.github.com/_deploy$ git pull origin master
username.github.com/_deploy$ cd ..
username.github.com$
```
After you do all that, make sure you get the latest version from the repo using the scripts in the top of the post.
Hope that helps!
