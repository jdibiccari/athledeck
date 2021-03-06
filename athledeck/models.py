from django.db import models

class Athlete(models.Model):
  first_name = models.CharField(max_length = 140)
  last_name = models.CharField(max_length = 140)
  bio = models.TextField(max_length = 600, default= "")
  sport = models.CharField(max_length = 140)
  league = models.CharField(max_length = 140)
  team = models.CharField(max_length = 140)
  image = models.ImageField(upload_to='images/%Y%m%d', default='/static/images/no-image.png')

  def __str__(self):
    return "%s %s" % (str(self.first_name), str(self.last_name))