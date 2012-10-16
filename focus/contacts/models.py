from django.forms import ModelForm
from django.db import models
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField

class Person(models.Model):
    ETHNICITY_CHOICES = (
        ('Caucasian',                      'Caucasian'),
        ('African-American',               'African-American'),
        ('Asian/Pacific Islander',         'Asian/Pacific Islander'),
        ('Hispanic',                       'Hispanic'),
        ('American Indian/Alaskan Native', 'American Indian/Alaskan Native'),
        ('Subcontinental Asian',           'Subcontinental Asian')
    )

    # Cellphone mapping
    CELLPHONE_MAKE = (
        ('Acer', 'Acer'),
        ('Apple', 'Apple'),
        ('BenQ-Siemens', 'BenQ-Siemens'),
        ('Dell', 'Dell'),
        ('Ericsson', 'Ericsson'),
        ('Garmin-Asus', 'Garmin-Asus'),
        ('HP', 'HP'),
        ('HTC', 'HTC'),
        ('Huawei', 'Huawei'),
        ('Kyocera', 'Kyocera'),
        ('LG', 'LG'),
        ('Meizu', 'Meizu'),
        ('Motorola', 'Motorola'),
        ('Nokia', 'Nokia'),
        ('Palm', 'Palm'),
        ('Panasonic', 'Panasonic'),
        ('Philips', 'Philips'),
        ('RIM', 'RIM'),
        ('Samsung', 'Samsung'),
        ('Sharp', 'Sharp'),
        ('Siemens', 'Siemens'),
        ('Sony', 'Sony'),
        ('Sony Ericsson', 'Sony Ericsson'),
        ('Toshiba', 'Toshiba'),
        ('ViewSonic', 'ViewSonic'),
    )

    CELLPHONE_PROVIDER = (
        ('AT&T Mobility', 'AT&T Mobility'),
        ('Verizon Wireless', 'Verizon Wireless'),
        ('Sprint Nextel', 'Sprint Nextel'),
        ('T-Mobile USA', 'T-Mobile USA'),
        ('TracFone Wireless', 'TracFone Wireless'),
        ('MetroPCS', 'MetroPCS'),
        ('Cricket Wireless', 'Cricket Wireless'),
        ('U.S. Cellular', 'U.S. Cellular'),
        ('Virgin Mobile USA', 'Virgin Mobile USA'),
        ('Boost Mobile', 'Boost Mobile'),
        ('Clear Talk', 'Clear Talk'),
        ('Wal-Mart Family Mobile', 'Wal-Mart Family Mobile')
    )

    # Gender
    MALE   = 1;
    FEMALE = 2;
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
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
    gender     = models.IntegerField(max_length=2, choices=GENDER_CHOICES, default=MALE)

    birthdate  = models.DateField('birthdate')
    occupation = models.CharField(max_length=400, default='', blank=True, null=True)
    employer   = models.CharField(max_length=400, default='', blank=True, null=True)
    ethnicity  = models.CharField(max_length=40, choices=ETHNICITY_CHOICES, default='Caucasian')

    email           = models.CharField(max_length=255, default='', blank=True, null=True)
    home_phone_no   = PhoneNumberField('Home Phone #', default='', blank=True, null=True)
    mobile_phone_no = PhoneNumberField('Mobile Phone #', default='', blank=True, null=True)
    work_phone_no   = PhoneNumberField('Work Phone #', default='', blank=True, null=True)

    cell_make       = models.CharField('Cellphone Make', max_length=255,
                                        choices=CELLPHONE_MAKE, blank=True, null=True)
    cell_model      = models.CharField('Cellphone Model', max_length=255, blank=True, null=True)
    cell_provider   = models.CharField('Cellphone Provider', max_length=255,
                                        choices=CELLPHONE_PROVIDER, blank=True, null=True)

    car_make        = models.CharField('Car Make', max_length=255, blank=True, null=True)
    car_model       = models.CharField('Car Model', max_length=255, blank=True, null=True)
    car_year        = models.IntegerField('Car Year', max_length=4, blank=True, null=True)

    city  = models.CharField(max_length=255)
    state = USStateField()

    notes = models.TextField(blank=True, null=True)

    add_date   = models.DateTimeField('Date added', auto_now_add=True)
    add_method = models.IntegerField('Method', max_length=2, choices=METHOD_CHOICES, default=INTERNAL)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

class PersonForm(ModelForm):
    class Meta:
        model = Person