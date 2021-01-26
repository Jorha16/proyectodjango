from django.db import models
from django.db.models.fields import BooleanField, CharField, TextField
from ckeditor.fields import RichTextField
# Create your models here.

class page(models.Model):
    title = models.CharField(verbose_name="Titulo",max_length=50)
    content = RichTextField(verbose_name="Contenido")
    slug = models.CharField(unique=True,max_length=150,verbose_name="URL amigable")
    order = models.IntegerField(default=0, verbose_name="Orden")
    visible = models.BooleanField(verbose_name="Publicado?")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Creado el")
    created_at = models.DateTimeField(auto_now=True,verbose_name="Actualizado el")

    class Meta:
        verbose_name ="Pagina"
        verbose_name_plural ="Paginas"
    
    def __str__(self):
        return self.title

