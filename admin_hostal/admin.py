from django.contrib import admin
from .models import Cliente, Contrato, Factura, Habitacion, Minuta, OrdenCompra, OrdenPedido, Plato, Producto, Proveedor, Empleado, Huesped, Usuario
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Empleado)
admin.site.register(Huesped)
admin.site.register(Producto)
admin.site.register(Plato)
admin.site.register(Habitacion)
admin.site.register(Factura)
admin.site.register(OrdenPedido)
admin.site.register(OrdenCompra)
admin.site.register(Usuario)
admin.site.register(Contrato)
admin.site.register(Minuta)




