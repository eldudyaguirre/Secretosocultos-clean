from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=150)
    activa = models.BooleanField(default=True)
    imagen_portada = models.ImageField(
        upload_to="categorias/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="productos"
    )
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="productos/")
    stock = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creado"]

    def __str__(self):
        return self.nombre
