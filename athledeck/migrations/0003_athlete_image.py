# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import athledeck.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('athledeck', '0002_athlete_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='image',
            field=models.ImageField(upload_to=athledeck.models.upload_image_to, blank=True, default=datetime.date(2014, 10, 16)),
            preserve_default=False,
        ),
    ]
