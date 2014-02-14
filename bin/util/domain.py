
from datetime   import datetime
from os         import system,environ
from os.path    import isfile, exists,join
from re         import compile, IGNORECASE, DOTALL
from random     import choice
from sys        import argv, stdin

from wiki  import *
from files import read_text
from tabs  import print_all_tabs


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

def show_domain_doc():
    path   = ['','']
    if len(argv)>1: 
        path = argv[1].split('/')

    doc = join(environ['pd'], doc_path(path))
    log_page(doc)
    text = read_text(doc)
    if text:
        print_all_tabs(text)
        return
    if exists(doc+'/Index'):
        redirect_path(path)
        return
    print 'No file found, '+doc

