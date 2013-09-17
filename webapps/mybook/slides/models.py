from django.db      import models
from django.forms   import ModelForm
from datetime       import datetime
from os             import system


# Data for Slides object
class Slides (models.Model):
    title    = models.CharField (max_length=50)
    author   = models.CharField (max_length=50)
    text     = models.TextField (blank=True)
    created  = models.DateField (default=datetime.now(), editable=False)
    modified = models.DateField (default=datetime.now(), editable=False)
    expires  = models.DateField (default=datetime.now(), editable=False)

    def get_values(self):
        return [ self.pk, self.title, self.author, self.text, 
                 self.created , self.modified , self.expires ]
    
# Edit form for Slides
class SlidesForm (ModelForm):
    class Meta: model = Slides

# List all the slides
def list_slides():
    return [ s.get_values() for s in Slides.objects.all() ]

# Create a new slides object
def new_slides (title, author, text_file):
    print 'Creating new slides', title, author
    s        = Slides()
    s.title  = title
    s.text   = open(text_file).read()
    s.author = author
    s.save()

# Print the field of the slide decks
def print_slides():
    for s in list_slides():
        print s[0],  ' Title:',  "%-20s"%s[1],
        print '  Author:', "%-20s"%s[2]
        #print 'Text:\n', s[3]

# Save all of the slides as text files
def save_text():
    for s in Slides.objects.all():
        f = open('/home/seaman/Documents/slides/text/'+s.title+'.txt','w')
        f.write(s.text)
        f.close()
        #print 'Write',s.title

# Build a presentation from a slide object
def build_slides():
    save_text()
    system ('slide-build')

def delete_slides(id):
    Slides.objects.get(pk=id).delete()
