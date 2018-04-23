# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='idnum',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='idnum',
        ),
        migrations.AlterField(
            model_name='patient',
            name='symptoms',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
