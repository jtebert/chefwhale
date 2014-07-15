from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chefwhale.views.home', name='home'),
    url(r'^', include('recipes.urls', namespace="recipes")),

    url(r'^admin/', include(admin.site.urls)),
)
