from rest_framework.serializers import ModelSerializer
from aplication_back.models import LocalComercial
from aplication_back.models import Venta, ProductoVenta
from aplication_back.models import Categoria , Producto
from aplication_back.models import Orden, ProductoOrden

class LocalComercialSerializer(ModelSerializer):
    class Meta:
        model = LocalComercial
        fields = ['nombre','direccion','created_at']
        # fields = '__all__' Cuando queremos enviar todos los datos del modelo



######### MODULO VENTAS ########
class VentaSerializer(ModelSerializer):
    class Meta:
        model = Venta
        fields = ['total','tipoPago','fecha','refLocalComercial']
class ProductoVentaSerializer(ModelSerializer):
    class Meta:
        model = ProductoVenta
        fields = '__all__'

####### MODULO MENU DE LOCAL COMERCIAL ########
class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

###### MODULO PARA GESTION DE ORDENES DE UN LOCAL COMERCIAL 
class OdenSerializer(ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'
class ProductoOrdenSerializer(ModelSerializer):
    class Meta:
        model = ProductoOrden
        fields = '__all__'




