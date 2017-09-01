# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



WEEK_CHOICES = (
		()
	)

class Team(models.Model):
	user = models.ForeignKey(User)
	team_name = models.CharField(max_length=50)
	owner_name = models.CharField(max_length=50)

	def __str__(self):
		return self.team_name



class Week(models.Model):
	number = models.IntegerField(choices=WEEK_CHOICES)
	date = models.DateField(default=timezone.now)

	def __str__(self):
		return str(self.number)


# class GameManager(models.Manager):
# 	def did_team_win(self):
# 		wins = 0
# 		losses = 0
# 		ties = 0
# 		if self.points_for > self.points_against:
# 			wins += 1
# 		elif self.points_for < self.points_against:
# 			losses += 1
# 		elif self.points_for == self.points_against:
# 			ties += 1
# 		return '{} - {} - {}'.format(wins,losses,ties)


class Game(models.Model):
	week = models.ForeignKey(Week)
	team = models.ForeignKey(Team, related_name='team')
	opponent = models.ForeignKey(Team, related_name='opponent', null=True, blank=True)
	points_for = models.FloatField()
	points_against = models.FloatField()
	# win = models.BooleanField(default=False)

	# objects = GameManager()

	def __str__(self):
		return '{} | week {} | {} - {}'.format(self.team, self.week, self.points_for, self.points_against)


# this is funky needs to be fixed
	def record(self):
		wins = 0
		losses = 0
		ties = 0
		if self.points_for > self.points_against:
			wins += 1
		elif self.points_for < self.points_against:
			losses += 1
		elif self.points_for == self.points_against:
			ties += 1
		return '{} - {} - {}'.format(wins,losses,ties)


	def total_pf(self, *pfs):
		total_pf = []
		for pf in pfs:
			total_pf.append(pf)
		return sum(total_pf)

		

	# def total_pa(self):
	# 	pass

	# def mean_pf(self):
	# 	pass

	# def mean_pa(self):
	# 	pass

	# def strength_of_schedule(self):
	# 	pass













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
		







