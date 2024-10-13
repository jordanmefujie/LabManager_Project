from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Existing dashboard view
@login_required
def dashboard_view(request):
    context = {
        'user': request.user,
    }
    return render(request, 'dashboard/home.html', context)

# New home view
def home(request):
    return render(request, 'dashboard/home.html')  # No comma here

# New contact view
def contact(request):
    return render(request, 'dashboard/contact.html')  # No comma here

def services(request):
    return render(request, 'dashboard/services.html')  # No comma here

def about(request):
    return render(request, 'dashboard/about.html')  # No comma here

def experiments_view(request):
    return render(request, 'dashboard/experiments.html')

def equipment_view(request):
    return render(request, 'dashboard/equipment.html')

def reports_view(request):
    return render(request, 'reports/reports.html')

def settings_view(request):
    return render(request, 'settings/settings.html')
