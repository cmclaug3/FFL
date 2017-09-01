# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from football.models import Team, Week, Game
import nflgame
from django.views import View



def home(request):
	if not request.user.is_authenticated:
		return redirect(reverse('account_login'))

	team_one_games = Team.objects.get(id=1).team.all()
	team_two_games = Team.objects.get(id=2).team.all()
	team_three_games = Team.objects.get(id=3).team.all()
	team_four_games = Team.objects.get(id=4).team.all()

	# team_one_games = Game.objects.filter(team__id=1)


	context = {
		'teams': Team.objects.all(),
		'team_one_games': team_one_games,
		'team_two_games': team_two_games,
		'team_three_games': team_three_games,
		'team_four_games': team_four_games
	}

	return render(request, 'home.html', context)
	# import ipdb; ipdb.set_trace()



def single_team(request, team_id):
	if not request.user.is_authenticated:
		return redirect(reverse('account_login'))
	context = {
		'team': Team.objects.get(user=request.user, id=team_id)
	}
	return render(request, 'single_team.html', context)



class PlayerStatsView(View):
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect(reverse('account_login'))

		season2017 = nflgame.games(2017, kind='PRE')
		players = nflgame.combine_game_stats(season2017)

		pass_yds = players.passing().sort('passing_yds').limit(8)
		pass_tds = players.passing().sort('passing_tds').limit(8)
		rush_yds = players.rushing().sort('rushing_yds').limit(8)
		rush_tds = players.rushing().sort('rushing_tds').limit(8)

		context = {
			'pass_yds': pass_yds,
			'pass_tds': pass_tds,
			'rush_yds': rush_yds,
			'rush_tds': rush_tds
		}
		return render(request, 'player_stats.html', context)











	# def single_team(request, team_id):
	# 	context = {
	# 		'team' = Team.objects.get(pk=team_id)
	# 	}
	# 	return render(request, 'single_team.html', context)



