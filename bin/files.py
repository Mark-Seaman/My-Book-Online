#!/usr/local/bin/python2.7
# Utilities for scripts
from os import remove, path, getcwd, system, listdir,   walk, environ
from os.path import isfile, isdir, join, dirname, exists, getsize
from subprocess import Popen,PIPE


# Create the absolute path name from a relative path name
def path_name (relative_filename):
    return join(getcwd(), relative_filename)

# Read lines from a file and strip off the tailing newline
def read_file(filename):
    if not exists(filename): return [ ]
    f=open(filename)
    results = [line[:-1] for line in f.readlines()]
    f.close()
    return results

# Write lines of text to a file
def write_file(filename, lines):
    f=open(filename, "w")
    f.write("\n".join(lines)+"\n")
    f.close()
 
# Delete a relative path name   
def delete_file(filename):  
    remove(filename)

# Recursive list
def recursive_list(d):
    matches = []
    for root, dirnames, filenames in walk(d):
        for filename in filenames:
            matches.append(join(root, filename))
    return matches


# Return the files as a list
def list_files(directory):
    return [ f for f in listdir(directory) if isfile(join(directory, f)) ]

# Return the files as a list
def list_dirs(directory):
    return [ f for f in listdir(directory) if isdir(join(directory, f)) ]

# Print the count and directory name
def count_files(directory):
    print len(list_files(directory)), directory
 
# Check to see if this file or directory exists
def exists(filepath):
    return exists(filepath)

# Print a flat list
def print_list (list):
    for f in list:
        print f

# Print a list two levels deep
def print_list2 (list):
    for v in list:
        for f in v:
            print f,
        print

# Run the command as a process and capture stdout & print it
def do_command(cmd, input=None):
    if input:
        p = Popen(cmd.split(), stdin=PIPE, stdout=PIPE)
        p.stdin.write(input)
        p.stdin.close()
    else:
        p = Popen(cmd.split(), stdout=PIPE)
    return  p.stdout.read()[:-1]

# Run a grep command and capture output
def grep(pattern,file):
    p = Popen(["grep", pattern, file ], stdout=PIPE)
    return  p.stdout.read()

