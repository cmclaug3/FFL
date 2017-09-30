# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


from django.views import View

import nflgame
import espnff
import statistics as s




def home(request):
	if not request.user.is_authenticated:
		return redirect(reverse('account_login'))

# ESPNFF API LEAGUE INFO
	league_id = 336227
	year = 2017
	our_league = espnff.League(league_id, year)


	context = {
		'league_team_list': our_league.teams,
		'league_scoreboard': our_league.scoreboard(), #current week
	}

	return render(request, 'home.html', context)




class PlayerStatsView(View):
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect(reverse('account_login'))

		season2017 = nflgame.games(2017)
		players = nflgame.combine_game_stats(season2017)

		pass_yds = players.passing().sort('passing_yds').limit(8)
		pass_tds = players.passing().sort('passing_tds').limit(8)
		rush_yds = players.rushing().sort('rushing_yds').limit(8)
		rush_tds = players.rushing().sort('rushing_tds').limit(8)

		all_games = nflgame.games(2017, kind="PRE")
		
		
		# ADD
		# receving, kickers, defense, etc

		context = {
			'pass_yds': pass_yds,
			'pass_tds': pass_tds,
			'rush_yds': rush_yds,
			'rush_tds': rush_tds
		}
		return render(request, 'player_stats.html', context)



class NflPicksView(View):
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect(reverse('account_login'))


# THIS NEEDS TO BE 2017 WEEK ONE (not working)
		week_one = nflgame.games(2017, week=1)

		context = {
			'week_one': week_one
		}
		return render(request, 'nfl_picks.html', context)















	# def single_team(request, team_id):
	# 	context = {
	# 		'team' = Team.objects.get(pk=team_id)
	# 	}
	# 	return render(request, 'single_team.html', context)



