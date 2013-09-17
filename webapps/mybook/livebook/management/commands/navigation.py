#!/usr/bin/python

from django.core.management.base    import BaseCommand
from livebook.wiki_links            import  navigation_text
from sys                            import argv

class Command(BaseCommand):
    print  navigation_text(argv[2])
    exit(0)
