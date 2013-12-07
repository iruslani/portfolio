from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my Portfolio")

def hello(request):
    return HttpResponse("Hello world")