# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='virtualserver',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
        ),
    ]
