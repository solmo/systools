from django.db import models
from os import system
#from .tasks import backup_vm


class Dispositivo(models.Model):
    id_dispositivo = models.PositiveSmallIntegerField('ID',primary_key=True,default=000)
    hostname = models.CharField(max_length=15,default ='hostname')
    ip = models.GenericIPAddressField(default='127.0.0.1')
    ubicacion = models.CharField(max_length=25, default='site')
    nombre = models.CharField(max_length=25)# ubicacion = Edificio de model
    backup = models.BooleanField(default=False)
    # f_ultimo_backup = models.DateTimeField(blank= True, null=True)
    # recursos = diccionario de recursos

    
    class Meta:
        abstract = True


class Server(Dispositivo):
    so = models.CharField(max_length=15)
    nodo = models.BooleanField(default=False)
    
    
    def __str__(self):
        return '%s %s' % (self.nombre, self.ubicacion)


    class Meta: 
        #ordering = ["self.hostname"]
        verbose_name_plural='Servers'


class VirtualServer(Dispositivo):
    host = models.ForeignKey(Server)
    # tener presente que storage podria cambiar si se usa para restaurar!
    storage = models.CharField(max_length=15,default ='backups')
    
    
    '''
    def hacer_backup(self):
        datos = (self.host.ip, self.id_dispositivo, self.nombre, self.storage)
        system('fab -H root@%s backup_vm:%s,%s,%s' % datos)
        #backup_vm.delay(datos)
    '''
    def __str__(self):
        return self.nombre

    class Meta: 
        #ordering = ["self.hostname"]
        verbose_name_plural='VirtualServers'


# class Base(models,Model):
#   pass
