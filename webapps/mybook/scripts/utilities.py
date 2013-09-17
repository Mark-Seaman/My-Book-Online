#!/usr/bin/python
# Utilities for MyBook application on the Web Faction server

from django.core.management.base    import BaseCommand, CommandError
from os         import system, chdir, environ
from settings   import project, project_url
from sys        import argv

# Execute rsync command 
def rsync (hostSource, destSource, extra):
    source = hostSource + '/ '
    dest   = destSource
    system ('rsync -auv  ' + extra + source + dest)      
  
# Copy the entire directory structure from the remote machine
def copy_from_remote():
    rsync (
        hostSource  = project_url+':webapps/'+project, 
        destSource  = '~/Documents/Code/mybook/', 
        extra       = '--exclude .git '+
                      '--exclude media '+
                      '--exclude logo '+
                      '--exclude lib '+
                      '--exclude MyBook '+
                      '--exclude apache2  ',
    )   

def publish():
     rsync (hostSource  = '~/Documents/MyBook', 
            destSource  = project_url+':webapps/'+project+'/MyBook', 
            extra       = '') 
     rsync (hostSource  = '~/Documents/Web', 
            destSource  = project_url+':webapps/'+project+'/media', 
            extra       = '')    

# Copy the entire directory structure to the remote machine
def copy_to_remote():
    rsync (
        hostSource  = '~/Documents/Code/mybook', 
        destSource  = project_url+':webapps/'+project, 
        extra       = '',
    )    

# Execute a command remotely through SSH on Web Faction
def execute_remote_command(command):
    system ('echo  /home/seaman/webapps/'+project+'/'+command+' '+project+' |ssh '+project_url)


