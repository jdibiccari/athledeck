from django.test import TestCase
from .models import Athlete
from django.core.urlresolvers import reverse



class AthleteViewTests(TestCase):
  def test_index_view_with_no_athletes(self):
    