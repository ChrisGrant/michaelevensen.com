# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('introduction', models.TextField(verbose_name=b'Introduction')),
                ('body', models.TextField(verbose_name=b'Body Text', blank=True)),
                ('link_text', models.CharField(max_length=200, verbose_name=b'Link Text')),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Title')),
                ('introduction', models.TextField(max_length=200, verbose_name=b'Introduction')),
                ('link_text', models.CharField(max_length=200, verbose_name=b'Link Text')),
                ('slug', models.SlugField()),
                ('image', models.FileField(upload_to=b'media/', null=True, verbose_name=b'Image', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Title')),
                ('introduction', models.TextField(max_length=200, verbose_name=b'Introduction')),
                ('body', models.TextField(verbose_name=b'Body Text', blank=True)),
                ('slug', models.SlugField()),
                ('case', models.ForeignKey(verbose_name=b'Associated Case', to='portfolio.Case')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
