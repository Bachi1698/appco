from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Application)
admin.site.register(models.CategorieApplication)
admin.site.register(models.Commentaire)
admin.site.register(models.Tag)
