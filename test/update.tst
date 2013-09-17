#!/usr/bin/env python
# Compare all project files to the projects they are derived from

from os.path import join
from os import environ,chmod
from stat import S_IEXEC,S_IREAD,S_IWRITE

def create_test(d1,d2,fn):
    tfile = fn+'.tst'
    print 'update-test '+fn
    path = join(environ['pt'],'update',tfile)
    f = open(path, 'w')
    f.write('filediff %s %s %s -v\n'%(fn,d1,d2))
    f.close()
    chmod (path, S_IEXEC|S_IREAD|S_IWRITE)


bin_files = '''trun
tlike
tdiff
tfail
tresults
tst
tout'''

test_files = '''docs
git
files
update'''

#print 'Bin  Files:', bin_files.split('\n')
#print 'Test Files:', test_files.split('\n')

d1='$p'
d2='~/wme/support-git'
for f in bin_files.split('\n'):
     create_test(d1,d2,join('bin',f))
for f in test_files.split('\n'):
     create_test(d1,d2,join('test',f))


# # bin 
# cd $x
# for f in 'bin/trun bin/tlike bin/tout'
# do
#     echo "filediff $p/$f $x/$f -v"
#     #echo 'echo "filediff $p/$f $x/$f -v" > $d/$f.tst'
#     #echo 'chmod +x $d/$f.tst'
# done

# # bin 
# cd $x
# for f in `ls bin/*`
# do
#     echo "filediff $p/$f $x/$f -v" > $d/$f.tst
#     chmod +x $d/$f.tst
# done

# # test
# cd $x
# for f in `ls test/*.tst`
# do
#     echo "filediff $p/$f $x/$f -v" > $d/$f
#     chmod +x $d/$f
# done

# Do comparisons for the update
# cd $pt
# ls update/test/*.tst |
# while read f
# do 
#     a=${f/.tst/}.correct
#     #rm $a;touch $a

#     # Compare each file
#     trun  $f

#     # Accept all answers
#     #tlike $f
# done
