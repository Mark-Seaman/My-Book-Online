# Read and write a system log file

from os import environ,remove
from datetime import datetime

from files import read_text,list_files


# Setup the file name
def log_file(logFile):
    return environ['p']+'/logs/user/'+logFile+'.log'


# Log the page hit in page.log  (time, ip, user, page, doc) 
def append_log(doc, filename='page'):
    f=open(log_file(filename),'a')
    f.write(str(datetime.now())+',  '+doc+'\n')
    f.close()


# Get the contents of a log file
def show_log(filename='page'):
    return read_text(log_file(filename))

# Get the contents of a log file
def list_logs():
    d = environ['p']+'/logs/'
    for f in list_files(d):
        f = f.replace('.log','')
        log = show_log(f)
        print len(log.split('\n')), log_file(f)

# Get the contents of a log file
def clear_logs():
    d = environ['p']+'/logs/'
    for f in list_files(d):
        f = f.replace('.log','')
        print 'remove', log_file(f)
        remove(log_file(f))
