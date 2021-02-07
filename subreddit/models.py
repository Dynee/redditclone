from django.db import models
from django.contrib.auth.models import User


class Subreddit(models.Model):
    name = models.CharField(max_length=25)
    user_id = models.ManyToManyField(User)

class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subreddit_id = models.ForeignKey(Subreddit, on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    comment_text = models.TextField()
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    
    
