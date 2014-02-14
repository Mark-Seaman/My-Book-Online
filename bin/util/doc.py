from sys        import argv, stdin
from os.path    import exists,join
from os         import environ,system
from util.tabs  import print_tab_doc, print_all_tabs
from util.wiki  import page_html


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

