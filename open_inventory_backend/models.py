from django.db.models import *

class Inventario(Model):
    id = IntegerField(primary_key=True)
    codigo = CharField(unique=True, max_length=50)
    name = CharField(max_length=50)

class Item(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=50)
    description = CharField(max_length=50)
    price = DecimalField(max_digits=10, decimal_places=2)
    inventory = ForeignKey(Inventario, on_delete=CASCADE)

class Prestamo(Model):
    id = IntegerField(primary_key=True)
    item = ForeignKey(Item, on_delete=CASCADE)
    fecha = DateTimeField()
    devuelto = BooleanField()