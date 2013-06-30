# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.cell_make'
        db.add_column('contacts_person', 'cell_make',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.cell_model'
        db.add_column('contacts_person', 'cell_model',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.cell_provider'
        db.add_column('contacts_person', 'cell_provider',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Person.work_phone_no'
        db.alter_column('contacts_person', 'work_phone_no', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, null=True))

        # Changing field 'Person.mobile_phone_no'
        db.alter_column('contacts_person', 'mobile_phone_no', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, null=True))

        # Changing field 'Person.home_phone_no'
        db.alter_column('contacts_person', 'home_phone_no', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, null=True))

    def backwards(self, orm):
        # Deleting field 'Person.cell_make'
        db.delete_column('contacts_person', 'cell_make')

        # Deleting field 'Person.cell_model'
        db.delete_column('contacts_person', 'cell_model')

        # Deleting field 'Person.cell_provider'
        db.delete_column('contacts_person', 'cell_provider')


        # User chose to not deal with backwards NULL issues for 'Person.work_phone_no'
        raise RuntimeError("Cannot reverse this migration. 'Person.work_phone_no' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Person.mobile_phone_no'
        raise RuntimeError("Cannot reverse this migration. 'Person.mobile_phone_no' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Person.home_phone_no'
        raise RuntimeError("Cannot reverse this migration. 'Person.home_phone_no' and its values cannot be restored.")

    models = {
        'contacts.person': {
            'Meta': {'object_name': 'Person'},
            'add_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'add_method': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '2'}),
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'car_make': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'car_model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'car_year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'cell_make': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cell_model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cell_provider': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'employer': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'ethnicity': ('django.db.models.fields.CharField', [], {'default': "'CA'", 'max_length': '40'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'home_phone_no': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'mobile_phone_no': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'work_phone_no': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['contacts']