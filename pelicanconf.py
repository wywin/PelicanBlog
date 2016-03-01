#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Wyatt Winters'

SITENAME = 'Wyatt Winters | Saving the world one computer at a time'
SITEURL = 'http://wyattwinters.com'
#SITEURL = 'http://localhost:8000'
TIMEZONE = 'UTC'

USE_FOLDER_AS_CATEGORY = True

DEFAULT_LANG = 'en'

SECTIONS = [('About', 'pages/about.html'),
        ('Blog', 'category/blog'),
        ('School-related', 'category/school')
        ]

DEFAULT_DATE_FORMAT = '%Y %m %d'
GITHUB_URL = 'http://github.com/wywin'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM= None
AUTHOR_FEED_RSS= None

DEFAULT_CATEGORY = 'Uncategorized'
DATE_FORMAT = {
'en': '%Y-%m-%d'
}
TWITTER_USERNAME = 'wyatt_winters'

PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_PAGINATION = 10

MAIL_USERNAME = 'blog'
MAIL_HOST = 'wyattwinters.com'

LINKEDIN_URL =''

STATIC_PATHS = ['images',
                'extra'
                ]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/pubkey.txt': {'path': 'pubkey.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/404.gif': {'path': '404.gif'},
    'extra/404.html': {'path': '404.html'},

    }

THEME = '/home/wywin/src/pelican-themes/flasky'

PLUGIN_PATH = '/home/wywin/src/pelican-plugins'

PLUGINS=['sitemap', 'thumbnailer']

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
IMAGE_PATH = '/home/wywin/src/PelicanBlog/content/images/'
THUMBNAIL_DIR = '/home/wywin/src/PelicanBlog/output/images/thumbnails'
THUMBNAIL_SIZES = {'regular' : '500x?'}
READERS = {"html": None}

AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

