from wiki_links import page_dictionary, topic_list
from os.path            import isfile, isdir, dirname, join, basename
from files              import exists


# Return the links to the Index, Previous, and Next pages
def page_links (filename):
    topic_table = page_dictionary(filename)
    return topic_table[basename(filename)]

# Return the order of the topics from the Index page
def reading_order(filename):
    directory = dirname(filename)
    index = join(directory,'Index')
    topic_map = page_dictionary(index)
    if topic_map=={}: return []
    return topic_list(topic_map, 'Index') 

# Create a wiki link from a pair (page, text)
def make_link(link_file, link_text):
    return '[[%s][%s]]'%(link_file,link_text)

# Create an index link
def index_link(order):
    return  make_link('Index','Table of Contents')

# Create a link to the next page
def next_link(order, i):
    if len(order)<=i+1: return ''
    return  make_link (order[i+1],'Next Page')

# Create a link to the previous page
def previous_link(order, i):
    if i<1: return ''
    return make_link (order[i-1], 'Previous Page')

# Return Index, Previous, and Next pages
def navigation_links(filename):
    order = reading_order(filename)
    page = basename(filename)
    if order==[] or page=='Index': return []
    for i in range(len(order)):
        if order[i] == page:
            return [ index_link(order), previous_link(order, i), next_link(order, i) ]
    return []


# Format links as wiki text
def navigation_text(filename):
    return ''
    if not exists(filename): return ''
    links = [i for i in navigation_links(filename) if i!='' ]
    if links==[]:    return ''
    return 'See also '+', '.join(links)
