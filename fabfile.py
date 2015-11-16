#fabfile.py
#-*-coding:utf8-*-

from __future__ import with_statement
from fabric.decorators import task
from fabric.api import run, local, lcd, settings, cd
from datetime import date, timedelta
import time
import locale
import os

PATH = "/var/lib/vz/dump/"


@task
def backup_vm(id,hostname,storage='backups'):
    '''Realiza el backup de una VM en modo Stop.

    Argumentos:

    id -- Integer. ID de la VM.
    hostname -- String.
    storage -- String. Almacenamiento en el host.

    Ejemplo:
        
        fab -H 172.25.50.192 backup_vm:115,'pilaga' 
    '''
    id = str(id)
    with cd('/var/lib/vz/dump'):
        run('qm stop %s' % id)
        with settings(warn_only=True):
            run('rm %s*' % hostname) # Borra backup anterior
        run('vzdump %s -mode stop -compress gzip -storage %s' % (id, storage))
        run('qm start %s' % id)
        nombre_log = formatear_nombre(hostname,'log')
        run('mv *%s*.log %s' % (id, nombre_log)) # Renombra archivo .log
        run('scp /var/lib/vz/dump/%s root@172.25.50.150:/virtuales' % nombre_log)
        with settings(warn_only=True):
            nombre = formatear_nombre(hostname,'vma.gz') #Arma el nombre con fecha y extension
            run('mv *%s* %s' % (id, nombre)) #Renombra el archivo de backup
            run('scp /var/lib/vz/dump/%s root@172.25.50.150:/virtuales' % nombre)


def formatear_nombre(nombre, extension):
    '''Agrega la fecha actual y una extension al 'nombre'.

    Argumentos:

    nombre -- String.
    extension -- String. Se agrega al final del nombre.

    Return:
    nombre_fecha.extension

    Ejemplo:

    formatear_nombre(pilaga, log) ---> pilaga_25-10-2015.log

    '''

    locale.setlocale(locale.LC_ALL,"")
    fecha = '_'+time.strftime('%d-%b-%Y')
    nombre = nombre+fecha+'.'+extension
    return nombre
    


@task
def actualizar_tractas():
    with cd('/root/scripts_automotores'):
        run('psql -h localhost -p5432 -U postgres --dbname=bdSueldos < \
            actualizar_automotores_insert.sql')
        run('psql -h localhost -p5432 -U postgres --dbname=bdSueldos < \
            actualizar_motos_insert.sql')


@task
def actualizar_neike():
    with cd('/root'):
        run('psql -h localhost -p5432 -U postgres --dbname=bdSueldos < per_neike.sql')


@task
def ordenar_diario():
    '''
    Ordena los backups de las bases, comprimiendolos en su carpeta diario 
    '''
    for base in bases:
        nombre = formatear_nombre(base)
        with lcd('/bases'):
            with settings(warn_only=True):
                result = local('tar -zcvf %s.tgz %s' % (nombre, base), capture=True)
            if not result.failed:
                local('mv %s.tgz /bases/dir_%s/diario' % (nombre, base))
            else:
                continue
        if date.today().strftime('%d') == '01':
            ordenar_mensual(base)


@task
def ordenar_mensual(base):
    locale.setlocale(locale.LC_ALL,"")
    mes_anterior = (date.today() - timedelta(days=28)).strftime('%b')
    with lcd('/bases/dir_%s' % base):
        local('mkdir mensual/%s' % mes_anterior)
        local('mv diario/*%s* mensual/%s' % (mes_anterior, mes_anterior))


@task
def backup_nd(ip):
    with lcd('/comunicaciones'):
        local('ncftpget -u admin -p %s ftp://%s:/%s.backup' % (pass_routers, ip,
              routers[ip]))


@task
def crear():
    local('touch file.txt')
'''
@task
def listar(id):
    with settings(warn_only=True):
        result = local('ls %s*' % servers[id], capture=True)
    if result.failed:
        print result.command 
    prompt('hola')
'''


def agregar_base(nombre):
    pass


def agregar_router(ip):
    pass


def listar_bases():
    pass


def listar_routers():
    pass


@task
def backup_base(base, es_des=False):    
    '''
    Realiza un copia de la base, formatea el nombre y la almacena en /bases.

    Parametros que recibe: 
    El nombre de la base de datos y un boleano (es de desarrollo?)

    Ejemlo:
            fab -H 192.168.10.181 backup_base:bdsueldos         
    '''
    nombre_backup = base
    if es_des:
        nombre_backup = 'des_' + base
    run('pg_dump -x --disable-triggers -h localhost -p5432 -i -U postgres %s > \
        /var/backups/%s' % (base, nombre_backup))
    
    run('scp /var/backups/%s root@172.25.50.150:/bases' % nombre_backup)
    # Borrar el archivo local 
