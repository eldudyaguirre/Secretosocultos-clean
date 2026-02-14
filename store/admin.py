from django.contrib import admin
from .models import (
    Categoria,
    Producto,
    Post,
    CategoriaBlog,
    SuscriptorBoletin,
    PerfilUsuario,
    ProductoDetalle,
    
)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activa")
    search_fields = ("nombre",)
    list_filter = ("activa",)

class ProductoDetalleInline(admin.TabularInline):
    model = ProductoDetalle
    extra = 1

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "codigo",
        "nombre",
        "categoria",
        "precio",
        "stock",
        "activo",
        "creado",
    )
    list_filter = ("categoria", "activo")
    search_fields = ("nombre", "codigo")
    inlines = [ProductoDetalleInline]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "activo", "creado")
    list_filter = ("categoria", "activo")
    search_fields = ("titulo",)
    prepopulated_fields = {"slug": ("titulo",)}


@admin.register(CategoriaBlog)
class CategoriaBlogAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activa")
    prepopulated_fields = {"slug": ("nombre",)}


@admin.register(SuscriptorBoletin)
class SuscriptorBoletinAdmin(admin.ModelAdmin):
    list_display = ("email", "activo", "creado")
    search_fields = ("email",)
    list_filter = ("activo",)


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ("user", "acepta_boletin", "creado")
    search_fields = ("user__username", "user__email")
