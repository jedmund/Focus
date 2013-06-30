from django.contrib import admin
from groups.models import Study, Venue, Timeslot

admin.site.register(Study)
admin.site.register(Venue)
admin.site.register(Timeslot)