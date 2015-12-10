from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import logout

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'cloudgap.views.home', name='home'),
     url(r'^admin/', include(admin.site.urls)),
     #url(r'^api/$','cloudgap.views.api_handler'),
     url(r'^login/$','UserAccounts.views.auth_login'),
     url(r'^register/$','UserAccounts.views.register_user'),
     url(r'^logout/$','UserAccounts.views.user_logout'),
     url(r'^account/$', 'UserAccounts.views.user_settings'),
     url(r'^tbu/$', 'cloudgap.views.to_be_updated'),

)
