from django.urls import path

from . import views

urlpatterns = [
    path('<slug:subreddit>/', views.all, name='subreddit'),
]