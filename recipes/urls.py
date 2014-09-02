from django.conf.urls import patterns, include, url

from recipes import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^recipes/$', views.recipe_list, name='recipe_list'),
    url(r'^recipe/(?P<pk>\d+)/$', views.recipe_detail, name='recipe_detail'),
    url(r'^boxes/$', views.box_list, name='box_list')
)
