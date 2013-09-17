# Wiki page links

from files      import *
from os.path    import exists, dirname, basename, join
from re         import sub
from hyperlink  import wiki_words

# Get one link from a string as a list
def extract_link(str):
    link = sub ( r'\]\[.*', '', str)
    if link.find('/')==-1: return [ link ]
    else: return []
    
# Extract all of the links from one line of text
def get_links(line):
    x=line.find('[[') 
    y=line.find(']]')
    if x>=y: return []
    return extract_link(line[x+2:y]) + get_links(line[y+2:])

# Eliminate the duplication from a list
def unique(with_dups):
    s = set()
    for i in with_dups: s.add(i) 
    return [ i for i in s ] 
            
# Extract links from an array of text
def get_all_links(text):
    results = []
    for line in text:
        results += get_links(line)
    return  unique(results)

# Get the links contained in this MyBook file
def get_file_links(filename):
    return get_all_links(read_file(filename))

# Covert a list of links into a string
def link_string(links):
    return '\n    '.join(links)

# Print a list of links for a topic file
def print_links(topic, links):
    print topic+'\n    '+link_string(links)

# Print the table of topics
def print_topic_table(topic_table):
    for topic in topic_table:
        print_links(topic, topic_table[topic])

# Extract the links for one topic
def find_links(topic_table, directory, topic, depth):
    kids = get_file_links(directory+'/'+topic)
    topic_table[topic] = kids
    if depth>0:
        for t in kids:
            topic_table = find_links(topic_table, directory, t, depth-1)
    return topic_table

# Print the a single topic with indent
def print_topic(topic,indent):
    for i in range(indent): print '    ',
    print topic

# Print the nested children (expand each node only once)
def print_kids(topic_table,topic,indent):
    if topic_table.has_key(topic): 
        kids = topic_table[topic]
        topic_table[topic] = []
        for t in kids:
            print_nested(topic_table, t, indent+1)
    
# Print a table of topics in outline format
def print_nested(topic_table,topic,indent):
    print_topic(topic,indent)
    print_kids(topic_table,topic,indent)

# Print the outline for the for page
def print_outline(filename):
    if not exists(filename):
        print 'Could not open file,', filename
    else:
        print_nested (page_dictionary(filename), basename(filename), 0)

# Return a list of topics in reading order
def topic_list(topic_table, topic):
    results = [ topic ]
    if topic_table and topic_table.has_key(topic): 
        kids = topic_table[topic]
        topic_table[topic] = []
        for t in kids:
            results += topic_list(topic_table, t)
    return results

# Create a map of topics
def create_topic_map(directory,page):
    topic_table = {}
    return find_links(topic_table, directory, page, 2)

# Check to see if a page exists
def page_exists(directory, page_name):
     return exists(join(directory,page_name))

# Return a table of the pages in this directory
def page_dictionary(filename):
    directory = dirname(filename)
    if not page_exists(directory,'Index'):
        #print "No index"
        return {}
    else:
        #print "Found index"
        return create_topic_map(directory, 'Index')      
