from django.db import models
import datetime

class Team(models.Model):
	name = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	last_activity = models.DateTimeField(default=datetime.datetime(1, 1, 1))
	
	def is_active(self):
		return (datetime.datetime.now() - self.last_activity) < datetime.timedelta(seconds=2)
	is_active.boolean = True
	
	def __unicode__(self):
		return self.name

class Question(models.Model):
	number = models.IntegerField()
	title = models.CharField(max_length=255)
	question_image = models.ImageField(upload_to='questions/')
	correct_answer = models.TextField(blank=True)
	show_until = models.DateTimeField(default=datetime.datetime(1, 1, 1))
	
	def is_visible(self):
		return datetime.datetime.now() < self.show_until
	is_visible.boolean = True
	
	def time_left(self):
		now = datetime.datetime.now()
		if self.show_until <= now:
			return None
		else:
			return (self.show_until - now).seconds

	def __unicode__(self):
		return u'{0}. {1}'.format(self.number, self.title)
	
	def show_for(self, seconds):
		self.show_until = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
		Answer.objects.filter(question=self).delete()
		self.save()

class Answer(models.Model):
	team = models.ForeignKey(Team)
	question = models.ForeignKey(Question)
	text = models.TextField()
	correct = models.NullBooleanField()
	points = models.IntegerField(default=0)
	early_finish = models.DateTimeField(null=True, blank=True)

class Image(models.Model):
	image = models.ImageField(upload_to='images/')
