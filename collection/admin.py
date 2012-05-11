from django.contrib import admin
from django.views.decorators.http import *
from django.http import *
from django.shortcuts import *
from django.core.urlresolvers import *
from django.conf.urls.defaults import patterns, include, url
from collection.models import *
from protmusis.admin import site as mysite

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('number', 'title', 'is_visible', 'time_left', 'show_link')
	ordering = ('number',)
	exclude = ('show_until',)
	
	def show_link(self, obj):
		return '<a href="%s">Show for 60 seconds</a>' % (reverse('admin:show_question', args=(obj.id,)))
	show_link.short_description = 'Actions'
	show_link.allow_tags = True
	
	def get_urls(self):
		urls = super(QuestionAdmin, self).get_urls()
		my_urls = patterns('',
			url(r'^show_question/(\d+)/$', self.admin_site.admin_view(self.show_question), name='show_question')
		)
		return my_urls + urls
	
	def show_question(self, request, id):
		question = get_object_or_404(Question, pk=id)
		question.show_for(60)
		return redirect(reverse('admin:collection_question_changelist'))

class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'password', 'is_active')
	exclude = ('last_activity',)
	ordering = ('name',)
	

mysite.register(Team, TeamAdmin)
mysite.register(Question, QuestionAdmin)
