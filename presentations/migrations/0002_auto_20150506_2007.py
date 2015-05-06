# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presentations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presentation',
            old_name='pres_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='presentation',
            old_name='pres_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='presentation',
            old_name='pres_speaker',
            new_name='speaker',
        ),
    ]
