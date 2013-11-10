from django.conf.urls import patterns, include, url
from django.contrib import admin
from os.path import join

from settings import MEDIA_ROOT

admin.autodiscover()

lib_dir = {'document_root': MEDIA_ROOT}

urlpatterns = patterns(
    '',

    # static files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', lib_dir),

    # admin
    url(r'^at-admin',  include(admin.site.urls)),
    url(r'^login$',     'django.contrib.auth.views.login'),
    url(r'^logout$',    'django.contrib.auth.views.logout'),

    # App Thumper views
    url(r'^register$',  'doc.thumper.register'),
    url(r'^(?P<title>[\w\-_./]+)/enable$',  'doc.thumper.enable'),
    url(r'^(?P<title>[\w\-_./]+)/disable$', 'doc.thumper.disable'),

    # Hammer views
    url(r'^$',                              'doc.views.home'),
    url(r'^store/(?P<title>[\w\-_./]+)$',   'doc.views.store'),
    url(r'^(?P<title>[\w\-_./]+)/new$',     'doc.views.new'),
    url(r'^(?P<title>[\w\-_./]+)/missing$', 'doc.views.missing'),
    url(r'^(?P<title>[\w\-_./]+)/add$',     'doc.views.add'),
    url(r'^(?P<title>[\w\-_./]+)/edit$',    'doc.views.edit'),
    url(r'^(?P<title>[\w\-_./]+)/delete$',  'doc.views.delete'),
    url(r'^(?P<title>[\w\-_./]+)$',         'doc.views.doc'),

)
