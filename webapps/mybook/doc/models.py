from django.db          import models
from django.forms       import ModelForm
from subprocess         import Popen,PIPE
from os.path            import exists,join,dirname,basename
from os                 import listdir,remove
from settings           import DOC_ROOT

class Note (models.Model):
    '''
    Note data model
    '''
    path  = models.CharField (max_length=200, editable=False)
    body  = models.TextField ()

class NoteForm (ModelForm):
    '''
    Note form data model used to edit notes
    '''
    class Meta:
        model=Note


def title_text(title):
    '''
    Format the title with spaces to break each word.
    '''
    title = title[0] + ''.join([ " "+c if c.isupper() else c  for c in title[1:] ])
    return title 

    
def doc_file(title):
    '''
    Path to doc in file system
    '''
    return join(DOC_ROOT,title)


def is_doc(title):
    '''
    Look for the document
    '''
    #return True
    return exists(doc_file(title))     


def doc_template(title):
    '''
    Find the template file for this document
    '''
    folder = dirname(doc_file(title))
    template = folder+'/.template'
    if exists(template):
        text = open(template).read()[:-1]
        return text
    else:
        return 'Note'


def template_text(title):
    '''
    Copy the template into the new page folder
    '''
    t = doc_file(join('template', doc_template(title)))
    if exists(t):
        text = open(t).read() % title_text(basename(title))
        return text
    return 'None'


def do_command(cmd, input=None):
    '''
    Run the command as a process and capture stdout & print it
    '''
    if input:
        p = Popen(cmd.split(), stdin=PIPE, stdout=PIPE)
        p.stdin.write(input)
        p.stdin.close()
    else:
        p = Popen(cmd.split(), stdout=PIPE)
    return  p.stdout.read()


def format_doc(title):
    '''
    Run the wiki formatter on the document
    '''
    #return 'hammer-show %s'%title
    return do_command('hammer-show %s'%title)


def read_doc(title):
    '''
    Run the wiki formatter on the document
    '''
    #return do_command('hammer-read %s'%title)
    return do_command('doc-get %s'%title)


def add_doc(title):
    '''
    Create the document using a template
    '''
    #return do_command('hammer-add %s'%title)
    return do_command('hammer-add %s'%title)


def write_doc(title,body):
    '''
    Save the document file
    '''
    body = body.replace('\r','')
    #do_command('hammer-write %s'%title, body)
    do_command('doc-put %s'%title, body)


def delete_doc(title):
    if is_doc(title):
        remove(doc_file(title))


def list_tests(title):
    '''
    Generate a list of test files in CSV format
    '''
    return do_command('hammer-tests '+title)


def generate(title):
    '''
    Generate a list of test files in CSV format
    '''
    return do_command('hammer-wmd '+title)


def enable_app(user, title):
    '''
    Enable an app for a user
    '''
    do_command('app-enable %s %s'%(user,title))


def disable_app(user, title):
    '''
    Disable an app for a user
    '''
    do_command('app-disable %s %s'%(user,title))


def domain_map():
    '''
    Read the domain mapping from a file
    '''
    map = {}
    for d in open(doc_file('Domains')).read().split('\n'):
        d = d.replace('http://','').split(' ')
        if len(d)==2:
            map[d[0]] = d[1]
            #print d[0], d[1]
    return map


def host_root(host):
    '''
    Return the root of the doc tree
    '''
    m = domain_map()
    if m.has_key(host):
        return '/'+m[host]
    else:
        return '/'
