# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id_dispositivo', models.PositiveSmallIntegerField(verbose_name='ID', default=0, serialize=False, primary_key=True)),
                ('hostname', models.CharField(default='hostname', max_length=15)),
                ('ip', models.GenericIPAddressField(default='127.0.0.1')),
                ('backup', models.BooleanField(default=False)),
                ('f_ultimo_backup', models.DateTimeField(null=True, blank=True)),
                ('so', models.CharField(max_length=15)),
                ('nodo', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Servers',
            },
        ),
        migrations.CreateModel(
            name='VirtualServer',
            fields=[
                ('id_dispositivo', models.PositiveSmallIntegerField(verbose_name='ID', default=0, serialize=False, primary_key=True)),
                ('hostname', models.CharField(default='hostname', max_length=15)),
                ('ip', models.GenericIPAddressField(default='127.0.0.1')),
                ('backup', models.BooleanField(default=False)),
                ('f_ultimo_backup', models.DateTimeField(null=True, blank=True)),
                ('host', models.ForeignKey(to='devices.Server')),
            ],
            options={
                'verbose_name_plural': 'VirtualServers',
            },
        ),
    ]