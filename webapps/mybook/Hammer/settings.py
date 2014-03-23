# Django settings for Hammer project.

from socket import gethostname
from os.path import abspath, dirname, join
from os import environ
from local_settings import DATABASES

#-----------------------------------------------------------------------------
# General settings

if not environ.has_key('p'): environ['p'] = environ['HOME']

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Mark Seaman', 'mark.seaman@shrinking-world.com'),
)

MANAGERS = ADMINS


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Denver'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

#-----------------------------------------------------------------------------
# Static media


ROOT_DIR  = dirname(abspath(__file__))
DOC_ROOT  = join(ROOT_DIR, 'user_doc')
NOTES_DIR = DOC_ROOT
LOGIN_URL = '/login'


# Examples: "http://mybookonline.com/media/"
MEDIA_URL = ''

# Example: "http://mybookonline.com/static/"
STATIC_URL = '/static/'

# Example: "/var/www/mybookonline.com/static/"
STATIC_ROOT = ''

# Additional locations of static files
STATICFILES_DIRS = (
)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

if  gethostname().startswith('seaman-'):
    MEDIA_ROOT = join(ROOT_DIR, 'media/')
else:
    MEDIA_ROOT = ''

#-----------------------------------------------------------------------------
# Templates and apps

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-k_yz2l3s_r4lt^b^*y@+j^ef^m=cf9^rnw#w-@nuzwi036x(t'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Hammer.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'Hammer.wsgi.application'

#TEMPLATE_DIRS = (join(dirname(__file__), '..', '..', 'app', 'templates').replace('\\', '/'),)
TEMPLATE_DIRS = (
    "/home/seaman/webapps/mybook/templates",
    "/home/seaman/Projects/mybook/webapps/mybook/templates",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'doc',
    'livebook',
)


#-----------------------------------------------------------------------------
# Logging

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
