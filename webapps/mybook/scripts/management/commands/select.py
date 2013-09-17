#!/usr/bin/python
# Deploy the MyBook application to the Web Faction server

from django.core.management.base    import BaseCommand, CommandError
from scripts.utilities  import execute_remote_command
from os                 import system
from sys                import argv

# Prune unwanted files
class Command(BaseCommand):
    print "Select the development web site"
    system ('ln -f settings-'+argv[2]+'.py settings.py')
    system ('mb web dev')
    exit(0)
