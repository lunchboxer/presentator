from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',
                       #url(r'^login/$', 'login', name='login'),
                       url(r'^ajaxlogin$', 'ajaxlogin'),
                       #url(r'^logout/$', 'logout', name='logout'),
                       url(r'^ajaxlogout$', 'ajaxlogout'),
                       url(r'^ajaxregister$', 'ajaxregister'),
                       #url(r'^profile/$', 'profile'),
                       #url(r'^profile_edit/$', 'edit_profile'),
                       )
