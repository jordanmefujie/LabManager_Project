from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import UserPreference, AppConfig

# Create your views here.
@login_required
def user_settings(request):
    preferences = UserPreference.objects.filter(user=request.user)
    if request.method == 'POST':
        for pref in preferences:
            new_value = request.POST.get(pref.preference_name)
            if new_value:
                pref.preference_value = new_value
                pref.save()

                return redirect('user_settings')
            return render(request, 'settings/settings.html', {'preferences': preferences})

@login_required
def app_config(request):
    configs = AppConfig.objects.all()
    if request.method == 'POST':
        for config in configs:
            new_value = request.POST.get(config.config_name)
            if new_value:

                config.config_value = new_value
                config.save()
                return redirect('app_config')
            return render(request, 'settings/app_config.html', {'configs': configs})

def settings_view(request):
    return render(request, 'settings/settings.html')

# @login_required
# def settings_view(request):
#    if request.method == 'POST':
#	for pref in UserPreference.objects.filter(user=request.user):
#            pref_value = request.POST.get(pref.preference_name, '')
#            pref.preference_value = pref_value
#            pref.save()
#        return redirect('dashboard-settings')
#
#    preferences = UserPreference.objects.filter(user=request.user)
#    return render(request, 'settings/dashboard-settings.html', {'preferences': preferences})
@login_required
def settings_view(request):
    if request.method == 'POST':
        profile_form = UserChangeForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)
        
        if 'profile_update' in request.POST and profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard-settings')
        
        if 'password_update' in request.POST and password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('dashboard-settings')
    else:
        profile_form = UserChangeForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
    
    return render(request, 'settings/dashboard-settings.html', {
        'profile_form': profile_form,
        'password_form': password_form,
    })
