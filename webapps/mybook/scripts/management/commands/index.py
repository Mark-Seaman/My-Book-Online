#!/usr/bin/python

from django.core.management.base import BaseCommand
from livebook.wiki      import navigation_bar 
from sys                import argv

class Command(BaseCommand):
    navigation_bar(argv[2])
    exit(0)
