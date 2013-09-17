#!/usr/bin/python
# Deploy the MyBook application to the Web Faction server

from django.core.management.base    import BaseCommand, CommandError
from scripts.utilities  import execute_remote_command

# Copy the code to the server and restart Apache
class Command(BaseCommand):
    print "Restarting MyBook"
    execute_remote_command('apache2/bin/restart')
    exit(0)
