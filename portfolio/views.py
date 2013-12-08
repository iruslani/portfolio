from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def home(request):
    return HttpResponse("Welcome to my Portfolio")

def hello(request):
    return HttpResponse("Hello world")

def template(request):
    message = "Hello World"
    t = get_template('base.html')
    html = t.render(Context({'message': message}))
    return HttpResponse(html)