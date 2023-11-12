from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    cp = models.CharField(max_length=10)
    calle = models.CharField(max_length=255)
    colonia = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    foto_identificacion = models.CharField(max_length=255)
    roles = models.ManyToManyField(Group, related_name='usuarios_roles')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios_permissions')
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()
    estado_choice = [
        ('Excelente', 'Excelente'),
        ('Bueno', 'Bueno'),
        ('Regular', 'Regular'),
        ('Malo', 'Malo'),
    ]
    estado = models.CharField(max_length=255, choices=estado_choice)
    vendedor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='productos')

class Resena(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='resenasUsuario')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='resenasProducto')
    valoracion = models.IntegerField()
    comentario = models.TextField()
    fecha_reseña = models.DateField(auto_now_add=True)

class Carrito(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='carritos')
    productos = models.ManyToManyField(Producto, through='ItemCarrito')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

class Pedido(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='pedidos')
    detalle_pedido = models.OneToOneField(Carrito, on_delete=models.CASCADE, related_name='detalle_pedido')
    fecha_compra = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=255)

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def subtotal(self):
        return self.producto.precio * self.cantidad

class Pago(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='pagos')
    metodo_pago = models.CharField(max_length=255)
    fecha = models.DateField()