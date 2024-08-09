AUTHOR = 'Alexandros Psalidopoulos'
SITENAME = 'AP'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Athens'

DEFAULT_LANG = 'en'

THEME = 'themes/pneumatic'



# ---------------------------------------------------
# relevant to the pneumatic theme only:
ICONS_PATH='images/icons'
SITENAME='Alexandros Psalidopoulos'
BIO_TEXT='Currently living in Athens, Greece. Website work in progress.'
FOOTER_TEXT=''
SITE_AUTHOR='Alexandros Psalidopoulos'
TWITTER_USERNAME='alexandrospsal'
GOOGLE_PLUS_URL=''
INDEX_DESCRIPTION=''
SIDEBAR_LINKS=[]
GOOGLE_FONTS=[]
SOCIAL_ICONS = [
    ('https://www.linkedin.com/in/alexandros-psalidopoulos-78854615b/', 'Linkedin', 'fa-linkedin'),
    ('https://github.com/alexandrospsal', 'Github', 'fa-github'),
    ('https://instagram.com/alexandros.psal', 'Instagram', 'fa-instagram'),
    ]
# SOCIAL_ICONS	List of tuples in the form (link, title, icon-class)
THEME_COLOR='#000000'
# DOMAIN	Used for Google Analytics and Twitter Cards <meta>


ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'


PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Disable authors, categories, tags, and category pages
DIRECT_TEMPLATES = ['archives']
CATEGORY_SAVE_AS = ''
# ---------------------------------------------------







# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True