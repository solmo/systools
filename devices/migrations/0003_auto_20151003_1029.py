# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_auto_20151002_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='server',
            name='f_ultimo_backup',
        ),
        migrations.RemoveField(
            model_name='virtualserver',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='virtualserver',
            name='f_ultimo_backup',
        ),
    ]
