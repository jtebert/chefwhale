from django.conf.urls import patterns, include, url
from recipes import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView, name='index'),
)
