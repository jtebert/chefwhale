from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Recipes
    url(r'^', include('recipes.urls', namespace="recipes")),
    
    # Accounts
    url(r'^accounts/', include('userena.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)