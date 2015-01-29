# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u540d\u79f0')),
                ('slug', models.SlugField(max_length=100, verbose_name='URL')),
                ('sort', models.SmallIntegerField(verbose_name='\u6392\u5e8f')),
                ('parent', models.ForeignKey(related_name='catechild', blank=True, to='wiki.Category', null=True)),
            ],
            options={
                'ordering': ['sort'],
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, verbose_name='\u6807\u9898')),
                ('content', models.TextField(help_text=' ', verbose_name='\u5185\u5bb9')),
                ('publish_date', models.DateTimeField(verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('slug', models.SlugField(help_text='URL', unique=True, max_length=255, verbose_name='URL')),
                ('categories', models.ManyToManyField(related_name='categories', null=True, verbose_name='\u5206\u7c7b', to='wiki.Category', blank=True)),
            ],
            options={
                'ordering': ['-publish_date'],
                'verbose_name': '\u6587\u7ae0',
            },
            bases=(models.Model,),
        ),
    ]
