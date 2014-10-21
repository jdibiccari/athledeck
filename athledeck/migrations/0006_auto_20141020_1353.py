# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athledeck', '0005_auto_20141020_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='image',
            field=models.ImageField(default='/static/images/no-image.png', upload_to='images/%Y%m%d'),
        ),
    ]
