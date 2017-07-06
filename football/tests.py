# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse



class TestViews(TestCase):
	def setUp(self):
		self.user = User(username='test', email='test@email.com', first_name='Cor', last_name='McLaug')
		self.user.set_password('password')
		self.user.save()

	def test_home_invalid(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 302)

	def test_home_valid(self):
		self.client.force_login(self.user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        

