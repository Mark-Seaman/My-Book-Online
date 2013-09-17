#!/usr/bin/python
# Print an outline of the topics

from django.core.management.base import BaseCommand
from livebook.wiki      import print_nested_topics
from sys                import argv
from os.path            import exists


# Copy the web content to the server 
class Command(BaseCommand):
    
    if not exists(argv[2]):
        print 'Could not open file,', argv[2]
    else:
        print_nested_topics(argv[2])

    exit(0)
