from django.views.generic import TemplateView, ListView, DetailView

from .models import Subreddit, Post, Comment

# Create class based View for subreddit
class IndexPageView(ListView):
    model = Post
    template_name = 'subreddit/index.html'

    def get_queryset(self):
        return Post.objects.order_by('upvotes')

class SubredditView(ListView):
    model = Post
    template_name = 'subreddit/subreddit.html'

    def get_queryset(self):
        return Post.objects.filter(subreddit=Subreddit.objects.get(name=self.kwargs['subreddit']))

class SearchResultsView(ListView):
    model = Post
    template_name = 'subreddit/search.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        return Post.objects.filter(title__icontains=query)

class PostDetailView(DetailView):
    model = Post
    template_name = 'subreddit/post_detail.html'
    

