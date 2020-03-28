from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.
class CustomAdmin(admin.ModelAdmin):
    actions = ('activate','desactivate')
    list_filter = ('status',)
    list_per_page = 6
    date_hierachy = "date_add"

    def activate(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selection a été effectué avec succes')
    activate.short_description = "permet d'activer le champs selectionner"

    def desactivate(self,request,queryset):  
        queryset.update(status=False)
        self.message_user(request,'la selection a été effectué avec succes')
    desactivate.short_description = "permet de desactiver le champs selectionner"

class ProduitAdmin(CustomAdmin):
    list_display = ("nom","date_add","date_update")
    search_fields = ("nom",)
    ordering = ["nom"]
    fieldsets = [
                  ("info application",{"fields":["nom","description","prix"]}),
                  ("foreignkey",{"fields":['categorie']}),
                  ("standard",{"fields":["status"]})
    ]

class TypeAbonnementAdmin(CustomAdmin):
    list_display = ("nom","date_add","date_update","prix")
    search_fields = ("nom",)
    ordering = ["nom"]
    fieldsets = [
                  ("info application",{"fields":["nom","prix"]}),
                  ("standard",{"fields":["status"]})
    ]

class CategorieAdmin(CustomAdmin):
    list_display = ("nom","date_add","date_update","image")
    search_fields = ("nom",)
    ordering = ["nom"]
    fieldsets = [
                  ("info application",{"fields":["nom","description","image"]}),
                  ("standard",{"fields":["status"]})
    ]

def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.Categorie,CategorieAdmin)
_register(models.Produit,ProduitAdmin)
_register(models.TypeAbonnement,TypeAbonnementAdmin)
