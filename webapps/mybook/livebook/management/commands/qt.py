#!/usr/bin/python
# Deploy the MyBook application to the Web Faction server

from django.core.management.base import BaseCommand
from livebook.contents      import *
from livebook.wiki_links    import *
from sys                    import argv



# Prune unwanted files
class Command(BaseCommand):
    print  navigation_text (NOTES_DIR+'/SuperPower/Chapter1')
    print navigation_text (NOTES_DIR+'/Gallery/volcano/1016')
    exit(0)
