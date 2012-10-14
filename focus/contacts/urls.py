from django.conf.urls import patterns, url

urlpatterns = patterns('contacts.views',
    url(r'^$', 'index'),
    url(r'^(?P<person_id>\d+)/$', 'person'),
    url(r'^(?P<person_id>\d+)/edit/$', 'edit'),
    url(r'^create/$', 'create'),
)