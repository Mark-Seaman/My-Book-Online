#!/usr/bin/python

from django.core.management.base    import BaseCommand
from livebook.contents              import get_contents
from livebook.files                 import array_to_str
from sys                            import argv

class Command(BaseCommand):
    print  array_to_str(get_contents(argv[2]))
    exit(0)
