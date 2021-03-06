from django.db import models

# Create your models here.
class Producto_vendido(models.Model):
    factura = models.ForeignKey('facturas.Factura', on_delete=models.CASCADE, related_name='productosVendidos')
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    oferta = models.DecimalField(decimal_places=2, max_digits=10)
    cantidad_vendida = models.IntegerField()