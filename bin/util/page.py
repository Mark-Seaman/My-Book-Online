
from datetime   import datetime
from os         import system,environ
from os.path    import isfile, exists,join
from re         import compile, IGNORECASE, DOTALL

from wiki  import *
from tabs  import format_tabs, format_doc
from files import read_input, read_text, write_file, is_writable
from domain import domain_directory

# Log the page hit in page.log  (time, ip, user, page, doc) 
def log_page(doc):
    logFile=environ['p']+'/logs/user/doc.log'
    f=open(logFile,'a')
    f.write(str(datetime.now())+',  '+doc+'\n')
    f.close()


# Convert a url to a directory
def doc_path(path):
    dir = domain_directory(path[0])
    if not dir: 
        dir = '.'
    if len(path)>1:
        user = path[1].replace('Anonymous', 'Public')
    else:
        user = 'Public'
    return '/'.join( [user,dir] + path[2:] )


# Convert a url to a directory
def public_doc_path(path):
    path = doc_path(path.split('/'))
    path[1] = 'Public'
    return doc_path(path)


# Return the new url to visit  (Implied path host/user/doc)
def redirect_path(doc):
    path = doc.split('/')
    url = '/'.join(path[2:])
    return url


# lookup the path for the doc for this url
def map_doc_path(url):
    doc = doc_path(url.split('/'))
    log_page(doc)
    return join(environ['pd'], doc)


# Either format the doc or return the redirect page
def doc_redirect (url):
    doc = map_doc_path(url)
    if exists(doc):
        if not isfile(doc):
            index = join(doc,'Index')
            if exists(index):
                return redirect_path(url) + '/Index'
            else:
                return redirect_path(url) + '/Index/missing'
    else:
        return redirect_path(url) + '/missing' 


# Either format the doc or return the redirect page
def show_page(url):
    doc = map_doc_path(url)
    if exists(doc) and isfile(doc):
        return format_doc(doc)


# Put the document text in storage
def put_page(doc):
    write_file(map_doc_path(doc), read_input())


# Get the document text from storage
def get_page(doc):
    if not doc_redirect(doc):
        print read_text(map_doc_path(doc))
    else:
        print "redirect:%s/missing" % doc_redirect(doc)


# #  Formatter to add tabs to the HTML formatting
# def print_tab_doc(filename):
#     print format_doc(filename)

