from django import template


register = template.Library()


# @register.filter(name='avg')
# def avg(value, games_played):
# 	return (value / int(games_played))

