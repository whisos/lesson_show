"""
URL configuration for portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from authentication.views import base_view, login_view, logout_view, register_view, profile_view, edit_profile_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name="main.html"), name="main_page"),

    # Register --- Login --- Logout #
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    #--- Profile ---#
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),

    #--- Events ---#
    path('event/', include('event.urls')),

    # Voting polls #
    path('polls/', include('voting.urls')),

    # Forum #
    path('forum/', include('forum.urls'))
]
