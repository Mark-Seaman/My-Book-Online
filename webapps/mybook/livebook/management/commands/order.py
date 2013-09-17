#!/usr/bin/python

from django.core.management.base    import BaseCommand
from livebook.page_order            import reading_order
from sys                            import argv

class Command(BaseCommand):
    print '\n'.join (reading_order(argv[2]))
    exit(0)
