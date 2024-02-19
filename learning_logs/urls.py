"""Defines patterns of URL for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Initial page
    path('', views.index, name='index'),
    # Page that shows all the topics
    path('topics/', views.topics, name='topics'),
    # Details for each topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Add new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Add new entry
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
]
