from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^contacts/', include('contacts.urls')),
    url(r'^groups/', include('groups.urls')),
    url(r'^admin/', include(admin.site.urls)),
)