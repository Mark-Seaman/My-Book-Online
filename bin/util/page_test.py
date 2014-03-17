#!/usr/bin/env python
# Run a python script to test support center web pages

from os.path  import join,exists
from os import system,environ,chdir,mkdir
from platform import node
from subprocess import Popen,PIPE
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Global vars
browser = ''
accept_all_pages = False


# Get Support Center page
def get_page_text(host,page):
    try:
        browser.get(join(host,page))
        body = browser.find_element_by_tag_name('body')
        text = body.text.decode('ascii','ignore')
    except:
        text = 'File not found: '+join(host,page)
    text = '\n\nTitle:%s\n%s\n' % (browser.title, text )
    return text.replace('localhost:8054','shrinking-world.org')


# Login to the Support Center web site
def login(host,page):
    get_page_text(host,page)
    from local_settings import username,password
    username_field = browser.find_element_by_name('username')
    username_field.send_keys(username)
    password_field = browser.find_element_by_name('password')
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)


# Print the text from a Support Center page
def print_page_text(host,page):
    print get_page_text(host,page)


# Get the web page, extract the text, and save the file
def save_page_text(host,page,output):
    f=open(output, 'wt')
    text = get_page_text(host,page)
    f.write(text)
    f.close()


# select the file name to use
def page_names(url):
    page=url.replace('/','-')
    if page=='': 
        page='index'
    if not exists('pages'):
        mkdir ('pages')
    page = 'pages/'+page
    #print 'page_names:',  ( page+'.out', page+'.correct')
    return ( page+'.out', page+'.correct')


# Compare the actual page to the expected one
def test_page(host,url):
    output,correct = page_names(url)
    save_page_text(host,url,output)
    if not exists(correct):
        accept_page_text(url)


# Make the actual page be the expected one
def accept_page_text(url):
    output,correct = page_names(url)
    print 'Accept text from ',url
    system('cp '+output+' '+correct)


# Calculate the text difference for a test
def diff(t1,t2):
    diffs = Popen([ 'diff', t1, t2 ], stdout=PIPE).stdout.read()
    return diffs


# Print differences between the actual page to the expected one
def show_page_diffs(url):
    output,correct = page_names(url)
    diffs = diff(output, correct)
    #if len(diffs)>1 and url!='': 
    #    system('tdiff '+output[:-4])


# Test a single page from the requested host
def test_web_page(host,page):
    #print 'Testing', page, '...'
    if page=='login':
        login(host,'login')
        print 'Login done'
        return 
    test_page(host,page)
    if accept_all_pages: 
        accept_page_text(page)
    show_page_diffs(page)


# Get the home page, Login, Read all pages
def test_web_pages(host,pages):
    global browser
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    try:
       browser.implicitly_wait(5)
       for page in pages:
           print host+' '+page
           test_web_page('http://'+host,page)
    except:
        print 'Test web pages failed'

    browser.quit()
