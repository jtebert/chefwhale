from django.conf.urls import patterns, include, url

from recipes import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^recipes/$', views.RecipeListView.as_view(), name='recipe_list'),
    url(r'^recipe/(?P<pk>\d+)/$', views.recipe_detail, name='recipe_detail'),
)
