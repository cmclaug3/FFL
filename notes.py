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

# Q objects


# NFL API (nflgame)

# 	New page - Player stats League Leaders

