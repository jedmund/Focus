from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^contacts/$', 'contacts.views.index'),
    url(r'^contacts/(?P<poll_id>\d+)/$', 'contacts.views.person'),
    url(r'^contacts/(?P<poll_id>\d+)/edit/$', 'contacts.views.edit'),
    url(r'^contacts/create/$', 'contacts.views.create'),
    url(r'^admin/', include(admin.site.urls)),
)