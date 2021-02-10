from django.urls import path

from .views import PostDetailView, SubredditView

urlpatterns = [
    path('', SubredditView.as_view(), name='subreddit'),
    path('p/<int:pk>', PostDetailView.as_view(), name='post')
]