# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Team(models.Model):
	user = models.ForeignKey(User)
	team_name = models.CharField(max_length=50)
	owner_name = models.CharField(max_length=50)

	def __str__(self):
		return self.team_name


class Week(models.Model):
	number = models.IntegerField()
	date = models.DateField(default=timezone.now)

	def __str__(self):
		return self.number


class Game(models.Model):
	week = models.ForeignKey(Week)
	team = models.ForeignKey(Team)
	points_for = models.FloatField()
	points_against = models.FloatField()
	#opponent = models.ForeignKey(Team)

	def __str__(self):
		return '{} | week {} | {} - {}'.format(self.team, self.week, self.points_for, self.points_against,)





# class Game(models.Model):
# 	team = models.ForeignKey(User)
# 	game_number = models.IntegerField()
# 	points_for = models.FloatField()
# 	points_against = models.FloatField()

# 	def __str__(self):
# 		return '{} | {} | {}-{}'.format(self.team, self.game_number,
# 										self.points_for, self.points_against
# 		)

# 	class Meta:
# 		ordering = ['-game_number']

# 	def record(self):
# 		pass

# 	def total_points_for(self):
# 		tpf = []
		







