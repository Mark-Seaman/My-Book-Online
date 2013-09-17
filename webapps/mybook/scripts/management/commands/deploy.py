#!/usr/bin/python
# Deploy the MyBook application to the Web Faction server

from django.core.management.base    import BaseCommand, CommandError
from scripts.utilities  import execute_remote_command, copy_to_remote, publish
from os                 import system
from settings           import project_url

# Copy the code to the server and restart Apache
class Command(BaseCommand):
    print "Deploying the My Book Online to remote server"
    copy_to_remote()
    execute_remote_command('apache2/bin/restart')
    publish()
    system ('rbg firefox http://'+project_url)
    exit(0)
