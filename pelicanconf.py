#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Wyatt Winters'
SITENAME = u'if have_idea == 1: type(topic,words)'
SITEURL = 'http://wyattwinters.com'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

SECTIONS = [('Blog', 'index.html'),
        ('Archive', 'archives.html'),
        ('About', 'pages/about.html')]

GOOGLE_ANALYTICS_ACCOUNT = ''

DEFAULT_DATE_FORMAT = '%d %m %Y'
GITHUB_URL = 'http://github.com/wywin'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_CATEGORY = 'Uncategorized'
DATE_FORMAT = {
'en': '%d %m %Y'
}
TWITTER_USERNAME = 'wyatt_winters'

PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_PAGINATION = 10

MAIL_USERNAME = 'blog'
MAIL_HOST = 'wyattwinters.com'


LINKEDIN_URL ='http://www.linkedin.com/in/wyattwinters'

DEFAULT_PAGINATION = 100

STATIC_PATHS = ["images"]

FILES_TO_COPY = (
				('extra/404.gif', '404.gif'),
				('extra/404.html', '404.html'),
				('extra/favicon.ico', 'favicon.ico'),
				('extra/CNAME', 'CNAME'),
				('extra/robots.txt', 'robots.txt'),
				('extra/pubkey.txt', 'pubkey.txt'),
				)
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '/home/wywin/src/pelican-themes/flasky'

PLUGIN_PATH = '/home/wywin/src/pelican-plugins'

PLUGINS=['sitemap',]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}