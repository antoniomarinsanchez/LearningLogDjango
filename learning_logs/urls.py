"""Defines patterns of URL for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Initial page
    path('', views.index, name='index')
]
