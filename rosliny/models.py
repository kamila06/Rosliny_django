# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Index(models.Model):
    name = models.CharField(max_length=30, unique=True)
    # description = models.CharField(max_length=100)

#
class Catalog(models.Model):
    name = models.CharField(max_length=30, unique=True)
#     # subject = models.CharField(max_length=255)
#     # last_updated = models.DateTimeField(auto_now_add=True)
#     # board = models.ForeignKey(Board, related_name='topics')
#     # starter = models.ForeignKey(User, related_name='topics')
#
#
class Contact(models.Model):
    name = models.CharField(max_length=30, unique=True)
#     # message = models.TextField(max_length=4000)
#     # topic = models.ForeignKey(Topic, related_name='posts')
#     # created_at = models.DateTimeField(auto_now_add=True)
#     # updated_at = models.DateTimeField(null=True)
#     # created_by = models.ForeignKey(User, related_name='posts')
#     # updated_by = models.ForeignKey(User, null=True, related_name='+')