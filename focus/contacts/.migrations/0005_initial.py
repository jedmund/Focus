# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'contacts_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('gender', self.gf('django.db.models.fields.IntegerField')(default=1, max_length=2)),
            ('birthdate', self.gf('django.db.models.fields.DateField')()),
            ('occupation', self.gf('django.db.models.fields.CharField')(default='', max_length=400, null=True, blank=True)),
            ('employer', self.gf('django.db.models.fields.CharField')(default='', max_length=400, null=True, blank=True)),
            ('ethnicity', self.gf('django.db.models.fields.CharField')(default='Caucasian', max_length=40)),
            ('email', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('home_phone_no', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(default='', max_length=20, null=True, blank=True)),
            ('mobile_phone_no', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(default='', max_length=20, null=True, blank=True)),
            ('work_phone_no', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(default='', max_length=20, null=True, blank=True)),
            ('cell_make', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cell_model', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cell_provider', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('car_make', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('car_model', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('car_year', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.contrib.localflavor.us.models.USStateField')(max_length=2)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('add_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('add_method', self.gf('django.db.models.fields.IntegerField')(default=1, max_length=2)),
        ))
        db.send_create_signal(u'contacts', ['Person'])

        # Adding M2M table for field studies on 'Person'
        m2m_table_name = db.shorten_name(u'contacts_person_studies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'contacts.person'], null=False)),
            ('study', models.ForeignKey(orm[u'groups.study'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'study_id'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'contacts_person')

        # Removing M2M table for field studies on 'Person'
        db.delete_table(db.shorten_name(u'contacts_person_studies'))


    models = {
        u'contacts.person': {
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
            'ethnicity': ('django.db.models.fields.CharField', [], {'default': "'Caucasian'", 'max_length': '40'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '2'}),
            'home_phone_no': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'mobile_phone_no': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'studies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['groups.Study']", 'symmetrical': 'False'}),
            'work_phone_no': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'groups.study': {
            'Meta': {'object_name': 'Study'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['groups.Venue']"})
        },
        u'groups.venue': {
            'Meta': {'object_name': 'Venue'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cross_st': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['contacts']