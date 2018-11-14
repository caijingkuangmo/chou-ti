from django.contrib import admin
from rbac import models

# Register your models here.

admin.site.register(models.User)

class PermissionConfig(admin.ModelAdmin):
    list_display = ['title', 'url', 'action', 'group']
admin.site.register(models.Permission)
admin.site.register(models.Role)
admin.site.register(models.PermissionGroup)


