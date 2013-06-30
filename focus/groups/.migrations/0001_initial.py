# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Venue'
        db.create_table('groups_venue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.contrib.localflavor.us.models.USStateField')(max_length=2)),
            ('zip_code', self.gf('django.contrib.localflavor.us.models.USPostalCodeField')(max_length=2)),
        ))
        db.send_create_signal('groups', ['Venue'])

        # Adding model 'Group'
        db.create_table('groups_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('spots', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['groups.Venue'])),
            ('respondent_price', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('compensation', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('groups', ['Group'])


    def backwards(self, orm):
        # Deleting model 'Venue'
        db.delete_table('groups_venue')

        # Deleting model 'Group'
        db.delete_table('groups_group')


    models = {
        'groups.group': {
            'Meta': {'object_name': 'Group'},
            'compensation': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'respondent_price': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'spots': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['groups.Venue']"})
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