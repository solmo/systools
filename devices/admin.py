from django.contrib import admin
from .models import Server,VirtualServer

class VirtualServerAdmin(admin.ModelAdmin):
	list_display = ('hostname', 'ip', 'host','backup')

admin.site.register(Server)
admin.site.register(VirtualServer, VirtualServerAdmin)

# Register your models here.
