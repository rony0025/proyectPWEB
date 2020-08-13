from django.db import models
from django.urls import reverse

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
        max_length = 15,
        choices = TIPO_DE_HABITACION,
        default = SENCILLA,
    ) #  seleccionar el tipo de habitacion.

    dias        = models.PositiveIntegerField(null = True) # Dias ocupado
    servicios   = models.PositiveIntegerField(null = True) # Servicios al dia
    numero      = models.PositiveIntegerField() # id de la habitacion
    estado      = models.BooleanField(default = False) # False = Ocupadoimineto = models.BooleanField(default = False)
    mantenimiento = models.BooleanField(default = False) 
    descripcion = models.CharField(max_length = 100)

    def get_absolute_url(self):
        return  str(self.id)
        #return reverse('hotel:habi-detail', kwargs = {'pk':self.id})
        
   # def update(self, estado):
       # self.dias = dias
       # self.servicios = servicios
    #    self.estado = estado
   
class Cliente(models.Model):
    nombres     = models.CharField(max_length=30) # Nombres del cliente
    apellidos   = models.CharField(max_length=30) # Apellidos del cliente
    tarjeta     = models.PositiveIntegerField()   # Numero de tarjeta
    dni         = models.PositiveIntegerField()   # Numeor de DNI
    habitacion  = models.ForeignKey('Habitacion', on_delete=models.CASCADE)    

    def get_abslute_url(self):
        return "/cliente/" + str(self.id) + "/"
        #return reverse('hotel:habi-detail', kwargs = {'pk':self.id})

