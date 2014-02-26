
from datetime   import datetime
from os         import system,environ
from os.path    import isfile, exists,join
from re         import compile, IGNORECASE, DOTALL

from wiki  import *
from tabs  import print_tab_doc
from files import read_input, read_text, write_file, is_writable


# Log the page hit in page.log  (time, ip, user, page, doc) 
def log_page(doc):
    logFile=environ['p']+'/logs/user/doc.log'
    f=open(logFile,'a')
    f.write(str(datetime.now())+',  '+doc+'\n')
    f.close()


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
def show_domain_doc(url):
    doc = map_doc_path(url)
    if exists(doc) and isfile(doc):
        print_tab_doc(doc)


# Put the document text in storage
def put_domain_doc(doc):
    print 'WRITE1:',doc
    doc = map_doc_path(doc)
    print 'WRITE2:',doc
    write_file(doc, read_input())


# Get the document text from storage
def get_domain_doc(doc):
    if not doc_redirect(doc):
        doc = map_doc_path(doc)
        print read_text(doc)
    else:
        print "redirect:%s/missing" % doc_redirect(doc)

