from django.db import models
from .product import Producto   # importa tu modelo Producto

class ProductoDetalle(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name="detalles"
    )
    titulo = models.CharField(max_length=100)
    valor = models.CharField(max_length=255)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return f"{self.titulo}: {self.valor}"
