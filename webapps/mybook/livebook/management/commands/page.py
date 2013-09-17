#!/usr/bin/python
# Deploy the MyBook application to the Web Faction server

from django.core.management.base import BaseCommand
from livebook.page import page
from sys           import argv



# Prune unwanted files
class Command(BaseCommand):
    print  page(argv[2])
    exit(0)
