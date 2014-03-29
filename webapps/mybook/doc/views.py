from datetime           import datetime
from django.contrib.auth.decorators import login_required
from django.http        import HttpResponseRedirect, HttpResponse
from django.utils.html  import escape
from os.path            import join, exists, dirname
from os                 import system,environ
from django.template    import loader, Context

from models             import *
from util.page          import show_page,put_page,get_page,page_redirect

page_data = { 'M_name': 'Not set', 'M_address': 'Not set', 'M_phone':'None' }

# Create a page for testing
def try_view(request):
    data = {'title': 'Data Binding', 
            'name': '{{name}}', 
            'address': '{{address}}', 
            'text': 'Three way data binding synchronizes the controls, models, and storage.'+
                    'This data is saved with every keystroke.',
            'var': 'Variable name',
            'value': 'Value amount'}
    return  render(request,'try.html',data)

# Get and put
def var_get(request,title):
    title = 'M_'+title
    return HttpResponse (page_data[title])

def var_set(request,title,value):
    title = 'M_'+title
    page_data[title] = value
    return HttpResponse (page_data[title])


logFile=environ['p']+'/logs/user/page.log'

# Render a web page
def render(request,template,data): 
    page = loader.get_template (template)
    return HttpResponse (page.render (Context(data)))


# Get the IP address for the request
def ip(request):
    if request.META['REMOTE_ADDR']=='127.0.0.1':
        return request.META['REMOTE_ADDR']
    return request.META['HTTP_X_FORWARDED_FOR']


# Name of requesting user
def user(request):
    if not request.user.is_anonymous():
        return request.user.username
    else:
        return 'Anonymous'

# Display the public document
def public_doc(request,title):
    return join(request.get_host(),'Public',title)


# Return the document for this user.
def user_doc(request,title):
    host = request.get_host()
    username = user(request)
    return join(host,username,title)


# Log the page hit in page.log  (time, ip, user, page, doc) 
def log_page(request,title):
    u   = user(request)
    f=open(logFile,'a')
    options = (str(datetime.now()), ip(request), user_doc(request,title))
    f.write(', '.join(options)+'\n')
    f.close()


# Render the view for a missing document
def new(request,title):
    #host = request.get_host()
    #text = show_page(host, user(request),'NewPage') # % title
    text = 'Creating a new page,'+title
    data = {'title':title, 'dir':dirname(title), 'text':text, 
            'default':basename(title), 'newpage':'{{newpage}}'}
    return render(request, 'new.html', data)


# Render the view for a missing document
def missing(request,title):
    text = 'Missing File:' + title
    data = {'title':title, 'dir':dirname(title), 'text':text, 
            'default':basename(title), 'newpage':'{{newpage}}'}
    return render(request, 'missing.html', data)


# Go to a specific page
def redirect(request,title):
    log_page (request,title)
    return HttpResponseRedirect('/'+title) 


# Render the appropriate doc view
def doc(request,title):
    doc = user_doc(request,title)
    log_page (request, title)
    host = request.get_host()
    u = user(request)
    p = page_redirect(host,u,title)
    if p: 
        return redirect(request,p)
    text = show_page(host,u,title)
    content =  {'site_title':request.get_host(), 'user':request.user, 'title': title, 'text': text}
    return render(request, 'doc.html', content)


# Render the home view
def home(request):
    return  doc(request,'Index')


@login_required(login_url='/login')
def private(request,title):
    return doc(request,title)


#-----------------------------------------------------------------------------
# Login


#@login_required(login_url='/login')
# Get and put doc directly
def store(request,title):
    log_page (request, title)
    doc  = user_doc(request,title)
    text = read_doc(doc)
    return HttpResponse(text)


#@login_required(login_url='/login')
# Create a form for editing the object details
def edit_form (request, doc, title=None, text=None):
    log_page (request, 'form:%s'%doc)
    return missing(request,title)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if request.POST.get('cancel', None):
            return redirect(request,title)
        else:
            if form.is_valid():
                log_page (request, 'save:%s'%doc)
                text =  form.cleaned_data['body']
                text = text.encode('ascii', 'ignore')
                text = text.replace('\r','')
                write_doc(doc,text)
                return redirect(request,title)
    else:
        note =  Note()
        note.path = title
        log_page (request,'read:%s'%doc)
        if not text:
            #text = read_doc(doc)
            text = get_page(request.get_host(),user(request),title)
        note.body = text
        form =  NoteForm(instance=note)
    data =  { 'form': form, 'title': title, 'banner': True  }
    return render(request, 'docedit.html', data)


# Render the add view
def edit(request,title):
    doc = user_doc(request,title)
    log_page (request, 'edit:%s'%doc)
    return edit_form (request, doc, title)


# Render the add view
def add(request,title):
    log_page (request,'add:%s'%title)
    return missing(request,title)
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
    return missing(request,title)
    delete_doc (doc)
    return redirect(request,dirname(title))


# Check for all security violations
def permitted(request,title=''):
    return title.startswith('Anonymous') or user(request)!='Anonymous'


# Check for permissions
def illegal(request):
    title = 'IllegalMachine'
    log_page (request, 'illegal: %s'%title)
    user = str(request.user)
    text = user+format_doc(title)%ip(request)
    return render(request, 'doc.html', {'title': title, 'text': text})


# Check the IP address for the request
def ip_ok(request):
    valid = [ '108.59.4.75', '50.134.243.56', '127.0.0.1' ]
    return ip(request) in valid
