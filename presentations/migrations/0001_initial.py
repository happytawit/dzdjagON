# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pres_name', models.CharField(max_length=150)),
                ('pres_description', models.CharField(max_length=250)),
                ('pres_speaker', models.ForeignKey(to='speakers.Speaker')),
            ],
        ),
    ]
