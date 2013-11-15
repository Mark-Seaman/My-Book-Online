from django.conf.urls import patterns, include, url
from django.contrib     import admin
from livebook.views     import *
from livebook.message   import message

from settings           import ROOT_DIR,MEDIA_URL

admin.autodiscover()

slides_dir  = { 'document_root' : '/home/seaman/Documents/Slides/'  }
media_dir   = {'document_root': ROOT_DIR+MEDIA_URL}

urlpatterns = patterns(
    '',

    #url(r'^show/new',              'slides.views.add_view'),
    #url(r'^show/(?P<id>.*)$',      'slides.views.text_view'),

    url(r'^slides/(?P<path>.*)$',   'django.views.static.serve', slides_dir),
    url(r'^media/(?P<path>.*)$',    'django.views.static.serve', media_dir),

    url(r'^admin/',                 include(admin.site.urls)),
    url(r'^accounts/profile/',      hoa_site),
    url(r'^login$',                 'django.contrib.auth.views.login'),
    url(r'^logout$',                'django.contrib.auth.views.logout'),

    # App Thumper views
    url(r'^register$',  'doc.thumper.register'),

    # old private view
    url(r'^private$',               private_home),
    url(r'^private/(?P<topic>[A-Za-z0-9\-\/\_\.]+)$', private),

    # Hammer views
    url(r'^$',                              'doc.views.home'),
    url(r'^store/(?P<title>[\w\-_./]+)$',   'doc.views.store'),
    url(r'^(?P<title>[\w\-_./]+)/new$',     'doc.views.new'),
    url(r'^(?P<title>[\w\-_./]+)/missing$', 'doc.views.missing'),
    url(r'^(?P<title>[\w\-_./]+)/add$',     'doc.views.add'),
    url(r'^(?P<title>[\w\-_./]+)/edit$',    'doc.views.edit'),
    url(r'^(?P<title>[\w\-_./]+)/delete$',  'doc.views.delete'),
    url(r'^(?P<title>[\w\-_./]+)$',         'doc.views.doc'),

    # old views
    #url(r'^$',                             guides),
    #(r'^(?P<topic>[A-Za-z0-9\-\/\_\.]+)$', livebook),
    #(r'^livebook/(?P<topic>[A-Za-z0-9\-\/\_\.]+)$', livebook),
)
