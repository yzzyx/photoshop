from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'books.views.index', name='index'),
    url(r'^books/', include('books.urls', 'books')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('books:index'),
          permanent=False), name='index'),


    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
