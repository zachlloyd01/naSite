from django.db import models
import datetime
from django import forms

class NewsFeed(models.Model):
    title = models.CharField(max_length=160, default='')
    body = models.TextField(default='')
    def __str__(self):
        return self.title

class comment_page(models.Model):
    name = models.CharField(max_length=400, default='')
    date = models.DateField(default=datetime.datetime.now())
    comment = models.CharField(max_length=1000, default='')
    def __str__(self):
        return self.name

class password_reset(models.Model):
    username = models.CharField(max_length=400, default='')
    password = models.CharField(max_length=400, default='')

class news_application(models.Model):
    user = models.CharField(max_length=400, default='')
    name = models.CharField(max_length=400, default='')
    reason = models.TextField(max_length=400, default='', help_text="Please give a few sentences detailing why you would be a good writer for the site, and links to samples")
    def __str__(self):
        return self.user