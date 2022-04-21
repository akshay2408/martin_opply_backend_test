from django.contrib import admin
from app import models

admin.site.register(models.Product)
admin.site.register(models.Customer)
admin.site.register(models.CustomerProductHistory)
