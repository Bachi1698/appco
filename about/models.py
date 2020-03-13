from django.db import models

# Create your models here.
class Presentation(models.Model):
    presentation = models.TextField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'presentation'
        verbose_name_plural = 'presentations'

    def __str__(self):
        return self.presentation

class SiteInfo(models.Model):
    logo = models.ImageField('images/SiteInfo')
    slogan = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'site info'
        verbose_name_plural = 'sites infos'
    
    def __str__(self):
        return self.slogan

class Temoignage(models.Model):
    photo = models.ImageField('images/Temoignage')
    message = models.TextField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'temoignage'
        verbose_name_plural = 'temoignages'

    def __str__(self):
        return self.message

class Service(models.Model):
    image = models.ImageField('images/Service')
    nom = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def __str__(self):
        return self.nom
 


