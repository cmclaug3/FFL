# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from football.models import Team, Week, Game



def home(request):
	if not request.user.is_authenticated:
		return redirect(reverse('account_login'))
	context = {
		'teams': Team.objects.all()
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










	# def single_team(request, team_id):
	# 	context = {
	# 		'team' = Team.objects.get(pk=team_id)
	# 	}
	# 	return render(request, 'single_team.html', context)



