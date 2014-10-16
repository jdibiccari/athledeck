# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athledeck', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='bio',
            field=models.TextField(max_length=400, default=''),
            preserve_default=True,
        ),
    ]
