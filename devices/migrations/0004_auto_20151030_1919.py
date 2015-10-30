# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_auto_20151003_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='nombre',
            field=models.CharField(max_length=25, default='nombre_default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='ubicacion',
            field=models.CharField(max_length=25, default='site'),
        ),
        migrations.AddField(
            model_name='virtualserver',
            name='nombre',
            field=models.CharField(max_length=25, default='nombre_default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='virtualserver',
            name='storage',
            field=models.CharField(max_length=15, default='local'),
        ),
        migrations.AddField(
            model_name='virtualserver',
            name='ubicacion',
            field=models.CharField(max_length=25, default='site'),
        ),
    ]
