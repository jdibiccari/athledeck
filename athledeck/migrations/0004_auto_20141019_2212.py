# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athledeck', '0003_athlete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='bio',
            field=models.TextField(default='', max_length=600),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='image',
            field=models.ImageField(default='/static/images/no-image.png', upload_to='images/'),
        ),
    ]
