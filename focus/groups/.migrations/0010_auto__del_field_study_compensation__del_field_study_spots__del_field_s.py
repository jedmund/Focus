# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Study.compensation'
        db.delete_column('groups_study', 'compensation')

        # Deleting field 'Study.spots'
        db.delete_column('groups_study', 'spots')

        # Deleting field 'Study.coop_price'
        db.delete_column('groups_study', 'coop_price')

        # Adding field 'Study.time'
        db.add_column('groups_study', 'time',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['groups.Timeslot']),
                      keep_default=False)

        # Deleting field 'Timeslot.study'
        db.delete_column('groups_timeslot', 'study_id')

        # Adding field 'Timeslot.coop_price'
        db.add_column('groups_timeslot', 'coop_price',
                      self.gf('django.db.models.fields.IntegerField')(default=1, max_length=4),
                      keep_default=False)

        # Adding field 'Timeslot.compensation'
        db.add_column('groups_timeslot', 'compensation',
                      self.gf('django.db.models.fields.IntegerField')(default=1, max_length=4),
                      keep_default=False)

        # Adding field 'Timeslot.spots'
        db.add_column('groups_timeslot', 'spots',
                      self.gf('django.db.models.fields.IntegerField')(default=1, max_length=3),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Study.compensation'
        db.add_column('groups_study', 'compensation',
                      self.gf('django.db.models.fields.IntegerField')(default=1, max_length=4),
                      keep_default=False)

        # Adding field 'Study.spots'
        db.add_column('groups_study', 'spots',
                      self.gf('django.db.models.fields.IntegerField')(default=1, max_length=3),
                      keep_default=False)

        # Adding field 'Study.coop_price'
        db.add_column('groups_study', 'coop_price',
                      self.gf('django.db.models.fields.IntegerField')(default=1, max_length=4),
                      keep_default=False)

        # Deleting field 'Study.time'
        db.delete_column('groups_study', 'time_id')

        # Adding field 'Timeslot.study'
        db.add_column('groups_timeslot', 'study',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.datetime(2012, 10, 20, 0, 0), to=orm['groups.Study']),
                      keep_default=False)

        # Deleting field 'Timeslot.coop_price'
        db.delete_column('groups_timeslot', 'coop_price')

        # Deleting field 'Timeslot.compensation'
        db.delete_column('groups_timeslot', 'compensation')

        # Deleting field 'Timeslot.spots'
        db.delete_column('groups_timeslot', 'spots')


    models = {
        'groups.study': {
            'Meta': {'object_name': 'Study'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['groups.Timeslot']"}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['groups.Venue']"})
        },
        'groups.timeslot': {
            'Meta': {'object_name': 'Timeslot'},
            'compensation': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'coop_price': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spots': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
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