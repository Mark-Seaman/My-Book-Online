#!/usr/bin/python
# Deploy the MyBook application to the Web Faction server

from django.core.management.base import BaseCommand
from book.topicText import print_book_topics
from book.export    import save_book_topics
from sys            import argv

class Command(BaseCommand):
    #print_book_topics(argv[2])
    save_book_topics(argv[2])

    exit(0)
