# Deploy the MyBook application to the Web Faction server

from django.core.management.base    import BaseCommand, CommandError
from scripts.utilities  import execute_remote_command, copy_from_remote
from os                 import system, chdir, environ
from settings           import project


# Copy the code to the server and restart Apache
class Command(BaseCommand):

    print "Save MyBook Data on WebFaction host"
    execute_remote_command('bin/savedata '+project)
    copy_from_remote()

    exit(0)
