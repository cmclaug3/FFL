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



