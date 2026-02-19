from django.db import models
from cloudinary.models import CloudinaryField


class CategoriaBlog(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Post(models.Model):

    AUTORES = [
        ("secretos", "Secretos Ocultos"),
        ("jonas", "Jonás Dante"),
    ]

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    resumen = models.TextField(blank=True)
    contenido = models.TextField()

    imagen = CloudinaryField("imagen", blank=True, null=True)

    autor_blog = models.CharField(
        max_length=20,
        choices=AUTORES,
        default="secretos"
    )

    categoria = models.ForeignKey(
        CategoriaBlog,
        on_delete=models.PROTECT,
        related_name="posts"
    )

    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-creado"]

    def __str__(self):
        return self.titulo

    def get_autor_imagen(self):
        if self.autor_blog == "secretos":
            return "img/events/35x35secretosocultos.jpg"
        return "img/events/35x35jonasdante.jpg"
