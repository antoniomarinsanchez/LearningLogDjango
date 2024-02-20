"""Defines url patterns for users"""

from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # Includes predefined authentication url
    path('', include('django.contrib.auth.urls')),
    # Register web page
    path('register/', views.register, name='register'),
]