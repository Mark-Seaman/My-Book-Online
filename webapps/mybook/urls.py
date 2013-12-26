from django.conf.urls import patterns, include, url
from django.contrib     import admin

from settings           import ROOT_DIR,MEDIA_URL
from slides.views     import *
import doc.urls

admin.autodiscover()

slides_dir  = { 'document_root' : '/home/seaman/Documents/Slides/'  }
media_dir   = { 'document_root' : ROOT_DIR+MEDIA_URL}

urlpatterns = patterns(
    '',

    # static files
    url(r'^media/(?P<path>.*)$',    'django.views.static.serve', media_dir),

    # Slides
    #url(r'^show/new',              'slides.views.add_view'),
    #url(r'^show/(?P<id>.*)$',      'slides.views.text_view'),
    url(r'^slides/(?P<path>.*)$',   'django.views.static.serve', slides_dir),

    # Users
    #url(r'^admin/',                 include(admin.site.urls)),
    url(r'^login$',                 'django.contrib.auth.views.login'),
    url(r'^logout$',                'django.contrib.auth.views.logout'),
    url(r'^register$',              'doc.thumper.register'),

     # Hammer
    url(r'^',                       include(doc.urls)),
)
