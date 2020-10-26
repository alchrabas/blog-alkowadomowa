#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Aleksander Chrabąszcz'
SITENAME = 'Alkowa Domowa'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'pl'

THEME = './voce'

DEFAULT_DATE_FORMAT = '%d.%m.%Y'
ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAGS_URL = 'tag/{slug}.html'

USER_LOGO_URL = "/images/logo.png"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
  ('Strona główna', '/'),
  ('Nalewki', '/nalewki'),
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

