#!/usr/bin/python
# Create a list of links from this page

from django.core.management.base import BaseCommand
from livebook.wiki_links         import get_file_links
from sys                         import argv

class Command(BaseCommand):
    for lnk in get_file_links(argv[2]):
        print lnk
    exit(0)
