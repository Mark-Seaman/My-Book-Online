#!/usr/bin/python
# Deploy the MyBook application to the Web Faction server

from django.core.management.base import BaseCommand
from livebook.book import directory
from sys           import argv

# Prune unwanted files
class Command(BaseCommand):
    print  directory(argv[2].replace('http://',''),argv[3])
    exit(0)
