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

class TagAdmin(CustomAdmin):
    list_display = ('nom','date_add','date_update','status',)
    search_fields = ('nom',)
    ordering = ['nom']
    fieldsets = [
                  ("info tag",{"fields":["nom","description",]}),
                  ("standard",{"fields":["status"]})
    ]

class ApplicationAdmin(CustomAdmin):
    list_display = ('nom','date_add','date_update','status','image_view')
    search_fields =('nom',)
    ordering = ['nom']
    readonly_fields = ['image_view']
    filter_horizontal = ["tag"]
    fieldsets = [
                  ("info application",{"fields":["nom","description","image"]}),
                  ("foreignkey",{"fields":["tag",'categorie']}),
                  ("standard",{"fields":["status"]})
    ]

    def image_view(self,obj):
        return mark_safe("<img src ='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class CategorieApplicationAdmin(CustomAdmin):
    list_display = ('nom','date_add','date_update','status','image')
    search_fields =('nom',)
    ordering = ['nom']
    readonly_fields = ['image_view']
    fieldsets = [
                  ("info categorie",{"fields":['nom','description','image']}),
                  ("standard",{"fields":["status"]})
    ] 
    
    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))


class CommentaireAdmin(CustomAdmin):
    list_display = ('message','date_add','date_update','status')
    search_fields = ('message',)
    fieldsets =[
                 ("info application",{"fields":["message",]}),
                  ("foreignkey",{"fields":['application']}),
                  ("standard",{"fields":["status"]})
    ]


def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.Application,ApplicationAdmin)
_register(models.CategorieApplication,CategorieApplicationAdmin)
_register(models.Commentaire,CommentaireAdmin)
_register(models.Tag,TagAdmin)

