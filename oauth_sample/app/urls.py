from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views as app_views

urlpatterns = [
    url(r'^home/$', app_views.home, name='home'),
    url(r'^acceder/$', app_views.acceder, name='acceder'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
