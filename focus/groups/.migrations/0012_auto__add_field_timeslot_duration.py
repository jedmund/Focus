# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Timeslot.duration'
        db.add_column('groups_timeslot', 'duration',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Timeslot.duration'
        db.delete_column('groups_timeslot', 'duration')


    models = {
        'groups.study': {
            'Meta': {'object_name': 'Study'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['groups.Venue']"})
        },
        'groups.timeslot': {
            'Meta': {'object_name': 'Timeslot'},
            'compensation': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'coop_price': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'duration': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spots': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['groups.Study']"})
        },
        'groups.venue': {
            'Meta': {'object_name': 'Venue'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cross_st': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['groups']