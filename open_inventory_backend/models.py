from django.db.models import *

class Inventario(Model):
    codigo = CharField(max_length=50)
    name = CharField(max_length=50)
    estado = BooleanField(default=True) # True = Disponible, False = Prestado
    costo = IntegerField(default=0)


class Prestamo(Model):
    id_persona = IntegerField()
    item = ForeignKey(Inventario, on_delete=CASCADE)
    fecha = DateTimeField()
    devuelto = BooleanField(default=False) # True = Devuelto, False = No devuelto