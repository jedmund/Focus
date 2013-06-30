# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Study.respondent_price'
        db.delete_column('groups_study', 'respondent_price')

        # Adding field 'Study.coop_price'
        db.add_column('groups_study', 'coop_price',
                      self.gf('django.db.models.fields.IntegerField')(default=1, max_length=4),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Study.respondent_price'
        db.add_column('groups_study', 'respondent_price',
                      self.gf('django.db.models.fields.IntegerField')(default=1, max_length=4),
                      keep_default=False)

        # Deleting field 'Study.coop_price'
        db.delete_column('groups_study', 'coop_price')


    models = {
        'groups.study': {
            'Meta': {'object_name': 'Study'},
            'compensation': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'coop_price': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'spots': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['groups.Venue']"})
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