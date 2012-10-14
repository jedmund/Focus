from django.db import models
from django.contrib.localflavor.us.models import USStateField, USPostalCodeField, PhoneNumberField
from contacts.models import Person

class Venue(models.Model):
    name     = models.CharField(max_length=400)
    address  = models.CharField(max_length=400)
    city     = models.CharField(max_length=255)
    state    = USStateField()
    zip_code = USPostalCodeField()

class Study(models.Model):
    topic = models.CharField(max_length=255)
    spots = models.IntegerField(max_length=3)
    venue = models.ForeignKey(Venue)

    respondent_price = models.IntegerField('Price per Respondent', max_length=4)
    compensation     = models.IntegerField('Participation Compensation', max_length=4)

    notes = models.TextField(blank=True, null=True)

class Timeslot(models.Model):
    study = models.ForeignKey(Study)
    datetime = models.DateTimeField()