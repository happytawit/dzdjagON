# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_name', models.CharField(max_length=150)),
                ('contact_phone_number', models.CharField(max_length=20)),
                ('contact_email', models.CharField(max_length=30)),
                ('contact_address', models.CharField(max_length=150)),
            ],
        ),
    ]
