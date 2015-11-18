# -*- coding: utf-8 -*-
from celery import shared_task
from os import system
from .models import VirtualServer

@shared_task
def listar_vm():
    for vm in VirtualServer.objects.all():
        if vm.backup:
            print vm
            print type(vm)

@shared_task
def backup_vms():
    for vm in VirtualServer.objects.all():
    	if vm.backup:
    		vm.hacer_backup()

'''
@shared_task
def backup_vm(*datos):
    #system('fab -H root@%s backup_vm:%s,%s,%s' % datos)
    print datos
'''