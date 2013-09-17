
def page(url):
    return '\n'.join([ text(url), page_html(url), context(url) ])

def text(url):
    return "text: "+url

def page_html(url):
    return "html: "+url

def context(url) :
    return "context: "+url
