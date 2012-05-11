# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Question.show_until'
        db.alter_column('collection_question', 'show_until', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Team.last_activity'
        db.alter_column('collection_team', 'last_activity', self.gf('django.db.models.fields.DateTimeField')())


    def backwards(self, orm):
        
        # Changing field 'Question.show_until'
        db.alter_column('collection_question', 'show_until', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Team.last_activity'
        db.alter_column('collection_team', 'last_activity', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))


    models = {
        'collection.question': {
            'Meta': {'object_name': 'Question'},
            'answer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'question_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'show_until': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1, 1, 1, 0, 0)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'collection.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_activity': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1, 1, 1, 0, 0)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['collection']
