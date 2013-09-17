from files              import read_file
from settings           import NOTES_DIR
from os.path            import join

# Get the file system path name to the notes file or directory
def get_path(note):
    return join(NOTES_DIR,note)

# Read the mapping from a file on the server
def domain_map():
    domains = {}
    for b in read_file(get_path('Domains')):
        (domain,directory) = b.split(' ')
        domains[domain] = directory
    return domains

# Get the directory that matches the domain
def domain(host):
    domains = domain_map()
    if domains.has_key(host):  return domains[host]
    return '.'

def directory(host, page):
    return domain('http://'+host)+'/'+page

def page_url(url):
    return "page_url(url)"

def is_private(url):
    return "is_private(url)"

def books():
    return "books()"

def pages(url):
    return "pages(url)"

def page_name(url):
    return "page_name(url)"


# Return all of info about the requested book
def book(url):
    return [ 
        "Domain:    "+domain('http://ideas.shrinking-world.org'), 
        "Domain:    "+domain('http://exteriorbrain.com'), 
        "Domain:    "+domain('http://effectiveness.shrinking-world.org'), 
        "Domain:    "+domain('http://shrinking-world.org'), 
        "Domain:    "+domain('http://eas.shrinking-world.org'), 
        "Domain:    "+domain('http://localhost'), 

        "Directory: "+directory('ideas.shrinking-world.org','Home'), 
        page_url(url), 
        is_private(url), 
        books(), 
        pages(url), 
        page_name(url) 
        ]
