from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^athlete/(?P<pk>[0-9]+)/$', views.show)
)