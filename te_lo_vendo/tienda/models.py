from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(User):

    rut = models.CharField()
    nombre = models.CharField()
    apellido = models.CharField()

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = 'Usuarios'

class Producto(models.Model):
    nombre = models.CharField()
    precio = models.IntegerField()
    descripcion = models.CharField()
    sku = models.IntegerField()
    disponible = models.BooleanField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = 'Productos'

class Pedido(models.Model):
    cantidad = models.IntegerField()
    direccion = models.CharField()

    CHOICES_PAGO = [
        ("DEBITO", "Debito"),
        ("CREDITO", "Credito"),
        ("TRANSFERENCIA", "Transferencia"),
    ]

    formas_pago = models.CharField(choices=CHOICES_PAGO, default="DEBITO")
    

    CHOICES_ESTADO = [
        ("PENDIENTE", "Pendiente"),
        ("PREPARACION", "Preparacion"),
        ("ENVIADO", "Enviado"),
    ]

    estado_pedido = models.CharField(choices=CHOICES_ESTADO, default="PENDIENTE")

    
    usuario = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
    producto = models.ForeignKey(Producto, on_delete=models.SET_DEFAULT, default=None)

    def __str__(self):
        return self.usuario
    
    class Meta:
        verbose_name_plural = 'Pedidos'


