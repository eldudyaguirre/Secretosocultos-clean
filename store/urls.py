from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('homein/',views.homein, name='homein'),
    path('signin/', views.do_signin, name='signin'),
    path('logout/', views.do_logout, name='logout'),
    path("signup/", views.signup, name="signup"),
    path('resetpassword', views.resetpassword, name='resetpassword'),
#    path('success-signup/', views.success_signup, name='success_signup'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.get_shopping_cart, name='cart'),
#    path('pedidos/', views.crear_pedido, name='crear_pedido'),
    path('quienes/', views.quienes_somos, name='quienes'),
    path('about/', views.about, name='about'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('blog-details/', views.blogdetails, name='blog-details'),
    path('blog-grid/', views.bloggrid, name='blog-grid'),
    path('blog-standard/', views.blogstandard, name='blog-standard'),
    path('tienda/', views.tienda, name='tienda'),
    path("tienda/<str:categoria_nombre>/", views.tienda_categoria, name="tienda_categoria"),
#    path('tienda/<slug:slug>/', views.productos_por_categoria, name='productos_por_categoria'),
    path("producto/<int:producto_id>/", views.tienda_producto, name="tienda_producto"),
    path('catalog/', views.catalog, name='catalog'),
    path('events-details/', views.eventsdetails, name='events-details'),
    path('tarot/', views.tarot, name='tarot'),
    path('events/', views.events, name='events'),
    path('veladoras/', views.veladoras, name='veladoras'),
    path('articulos/', views.articulos, name='articulos'),
    path('talismanes/', views.talismanes, name='talismanes'),
    path('rituales/', views.rituales, name='rituales'),
    path('faq/', views.faq, name='faq'),
    path('history/', views.history, name='history'),
    path('index-2/', views.index2, name='index-2'),
    path('projectnew/', views.projectnew, name='projectnew'),
    path('project-gallery/', views.projectgallery, name='project-gallery'),
    path('project-image/', views.projectimage, name='project-image'),
    path('project-video/', views.projectvideo, name='project-video'),
    path('reset-password/', views.resetpassword, name='reset-password'),
    path('boletin/', views.boletin, name='boletin'),
    #path('signinnow/', auth_views.LoginView.as_view(template_name='sign-in.html'), name='signinnow'),
    #path('logoutnow/',auth_views.LoginView.as_view(template_name='index.html'), name='logoutnow'),
    #path('sign-up/', views.signupnow, name='sign-up'),

]

