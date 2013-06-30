# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Study.venue'
        db.delete_column('groups_study', 'venue_id')


    def backwards(self, orm):
        # Adding field 'Study.venue'
        db.add_column('groups_study', 'venue',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['groups.Venue']),
                      keep_default=False)


    models = {
        'groups.study': {
            'Meta': {'object_name': 'Study'},
            'compensation': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'coop_price': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'spots': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'groups.timeslot': {
            'Meta': {'object_name': 'Timeslot'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['groups.Study']"})
        },
        'groups.venue': {
            'Meta': {'object_name': 'Venue'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'zip_code': ('django.contrib.localflavor.us.models.USPostalCodeField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['groups']