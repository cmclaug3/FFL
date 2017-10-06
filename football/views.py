# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


from django.views import View

import nflgame
from espnff import League, Team
import statistics as s


class BetterTeam(Team):
    
    def __repr__(self):
        return 'BetterTeam({})'.format(self.team_name)

    #take zeros (unplayed games) out of pf (points scored) list
    @property
    def strict_pf_list(self):
        return [i for i in self.scores if i != 0]

    #take zeros (unplayed games) out of pa (opponent points scored) list
    #after generating poinsts against list from (scores_list - margin_of_victory_list)
    @property
    def strict_pa_list(self):
        pa_list = [x-y for x, y in zip(self.scores, self.mov)]
        return [i for i in pa_list if i != 0]

    #average pf VS average pa
    @property
    def average_week(self):
        games = len(self.strict_pf_list)
        apf = round(s.mean(self.strict_pf_list), 1)
        apa = round(sum(self.strict_pa_list) / float(games), 1)
        return '{}-{}'.format(apf, apa)

    #spread (standard deviation of scores)
    @property
    def consistency(self):
        return round(s.stdev(self.strict_pf_list), 1)

    #outlier contribution
    @property
    def speculation(self):
        return round(100 * (s.median(self.strict_pf_list) / s.mean(self.strict_pf_list) - 1), 2)

    #lowest score
    @property
    def minimum(self):
        return min(self.strict_pf_list)

    #highest score
    @property
    def maximum(self):
        return max(self.strict_pf_list)




class BetterLeague(League):

    def __repr__(self):
        return 'BetterLeague({})'.format(self.league_name)

    def _fetch_teams(self, data):
        '''Fetch teams in league'''
        teams = data['leaguesettings']['teams']

        for team in teams:
            self.teams.append(BetterTeam(teams[team]))

        # replace opponentIds in schedule with team instances
        for team in self.teams:
            for week, matchup in enumerate(team.schedule):
                for opponent in self.teams:
                    if matchup == opponent.team_id:
                        team.schedule[week] = opponent

        # calculate margin of victory
        for team in self.teams:
            for week, opponent in enumerate(team.schedule):
                mov = team.scores[week] - opponent.scores[week]
                team.mov.append(mov)

        # sort by team ID
        self.teams = sorted(self.teams, key=lambda x: x.team_id, reverse=False)

    #Sets callable attribute pr (power rank) to Team objects
    def pwr_ranking(self):
        pf_master_list = []
        for team in self.teams:
            pf_master_list.append([team, sum(team.strict_pf_list)])
        new = sorted(pf_master_list, key=lambda x: x[1], reverse=True)
        rank = 1
        for player in new:
            setattr(player[0], 'pr', rank)
            rank += 1

            
    #Sets callable attribute sos (strength of schedule) to Team objects
    def strength_of_schedule(self):
        pa_master_list = []
        for team in self.teams:
            pa_master_list.append([team, sum(team.strict_pa_list)])
        new = sorted(pa_master_list, key=lambda x: x[1], reverse=True)
        rank = 1
        for player in new:
            setattr(player[0], 'sos', rank)
            rank += 1






'''
Views
'''

def home(request):
	if not request.user.is_authenticated:
		return redirect(reverse('account_login'))

# ESPNFF API LEAGUE INFO
	league_id = 336227
	year = 2017
	our_league = BetterLeague(league_id, year)
	our_league.pwr_ranking()
	our_league.strength_of_schedule()

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



