# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athledeck', '0004_auto_20141019_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='image',
            field=models.ImageField(upload_to='/images/%Y%m%d', default='/static/images/no-image.png'),
        ),
    ]
