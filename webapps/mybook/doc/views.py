from datetime           import datetime
from django.contrib.auth.decorators import login_required
from django.http        import HttpResponseRedirect, HttpResponse
from django.utils.html  import escape
from os.path            import join, exists, dirname
from os                 import system,environ
from django.template    import loader, Context

from models             import *

logFile=environ['p']+'/logs/user/page.log'

def render(request,template,data): 
    page = loader.get_template (template)
    return HttpResponse (page.render (Context(data)))

def ip(request):
    '''
    Get the IP address for the request
    '''
    if request.META['REMOTE_ADDR']=='127.0.0.1':
        return request.META['REMOTE_ADDR']
    return request.META['HTTP_X_FORWARDED_FOR']


def user(request):
    '''
    Name of requesting user
    '''
    if not request.user.is_anonymous():
        return request.user.username
    else:
        return 'Anonymous'


def user_doc(request,title):
    '''
    Return the document for this user.
    '''
    host = request.get_host()
    username = user(request).replace ('Anonymous','Public')
    return join(username,title)
    #return  title


def log_page(request,title):
    '''
    Log the page hit in page.log  (time, ip, user, page, doc) 
    '''
    u   = user(request)
    if ':' in title:
        doc = title
    else:
        doc = join(u, title)
    f=open(logFile,'a')
    options = (str(datetime.now()), ip(request), request.get_host(), u, request.path, doc)
    f.write(', '.join(options)+'\n')
    f.close()


def new(request,title):
    '''
    Render the view for a missing document
    '''
    text = format_doc('Anonymous/NewPage') # % title
    data = {'title':title, 'dir':dirname(title), 'text':text, 
            'default':basename(title), 'newpage':'{{newpage}}'}
    return render(request, 'new.html', data)


def missing(request,title):
    '''
    Render the view for a missing document
    '''
    #if not permitted(request):
    #    return redirect(request,'login')
    text = format_doc('Anonymous/MissingFile') % title
    data = {'title':title, 'dir':dirname(title), 'text':text, 
            'default':basename(title), 'newpage':'{{newpage}}'}
    return render(request, 'missing.html', data)


def redirect(request,title):
    '''
    Go to a specific page
    '''
    log_page (request,'redirect:%s'%title)
    return HttpResponseRedirect('/'+title) 


def doc(request,title):
    '''
    Render the appropriate doc view
    '''
    doc = user_doc(request,title)
    log_page (request, title)
    text = format_doc(doc)
    if text.startswith('redirect:'):
        return redirect(request,text[len('redirect:'):-1])
    #if not permitted(request, doc):
    #    return redirect(request,'login')
    content =  {'site':request.get_host(), 'title': title, 'text': text}
    return render(request, 'doc.html', content)


def home(request):
    '''
    Render the home view
    '''
    return  doc(request,'Index')
    # if request.user.is_anonymous():
    #     doc = 'Index'
    #     log_page (request, 'Index')
    #     data = {'title': 'Index', 'text': format_doc(doc)}
    #     return render(request, 'doc.html', data)
    # return redirect (request,'Index')


#@login_required(login_url='/login')
def store(request,title):
    '''
    Get and put doc directly
    '''
    log_page (request, title)
    doc  = user_doc(request,title)
    text = read_doc(doc)
    return HttpResponse(text)


#@login_required(login_url='/login')
def edit_form (request, doc, title=None, text=None):
    '''
    Create a form for editing the object details
    '''
    log_page (request, 'form:%s'%title)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if request.POST.get('cancel', None):
            return redirect(request,title)
        else:
            if form.is_valid():
                log_page (request, 'save:%s'%title)
                text =  form.cleaned_data['body']
                text = text.encode('ascii', 'ignore')
                text = text.replace('\r','')
                write_doc(doc,text)
                return redirect(request,title)
    else:
        note =  Note()
        note.path = title
        log_page (request,'read:%s'%title)
        if not text:
            if is_doc(doc):
                text = read_doc(doc)
        note.body = text
        form =  NoteForm(instance=note)
    data =  { 'form': form, 'title': title, 'banner': True  }
    return render(request, 'docedit.html', data)


def edit(request,title):
    '''
    Render the add view
    '''
    doc = user_doc(request,title)
    log_page (request, 'edit:%s'%title)
    return edit_form (request, doc, title)


def add(request,title):
    '''
    Render the add view
    '''
    log_page (request,'add:%s'%title)
    text = add_doc(user_doc(request,title))
    if text.startswith('redirect:'):
        return redirect(request,text[len('redirect:'):-1])
    return missing(request,title)

def delete(request,title):
    '''
    Delete the record
    '''
    doc = user_doc(request,title)
    log_page (request, 'delete: %s'%title)
    delete_doc (doc)
    return redirect(request,dirname(title))


def permitted(request,title=''):
    '''
    Check for all security violations
    '''
    return title.startswith('Anonymous') or user(request)!='Anonymous'


def illegal(request):
    title = 'IllegalMachine'
    log_page (request, 'illegal: %s'%title)
    user = str(request.user)
    text = user+format_doc(title)%ip(request)
    return render(request, 'doc.html', {'title': title, 'text': text})


def ip_ok(request):
    '''
    Check the IP address for the request
    '''
    valid = [ '108.59.4.75', '50.134.243.56', '127.0.0.1' ]
    return ip(request) in valid
