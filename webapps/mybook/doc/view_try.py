from django.http        import HttpResponse


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
