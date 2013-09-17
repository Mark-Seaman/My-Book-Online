#!/usr/bin/python
# Print an outline of the topics

from django.core.management.base import BaseCommand
from livebook.wiki_links    import print_outline
from sys                    import argv

class Command(BaseCommand):
    
    print_outline(argv[2])

    exit(0)
