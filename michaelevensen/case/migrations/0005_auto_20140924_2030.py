# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0004_auto_20140924_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='image',
            field=models.FileField(upload_to=b'/media/', null=True, verbose_name=b'Image', blank=True),
        ),
    ]
