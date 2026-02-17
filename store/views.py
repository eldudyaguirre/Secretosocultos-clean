from django.shortcuts import render, redirect, get_object_or_404
from store.models import Producto, Categoria, PerfilUsuario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistroUsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from datetime import datetime
from .cart_session import ShoppingCartSession
import json
from django.http import JsonResponse
from django.db import transaction
import string
import random
import subprocess

def error_404(request, exception):
    return render(request, '404.html',{})

def home(request):
    crear_admin()
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def homein(request):
    return render(request, 'index-2.html')

def do_signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Usuario o contraseña inválidos.')
        else:
            messages.error(request, 'Usuario o contraseña inválidos.')        
    
    form = AuthenticationForm()
    return render(request, 'sign-in.html', {'signin_form': form})

def do_logout(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()

            PerfilUsuario.objects.create(
                user=user,
                acepta_boletin=request.POST.get("acepta_boletin") == "on"
            )

            login(request, user)

            messages.success(
                request,
                "🎉 Registro exitoso. Bienvenido/a a Secretos Ocultos."
            )

            return redirect("home")
        else:
            messages.error(
                request,
                "⚠️ Revisa los campos. Hay errores en el formulario."
            )

    else:
        form = RegistroUsuarioForm()

    return render(request, "sign-up.html")


def add_to_cart(request):
    cart = ShoppingCartSession(request)
    
    payload = json.loads(request.body)
    
    producto_id = int(payload.get('producto_id'))
    cantidad = int(payload.get('cantidad'))
    
    try:    
        producto_existente = Producto.objects.get(pk=producto_id)
        cart.add(producto_existente.id, cantidad)
        return JsonResponse(status=200, data={'result': True, 'message': 'OK', 'count_cart_items': cart.__len__()})
    except Producto.DoesNotExist:
        return JsonResponse(status=404, data={'result': False, 'message': 'El producto no existe'})    
    

def remove_from_cart(request):
    cart = ShoppingCartSession(request)
    
    payload = json.loads(request.body)    
    producto_id = int(payload.get('producto_id'))    
    cart.delete(producto_id)    
    return JsonResponse(status=200, data={'result': True, 'message': 'OK', 'count_cart_items': cart.__len__()})   


def get_shopping_cart(request):
    cart = ShoppingCartSession(request)
    return render(request, 'cart.html', {'cart': cart.get_cart_detail(), 'count_cart_items': cart.__len__(), 'cart_total': cart.get_total()})
    
    
def generar_codigo_pedido():
    caracteres = string.ascii_letters + string.digits
    codigo_pedido = 'PED-' + ''.join(random.choice(caracteres) for _ in range(5))
    return codigo_pedido

def tienda(request):
    productos = Producto.objects.filter(activo=True)
    return render(request, "store/tienda.html", {
        "productos": productos
    })

def quienes_somos(request):
    return render(request, 'quienes.html')

def success_signup(request):
    return render(request, 'imdex.html')

def about(request):
    return render(request, 'about.html')

def contactanos(request):
    return render(request, 'contact.html')

def catalog(request):
    return render(request, 'catalog.html')

def blogdetails(request):
    return render(request, 'blog-details.html')

def bloggrid(request):
    return render(request, 'blog-grid.html')

def blogstandard(request):
    return render(request, 'blog-standard.html')

def eventsdetails(request):
    return render(request, 'events-details.html')

def events(request):
    return render(request, 'events.html')

def faq(request):
    return render(request, 'faq.html')

def history(request):
    return render(request, 'history.html')

def index2(request):
    return render(request, 'index-2.html')

def projectnew(request):
    return render(request, 'project-new.html')

def projectgallery(request):
    return render(request, 'project-gallery.html')

def projectimage(request):
    return render(request, 'project-image.html')

def projectvideo(request):
    return render(request, 'project-video.html')

def resetpassword(request):
    return render(request, 'reset-password.html')

def tienda(request):
    return render(request, 'tienda.html')

def tarot(request):
    return render(request, 'tarot.html')

def veladoras(request):
    return render(request, 'veladoras.html')

def articulos(request):
    return render(request, 'articulos.html')

def talismanes(request):
    return render(request, 'talismanes.html')

def rituales(request):
    return render(request, 'rituales.html')

def tienda_categoria(request, categoria_nombre):
    categoria = get_object_or_404(
        Categoria,
        nombre__iexact=categoria_nombre,
        activa=True
    )

    productos = Producto.objects.filter(
        categoria=categoria,
        activo=True
    )
    nombre = categoria.nombre.strip().lower()

    imagenes_categoria = {
        "velas": "img/tienda/velas/Velas-01.jpg",
        "amuletos": "img/tienda/amuletos/Amuletos-01.jpg",
        "sahumerios": "img/tienda/sahumerios/Sahumerios-01.jpg",
        "corporales": "img/tienda/corporales/Corporales-01.jpg",
        "efigies": "img/tienda/efigies/Efigies-01.jpg",
        "literatura": "img/tienda/literatura/Literatura-01.jpg",
        "servicios": "img/tienda/servicios/Servicios-01.jpg",
        "18+": "img/tienda/18+/18-01.jpg",
    }

    imagen_portada = "img/tienda/default.jpg"

    for clave, ruta in imagenes_categoria.items():
        if nombre.startswith(clave):
            imagen_portada = ruta
            break

    return render(request, "tienda_categoria.html", {
        "categoria": categoria,
        "productos": productos,
        "imagen_portada": imagen_portada,
    })

def boletin(request):
    return render(request,'contact.html')

def tienda_producto(request, producto_id):
    producto = get_object_or_404(
        Producto,
        id=producto_id,
        activo=True
    )

    return render(request, "tienda_producto.html", {
        "producto": producto
    })

#
#def signinnow(request):
#    return render(request, 'sign-in.html')
#
#def signupnow(request):
#    return render(request, 'sign-up.html')

from django.contrib.auth.models import User

def crear_admin():
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="eldudyaguirre@gmail.com",
            password="SMjonasdante2026"
        )