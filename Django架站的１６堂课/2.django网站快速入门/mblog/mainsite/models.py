#! -*- coding:utf-8 -*-

from django.db import models

# Create your models here.

from django.utils import timezone

import importlib,sys
importlib.reload(sys)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
