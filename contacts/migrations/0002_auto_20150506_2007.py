# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='contact_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='contact_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='contact_phone_number',
            new_name='phone_number',
        ),
    ]
