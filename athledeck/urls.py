from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^athlete/(?P<pk>[0-9]+)/$', views.show),
    url(r'^athlete/new/$', views.new, name='athlete_new'),
    url(r'^athlete/(?P<pk>[0-9]+)/edit/$', views.edit, name='athlete_edit'),
)