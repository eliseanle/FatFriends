from django.conf.urls.defaults 
import patterns, include, url
from django.views.static import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
  #url('^hello/$', 'hello.views.hello'),
  (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
                          {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
                             {'document_root': settings.MEDIA_ROOT}),
    # Examples:
    # url(r'^$', 'FatFriends.views.home', name='home'),
    # url(r'^FatFriends/', include('FatFriends.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
