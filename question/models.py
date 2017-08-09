from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)
    publication_date = models.DateTimeField()

class Answer(models.Model):
    question = models.ForeignKey(Question)
    content = models.TextField()
# Create your models here.
