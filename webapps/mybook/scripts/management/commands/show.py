#!/usr/bin/python
# Deploy the MyBook application to the Web Faction server

from django.core.management.base    import BaseCommand, CommandError
from os         import system
from sys        import argv
from settings   import project_url

# Show MyBook in a web browser
class Command(BaseCommand):
    print "Reading MyBook"
    system ('rbg firefox http://localhost/mybook/SuperPower/Home')
        
    exit(0)
