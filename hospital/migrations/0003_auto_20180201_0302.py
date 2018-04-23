# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20180201_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(blank=True, max_length=20, choices=[(b'pathology', b'pathology'), (b'cardiology', b'cardiology'), (b'physiology', b'physiology')]),
        ),
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.CharField(blank=True, max_length=20, choices=[(b'pathology', b'pathology'), (b'cardiology', b'cardiology'), (b'physiology', b'physiology')]),
        ),
    ]
