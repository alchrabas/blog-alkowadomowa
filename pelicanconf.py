#!/usr/bin/env python

AUTHOR = 'Aleksander Chrabąszcz'
SITENAME = 'Alkowa Domowa'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'pl'

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['render_math']

THEME = './voce'

DEFAULT_DATE_FORMAT = '%d.%m.%Y'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAGS_URL = 'tag/{slug}.html'

IGNORE_FILES = [".venv", "scripts"]

USER_LOGO_URL = "/images/logo.png"

EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
    'images/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'images/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'images/favicon-96x96.png': {'path': 'favicon-96x96.png'},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GOOGLE_ANALYTICS_ID = "UA-207318322-1"
GOOGLE_ANALYTICS_PROP = "alkowadomowa.pl"

DISQUS_SITENAME = "alkowadomowa"

# Blogroll
LINKS = (
    ('Strona główna', '/'),
    ('Nalewki', '/nalewki'),
    ('O mnie', '/o-mnie'),
)

# Social widget
SOCIAL = (
    ("Mail", "mailto:alkowadomowa@chrabasz.cz"),
    ("GitHub", "https://github.com/alchrabas/blog-alkowadomowa"),
    ("Twitter", "https://twitter.com/alchrabas"),
    ("Instagram", "https://www.instagram.com/alkowadomowa/"),
)

DEFAULT_PAGINATION = 10

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

