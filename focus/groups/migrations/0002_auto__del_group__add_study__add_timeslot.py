# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Group'
        db.delete_table('groups_group')

        # Adding model 'Study'
        db.create_table('groups_study', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('spots', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['groups.Venue'])),
            ('respondent_price', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('compensation', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('groups', ['Study'])

        # Adding model 'Timeslot'
        db.create_table('groups_timeslot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['groups.Study'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('groups', ['Timeslot'])


    def backwards(self, orm):
        # Adding model 'Group'
        db.create_table('groups_group', (
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('compensation', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('respondent_price', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['groups.Venue'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('spots', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
        ))
        db.send_create_signal('groups', ['Group'])

        # Deleting model 'Study'
        db.delete_table('groups_study')

        # Deleting model 'Timeslot'
        db.delete_table('groups_timeslot')


    models = {
        'groups.study': {
            'Meta': {'object_name': 'Study'},
            'compensation': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'respondent_price': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
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