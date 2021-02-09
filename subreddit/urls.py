from django.urls import path

from .views import SubredditView

urlpatterns = [
    path('<slug:subreddit>/', SubredditView.as_view(), name='subreddit'),
]