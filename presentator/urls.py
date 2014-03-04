from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'presentor.views.play'),
                       url(r'^presentor/', include('presentor.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/', include('accounts.urls')),
                       url(r'^accounts/', include('django.contrib.auth.urls')),
                       )
