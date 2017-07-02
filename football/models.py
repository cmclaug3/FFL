# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Owner(models.Model):
	owner = models.ForeignKey(User)
	date = models.DateField()


class Stats(models.Model):
	