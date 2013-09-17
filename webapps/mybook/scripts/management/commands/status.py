#!/usr/bin/python
# Deploy the MyBook application to the Web Faction server

from django.core.management.base    import BaseCommand, CommandError
from os         import system
from os.path    import exists

# List files 
class Command(BaseCommand):
    print "Status of project files"
    if exists ("."):
        system ('git status')
    exit(0)
