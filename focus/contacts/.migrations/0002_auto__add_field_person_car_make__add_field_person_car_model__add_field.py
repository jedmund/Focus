# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.car_make'
        db.add_column('contacts_person', 'car_make',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.car_model'
        db.add_column('contacts_person', 'car_model',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.car_year'
        db.add_column('contacts_person', 'car_year',
                      self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Person.car_make'
        db.delete_column('contacts_person', 'car_make')

        # Deleting field 'Person.car_model'
        db.delete_column('contacts_person', 'car_model')

        # Deleting field 'Person.car_year'
        db.delete_column('contacts_person', 'car_year')


    models = {
        'contacts.person': {
            'Meta': {'object_name': 'Person'},
            'add_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'add_method': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '2'}),
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'car_make': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'car_model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'car_year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'employer': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'ethnicity': ('django.db.models.fields.CharField', [], {'default': "'CA'", 'max_length': '40'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'home_phone_no': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'mobile_phone_no': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'work_phone_no': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['contacts']