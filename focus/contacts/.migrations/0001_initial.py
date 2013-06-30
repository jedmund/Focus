# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('contacts_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('birthdate', self.gf('django.db.models.fields.DateField')()),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('employer', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('ethnicity', self.gf('django.db.models.fields.CharField')(default='CA', max_length=40)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('home_phone_no', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20)),
            ('mobile_phone_no', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20)),
            ('work_phone_no', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.contrib.localflavor.us.models.USStateField')(max_length=2)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('add_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('add_method', self.gf('django.db.models.fields.IntegerField')(default=1, max_length=2)),
        ))
        db.send_create_signal('contacts', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('contacts_person')


    models = {
        'contacts.person': {
            'Meta': {'object_name': 'Person'},
            'add_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'add_method': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '2'}),
            'birthdate': ('django.db.models.fields.DateField', [], {}),
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