from sys        import argv
from os.path    import exists,join
from os         import environ,system
from util.tabs  import print_tab_doc
from util.wiki  import page_html

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



