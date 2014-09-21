from django.conf.urls import patterns, include, url

from recipes import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^recipes/$', views.recipe_list, name='recipe_list'),
    url(r'recipes/add/$', views.recipe_add, name='recipe_add'),
    url(r'^recipes/(?P<pk>\w+)/edit/$', views.recipe_edit, name='recipe_edit'),
    url(r'^recipes/(?P<pk>\w+)/$', views.recipe_detail, name='recipe_detail'),
    url(r'^boxes/$', views.box_list, name='box_list'),
    url(r'^box/(?P<pk>\d+)/$', views.box_detail, name='box_detail'),
    url(r'^about/$', views.about, name='about'),
)
