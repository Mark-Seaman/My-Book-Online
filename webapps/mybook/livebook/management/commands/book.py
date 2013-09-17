#!/usr/bin/python
# Deploy the MyBook application to the Web Faction server

from django.core.management.base import BaseCommand
from livebook.book import book
from sys           import argv



# Prune unwanted files
class Command(BaseCommand):
    print 'BOOK:',argv[2]
    print  '\n'.join(book(argv[2]))
    exit(0)
