from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime

def home(request):
    return HttpResponse("Welcome to my Portfolio")

def hello(request):
    return HttpResponse("Hello world")

def template(request):
    message = "Hello World"
    t = get_template('base.html')
    html = t.render(Context({'message': message}))
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('base.html')
    html = t.render(Context({'message': now}))
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = get_template('base.html')
    message = "In %s hour(s), it will be %s." % (offset, dt)
    html = t.render(Context({'message': message}))    
    return HttpResponse(html)