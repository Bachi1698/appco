from django.db import models

# Create your models here.
class CategorieApplication(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField('images/CategorieApplication')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'categorie application'
        verbose_name_plural = 'categories applications'

    def __str__(self):
        return self.nom

class Application(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField('images/Application')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'application'
        verbose_name_plural = 'applications'

    def __str__(self):
        return self.nom

class Commentaire(models.Model):
    message = models.TextField(max_length=255)
    application = models.ForeignKey(Application,on_delete=models.CASCADE,related_name='application_commentaire')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'commentaire'
        verbose_name_plural = 'commentaires'

    def __str__(self):
        return self.message

class Tag(models.Model):
    description = models.TextField(max_length=255)
    nom = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.nom

