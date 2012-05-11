# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Team'
        db.create_table('collection_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('collection', ['Team'])

        # Adding model 'Question'
        db.create_table('collection_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('question_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('collection', ['Question'])


    def backwards(self, orm):
        
        # Deleting model 'Team'
        db.delete_table('collection_team')

        # Deleting model 'Question'
        db.delete_table('collection_question')


    models = {
        'collection.question': {
            'Meta': {'object_name': 'Question'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'question_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'collection.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['collection']
