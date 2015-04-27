from django.conf.urls import include, url
from django.contrib import admin
from selfblog.views import IndexView, PostDetailView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post'),
    url(r'^admin/', include(admin.site.urls)),
]
