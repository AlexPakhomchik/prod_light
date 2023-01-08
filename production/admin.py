from django.contrib import admin

from production.models import AluminiumProfile, LightModule, Driver, Cover, MountingSystem

admin.site.register(AluminiumProfile)
admin.site.register(LightModule)
admin.site.register(Driver)
admin.site.register(Cover)
admin.site.register(MountingSystem)