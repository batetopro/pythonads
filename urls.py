from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.index'),
    url(r'^checker/(?P<path>.*)$', 'views.checker'),
    url(r'^download$', 'views.download'),
    url(r'^preview/(?P<path>.*)$', 'views.preview'),
    url(r'^check/(?P<checker>.*)/(?P<path>.*)$', 'views.check'),
)
