#!/usr/bin/env python
# Compare all project files to the projects they are derived from

from os.path import join
from os import environ,chmod,system
from stat import S_IEXEC,S_IREAD,S_IWRITE

def create_test(d1,d2,fn):
    tfile=fn
    if not fn.endswith('.tst'):
        tfile = fn+'.tst'
    path = join(environ['pt'],'update',tfile)
    f = open(path, 'w')
    f.write('filediff %s %s %s -v\n'%(fn,d1,d2))
    f.close()
    chmod (path, S_IEXEC|S_IREAD|S_IWRITE)

def do_test(filename):
    system ('update-test '+filename)

def execute_test(d1,d2,f):
    create_test(d1,d2,f)
    do_test(f)


bin_files = '''trun
tlike
tdiff
tfail
tresults
tst
tout'''

test_files = '''docs
git
files'''

#print 'Bin  Files:', bin_files.split('\n')
#print 'Test Files:', test_files.split('\n')

d1='$p'
d2='~/wme/support-git'

for f in bin_files.split('\n'):
    execute_test(d1,d2,join('bin',f))

for f in test_files.split('\n'):
    execute_test(d1,d2,join('test',f+'.tst'))
