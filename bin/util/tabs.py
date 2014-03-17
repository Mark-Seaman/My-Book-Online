#!/usr/bin/env python
# Create a tabbed view of a user document

from os         import chdir,environ
from sys        import argv
from os.path    import join,exists
from re         import compile, IGNORECASE, DOTALL
from subprocess import Popen,PIPE

from util.wiki  import convert_html
from util.files import do_command,read_text
from util.widgets import format_widgets


def group_tabs(text):
    results = []
    groups = text.split('**')
    for i,g in enumerate(groups):
        if i%2>0:
            if i+1<len(groups):
                results.append(groups[i]+groups[i+1])
            else:
                results.append(groups[i])
    return results


# Format one tab of text
def format_tab(text):
    results = ''
    lines   = text.split('\n')
    heading = lines[0]
    body    = lines[1:]
    results += '     <tab heading="%s">\n'%heading
    results +=  '        <div class="page">\n'
    results +=  '        <b>'+heading+'</b>\n'
    results +=  convert_html(body)
    results +=  '        </div>\n'
    results +=  '     </tab>\n'
    return results


# Print one tab of text
def print_tab(text):
    print format_tab(text)


# Print all the tabs of text from the file
def print_all_tabs(text):
    tab_groups = group_tabs(text)
    tabs = text.split('**')
    body = tabs[0].split('\n')
    print convert_html(body)
    if len(tab_groups)>1:
        print '<div ng-controller="TabbedViewCtrl">'
        print '  <tabset ng-show="true">'
        for g in tab_groups:
            print_tab(g)
        print '  </tabset>'
        print '</div>'


#  Formatter to add tabs to the HTML formatting
def print_tab_doc(f):
    text = read_text(f)
    text = format_widgets(f,text)
    print_all_tabs(text)
