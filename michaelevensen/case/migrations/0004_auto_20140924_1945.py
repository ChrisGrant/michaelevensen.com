# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0003_auto_20140924_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='slug',
            field=models.SlugField(default=datetime.date(2014, 9, 24)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='case',
            name='title',
            field=models.CharField(max_length=200, verbose_name=b'Title'),
        ),
    ]
