from django.contrib import admin
from subreddit.models import Subreddit, Post, Comment

class SubredditAdmin(admin.ModelAdmin):
    list_display = ['name', 'creation_date']
    ordering = ['creation_date']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'subreddit', 'posted_at']
    ordering = ['posted_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_text', 'user', 'commented_at']
    ordering = ['commented_at']

admin.site.register(Subreddit, SubredditAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)