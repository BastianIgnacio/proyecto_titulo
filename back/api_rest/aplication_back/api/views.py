from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend



###########  MODELOS #############

# Modelos para el modulo de localComercial
from aplication_back.models import LocalComercial
# Modelos para el modulo Ventas
from aplication_back.models import Venta, ProductoVenta
# Modelos para el modulo de Menu localComercial 
from aplication_back.models import Categoria , Producto
#Modelos para el modulo de ORDENES de local comercial
from aplication_back.models import Orden, ProductoOrden



######### SERIALIZADORES #############

#Serializadores para el modulo localComercial
from aplication_back.api.serializers import LocalComercialSerializer
#Serializadores para el modulo Ventas
from aplication_back.api.serializers import VentaSerializer , ProductoVentaSerializer
#Serializadores para el modulo Menu localcomercial
from aplication_back.api.serializers import CategoriaSerializer , ProductoSerializer
#Serializadores para el modulo de ORDENES de local comercial
from aplication_back.api.serializers import OdenSerializer, ProductoOrdenSerializer




class LocalComercialModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LocalComercialSerializer
    queryset = LocalComercial.objects.all()


class VentaModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['fecha']
    filterset_fields = ['refLocalComercial']
class ProductoVentaModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductoVentaSerializer
    queryset = ProductoVenta.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering =['-total']
    filterset_fields = ['refVenta']


class CategoriaModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.filter(esVisible=True)
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['refLocalComercial']
class ProductoModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter(esVisible=True)
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['refCategoria']



class OrdenModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OdenSerializer
    queryset = Orden.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['refLocalComercial']
class ProductoOrdenModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductoOrdenSerializer
    queryset = ProductoOrden.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['refOrden']



"""
class LocalComercialApiView(APIView):
    def get(self,request):
        #locales = LocalComercial.objects.all()
        #locales = [local.nombre for local in LocalComercial.objects.all()]
        serializer = LocalComercialSerializer(LocalComercial.objects.all(),many=True)
        return Response(status=status.HTTP_200_OK,data=serializer.data)
    
    def post(self,request):
        serializer = LocalComercialSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED,data=serializer.data)
"""

"""
class LocalComercialViewSet(ViewSet):

    def list(self,request):
        #locales = LocalComercial.objects.all()
        #locales = [local.nombre for local in LocalComercial.objects.all()]
        serializer = LocalComercialSerializer(LocalComercial.objects.all(),many=True)
        return Response(status=status.HTTP_200_OK,data=serializer.data)
    
    def retrieve(self, request, pk:int):
        local = LocalComercialSerializer(LocalComercial.objects.get(id=pk))
        return Response(status=status.HTTP_200_OK,data = local.data)

    
    def create(self,request):
        serializer = LocalComercialSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED,data=serializer.data)
"""

