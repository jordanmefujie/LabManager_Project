from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home/home.html')

def contact_view(request):
    return render(request, 'contact')

def services_view(request):
    return render(request, 'services')

def about_view(request):
    return render(request, 'about')

def register(request):
    return render(request, 'register')

def views_login(request):
    return render(request, 'login')

def apps_link_view(request):
    return render(request, 'home/apps_link.html')
