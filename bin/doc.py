
from datetime   import datetime
from os         import system,environ
from os.path    import isfile, exists,join
from re         import compile, IGNORECASE, DOTALL
from random     import choice
from sys        import argv, stdin

from wiki import *


#-----------------------------------------------------------------------------
# File processing


def log_page(doc):
    '''
    Log the page hit in page.log  (time, ip, user, page, doc) 
    '''
    logFile=environ['p']+'/logs/user/doc.log'
    f=open(logFile,'a')
    f.write(str(datetime.now())+',  '+doc+'\n')
    f.close()


def read_text(f):
    '''
    Return the text from the file
    '''
    if exists(f) and isfile(f):
        return open(f).read()

#-----------------------------------------------------------------------------
# Domains

def domain_map():
    '''
    Read the domain mapping from a file
    '''
    map = {}
    for d in open(join(environ['pd'],'Domains')).read().split('\n'):
        d = d.split(' ')
        if len(d)==2:
            map[d[0]] = d[1]
    return map


def doc_path(path):
    '''
    Convert a url to a directory
    '''
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


def redirect_path(path):
    '''
    Return the new url to visit
    '''
    print 'redirect:%s/Index' % '/'.join(path[2:])


def map_doc_path(url):
    '''
    lookup the path for the doc for this url
    '''
    doc = doc_path(url.split('/'))
    log_page(doc)
    return doc

#-----------------------------------------------------------------------------
# Page

# def do_command(cmd, input=None):
#     '''
#     Run the command as a process and capture stdout & print it
#     '''
#     try:
#         if input:
#             p = Popen(cmd.split(), stdin=PIPE, stdout=PIPE)
#             p.stdin.write(input)
#             p.stdin.close()
#         else:
#             p = Popen(cmd.split(), stdout=PIPE)
#             return  p.stdout.read()
#     except:
#         return '<h1>Command Error</h1>'+\
#             '<p>An error occurred while trying to execute the command:</p>'+\
#             '<p>COMMAND: %s</p>'%cmd +\
#             '<p>INPUT: %s</p>'%input


# def print_page_html():
#     '''
#     Create html file contents from stdin
#     '''
#     text = stdin.read() 
#     print_all_tabs(text)


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

