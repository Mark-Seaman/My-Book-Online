# Create your views here.
from contents           import gather_page_data, is_wisdom
from django.contrib.auth.decorators import login_required
from django.db          import models
from django.forms       import ModelForm
from django.http        import HttpResponse
from django.template    import loader, Context
from send               import send_email
from views              import livebook
from contents           import gather_page_data

#-----------------------------------------------------------------------------
# Messages for feedback

# Define the fields in a message
class Message(models.Model):
    subject = models.CharField (max_length=100)
    body    = models.TextField (null=True, default="None")

# Create a form for input
class MessageForm(ModelForm):
    class Meta:
        model=Message

# Send a message via email
def message(request):
    if request.POST:
        data    = MessageForm(request.POST, instance=Message()).data
        subject = data['subject']
        body    = data['body']
        send_email('', subject, body)
        return  livebook (request, './Sent')
    else:
        template='message.html'
        page = loader.get_template (template)
        data =  Context (gather_page_data (request, "Home"))
        data['title'] ='New Message'
        data['form'] = MessageForm()
        data['show_unsubscribe'] = False
        data['show_subscribe']   = False    
        return HttpResponse (page.render (data))
