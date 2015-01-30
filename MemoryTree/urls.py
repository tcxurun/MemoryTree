from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import RSSFeed

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'MemoryTree.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^$', 'blog.views.index'),
    url(r'^blog/$', 'blog.views.index', name='home'),
    url(r'^blog/(?P<id>\d+)/$', 'blog.views.detail', name='detail'),
    url(r'^blog/archive/(?P<id>\d+)/$', 'blog.views.category_archive', name
        ='blog-category-archive'),
    url(r'^blog/archive/(?P<year>[\d]+)/(?P<month>[\d]+)/$', 'blog.views.date_archive',
        name='blog-date-archive'),
    url(r'^aboutme/$', 'blog.views.about_me', name='about_me'),
    url(r'^feed/$', RSSFeed(), name='RSS'),

    url(r'^wiki/$', 'wiki.views.index', name='wiki-index'),
    url(r'^wiki/(?P<id>\d+)/$', 'wiki.views.single', name='wiki-single'),
    url(r'^wiki/archive/(?P<id>\d+)/$', 'wiki.views.category_archive', name
        ='wiki-category-archive'),
    url(r'^wiki/category/view/$', 'wiki.views.category_view', name='category-view'),
)
