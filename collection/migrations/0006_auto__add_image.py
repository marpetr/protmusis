# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Image'
        db.create_table('collection_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('collection', ['Image'])


    def backwards(self, orm):
        
        # Deleting model 'Image'
        db.delete_table('collection_image')


    models = {
        'collection.answer': {
            'Meta': {'object_name': 'Answer'},
            'correct': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'early_finish': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collection.Question']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collection.Team']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'collection.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'collection.question': {
            'Meta': {'object_name': 'Question'},
            'correct_answer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
