from django.db import models

class Person(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)

    birthdate=models.DateField('birthdate')
    occupation=models.CharField(max_length=400)
    employer=models.CharField(max_length=400)
    ethnicity=models.CharField(max_length=40)

    email=models.CharField(max_length=255)
    home_phone_no=models.CharField(max_length=50)
    mobile_phone_no=models.CharField(max_length=50)
    work_phone_no=models.CharField(max_length=50)

    city=models.CharField(max_length=255)
    state=models.CharField(max_length=2)

    notes=models.TextField()