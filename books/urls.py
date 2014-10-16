from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'books.views.index', name='index'),
    url(r'^book/(?P<id>\d+)/', 'books.views.book', name='book'),
)
