import datetime, pytz
from django.db import models
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField
from django.forms import ModelForm, NumberInput

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
    duration     = models.IntegerField('Duration (minutes)', max_length=4) # Duration in minutes
    coop_price   = models.IntegerField('Co-op price', max_length=4)
    compensation = models.IntegerField('Participation Compensation', max_length=4)
    spots = models.IntegerField(max_length=3)

    def __unicode__(self):
        return self.study.topic + ' on ' + self.datetime.strftime('%m/%d/%Y') + ' at ' + self.datetime.strftime('%I:%M %p')

class TimeslotForm(ModelForm):
    class Meta:
        model = Timeslot
        widgets = {
            'duration'     : NumberInput(attrs={'class':'duration', 'min':'0', 'step':'5'}),
            'coop_price'   : NumberInput(attrs={'class':'coop_price', 'min':'0', 'step':'5'}),
            'compensation' : NumberInput(attrs={'class':'compensation', 'min':'0', 'step':'5'}),
            'spots'        : NumberInput(attrs={'class':'spots', 'min':'1', 'step':'1'}),
        }