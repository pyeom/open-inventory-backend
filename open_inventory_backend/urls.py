"""
URL configuration for open_inventory_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from ninja import NinjaAPI, Schema
from ninja.errors import HttpError
from open_inventory_backend.models import *
from .models import Prestamo
#from open_inventory_backend import utils
from datetime import datetime, timedelta, time, date

api = NinjaAPI()

class Item(Schema):
    name: str
    codigo: str
    costo: int
    estado: bool

class Detail(Schema):
    message: str

class PushItem(Schema):
    codigo: str
    name: str
    estado: bool
    costo: int

@api.get("/hello")
def hello(request):
    return "Hello world!"

# Todos los artículos del inventario
@api.get("/inventario")
def get_inventory(request):
    return Inventario.objects.all()

@api.post("/inventario")
def add_item(request, payload: PushItem):
    try:
        item = Inventario.objects.create(**payload.dict())
    except Exception as e:
        raise HttpError(400, str(e))


    return 200, {
        "name": item.name,
        "codigo": item.codigo,
        "costo": item.costo,
        "estado": item.estado
    }


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
