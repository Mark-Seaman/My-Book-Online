# Create your views here.
from contents           import gather_page_data, is_wisdom
from django.contrib.auth.decorators import login_required
from django.db          import models
from django.forms       import ModelForm
from django.http        import HttpResponseRedirect, HttpResponse
from django.shortcuts   import render_to_response
from django.template    import loader, Context
from send               import send_email

# Create a form for input
class Email(models.Model):
    email = models.CharField (max_length=100)

class EmailForm(ModelForm):
    class Meta:
        model=Email

# Decide which forms to show
def show_forms(request, topic, data):
    if topic=='Unsubscribe':  
        data['show_unsubscribe'] = True
    else:
        data['show_subscribe'] = True
    return data

#-----------------------------------------------------------------------------
# Normal pages

# Render a simple watermill page view
def livebook (request, topic):
    template='livebook.html'
    page = loader.get_template (template)
    data =  Context (gather_page_data (request, topic))
    #show_forms(request, topic, data)
    #data ['form'] = EmailForm()
    return HttpResponse (page.render (data))

# Load a Livebook page to display a topic
def guides(request):
    if 'harborwalk.shrinking-world.org'==request.get_host(): 
        return HttpResponseRedirect('http://shrinking-world.org/private/HarborWalk/Home')
    return livebook (request, 'Home')

#-----------------------------------------------------------------------------

# Load the subscribe page
def subscribe (request):
    if request.POST:
        data    = EmailForm(request.POST, instance=Email()).data
        subject = "Subscribe to Seaman's Log"
        page = 'http://'+request.get_host()+request.path
        message = "Please subscribe me to Seaman's Log\n\n"+\
            page + '\n\n' + data['email']
        send_email('', subject, message)
        return livebook(request,'Subscribed')
    else:
        return livebook (request,'Subscribe')

# Load the unsubscribe page
def unsubscribe (request):
    if request.POST:
        data    = EmailForm(request.POST, instance=Email()).data
        page    = 'http://'+request.get_host()+request.path
        subject = "Unsubscribe to Seaman's Log"
        message = "Please remove me from Seaman's Log\n\n"+\
            page + '\n\n' + data['email']
        send_email('', subject, message)
        return livebook(request,'Unsubscribed')
    else:
        return livebook (request,'Unsubscribe')

#-----------------------------------------------------------------------------
# Private pages

# Load hoa home page
def hoa_site(request):
    return HttpResponseRedirect('http://shrinking-world.org/private/HarborWalk/Home')

# Load a private page to display a topic
@login_required
def private(request,topic):
    return livebook (request,'../Private/'+topic)

# Load a private page to display a topic
@login_required
def private_home(request):
    return livebook (request, '../Private/Home')

