from django.contrib import admin
from aplication_back.models import LocalComercial, Venta , ProductoVenta, Categoria, Producto,Orden, ProductoOrden
# Register your models here.

@admin.register(LocalComercial)
class LocalComercialAdmin(admin.ModelAdmin):
    list_display = ['nombre','direccion','created_at']

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['total','tipoPago','fecha','refLocalComercial']

@admin.register(ProductoVenta)
class ProductoVentaAdmin(admin.ModelAdmin):
    #list_display = 
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    #list_display = 
    pass

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    #list_display = 
    pass

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    #list_display = 
    pass

@admin.register(ProductoOrden)
class ProductoOrdenAdmin(admin.ModelAdmin):
    #list_display = 
    pass