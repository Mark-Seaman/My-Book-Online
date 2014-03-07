from random import choice
from files  import list_files, read_text, do_command
from list   import split_lines,join_lines
from os.path import dirname,join


# Get a directory of possible selection
def directory_listing(dir):
    return [ x for x in list_files(dir) if not x in ['Index','Random'] ]


# Insert a random selected file into this spot if requested
def lookup_file(dir, line):
    if '[[PICK]]' in line:
        pick = directory_listing(dir)
        pick = choice(pick)
        #return 'selection:%s\n\n%s'%(pick,read_text(join(dir,pick)))
        return read_text(join(dir,pick))
    return line


# Insert a random selected file into this spot if requested
def insert_random_text(dir,lines):
    return [ lookup_file(dir, l) for l in lines ]
    

# Feature a single line of the input stream
def lookup_quote(line, lines):
    if '[[QUOTE]]' in line:
        t = filter(lambda l:len(l)>4, lines[2:])
        t = filter(lambda l:not '**' in l, t)
        t = filter(lambda l:not '[[QUOTE]]' in l, t)
        return '<b>'+choice(t)+'</b><br>'
    return line


# Select a line of text to feature
def extract_random_line(lines):
    return [ lookup_quote(l, lines) for l in lines ]


# Replace a single include
def replace_include (dir,line):
    if '[[INCLUDE:' in line:
        filename = dir+'/'+line[10:-2]
        return read_text(filename)
    return line


# Replace a single include
def replace_scripts (line):
    if '[[SCRIPT:' in line:
        filename = line[9:-2]
        return do_command(filename)
    return line


# Map all of the include lines to their file replacements
def map_include_files(dir,lines):
    return  [ replace_include(dir,l) for l in lines ] 


# Map all of the include lines to their file replacements
def map_scripts(lines):
    return  [ replace_scripts(l) for l in lines ] 


# Format this text as a page with embedded widgets
def format_widgets(filename, text):
    dir = dirname(filename)
    lines = split_lines(text)
    lines = map_scripts(lines)
    lines = map_include_files(dir,lines)
    lines = split_lines(join_lines(lines))
    lines = insert_random_text(dir,lines)
    lines = extract_random_line(lines)
    return join_lines(lines)

