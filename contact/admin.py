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

class ContactAdmin(CustomAdmin):
    list_display = ("email","nom","date_add","date_update",)
    search_fields = ("nom",)
    ordering = ["nom"]
    fieldsets = [
                  ("info contact",{"fields":["nom","email","message","sujet"]}),
                  ("standard",{"fields":["status"]})
    ]

class NewsletterAdmin(CustomAdmin):
    list_display = ("email","date_add","date_update",)
    search_fields = ("email",)
    ordering = ["email"]
    fieldsets = [
                  ("info newsletter",{"fields":["email",]}),
                  ("standard",{"fields":["status"]})
    ]

def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.Contact,ContactAdmin)
_register(models.Newsletter,NewsletterAdmin)
