# Django settings for mybook project.
import socket
from os.path import abspath, dirname

DEBUG = True
TEMPLATE_DEBUG = DEBUG

project     = 'mybook'
project_url = 'mybookonline.org'
project_db  = project
site_title  = "Shrinking World Guides"

ADMINS = (
    ('Mark Seaman', 'mark.seaman@shrinking-world.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     'seaman_'+project_db,
        'USER':     'seaman_'+project_db,      
        'PASSWORD': 'mds959SQ', 
        'HOST': '',
        'PORT': '',                
    }
}

if socket.gethostname().startswith('seaman-'):
    # Customizations for development servers
    #print "Development server"
    PYTHON_BASE         = '/usr/bin/python2.7'
    LOGIN_URL           = '/login'
    LOGOUT_URL          = '/login'
    NOTES_DIR           = 'user_doc'
    print 'host: local',NOTES_DIR
else: 
    # Customizations for production server
    #print socket.gethostname()
    PYTHON_BASE         = '/home/seaman/webapps/'+project+'/lib/python2.6'
    LOGIN_URL           = '/login'
    LOGOUT_URL          = '/login'
    NOTES_DIR           = '/home/seaman/webapps/'+project+'/MyBook'

ADMIN_MEDIA_PREFIX  = '/media/admin/'
MEDIA_URL           = '/media/'
ROOT_DIR            = dirname(abspath(__file__))


TIME_ZONE           = 'America/Denver'
LANGUAGE_CODE       = 'en-us'
SITE_ID             = 1
USE_I18N            = True


# Make this unique, and don't share it with anybody.
SECRET_KEY = '!ik7%d5#_9#!82o5!n&kzyh%hv#&9xeir4#6kt)1jnumezj2=#'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    "/home/seaman/webapps/mybook/templates",
    "/home/seaman/Projects/mybook/webapps/mybook/templates",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'doc',
    'livebook',
    #'slides',
    #'thoughts',
)

