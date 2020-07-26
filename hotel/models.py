from django.db import models

# Create your models here.
class Habitacion(models.Model):
    SENCILLA = 'SENCILLA'
    DOBLE  = 'DOBLE'
    MATRIMONIAL = 'MATRIMONIAL'
    SUITE       = 'SUITE'
    TIPO_DE_HABITACION = [
        (SENCILLA,  'Sencilla'),
        (DOBLE, 'Doble'),
        (MATRIMONIAL, 'Matrimonial'),
        (SUITE, 'Suite'),
    ]

    tipo = models.CharField(
        max_length = 10,
        choices = TIPO_DE_HABITACION,
        default = SENCILLA,
    ) #  seleccionar el tipo de habitacion.

    dias        = models.PositiveIntegerField() # Numero de dias ocupado
    servicios   = models.PositiveIntegerField() # Numero de servicios al dia
    numero      = models.PositiveIntegerField() # id de la habitacion

    cliente     = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tipo
    
    def get_absolute_url(self):
        return reverse('hotel:habi-detail', kwargs = {'pk': self.id})
    
class Cliente(models.Model):
    nombres     = models.CharField(max_length=30) # Nombres del cliente
    apellidos   = models.CharField(max_length=30) # Apellidos del cliente
    tarjeta     = models.PositiveIntegerField()   # Numero de tarjeta
    dni         = models.PositiveIntegerField()   # Numeor de DNI
    

    def __str__(self):
        return self.nombres

    def get_abslute_url(self):
        return "/hotel/cliente/" + str(self.id)

