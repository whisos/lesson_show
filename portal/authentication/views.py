from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import login as auth_login

from django.urls import reverse_lazy
from django.views.generic.base import RedirectView

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.contrib.auth.models import User
from authentication.models import CustomUser
from django.db import IntegrityError
# Create your views here.
def base_view(request):
    return render(request, 'base.html')


def test_view(request):
    return render(request, 'test.html')

# Register --- Login --- Logout #

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                login(request, user)  # Вхід користувача в систему після реєстрації
                return redirect('base')
            except IntegrityError:
                return HttpResponse("Ім'я користувача вже існує. Будь ласка, виберіть інше ім'я користувача.")
        else:
            return HttpResponse("Паролі не співпадають.")
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('base')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('base'))


# --- Profile --- #
@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        user = request.user
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        
        return redirect('profile')
    
    return render(request, 'edit_profile.html')