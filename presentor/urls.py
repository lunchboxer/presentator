from django.conf.urls import patterns, url
from presentor import views

urlpatterns = patterns('',
                       url(r'^show', views.show),
                       url(r'^fetchshow/(?P<id>\d+)/$', views.fetchshow),
                       url(r'^control/(?P<id>\d+)/$', views.control,
                           name="control"),
                       url(r'^student', views.student),
                       url(r'^$', views.play),
                       url(r'^listslideshows', views.listslideshows),
                       url(r'^about', views.about),
                       )
