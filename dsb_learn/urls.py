from django.conf.urls import include, url
from django.contrib import admin
from selfblog.views import IndexView

urlpatterns = [
    # Examples:
    url(r'^$', IndexView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
