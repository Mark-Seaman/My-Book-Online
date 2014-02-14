from datetime   import datetime
from os         import system,environ
from os.path    import isfile, exists,join
from re         import compile, IGNORECASE, DOTALL
from random     import choice
from sys        import argv, stdin

#-----------------------------------------------------------------------------
# File processing


# Log the page hit in page.log  (time, ip, user, page, doc) 
def log_page(doc):
    logFile=environ['p']+'/logs/user/doc.log'
    f=open(logFile,'a')
    f.write(str(datetime.now())+',  '+doc+'\n')
    f.close()


# Return the text from the file
def read_text(f):
    if exists(f) and isfile(f):
        return open(f).read()

#-----------------------------------------------------------------------------
# Domains

# Read the domain mapping from a file
def domain_map():
    map = {}
    for d in open(join(environ['pd'],'Domains')).read().split('\n'):
        d = d.split(' ')
        if len(d)==2:
            map[d[0]] = d[1]
    return map


# Convert a url to a directory
def doc_path(path):
    m = domain_map()

    domain = path[0]
    if m.has_key(domain):
        domain = m[domain]
    else:
        domain = '.'

    if len(path)>1:
        user = path[1].replace('Anonymous', 'Public')
    else:
        user = 'Public'

    file = path[2:]
    return '/'.join([user,domain] + file).replace('/./','/')


# Return the new url to visit
def redirect_path(path):
    print 'redirect:%s/Index' % '/'.join(path[2:])


# lookup the path for the doc for this url
def map_doc_path(url):
    doc = doc_path(url.split('/'))
    log_page(doc)
    return doc

#-----------------------------------------------------------------------------
# Page

def show_doc():
    path   = ['','']
    if len(argv)>1: 
        path = argv[1].split('/')

    doc = join(environ['pd'], doc_path(path))
    log_page(doc)
    text = read_text(doc)
    if text:
        print_all_tabs(text,doc)
        return
    if exists(doc+'/Index'):
        redirect_path(path)
        return
    print 'No file found, '+doc



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

