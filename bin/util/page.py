
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
def doc_path(host,user,path):
    dir = domain_directory(host)
    if not dir: 
        dir = '.'
    user = user.replace('Anonymous', 'Public')
    doc = user+'/'+dir+'/'+path
    log_page(doc)
    return environ['pd']+'/'+doc


# Either format the doc or return the redirect page
def page_redirect (host,user,path):
    doc = doc_path(host,user,path)
    if exists(doc):
        if not isfile(doc):
            index = join(doc,'Index')
            if exists(index):
                return path+'/Index'
            return  path+'/Index/missing'
    else:
        return path + '/missing' 
 

# Format the doc contents into HTML
def show_page(host,user,path):
    return format_doc(doc_path(host,user,path))


# Put the document text in storage
def put_page(host,user,path):
    write_file(doc_path(host,user,path), read_input())


# Get the document text from storage
def get_page(host,user,path):
    return read_text(doc_path(host,user,path))

