from django.db import models

def upload_image_to(instance, filename):
  import os
  from django.utils.timezone import now
  filename_base, filename_ext = os.path.splitext(filename)
  return 'profiles/%s%s' % (now().strftime("%Y%m%d%H%M%S"), filename_ext.lower())

class Athlete(models.Model):
  first_name = models.CharField(max_length = 140)
  last_name = models.CharField(max_length = 140)
  bio = models.TextField(max_length = 400, default= "")
  sport = models.CharField(max_length = 140)
  league = models.CharField(max_length = 140)
  team = models.CharField(max_length = 140)
  image = models.ImageField(_("Avatar"), upload_to=upload_image_to, blank=True)

  def __str__(self):
    return "%s %s" % (str(self.first_name), str(self.last_name))