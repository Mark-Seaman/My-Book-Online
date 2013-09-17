#!/usr/bin/python
# Deploy the MyBook application to the Web Faction server

from django.core.management.base    import BaseCommand, CommandError
from os                 import system, remove, path

delete_files = [
    'manage.py-localhost',
    'settings.py-localhost',
    'data/all.json',
    'media/media',
    'test.html',
    'etc-apache2-httpd.conf',
]
# Prune unwanted files
class Command(BaseCommand):
    print "Prune unwanted files"
    for f in delete_files:
        if path.exists(f): remove(f)
    exit(0)
