# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0002_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Header')),
                ('intro', models.TextField(max_length=200, verbose_name=b'Intro')),
                ('link_text', models.CharField(max_length=200, verbose_name=b'Link Text')),
                ('image', models.FileField(upload_to=b'media/img/', null=True, verbose_name=b'Image', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Index',
        ),
        migrations.AddField(
            model_name='chapter',
            name='case',
            field=models.ForeignKey(default=1, to='case.Case'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chapter',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chapter',
            name='body',
            field=models.TextField(verbose_name=b'Body', blank=True),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='title',
            field=models.CharField(max_length=200, verbose_name=b'Title'),
        ),
    ]
