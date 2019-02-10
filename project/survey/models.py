from __future__ import unicode_literals

from django.db import models
import datetime

class Question(models.Model):
	LANG_CHOICES = (
		(0, 'Spanish'),
		(1, 'English')
		)
	text = models.CharField(max_length=200)
	active = models.BooleanField(default=False)
	reg_date = models.DateTimeField('date registrated', default=datetime.datetime.now)
	lang = models.IntegerField(choices=LANG_CHOICES, default=0)

	def __unicode__(self):
		return self.text

class Answer(models.Model):
	question = models.ForeignKey(Question)
	value = models.CharField(max_length=200)
	active = models.BooleanField(default=False)

	def __unicode__(self):
		return self.value

class Response(models.Model):
	answer = models.ForeignKey(Answer)
	reg_date = models.DateTimeField('date registrated', default=datetime.datetime.now)

	def __unicode__(self):
		return self.answer
