from django.db import models

class Gasto(models.Model):
    descripcion = models.CharField(max_length=200)
    cantidad = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.descripcion} - ${self.cantidad}"
