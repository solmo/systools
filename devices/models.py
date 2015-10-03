from django.db import models


class Dispositivo(models.Model):
    id_dispositivo = models.PositiveSmallIntegerField('ID',primary_key=True,default=000)
    hostname = models.CharField(max_length=15,default ='hostname')
    ip = models.GenericIPAddressField(default='127.0.0.1')
    # ubicacion = Edificio de model
    backup = models.BooleanField(default=False)
    # f_ultimo_backup = models.DateTimeField(blank= True, null=True)
    # recursos = diccionario de recursos

    class Meta:
        abstract = True


class Server(Dispositivo):
    so = models.CharField(max_length=15)
    nodo = models.BooleanField(default=False)
    
    def __str__(self):
        return self.hostname

    class Meta: 
        #ordering = ["self.hostname"]
        verbose_name_plural='Servers'


class VirtualServer(Dispositivo):
    host = models.ForeignKey(Server)

    def __str__(self):
        return self.hostname

    class Meta: 
        #ordering = ["self.hostname"]
        verbose_name_plural='VirtualServers'


# class Base(models,Model):
#   pass
