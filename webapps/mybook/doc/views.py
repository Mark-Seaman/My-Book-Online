from django.contrib.auth.decorators import login_required
from django.http        import HttpResponseRedirect, HttpResponse
from django.shortcuts   import render
from os.path            import join, exists, dirname
from os                 import system,environ

from models             import *


def ip(request):
    '''
    Get the IP address for the request
    '''
    if request.META['REMOTE_ADDR']=='127.0.0.1':
        return request.META['REMOTE_ADDR']
    return request.META['HTTP_X_FORWARDED_FOR']


def ip_ok(request):
    '''
    Check the IP address for the request
    '''
    valid = [ '108.59.4.75', '50.134.243.56', '127.0.0.1' ]
    return ip(request) in valid


def missing(request,title):
    '''
    Render the view for a missing document
    '''
    text = format_doc('MissingFile')
    template = doc_template(title)
    link = '<a href="/doc/%s/%s/add">%s</a>'%(title,template,title)
    #'banner':True, 
    return render(request, 'doc.html', {'title': title, 'text': text%link })


def illegal(request):
    title = 'IllegalMachine'
    user = str(request.user)
    text = user+format_doc(title)%ip(request)
    return render(request, 'doc.html', {'title': title, 'text': text})


def doc(request,title):
    '''
    Render the appropriate doc view
    '''
    print 'doc: %s'%(title)
    if ip_ok(request) or request.user.is_superuser:
        if title.endswith('/'):
            return redirect(title+'Index')
        text = format_doc(title)
        content =  {'title': title, 'text': text}
        if request.user.is_superuser:
            content['banner'] = True 
        return render(request, 'doc.html', content)
    else:
        return illegal(request)


def home(request):
    '''
    Render the home view
    '''
    return doc(request, 'Index')


def redirect(title):
    '''
    Go to a specific page
    '''
    print 'redirect: %s'%(title)
    return HttpResponseRedirect('/doc/'+title) 


def edit_form (request, title=None):
    '''
    Create a form for editing the object details
    '''
    print 'form: %s'%(title)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if request.POST.get('cancel', None):
            title = form.data['path']
            if not title:
                title = 'Home'
            return redirect(title)
        else:
            if form.is_valid():
                title = form.data['path']
                print 'save: %s'%(title)
                text =  form.cleaned_data['body']
                text = text.replace('\r','')
                write_doc(title,text)
                return redirect(title)
    else:
        note =  Note()
        if  title:
            note.path = title
            if read_doc(title):
                print 'read: %s'%(title)
                note.body = read_doc(title)
        form =  NoteForm(instance=note)
    #  'banner':True,
    data =  { 'form': form, 'title': title  }
    return render(request, 'docedit.html', data)


def add(request,title,template):
    '''
    Render the add view
    '''
    print 'add: %s, %s'%(title,template)
    clone_template(title)
    return edit_form (request,title)
   


def edit(request,title):
    '''
    Render the add view
    '''
    print 'edit: %s'%(title)
    return edit_form (request,title)


def delete(request,title):
    '''
    Delete the record
    '''
    print 'delete: %s'%(title)
    delete_doc (title)
    return redirect(dirname(title))


# Sample code:
#    if request.user.is_anonymous(): return 0
#    if not request.user.is_superuser:  return redirect('/NoAccess') 
#    u = UserAccount.objects.get(pk=request.user.pk).pk
#    if not u==user_id:    return redirect('/NoAccess')
