#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Charles Holmes'
SITENAME = u'afrocheese'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = u'en'

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-toc']

# Static content
STATIC_PATHS = ['static']

# Theme
THEME = 'themes/pelican-twitchy'
PYGMENTS_STYLE = 'github'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
SOCIAL = [
    ('Github', 'https://github.com/afrocheese'),
    ('Twitter', 'https://twitter.com/afrocheese'),
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
