# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athledeck', '0002_athlete_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='image',
            field=models.ImageField(default='static/images/no-image.png', upload_to=''),
            preserve_default=True,
        ),
    ]
