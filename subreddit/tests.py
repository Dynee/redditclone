from django.test import TestCase
from django.contrib.auth.models import User
from .models import Subreddit, Post, Comment
from django.utils import timezone

import datetime


class SubredditTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create('testUser', 'test@example.com', 'password')
        self.subreddit = Subreddit.objects.create(name='Missing411', creation_date=timezone.now())
        Post.objects.create(
            title='post 1', 
            body='this is postbody1', 
            upvotes=0, 
            downvotes=0, 
            user=self.user, 
            subreddit=self.subreddit,
            posted_at=timezone.now()
        )
        Post.objects.create(
            title='post 2', 
            body='this is postbody2', 
            upvotes=0, 
            downvotes=0, 
            user=self.user, 
            subreddit=self.subreddit,
            posted_at=timezone.now()
        )
        Post.objects.create(
            title='post 3', 
            body='this is postbody3', 
            upvotes=0, 
            downvotes=0, 
            user=self.user, 
            subreddit=self.subreddit,
            posted_at=timezone.now()
        )
    
    def test_sort_by_new_should_return_posts_created_within_24_hours(self):
        sr = Subreddit.objects.get(name='Missing411')
        posts = sr.sort_by_new()
        
        


