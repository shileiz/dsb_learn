from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Post
# TODO 后续移到 setting 里
PAGE_NUM = 10


class IndexView(ListView):
    query = None
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        paginator = Paginator(self.object_list, PAGE_NUM)
        # TODO page(1) 需要改为 page(self.cur_page)
        kwargs['posts'] = self.object_list
        kwargs['query'] = self.query
        return super(IndexView, self).get_context_data(**kwargs)

    def get_queryset(self):
        posts = Post.objects.defer('content', 'content_html').filter(status=0)
        return posts

