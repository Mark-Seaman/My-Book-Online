#!/usr/bin/python
# Deploy the MyBook application to the Web Faction server

from django.core.management.base    import BaseCommand, CommandError
from os         import system

# Load a fixture into the database
def load_data(table):
    system('manage.py loaddata data/'+table+'.json')
        
# Load the data tables for the MyBook in JSON format
class Command(BaseCommand):
    print "Load MyBook Data"
    system('manage.py syncdb')
    load_data('all')

    exit(0)
