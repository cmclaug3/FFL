# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Stat(models.Model):
	team = models.ForiegnKey(User)
	game = models.IntegerField()
	points_for = FloatField()
	points_against = FloatField()

	def __str__(self):
		pass

	def record(self):
		pass




