from django.contrib import admin
from .models import Server,VirtualServer


class VirtualServerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ip', 'host','backup')


class ServerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'ip', 'nodo')

admin.site.register(Server, ServerAdmin)
admin.site.register(VirtualServer, VirtualServerAdmin)

# Register your models here.
