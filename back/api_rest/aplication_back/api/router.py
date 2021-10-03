from rest_framework.routers import DefaultRouter
from aplication_back.api.views import LocalComercialModelViewSet
from aplication_back.api.views import VentaModelViewSet , ProductoVentaModelViewSet
from aplication_back.api.views import CategoriaModelViewSet , ProductoModelViewSet
from aplication_back.api.views import OrdenModelViewSet, ProductoOrdenModelViewSet


router_localComercial = DefaultRouter()

router_venta = DefaultRouter()
router_productoVenta = DefaultRouter()

router_categoria= DefaultRouter()
router_producto = DefaultRouter()

router_orden = DefaultRouter()
router_productoOrden = DefaultRouter()


router_localComercial.register(prefix="localComercials",basename="localComercials",viewset=LocalComercialModelViewSet)

router_venta.register(prefix="ventas",basename="ventas",viewset=VentaModelViewSet)
router_productoVenta.register(prefix="productoVentas",basename="productoVentas",viewset=ProductoVentaModelViewSet)

router_categoria.register(prefix="categorias", basename="categorias", viewset = CategoriaModelViewSet)
router_producto.register(prefix="productos",basename="productos",viewset=ProductoModelViewSet)

router_orden.register(prefix="ordenes",basename="ordenes",viewset=OrdenModelViewSet)
router_productoOrden.register(prefix="productoOrdens",basename="productoOrdens",viewset=ProductoOrdenModelViewSet)