from django.conf.urls import patterns, url
from register import views

urlpatterns = patterns('',
        url(r'^$', views.get_name, name='index'))
