from django.contrib import admin

# Register your models here.
from mysite import models

admin.site.register(models.Maker)
admin.site.register(models.PModel)
admin.site.register(models.Product)
admin.site.register(models.PPhoto)
