from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http        import HttpResponseRedirect, HttpResponse
from django.shortcuts   import render
from models             import *
from views              import user_doc,user,log_page,redirect
from json               import dumps




#----------------------------------------------------------------
#  Job Thumper specific code

def build_json(doc):
    text = read_doc(doc+'.res')
    keys = read_doc(doc+'.phrases')
    nonkeys = read_doc(doc+'.unknown')
    content = [
        { 'title':"Resume Text", 'content':text },
        { 'title':"Keys",        'content':keys },
        { 'title':"Non-keys",    'content':nonkeys }
        ]
    return dumps(content)


def load_job (doc, title):
    json = build_json(doc)
    return {'title':title, 'content':json,
            'tabtitle':'{{tab.title}}', 'tabcontent':'{{tab.content}}'}


@login_required(login_url='/login')
def jobs(request,title):
    '''
    Render the jobs view
    '''
    doc = join(user(request), 'jobs', title)
    log_page (request, title)
    data = load_job (doc, title)
    return render(request, 'jobs.html', data)
    

def register(request):
    '''
    Allow a new user to register
    '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            form.save()
            user = authenticate(username=username, password=password)
            user.is_staff = True
            user.save()
            return HttpResponseRedirect("/login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })

def enable(request,title):
    '''
    Enable an application for this user
    '''
    doc = user_doc(request,title)
    log_page (request, 'enable: %s'%doc)
    enable_app(user(request),title)
    return redirect(request,'Apps')


def disable(request,title):
    '''
    Disable an application for this user
    '''
    doc = user_doc(request,title)
    log_page (request, 'disable: %s'%doc)
    disable_app(user(request),title)
    return redirect(request,'Apps')
