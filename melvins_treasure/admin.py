from django.contrib import admin
from .models import CustomUser, Producto, Resena, Pedido, Carrito, ItemCarrito, Pago

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Producto)
admin.site.register(Resena)
admin.site.register(Pedido)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
admin.site.register(Pago)