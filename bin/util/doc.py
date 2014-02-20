# from datetime   import datetime
# from os         import system,environ
# from os.path    import isfile, exists,join
# from re         import compile, IGNORECASE, DOTALL
# from random     import choice
# from sys        import argv, stdin


from sys        import argv, stdin
from os.path    import exists,join
from os         import environ,system
from util.tabs  import print_tab_doc, print_all_tabs
from util.wiki  import convert_html
from util.files import read_file, write_file

#-----------------------------------------------------------------------------
# Add ins

from os.path import join,exists,basename
from os      import environ
from files   import do_command,list_files,list_dirs

# Create links for each item in the folder
def app_links(files):
    return [ ' * [[%s][%s]]'%(x,title_text(x)) for x in files   if len(x)>0 ]

# Return the directory list
def directory_list(d):
    dirs = [ basename(f) for f in list_dirs(d) ]
    return  '\n'.join(app_links(dirs))


# Return the directory list
def item_list(d):
    dirs = [ basename(f) for f in list_files(d) if not f.startswith('.') and not f.startswith('Index') ]
    return  '\n'.join(app_links(dirs))


# Add a list of directory entries
def include_dirs(text,d):
    return [ l if not '[[DIRS]]' in l else directory_list(d)   for l in text ]
            

# Add a list of directory entries
def include_items(text,d):
    return [ l if not '[[ITEMS]]' in l else item_list(d)   for l in text ]
            

# Create wiki text for the index page
def index_text(doc):
    d = join(environ['pd'],doc)
    text = read_index(join(d,'.index')).split('\n')
    text = include_dirs(text,d)
    #print 'include ',d
    text = include_items(text,d)
    text.append('')
    return '\n'.join(text)

#-----------------------------------------------------------------------------
# Docs

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

