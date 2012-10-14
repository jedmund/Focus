from django.db import models
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField

class Person(models.Model):

    # Ethnicity mapping
    CAUCASIAN        = 'CA'
    AFRICAN_AMERICAN = 'AA'
    ASIAN_PACIFIC    = 'AP'
    HISPANIC         = 'HS'
    AMERICAN_INDIAN  = 'AI'
    SUBCONTINENTAL   = 'SA'

    ETHNICITY_CHOICES = (
        (CAUCASIAN,        'Caucasian'),
        (AFRICAN_AMERICAN, 'African-American'),
        (ASIAN_PACIFIC,    'Asian/Pacific Islander'),
        (HISPANIC,         'Hispanic'),
        (AMERICAN_INDIAN,  'American Indian/Alaskan Native'),
        (SUBCONTINENTAL,   'Subcontinental Asian')
    )

    # Method mapping
    INTERNAL = 1;
    APPLIED  = 2;

    METHOD_CHOICES = (
        (INTERNAL, 'Added internally'),
        (APPLIED,  'Applied via web form')
    );


    first_name = models.CharField(max_length=200)
    last_name  = models.CharField(max_length=200)

    birthdate  = models.DateField('birthdate')
    occupation = models.CharField(max_length=400, blank=True, null=True)
    employer   = models.CharField(max_length=400, blank=True, null=True)
    ethnicity  = models.CharField(max_length=40, choices=ETHNICITY_CHOICES, default=CAUCASIAN)

    email           = models.CharField(max_length=255, blank=True, null=True)
    home_phone_no   = PhoneNumberField(models.CharField('Home Phone #', blank=True, null=True))
    mobile_phone_no = PhoneNumberField(models.CharField('Mobile Phone #', blank=True, null=True))
    work_phone_no   = PhoneNumberField(models.CharField('Work Phone #', blank=True, null=True))

    city  = models.CharField(max_length=255)
    state = USStateField()

    notes = models.TextField(blank=True, null=True)

    add_date   = models.DateTimeField('Date added', auto_now_add=True)
    add_method = models.IntegerField('Method', max_length=2, choices=METHOD_CHOICES, default=INTERNAL)