#!/usr/bin/python
# Deploy the MyBook application to the Web Faction server

from django.core.management.base    import BaseCommand, CommandError
from scripts.utilities              import execute_remote_command, copy_from_remote

# Download the MyBook application from the Web Faction server
class Command(BaseCommand):
    print "Download MyBook"
    execute_remote_command('bin/savedata')
    copy_from_remote()
    exit(0)
