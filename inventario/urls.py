from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('agregar/', views.agregar_inventario, name='agregar_inventario'),
    path('cantidad/', views.cantidad_inventario, name='cantidad_inventario'),
    path('ver/', views.ver_inventario, name='ver_inventario'),
]
