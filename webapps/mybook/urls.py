from django.conf.urls.defaults import *
from django.contrib     import admin
from livebook.views     import *
from livebook.message   import message

admin.autodiscover()

slides_dir = { 'document_root' : '/home/seaman/Documents/Slides/'  }
media_dir  = { 'document_root' : '/home/seaman/Documents/Web/'     }

urlpatterns = patterns(
    '',
    # doc views
    url(r'^doc$',                               'doc.views.home'),
    url(r'^doc/register$',                      'doc.views.register'),
    url(r'^doc/(?P<title>[\w\-_./]+)/missing$', 'doc.views.missing'),
    url(r'^doc/(?P<title>[\w\-_./]+)/(?P<template>[\w\-_./]+)/add$',  'doc.views.add'),
    url(r'^doc/(?P<title>[\w\-_./]+)/edit$',    'doc.views.edit'),
    url(r'^doc/(?P<title>[\w\-_./]+)/delete$',  'doc.views.delete'),
    url(r'^doc/(?P<title>[\w\-_./]+)$',         'doc.views.doc'),

    #url(r'^show/new',           'slides.views.add_view'),
    #url(r'^show/(?P<id>.*)$',   'slides.views.text_view'),

    url(r'^slides/(?P<path>.*)$', 'django.views.static.serve', slides_dir),
    url(r'^media/(?P<path>.*)$',  'django.views.static.serve', media_dir),

    (r'^admin/',            include(admin.site.urls)),
    (r'^accounts/profile/', hoa_site),
    (r'^login$',            'django.contrib.auth.views.login'),

    (r'unsubscribe$',      unsubscribe),
    (r'subscribe$',        subscribe),

    (r'^private$',          private_home),
    (r'^private/(?P<topic>[A-Za-z0-9\-\/\_\.]+)$', private),

    (r'^message$',          message),

    (r'^$',                 guides),
    (r'^(?P<topic>[A-Za-z0-9\-\/\_\.]+)$', livebook),
)
