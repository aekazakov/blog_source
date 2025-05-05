AUTHOR = 'aekazakov'
SITENAME = 'Have you tried turning it off and on again?'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("GenomeDepot documentation", "https://aekazakov.github.io/genome-depot/"),
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Social widget
SOCIAL = (
    ("Mastodon", "https://genomic.social/@aek"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
PORT = 8010
BIND = '0.0.0.0'

THEME = "relapse"
INDEX_SAVE_AS = 'blog_index.html'
USE_FOLDER_AS_CATEGORY = False
PATH_METADATA = r"(?P<path_no_ext>.*)\..*"
ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = "{path_no_ext}.html"
