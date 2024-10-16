from django.shortcuts import render

# Create your views here.
def contact_view(request):
    return render(request, 'Links/contact.html')

def services_view(request):
    return render(request, 'Links/services.html')

def about_view(request):
    return render(request, 'Links/about.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')
