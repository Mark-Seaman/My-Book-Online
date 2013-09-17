from django.db      import models
from django.forms   import ModelForm
from datetime       import datetime
from os             import system


# Data for ThoughtGram object
class ThoughtGram (models.Model):
    title    = models.CharField (max_length=50)
    author   = models.CharField (max_length=50)
    text     = models.TextField (blank=True)
    created  = models.DateField (default=datetime.now(), editable=False)
    modified = models.DateField (default=datetime.now(), editable=False)
    expires  = models.DateField (default=datetime.now(), editable=False)

    def get_values(self):
        return [ self.pk, self.title, self.author, self.text, 
                 self.created , self.modified , self.expires ]
    
# Edit form for ThoughtGram
class ThoughtGramForm (ModelForm):
    class Meta: model = ThoughtGram

# List all the thoughts
def list_thoughts():
    return [ s.get_values() for s in ThoughtGram.objects.all() ]

# Create a new thoughts object
def new_thought (title, author, text_file):
    print 'Creating new thoughts', title, author
    s        = ThoughtGram()
    s.title  = title
    s.text   = open(text_file).read()
    s.author = author
    s.save()

# Print the field of the slide decks
def print_thought():
    for s in list_thoughts():
        print s[0],  ' Title:',  "%-20s"%s[1],
        print '  Author:', "%-20s"%s[2]
        #print 'Text:\n', s[3]

# Delete one thought gram
def delete_thought(id):
    ThoughtGram.objects.get(pk=id).delete()
