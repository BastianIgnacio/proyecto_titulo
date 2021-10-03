from django.db import models

# Create your models here.

# Modelo que representa a cada local comercial
class LocalComercial(models.Model):
    tittle = models.CharField(max_length=250)
    nombre = models.CharField(max_length=250)
    direccion = models.TextField()
    link = models.CharField(max_length=500)
    horarioAtencion = models.TextField()
    tieneDelivery = models.BooleanField()
    estado = models.CharField(max_length=250)
    privateKeyMercadopago = models.TextField()
    publicKeyMercadopago = models.TextField()
    tieneMercadopago = models.BooleanField()
    rutaLogo = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_created=True)





#Modelo que representa a cada Venta
class Venta(models.Model):
    total = models.IntegerField()
    tipoPago = models.CharField(max_length=250)
    fecha = models.DateTimeField(auto_created=True)
    refLocalComercial = models.ForeignKey(LocalComercial,on_delete=models.CASCADE)
#Modelo que representa a cada detalle de una venta
class ProductoVenta(models.Model):
    precioUnitario = models.IntegerField()
    cantidad = models.IntegerField()
    total = models.IntegerField()
    refVenta = models.ForeignKey(Venta,on_delete=models.CASCADE)



#Modelo que representa a las categorias de un local comercial
class Categoria(models.Model):
    nombre = models.CharField(max_length=250)
    esVisible = models.BooleanField()
    rutaFoto = models.CharField(max_length=250)
    refLocalComercial = models.ForeignKey(LocalComercial,on_delete=models.CASCADE)
#Modelo que representa a todos los productos que posee una categoria
class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    precioActual = models.IntegerField()
    descripcion = models.TextField()
    esVisible = models.BooleanField()
    rutaFoto = models.CharField(max_length=250)
    refCategoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)





#Modelo que representar una orden que se le hace a un local comercial
class Orden(models.Model):
    fecha = models.DateTimeField(auto_created=True)
    tipoEntrega = models.CharField(max_length=250)
    estado = models.CharField(max_length=250)
    datosEntrega = models.TextField()
    refLocalComercial = models.ForeignKey(LocalComercial,on_delete=models.CASCADE)
#Modelo que representa los productos de una orden
class ProductoOrden(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    notaEspecial = models.TextField()
    refOrden = models.ForeignKey(Orden,on_delete=models.CASCADE)





