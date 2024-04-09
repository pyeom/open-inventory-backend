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
from open_inventory_backend.models import *
from .models import Prestamo
#from open_inventory_backend import utils

api = NinjaAPI()

@api.get("/hello")
def hello(request):
    return "Hello world!"

""" @api.get("/inventory/")
def get_inventory(request):
    # Your logic to retrieve inventory items goes here
    # Return a list of inventory items
    return {"message": "List of inventory items"}
 """

""" @api.post("/prestar-item/")
def crear_prestamo(request):
    item_id = request.data.get('item_id')
    borrower_id = request.data.get('borrower_id')
    fecha_prestamo = request.data.get('fecha_prestamo')
    is_paid = request.data.get('is_paid')
    fee = request.data.get('fee')

    # Your logic to create the lending transaction goes here
    # Example: Create a new LendingTransaction object in the database

    # Return a success message or relevant data
    return {"message": "Lending transaction created successfully"}
 """
""" @api.get("/prestar-item")
def get_lending_transactions(request):
    # Your logic to retrieve lending transactions goes here
    # Return a list of lending transactions
    return {"message": "List of lending transactions"}
 """
""" @api.post("/prestar-item/{prestamo-id}")
def devolver_item(request, prestamo_id: int):
    # Your logic to mark the lending transaction as returned goes here
    # Example: Update the LendingTransaction object in the database

    # Return a success message or relevant data
    return {"message": "Item returned successfully"}
 """
""" @api.get("/prestamos/")
def get_all_transactions(request):
    transactions = Prestamo.objects.all()
    # You can customize the data returned (e.g., select specific fields)
    return {"transactions": transactions} """

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
