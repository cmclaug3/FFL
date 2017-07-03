# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from football.models import Team, Week, Game


admin.site.register(Team)
admin.site.register(Week)
admin.site.register(Game)







