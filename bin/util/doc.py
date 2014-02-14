from datetime   import datetime
from os         import system,environ
from os.path    import isfile, exists,join
from re         import compile, IGNORECASE, DOTALL
from random     import choice
from sys        import argv, stdin

#-----------------------------------------------------------------------------
# File processing





#---------------------------
# Old code

from sys        import argv, stdin
from os.path    import exists,join
from os         import environ,system
from util.tabs  import print_tab_doc, print_all_tabs
from util.wiki  import convert_html
from util.files import read_file, write_file


# Create html file contents from stdin
def page_html():
    text = stdin.read().split('\n')
    return convert_html(text)


# Create html file contents from stdin
def print_page_html():
    text = stdin.read() 
    print_all_tabs(text)


# Show the formatted document for the file
def doc_show(doc):

    d = doc[doc.find('/')+1:]
    path = join(environ['pd'],doc)

    if not exists(path):
        index = join(path,'Index')
        if exists(index):
            print "redirect:%s/Index" % d
        else:
            print "redirect:%s/missing" % d
    else:
        system ('hammer-show '+doc)


# Put the document text in storage
def doc_put(doc):
    write_file(doc, read_input())


# Get the document text from storage
def doc_get(doc):
    return read_file(doc)

