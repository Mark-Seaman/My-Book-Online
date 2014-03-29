
from datetime   import datetime
from os         import system,environ,chdir,getcwd
from os.path    import isfile, isdir, exists, join
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
    user = user.replace('Anonymous', 'Public')
    if dir: 
        doc = user+'/'+dir+'/'+path
    else:
        doc = user+'/'+path
    log_page(doc)
    return environ['pd']+'/'+doc


# Return the redirect page (after looking for Public & Private doc)
def page_redirect (host,user,path):

    doc = doc_path(host,'Public',path)
    index = join(doc,'Index')

    if exists(doc) and isfile(doc):
        return

    if exists(doc) and isdir(doc) and exists(index):
        return path+'/Index'
       
    if exists(doc) and isdir(doc) and not exists(index):
        return  path+'/Index/missing'

    doc = doc_path(host,user,path)
    index = join(doc,'Index')
    
    if exists(doc) and isfile(doc):
        return

    if exists(doc) and isdir(doc) and exists(index):
        return path+'/Index'
   
    return path + '/missing' 
 

# Format the doc contents into HTML
def show_page(host,user,path):

    doc = doc_path(host,'Public',path)
    if exists(doc):
        return format_doc(doc)

    doc = doc_path(host,user,path)
    if exists(doc):
        return format_doc(doc)        


# Put the document text in storage
def put_page(host,user,path):
    write_file(doc_path(host,user,path), read_input())


# Get the document text from storage
def get_page(host,user,path):
    return read_text(doc_path(host,user,path))

