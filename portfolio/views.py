from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime

def home(request):
    current_section = "Home"
    message = "Welcome to my Portfolio"
    t = get_template('page.html')
    html = t.render(Context({'message': message, "current_section": current_section}))
    return HttpResponse(html)

def hello(request):
    current_section = request.path
    message = "Hello world"
    t = get_template('page.html')
    html = t.render(Context({'message': message, "current_section": current_section}))
    return HttpResponse(html)

def template(request):
    message = "Hello World"
    t = get_template('page.html')
    html = t.render(Context({'message': message}))
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('page.html')
    current_section = "Hours Ahead"
    html = t.render(Context({'message': now , "current_section": current_section} ))
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = get_template('page.html')
    message = "In %s hour(s), it will be %s." % (offset, dt)
    current_section = "Hours Ahead"
    html = t.render(Context({'message': message, "current_section": current_section}))    
    return HttpResponse(html)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search(request):
    if 'search' in request.GET:
        message = 'You searched for: %s' % request.GET['search']
    else:
        message = 'You submitted an empty form or the submit string is missing.'
    t = get_template('page.html')
    html = t.render(Context({'message': message}))  
    return HttpResponse(html)