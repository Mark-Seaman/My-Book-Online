from sys        import argv
from os         import environ,mkdir
from os.path    import join,exists
from shutil     import copy

from util.files import list_dirs, is_writable, write_file, read_file, read_input


# Get the doc file for this request
def event_doc(f):
    return join(environ['pd'],f)


# Get the events for this directory
def event_list(d):
    return list_dirs(event_doc(d))


# Set up the event app for a user
def event_install(user):
    if exists(event_doc(user)):
        if not exists(event_doc(user+'/event')):
            mkdir (event_doc(user+'/event'))
            #print 'Created ',event_doc(user+'/event')
    copy (event_doc('template/event/Index'), event_doc(user+'/event/Index'))


# Add a new event for this user
def event_add(e):
    path = event_doc(e)
    if not exists(path): 
        mkdir (path)
        #print 'from:',event_doc('template/Event/Index')
        #print 'to:',join(path,'Index')
        copy (event_doc('template/Event/Index'), join(path,'Index'))
    

# Read the event options for editing
def event_read(f):
    path = event_doc(f)
    if  not is_writable(path):
        print 'File must be writable, ',path
        return
    return '\n'.join(read_file(path))


# Write the event options after editing
def event_write(f):
    path = event_doc(f)
    if  not is_writable(path):
        print 'File must be writable, ',path
        return
    write_file(path,read_input())

