#!/usr/bin/env python
# Map the url to a document

def domain_map():
    map = {}
    for d in open('Domains').read().split('\n'):
        d = d.replace('http://','').split(' ')
        if len(d)==2:
            map[d[0]] = d[1]
            #print d[0], d[1]
    return map

def map_url(dirs):
    m = domain_map()
    if m.has_key(dirs[0]):
        return '/'.join ([m[dirs[0]]]+dirs[1:])
    else:
        return '/'.join (dirs)

def testcase (url):
    print  url, map_url(url.split('/'))

def test ():
    testcase('dr-prof.com/user/page')
    testcase('seaman/notes/page')
    testcase('acttolearn.org/new-page')
    testcase('spiritual-things')

test()
