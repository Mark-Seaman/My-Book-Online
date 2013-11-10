from django.contrib.auth.decorators import login_required
from django.shortcuts   import render
from django.utils.html  import escape
from json               import dumps
from models             import *
from os.path            import join, exists, dirname
from views              import user_doc


def doc_text(doc):
    '''
    Render text by reading and file and escaping it.
    '''
    return  escape(read_doc(doc)).split('\n')


def add_page(doc,year):
    '''
    Add a JS object for a subpage to be displayed in an accordion view
    '''
    return { "title": str(year), "content": doc_text(doc+year) }


def build_json(doc):
    '''
    Create JSON for the object for all subpages to be displayed in an accordion view
    '''
    num_years = 54
    years = [ str(1959+year) for year in range(num_years) ]
    pages = map(lambda y:add_page(doc,y), years)
    #pages = [ { "title":"First Topic",  "content":["No Content","Line 2"] },
    #          { "title":"Second Topic", "content":["Still No Content"] }]
    return dumps(pages)
 

@login_required(login_url='/login')
def story(request,title):
    '''
    Render the home view
    '''
    doc = user_doc(request,'story/')
    data = { 'pages':  build_json(doc), 'gtitle':'{{group.title}}'}
    return render(request, 'story.html', data)
  
