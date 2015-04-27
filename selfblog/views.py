from django.views.generic import ListView, DetailView
from .models import Post


class IndexView(ListView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs['posts'] = self.object_list
        return super(IndexView, self).get_context_data(**kwargs)

    def get_queryset(self):
        posts = Post.objects.defer('content', 'content_html').filter(status=0)
        return posts


class PostDetailView(DetailView):
    template_name = 'detail.html'