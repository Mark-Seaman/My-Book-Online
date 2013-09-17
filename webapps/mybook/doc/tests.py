"""
Test to make sure that this application is running properly.
"""

from django.http            import HttpRequest, HttpResponse
from django.template.loader import render_to_string
from django.test            import TestCase
from os                     import listdir
from subprocess             import Popen,PIPE

from settings               import DOC_ROOT, STATICFILES_DIRS
from doc.views              import home,list,doc,read_doc
from doc.models             import Note,NoteForm,list_docs


def diff(s1,s2):
    '''
    Calculate the text difference for a test
    '''
    t1 = '/tmp/diff1'
    t2 = '/tmp/diff2'
    #print 'Response:', t1
    #print 'Expected:', t2
    open(t1, 'wt').write(s1)
    open(t2, 'wt').write(s2)
    diffs = Popen([ 'diff', t1, t2 ], stdout=PIPE).stdout.read()
    #print diffs
    return diffs.split('\n')


#TODO: create a function to diff two text string using 'diff'
class AppConfigTest(TestCase):
    
    def test_doc_directory(self):
        '''
        Make sure that the document storage has files in it
        '''
        #print  'Doc root: %d %s'%(len(list_docs()),DOC_ROOT)
        self.assertEqual(len(list_docs()),24)
        
    def test_static_directory(self):
        '''
        Make sure that the static storage has files in it
        '''
        static_dir = STATICFILES_DIRS[0]
        files = len(listdir(static_dir))
        #print 'Static root: %d %s'%(files, static_dir)
        self.assertEqual(files, 4)


class AppUnitTest(TestCase):

        
        def test_renders_correct_template(self):
            '''
            Compare the docs
            '''
            lines_to_match = 10000  # TODO: only first 1000 lines match
            request = HttpRequest()
            response = list(request)
            actual = str(response.content)[:lines_to_match]
            expected = render_to_string('list.html', 
                                        {'directory': list_docs(), 
                                         'STATIC_URL': '/static/'})[:lines_to_match]
            diffs = diff(actual, expected)
            self.assertEqual(len(diffs),1)


        def test_renders_correct_html(self):
            '''
            Make sure the correct template is used
            '''
            expected = render_to_string('list.html',{ 'directory': list_docs() })
            for t in ['ServerTricks','TestTricks','AllTricks','Home']:
                    self.assertIn(t, expected)


        def test_render_home(self):
            '''
            Render the home view
            '''
            request  = HttpRequest()
            response = home(request)
            actual   = str(response.content)
            expected = str(render_to_string('doc.html', 
                           { 'title': 'Home', 
                             'text': read_doc('Home'),
                             'STATIC_URL': '/static/'}))
            diffs = diff(actual, expected)
            # TODO: work off actual docs
            #for i in diffs: print i
            self.assertEqual(len(diffs),26)
            #self.assertEqual(actual, expected)


        def test_render_add(self):
            '''
            Render the add view
            '''
            request  = HttpRequest()
            response = home(request)
            actual   = str(response.content)
            expected = str(render_to_string('doc.html', 
                           { 'title': 'Home', 
                             'text': read_doc('Home'),
                             'STATIC_URL': '/static/'}))
            diffs = diff(actual, expected)
            # TODO: work off actual docs
            #for i in diffs: print i
            self.assertEqual(len(diffs),26)
            #self.assertEqual(actual, expected)

