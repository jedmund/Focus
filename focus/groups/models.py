from django.db import models
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField
from django.forms import ModelForm

class Venue(models.Model):
    name     = models.CharField(max_length=400)
    address  = models.CharField(max_length=400)
    city     = models.CharField(max_length=255)
    state    = USStateField()
    zip_code = models.CharField(max_length=5)
    cross_st = models.CharField(max_length=255, blank=True, null=True)
    phone    = PhoneNumberField()

    def __unicode__(self):
        return self.name

class VenueForm(ModelForm):
    class Meta:
        model = Venue

class Study(models.Model):
    topic = models.CharField(max_length=255)
    venue = models.ForeignKey(Venue)
    notes = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.topic

class StudyForm(ModelForm):
    class Meta:
        model = Study

class Timeslot(models.Model):
    study        = models.ForeignKey(Study)
    datetime     = models.DateTimeField()
    coop_price   = models.IntegerField('Co-op price', max_length=4)
    compensation = models.IntegerField('Participation Compensation', max_length=4)
    spots = models.IntegerField(max_length=3)

    def __unicode__(self):
        return self.datetime

class TimeslotForm(ModelForm):
    class Meta:
        model = Timeslot