"""api_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from aplication_back.api.router import router_localComercial

from aplication_back.api.router import router_venta , router_productoVenta

from aplication_back.api.router import router_categoria , router_producto

from aplication_back.api.router import router_orden, router_productoOrden




#  path('api/', include(router_ urls)),
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_localComercial.urls)),
    path('api/', include(router_venta.urls)),
    path('api/', include(router_productoVenta.urls)),
    path('api/', include(router_categoria.urls)),
    path('api/', include(router_producto.urls)),
    path('api/', include(router_orden.urls)),
    path('api/', include(router_productoOrden.urls))

]
