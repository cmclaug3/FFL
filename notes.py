# Project TODO


# NOTES

# corey = Team.objects.get(id=1)
# corey_games = corey.team.all()
# corey_opponents_games = me.opponent.all()

# EX. equal because explicitly stated related_name
# Team.objects.get(id=1).team.all() == Team.objects.get(id=1).game_set.all()

# EX equal (forward and back relationship)
# Team.objects.get(id=1).team.all() == Game.objects.filter(team__id=1)



# EX totally stats? (team points against) (needs to be dynamic)

# team_pa = 0
# for y in Game.objects.filter(team__id=1):
#     team_pa += y.points_against
# print(team_pa)



# F Expressions
# do math through the database not python ?

# MODEL MANAGER?

# Q objects

# annotate/aggregate

# how to encapsulate the USER?? i think i am doing it wrong

# what is a wrapper?



# NFL API (nflgame)

# 	New page - Player stats League Leaders

	# Analyze and show stats by position...



# WEEKLY GAME PICKS
# 	scoring system = wins/loses AND points (underdog picks and THUR/SUN/MON
# 											night games are worth more)

# 	Payout = how much per game? / payout weekly-monthly-end of the seasons?


# 	show spread / show how many others (not who) have chosen each team
# 	game picks can be changed up until start time


# may need to scrape future (present) weeks schedule manually...
	
	# MODELS



# ESPNFF CONTROLS

# specific team

# .team_name
# .team_abbrev
# .owner
# .division_id
# .wins
# .losses
# .points_for
# .points_against
# .schedule
# .scores : (team) points for list
# .mov ????

# league settings




# MAIN FF LEAGUE STAT TABLE (SORTABLE/SEARCHABLE)

# EASY
	# team, record, pf, pa, Min, Max,


# MEDIUM
	# PR, SOS, RSOS, Con (sd), Spec (median/mean)

	# revised Con: 
	# 	med = stat.median(cmPfList)
	# 	men = stat.mean(cmPfList)
	# 	tots = 100 * ((med / men) - 1)


# HARD
	# opponent consistency
	# luck = opponent PF against you - opponent avgPF when they play you

	# weekly score ranking average (ranked position)

	# top 3 weeks / bottom 3 weeks

	# rank_point = PF / Average League PF


# <!-- CUSTOM FILTER TEST - CLOSE (may just be 0 division problem) -->
# 		<td>{{ team.points_for|avg:"(team.wins + team.losses)" }} - {{ team.points_against|avg:"(team.wins + team.losses)" }}</td> <!-- AW -->







# SORTABLE GRAPH IS sorting record wrong needs to have second value pf sort







