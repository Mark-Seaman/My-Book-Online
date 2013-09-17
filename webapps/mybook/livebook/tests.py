from contents       import *
from django.test    import TestCase
from files          import print_list
from hyperlink      import *
from settings       import NOTES_DIR
from wiki           import *
from wiki_links     import *
from page_order     import *
import re

#############################################################################
# Test data

input_text = '''
* Headline Text *        -*-muse-*-
http://localhost/media/images/sws_logo_75.png
[[images/sws_logo_75.png]]
[[images/Mark.Seaman.200.jpg]]
[[notes/testing][Testing notes]]
[[Notes/testing]]
notes/testing
NotesTestingAgain
[[NotesTestingAgain]]
[[NotesTestingAgain][Testing notes]]
do not format me
[[Link]]
[[link]]
'''

correct_output = '''</p><p>
* Headline Text *
<a href="http://localhost/media/images/sws_logo_75.png" target="_blank">http://localhost/media/images/sws_logo_75.png</a>
<img src="/media/mybook/images/sws_logo_75.png" alt="sws_logo_75.png">
<img src="/media/mybook/images/Mark.Seaman.200.jpg" alt="Mark.Seaman.200.jpg">
 <a href="notes/testing">Testing notes</a> 
 <a href="Notes/testing">Notes/testing</a> 
notes/testing
 <a href="NotesTestingAgain">NotesTestingAgain</a> 
 <a href="NotesTestingAgain">NotesTestingAgain</a> 
 <a href="NotesTestingAgain">Testing notes</a> 
do not format me
 <a href="Link">Link</a> 
 <a href="link">link</a> 
</p><p>'''

input_links = '''a
this is a test
[[link]]
[[link1]]   [[link2]]
[[link1][label text]]'''

output_links = [
    [],
    [],
    ['link'],
    ['link1','link2'],
    ['link1'],
]

all_output_links = [
    'link',
    'link1',
    'link2',
]

#############################################################################
# Helper functions

def test_domain(self, site,directory):
    self.assertEqual (get_domain_directory('http://'+site), directory)


#############################################################################
# Wiki content cases

class wiki_test (TestCase):

    def test_make_italic(self):
        correct='regular text'
        actual=make_italic(correct)
        self.assertEqual (actual,correct)
        correct='<i>italic text</i>'
        actual=make_italic('*italic text*')
        self.assertEqual (actual,correct)

    def test_make_bold(self):
        correct='regular text'
        actual=make_bold(correct)
        self.assertEqual (actual,correct)
        correct='<b>bold text</b>'
        actual=make_bold('**bold text**')
        self.assertEqual (actual,correct)

    def test_break_paragraphs(self):
        correct='line1\nline2\n\nline3\nline4'
        actual=break_paragraphs('line1\nline2\n\nline3\nline4')
        self.assertEqual (actual,correct)

    def test_remove_muse(self):
        correct='* this and that *'
        actual=remove_muse('* this and that *               -*-muse-*-')
        self.assertEqual (actual,correct)
        actual=remove_muse('* this and that *               -*- muse -*-')
        self.assertEqual (actual,correct)

    def test_preserve_spaces(self):
        correct = '&nbsp;&nbsp;&nbsp;&nbsp;indented text'
        actual = preserve_spaces('    indented text')
        self.assertEqual (actual,correct)

    def test_space_breaks(self):
        correct = '<br/>  '
        actual = space_breaks(' ')
        self.assertEqual (actual,correct)

    def test_format_bullets(self):
        correct = '<ul><li>bullet text</li></ul>'
        actual = format_bullets('  * bullet text')
        self.assertEqual (actual,correct)

    def test_convert_line(self):
        correct = 'line1'
        actual =  convert_line('line1 -*-muse-*-')
        self.assertEqual (actual,correct)

    def test_text_to_html(self):
        correct = correct_output.split('\n')
        ins = input_text.split('\n')
        for line in range(len(ins)):
            self.assertEqual (convert_line(ins[line]), correct[line])

    def test_links_by_line(self):
        ins = input_links.split('\n')
        outs = output_links
        for line in range(len(ins)):
            links = get_all_links([ ins[line] ])
            self.assertEqual ( links, outs[line])
        
    def test_all_links (self):
        text = input_links.split('\n')
        correct_output =  all_output_links
        self.assertEqual (get_all_links(text), correct_output)

    def test_domains(self):
        test_domain(self,'shrinking-world.org',                  './')
        test_domain(self,'effectiveness.shrinking-world.org',    'SuperPower/')
        test_domain(self,'leadership.shrinking-world.org',       'Leadership/')
        test_domain(self,'markseaman.org',                       'MarkSeaman/')
        test_domain(self,'ideas.shrinking-world.org',            'Ideas/')


#############################################################################
# Wiki Links cases
class wiki_links_test (TestCase):

    def test_get_links(self):
        text = '[[Folder/Contents][First Links]] [[FolderContents][First Links]]'+\
        '[[Folder/Contents]]  [[FolderContents][Wiki Links]]'
        self.assertEqual(get_links(text), ['FolderContents','FolderContents'])

    def test_get_all_links(self):
        text = ['WikiLinks [[link1]]','[[link2][Links and links]]']
        self.assertEqual(get_all_links(text), ['link1', 'link2'])

    def test_unique(self):
        self.assertEqual( unique([ 1, 2, 1, 3, 1 , 4, 1, 5 ]), [ 1, 2, 3, 4, 5 ])

    def test_get_file_links(self):
        answer = ['EveryoneHasASuperpower', 'FocusYourEnergy', 'IdentifyYourValues', 
                  'UnderstandYourStrengths', 'ClarifyYourPriorities', 'BuildYourHabits', 
                  'PursueYourPassion']
        self.assertEqual (get_file_links (NOTES_DIR+'/SuperPower/Chapter1'),answer)

    def test_link_string(self):
        pass

    def test_print_links(self):
        pass

    def test_print_topic_table(self):
        pass

    def test_find_links(self):
        pass

    def test_print_topic(self):
        pass

    def test_print_kids(self):
        pass

    def test_print_nested(self):
        pass

    def test_print_outline(self):
        pass

    def test_(self):
        pass

    def test_create_topic_map(self):
        pass

    def test_page_exists(self):
        pass

    def test_page_dictionary(self):
        pass

#############################################################################
# Page order cases
class page_order_test (TestCase):

    def test_page_links (self):
        pass

    def test_reading_order(self):
        answer = ['Index']+[ "%d"%(num+1001) for num in range(16) ]
        self.assertEqual (reading_order (NOTES_DIR+'/Gallery/volcano/Index'), answer)
        pass

    def test_index_link(self):
        pass

    def test_next_link(self):
        pass

    def test_previous_link(self):
        pass

    def test_navigation_links(self):
        pass

    def test_make_link(self):
        pass

    # Test page navigation
    def test_navigation_text(self):
        index    = 'See also [[Index][Table of Contents]], '
        pages = '[[YourLearningSystem][Previous Page]], [[MakeConstantImprovements][Next Page]]'
        self.assertEqual (navigation_text (NOTES_DIR+'/SuperPower/Chapter4'),index+pages)
        answer = 'See also [[Index][Table of Contents]], [[1003][Previous Page]], [[1005][Next Page]]'
        self.assertEqual (navigation_text (NOTES_DIR+'/Gallery/volcano/1004'), answer)
        answer = 'See also [[Index][Table of Contents]], [[1015][Previous Page]]'
        self.assertEqual (navigation_text (NOTES_DIR+'/Gallery/volcano/1016'), answer)



#############################################################################
# Wiki links cases

class WikiLinksTest(TestCase):

    # Convert the url in a string to an HTML anchor
    def test_muse_double_anchor(self):
        self.assertEqual(' <a href="This">this is it</a> ', 
                   muse_double_anchor('[[This][this is it]]'))
        self.assertEqual(' <a href="http://google.com">Google</a> ', 
                   muse_anchor('[[http://google.com][Google]]'))
        x = '[[../SuperPower/EveryoneHasASuperpower][Read more]]'
        y = ' <a href="../SuperPower/EveryoneHasASuperpower">Read more</a> '
        self.assertEqual(muse_double_anchor(x),y)

    # Convert the url in a string to an HTML anchor
    def test_muse_single_anchor(self):
        self.assertEqual(' <a href="this">this</a> ',
                   muse_single_anchor('[[this]]'))

    # Convert the url in a string to an HTML anchor
    def test_muse_anchor(self):
        self.assertEqual('x', 
                   muse_anchor('x'))
        self.assertEqual(' <a href="x">x</a> ',
                   muse_anchor('[[x]]'))
        self.assertEqual(' <a href="x">hey there</a> ',
                   muse_anchor('[[x][hey there]]'))
        self.assertEqual(' <a href="http://google.com">Google</a> ', 
                   muse_anchor('[[http://google.com][Google]]'))
    
    # Convert the url in a string to an HTML anchor
    def test_url_to_anchor(self):
        self.assertEqual('<a href="http://google.com" target="_blank">http://google.com</a>', 
                   url_to_anchor('http://google.com'))

    # Convert the url in a string to an HTML image tag
    def test_url_to_image(self):
        self.assertEqual('<img src="/media/mybook/images/xxx.jpg" alt="xxx.jpg">',
                   url_to_image('[[images/xxx.jpg]]'))
 
    # Convert the Wiki Words to hyperlinks
    def test_wiki_words(self):
        self.assertEqual(' <a href="WikiWords">WikiWords</a> ', wiki_words('WikiWords'))

    # Convert a single line of muse to html
    def test_convert_links(self):
        x = ' <a href="a">a</a>   <a href="b">c</a>  <a href="http://d.com" target="_blank">http://d.com</a>'
        self.assertEqual(x, convert_links('[[a]] [[b][c]] http://d.com'))
        self.assertEqual(' <a href="http://google.com">Google</a> ', 
                         convert_links('[[http://google.com][Google]]'))
        x = '[[../SuperPower/EveryoneHasASuperpower][Read more]]'
        y = ' <a href="../SuperPower/EveryoneHasASuperpower">Read more</a> '
        self.assertEqual(y,convert_links(x))
        x=' [[http://effectiveness.shrinking-world.org/EveryoneHasASuperpower][Read more]] '
        y = '  <a href="http://effectiveness.shrinking-world.org/EveryoneHasASuperpower">Read more</a>  ' 
        self.assertEqual(y,convert_links(x))

    # Process an entire file to extract links
    def test_get_all_links(self):
        #print get_file_links(NOTES_DIR+'/SuperPower/Index')
        self.assertEqual(get_file_links(NOTES_DIR+'/SuperPower/Index'), 
                         ['Home', 'Chapter1', 'EveryoneHasASuperpower', 'FocusYourEnergy', 'IdentifyYourValues', 
                          'UnderstandYourStrengths', 'ClarifyYourPriorities', 'BuildYourHabits', 
                          'PursueYourPassion', 'Chapter2', 'CraftYourPlans', 'Projects', 'Actions', 
                          'JustEnoughPlanning', 'Roles', 'UpdateYourPlan', 'Chapter3', 'BuildSupportSystems', 
                          'YourPlanningSystem', 'YourCommunicationSystem', 'YourInformationSystem', 
                          'YourLearningSystem', 'Chapter4', 'MakeConstantImprovements', 'Plan', 'Learn', 
                          'Develop', 'Teach', 'Chapter5', 'LearnGrowProduce', 'AchieverLearn', 'AchieverGrow', 
                          'AchieverProduce', 'AchieverPurpose', 'AchieverInfluence'])

    # Find the nested link tree
    def test_find_links(self):
        self.assertEqual (find_links ({}, NOTES_DIR+'/SuperPower','Index', 1)['Chapter4'][2], 
                          'TheNeedForInnovation')

    # Test the page dictionary for a specific file
    def test_page_dictionary(self):
        self.assertEqual (page_dictionary (NOTES_DIR+'/SuperPower/Index')['Chapter4'][2], 
                          'TheNeedForInnovation')
        self.assertEqual (page_dictionary (NOTES_DIR+'/Ideas/Index'), {})


    # Test page links for navigation
    def test_page_links(self):
       page_links (NOTES_DIR+'/SuperPower/Chapter4')[0]

   # Test page navigation
    def test_reading_order(self):
        self.assertEqual (reading_order (NOTES_DIR+'/SuperPower/Chapter4')[1],'Home')


    def test_get_contents(self):
        x = 'Unlock the secrets of your super-powers!'
        self.assertEqual (get_contents (NOTES_DIR+'/SuperPower/Home')[1],x)

#############################################################################
# Test contents.py

class contents_test (TestCase):

    def test_remove_slash(self):
        remove_slash('this')
        pass

    def test_get_directory(self):
        get_directory('')
        pass

    def test_get_path(self):
        get_path('')
        pass

    def test_get_site_directory(self):
        #get_site_directory('', '')
        pass

    def test_get_dev_site (self):
        #get_dev_site ('')
        pass

    def test_get_domain_directory(self):
        get_domain_directory('')
        pass

    def test_domain_map(self):
        domain_map()
        pass

    def test_get_site_title(self):
        get_site_title('')
        pass

    def test_get_headline(self):
        get_headline('')
        pass

    def test_get_contents(self):
        get_contents('')
        pass

    def test_page_name (self):
        #page_name ('Index')
        pass

    def test_gather_page_data(self):
        #gather_page_data(HttpRequest(), '')
        pass

#############################################################################
# Test views.py

class views_test (TestCase):

    def test_livebook_page(self):
        #livebook_page (request, topic)
        pass

    def test_guides(self):
        #guides(request)
        pass

    def test_livebook(self):
        #livebook(request,topic)
        pass


#############################################################################
# Test files.py

from files import  array_to_str,str_to_array

class files_test (TestCase):

    def test_livebook_page(self):
        s = '''
             line1
             line 2
             line 3
            '''
        self.assertEqual(s, array_to_str(str_to_array(s)))
