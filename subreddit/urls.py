from django.urls import path

from .views import SubredditView, PostDetailView

urlpatterns = [
    path('<slug:subreddit>/', SubredditView.as_view(), name='subreddit'),
    path('<slug:subreddit>/p/<int:id>', PostDetailView.as_view(), name='post')
]