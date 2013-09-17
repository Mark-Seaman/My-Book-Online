#!/usr/bin/python
# Deploy the MyBook application to the Web Faction server

from django.core.management.base import BaseCommand
from scripts.utilities  import publish
from os                 import system
from settings           import project_url

# Copy the web content to the server 
class Command(BaseCommand):
    print "Deploying the My Book content to remote server"
    publish()
    system ('rbg firefox http://shrinking-world.org')
    exit(0)
