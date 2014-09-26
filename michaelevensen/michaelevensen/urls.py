from django.conf.urls import patterns, include, url
from django.contrib import admin

from portfolio import views

urlpatterns = patterns('',
   
    url(r'^admin/', include(admin.site.urls)),

	url(r'^summernote/', include('django_summernote.urls')),

 	url(r'^$', 'portfolio.views.index'),
 	url(r'^(?P<case>[-\w]+)/(?P<chapter>[-\w]+)/$', 'portfolio.views.case'),
 	url(r'^(?P<case>[-\w]+)/$', 'portfolio.views.case'),
)