from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Subreddit(models.Model):
    name = models.CharField(max_length=25, unique=True)
    user = models.ManyToManyField(User)
    creation_date = models.DateTimeField()

    def posts(self):
        return Post.objects.filter(subreddit=self.name)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE, null=True)
    posted_at = models.DateTimeField()

    def __str__(self):
        return f"title:{self.title}, body:{self.body}, upvotes:{self.upvotes}, downvotes:{self.downvotes}, user={self.user}, subreddit:{self.subreddit}"

class Comment(models.Model):
    comment_text = models.TextField()
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    commented_at = models.DateTimeField()

    def __str__(self):
        return f"title:{self.comment_text}, upvotes:{self.upvotes}, downvotes:{self.downvotes}, user={self.user}, post:{self.post}"
    
    
