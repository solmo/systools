# -*- coding: utf-8 -*-
from celery import shared_task
from os import system
from .models import VirtualServer


@shared_task
def backup_vms():
    for vm in VirtualServer.objects.all():
        if vm.backup:
            # vm.hacer_backup()
            datos = (vm.host.ip, vm.id_dispositivo, vm.nombre, vm.storage)
            backup_vm.delay(datos)

@shared_task
def backup_vm(*datos):
    info = datos[0]
    system('fab -H root@%s backup_vm:%s,%s,%s' % info)