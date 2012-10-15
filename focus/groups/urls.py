from django.conf.urls import patterns, url

urlpatterns = patterns('groups.views',
    url(r'^$', 'index'),
    url(r'^(?P<study_id>\d+)/$', 'study'),
    url(r'^(?P<study_id>\d+)/edit/$', 'edit_study'),
    url(r'^create/$', 'create_study'),

    url(r'^venue/(?P<venue_id>\d+)/$', 'venue'),
    url(r'^venue/(?P<venue_id>\d+)/edit/$', 'edit_venue'),
    url(r'^venue/create/$', 'create_venue'),
)