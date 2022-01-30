from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.User)
admin.site.register(models.Car)
admin.site.register(models.Ride)
admin.site.register(models.Relationship)
