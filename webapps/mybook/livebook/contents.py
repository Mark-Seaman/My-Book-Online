from files              import read_file, exists, list_dirs, list_files
from hyperlink          import convert_links
from os                 import listdir, path
import os.path
from os.path            import isfile, isdir, dirname, join, basename
from settings           import NOTES_DIR
from wiki               import convert_line, text_to_html
from page_order         import navigation_text
from random             import randint

import re

# Select one random quote
def select_quote():
    quotes = read_file(join(NOTES_DIR,"SeamansLog/LifeLessons"))
    if len(quotes)>1:
        n = randint(0, len(quotes)-1)
        return  quotes[n]
    else:
        return 'No quote'

# Take off any trailing '/'
def remove_slash(path):
    if path[-1]=='/':
        return path[:-1]
    else:
        return path

# Get the file system directory matching this request
def get_directory(note):
    path = get_doc_path(note)
    if isdir(path):
       return remove_slash(path)
    else:
        return dirname(path)

# Get the file system path name to the notes file or directory
def get_doc_path(note):
    d = NOTES_DIR+note
    #print 'get_doc_path:',d
    return d

# Find the starting directory for this domain
def get_site_directory(request, title):
    if request.get_host()=='localhost': 
        return ''
    else:
        return title

# Get a dev site tag
def get_dev_site (request):
    if request==None:
        return '    (Test Version)' 
    else:
        return ' (on localhost)' if request.get_host()=='localhost' else ''

# Get the directory that matches the domain
def get_domain_directory(host):
    domains = domain_map()
    if domains.has_key(host): return domains[host]+'/'
    else: return '/'

# Read the mapping from a file on the server
def domain_map():
    domains = {}
    for b in read_file(get_doc_path('/Domains')):
        (domain,directory) = b.split(' ')
        domains[domain] = directory
    return domains

# Return the title for this page
def get_site_title(site):
    if site=='': site = '/'
    #file path:/home/seaman/webapps/mybook/Private/HarborWalk/EmailNeighbors 
    #site: ../Private/HarborWalk/
    content = read_file(get_doc_path(site+'Title'))
    if len(content)>0: 
        return [ convert_line(content[0]), content[1] ]
    return [ 'Shrinking World Guides', 'Tips for thriving in the modern world' ]

# Lookup the headline for this page
def  get_headline(page):
    text = read_file(page)
    if len(text)>0: return convert_line(text[0]).replace('*','')
    return 'Shrinking World Guides'
    
# Return the contents to display
def get_contents(filename):
    #print 'get_contents:', filename
    if not isfile(filename): return ''
    #print 'get_contents:2', filename
    return text_to_html(read_file(filename)[1:])

# Get the path for the page requested
def page_name (request):
    if request==None:
       return  None
    else:
       return request.path

# Get the path within the MyBook directory structure
def mybook_dir(request):
    return get_site_directory (request, get_domain_directory('http://'+request.get_host()))

# Check for a path to a DrProf/Home
def is_wisdom (request, topic):
    return mybook_dir(request)+topic=='DrProf/Home'

# Format debug info
def debug_info(request, topic, site):
    #return ''
    return 'page:%s, --  file path:%s, -- site:%s' % \
        (page_name(request), get_doc_path(mybook_dir(request)+topic), site)

# Create a list of details for possible display
def details(request, page, filepath):
    return [ "<br>URL:  http://"+ request.get_host()+request.path,
             "<br>Page: "+ page,
             "<br>Path: "+ filepath,
             "<br>"]

# Show either the file contents or an error message
def page_body(request,page,path):
    text = get_contents(path)
    if text!='': return text
    return [ "Sorry, but we could not read the requested file." ] + details(request,page,path)
    
# Gather up all the data for the page
def gather_page_data(request, topic):
    base        = request.get_host()

    bookdir    = get_site_directory(request, get_domain_directory('http://'+base))

    if topic.find('../Private')==0:
        titles      = get_site_title (dirname(topic)+'/')
    else:
        titles      = get_site_title (bookdir)

    path        = get_doc_path(bookdir+topic)
    sitetitle   = titles[0] + get_dev_site(request)
    pagetitle   = get_headline(path) +' - '+ titles[0] + get_dev_site(request)
    headline    = get_headline(path)
    text        = page_body(request,bookdir+topic,path) 
    navlinks    = convert_line(navigation_text(NOTES_DIR+'/'+bookdir+topic))

    data        =  { 
        'debug'     : debug_info(request, topic, bookdir),
        'base'      : base,
        'logo'      : 'sws_logo_150.png',
        'site'      : sitetitle,
        'title'     : pagetitle,
        'subtitle'  : titles[1],
        'headline'  : headline,
        'quote'     : select_quote(),
        'text'      : text,
        'navlinks'  : navlinks,
    }
    return data

#def page_html(book, topic):
#    path = get_path(bookdir+topic)
#    text = get_contents(path)
#    return '<html><body>%s</body></html>'
