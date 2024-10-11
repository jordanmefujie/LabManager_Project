from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dem(request):
    return HttpResponse ("<h1>DEMO</h1>")

def demo(request):
    return render(request, 'blog.html')

def home(request):
    return HttpResponse("<h1>Home page</>")

def login(request):
    return HttpResponse("<h1>Login page</>")

def about(request):
    return HttpResponse("<h1>About Us</>")

def contact(request):
    return HttpResponse("<h1>Contact Us</>")

def services(request):
    return HttpResponse("<h1>Services</>")

def home(request):
    return render(request, 'demo/home.html')
