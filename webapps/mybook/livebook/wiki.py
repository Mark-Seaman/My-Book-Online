# Wiki text formatter

from hyperlink      import convert_links
from files          import read_file
from os.path        import exists, dirname, basename, join
from os             import path

import re

# Create bold text if needed
def make_bold(line):
    pat = re.compile(r"\*\*(.*)\*\*", re.IGNORECASE | re.DOTALL)
    return pat.sub(r'<b>\1</b>', line)

# Create bold text if needed
def make_italic(line):
    pat = re.compile(r"\*([a-zA-Z0-9].*[a-zA-Z0-9])\*", 
                     re.IGNORECASE | re.DOTALL)
    return pat.sub(r'<i>\1</i>', line)

# Add paragraph breaks if needed
def break_paragraphs(line):
    if line=='':
        return '</p><p>'
    else:
        return line

# Remove the muse tag from the first line
def remove_muse(line):
    return line.replace ('-*-muse-*-', '').replace ('-*- muse -*-', '').rstrip()

# Preserve any four spaces together
def preserve_spaces(line):
    return line.replace('    ', '&nbsp;&nbsp;&nbsp;&nbsp;')

# Break lines for <space> at beginning
def space_breaks(line):
    if len(line)>0 and line[0]==' ':
        return  '<br/> '+line
    return line

# Add horizontal rules
def format_rules(line):
    i=line.find('---')
    if i!=-1:
       return line.replace('---', '<hr>')
    return line

# Add bullets
def format_bullets(line):
    i=line.find('  * ')
    if i!=-1:
        return "<ul><li>"+line[i+4:]+"</li></ul>"
    return line

# Convert a single text line to html
def convert_line(line):
    line = space_breaks(line)
    line = format_rules(line)
    line = format_bullets(line)
    line = break_paragraphs(line)
    line = remove_muse(line).rstrip()
    line = convert_links(line)
    line = preserve_spaces(line)
    line = make_bold(line)
    return make_italic(line)

# Convert text (array of strings) into an array of HTML strings
def text_to_html(text):
    return  [ convert_line(t) for t in text ] 

