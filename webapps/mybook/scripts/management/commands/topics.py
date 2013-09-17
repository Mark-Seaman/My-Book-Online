#!/usr/bin/python
# Deploy the MyBook application to the Web Faction server

from django.core.management.base    import BaseCommand
from book.data import book_url, is_orphan, root_topic, print_book_path
from book.topic import Topic
from book.book  import Book

# Handle None for the parent
def topic_number(t):
    if t==None:
        return str(t)
    else:
        return str(t.pk)

# Print the info for this book
def print_book_info(book):
    print '----------------------------------'
    print book.title, '[book = %s, root topic = %s]'%(book.pk,root_topic(book.pk).pk)
    print '----------------------------------'

# Create a orphan label if needed
def orphan_label(t):
    if is_orphan(t): return '** orphan **'
    return ''
    
# Print the info for one topic
def print_topic_info(t):
    print '%5d, %5s, '%(t.pk, topic_number(t.parent)),
    print '%-30s %s'%(t.title, orphan_label(t)),
    print_book_path(t)

# Show all of the topics in this book
def list_book_contents(book):
    print_book_info(book)
    for t in Topic.objects.all():
        if book==t.book:
            print_topic_info(t)

# List all of the topics in the database
def list_topics():
    for b in Book.objects.all():
        list_book_contents(b)

class Command(BaseCommand):   
    list_topics()
    exit(0)



