from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Recipes
    url(r'^', include('recipes.urls', namespace="recipes")),
    
    # Accounts
    url(r'^accounts/', include('userena.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
