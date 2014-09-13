from django.conf.urls import patterns, include, url

from recipes import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^recipes/$', views.recipe_list, name='recipe_list'),
    url(r'^recipe/(?P<pk>\d+)/$', views.recipe_detail, name='recipe_detail'),
    url(r'add-recipe/$', views.recipe_add, name='recipe_add'),
    url(r'^boxes/$', views.box_list, name='box_list'),
    url(r'^box/(?P<pk>\d+)/$', views.box_detail, name='box_detail'),
    url(r'^about/$', views.about, name='about'),
)
