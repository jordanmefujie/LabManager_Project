from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import views as auth_views
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile

# Register view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Create profile for the new user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after successful registration
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/profile.html', context)

# Password reset confirm view
class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

# Login view
def login_view(request):
    return render(request, 'accounts/login.html')

# Password reset view
def password_reset_view(request):
    return render(request, 'accounts/password_reset.html')
