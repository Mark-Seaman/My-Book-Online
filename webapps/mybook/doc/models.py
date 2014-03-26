from django.db          import models
from django.forms       import ModelForm
from subprocess         import Popen,PIPE
from os.path            import exists,join,dirname,basename
from os                 import listdir,remove

from Hammer.settings    import DOC_ROOT
from util.page          import show_page
from util.doc           import doc_show

#-----------------------------------------------------------------------------
# Note data

# Note data model
class Note (models.Model):
    path  = models.CharField (max_length=200, editable=False)
    body  = models.TextField ()

# Note form data model used to edit notes
class NoteForm (ModelForm):
    class Meta:
        model=Note

#-----------------------------------------------------------------------------

# Format the title with spaces to break each word.
def title_text(title):
    title = title[0] + ''.join([ " "+c if c.isupper() else c  for c in title[1:] ])
    return title 

    
# Path to doc in file system
def doc_file(title):
    return join(DOC_ROOT,title)


# Look for the document
def is_doc(title):
    #return True
    return exists(doc_file(title))     


# Find the template file for this document
def doc_template(title):
    folder = dirname(doc_file(title))
    template = folder+'/.template'
    if exists(template):
        text = open(template).read()[:-1]
        return text
    else:
        return 'Note'


# Copy the template into the new page folder
def template_text(title):
    t = doc_file(join('template', doc_template(title)))
    if exists(t):
        text = open(t).read() % title_text(basename(title))
        return text
    return 'None'


# Run the command as a process and capture stdout & print it
def do_command(cmd, input=None):
    if input:
        p = Popen(cmd.split(), stdin=PIPE, stdout=PIPE)
        p.stdin.write(input)
        p.stdin.close()
    else:
        p = Popen(cmd.split(), stdout=PIPE)
    return  p.stdout.read()


# # Run the wiki formatter on the document
# def format_doc(title):
#     #from util.doc import  doc_show
#     #return doc_show(title)

#     from util.page import  show_page
#     return show_page(title)

# #    return do_command('doc-page %s'%title)


# Check to see if this doc causes a redirect
def redirect_page(title):
    return do_command('doc-redirect %s'%title)


# Run the wiki formatter on the document
def read_doc(title):
    return do_command('doc-get %s'%title)


# Create the document using a template
def add_doc(title):
    return do_command('doc-add %s'%title)


# Save the document file
def write_doc(title,body):
    body = body.replace('\r','')
    do_command('doc-put %s'%title, body)


# Delete the document file
def delete_doc(title):
    if is_doc(title):
        remove(doc_file(title))
