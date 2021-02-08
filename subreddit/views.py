from django.shortcuts import render
from django.db.models import Max

from .models import Subreddit, Post, Comment

def index(request):
    """
    Return the posts with the max number of upvotes for each subreddit
    """
    subreddits = Subreddit.objects.all()
    top_posts = []
    for subreddit in subreddits:
        posts = Post.objects.filter(subreddit=subreddit).order_by('-upvotes')
        if posts:
            top_posts.append(posts[0])
    context = {'posts': top_posts}
    return render(request, 'subreddit/index.html', context)

def all(request, subreddit):
    sr = Subreddit.objects.get(name=subreddit)
    posts = Post.objects.filter(subreddit=sr).order_by('-posted_at')
    context = {'posts': posts, 'subreddit': subreddit}
    return render(request, 'subreddit/subreddit.html', context)

