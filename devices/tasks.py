# -*- coding: utf-8 -*-
from celery import shared_task
from .models import VirtualServer

@shared_task()
def listar_vm():
    for vm in VirtualServer.objects.all():
        if vm.backup:
            print(vm.host.ip, vm.nombre)

@shared_task
def saludar():
	print('Hola a Todos!!!')
            