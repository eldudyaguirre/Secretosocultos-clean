from django.db import models
from django.contrib.auth.models import User

class CategoriaBlog(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    resumen = models.TextField(blank=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="blog/", blank=True, null=True)

    categoria = models.ForeignKey(
        CategoriaBlog,
        on_delete=models.PROTECT,
        related_name="posts"
    )

    autor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-creado"]

    def __str__(self):
        return self.titulo
