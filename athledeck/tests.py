from django.test import TestCase
from .models import Athlete
from django.core.urlresolvers import reverse

#Testing index view
class AthleteViewTests(TestCase):
  def test_index_view_with_no_athletes(self):
    resp = self.client.get('/')
    self.assertEqual(resp.status_code, 200)
    self.assertContains(resp, "<strong>Sorry!</strong> There are no athletes to display.")
    self.assertTrue('athletes' in resp.context)
    self.assertQuerysetEqual(resp.context['athletes'], [])

  def test_index_view_with_athletes(self):
    a1 = Athlete.objects.create(first_name='Wayne', last_name='Gretzky', sport='Hockey', league='National Hockey Leauge', team='New York Rangers')
    a2 = Athlete.objects.create(first_name='Michael', last_name='Jordan', sport='Basketball', league='National Basketball Association', team='Chicago Bulls')
    resp = self.client.get('/')
    self.assertContains(resp, "Wayne Gretzky")
    self.assertContains(resp, "Michael Jordan")
    self.assertQuerysetEqual(resp.context['athletes'], ['<Athlete: Wayne Gretzky>', '<Athlete: Michael Jordan>'])
