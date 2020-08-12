from django import forms
from .models import Habitacion
from .models import Cliente


class RawHabitacionForm(forms.Form):
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
    tipo = forms.ChoiceField(
        choices = TIPO_DE_HABITACION,
        ) #  seleccionar el tipo de habitacion.
    dias        = forms.IntegerField() # Numero de dias ocupado   
    servicios   = forms.IntegerField() # Numero de servicios al dia
    numero      = forms.IntegerField() # id de la habitacion
    estado      = forms.BooleanField(initial = False, required = False)# Estado de la habitacion
    descripcion = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'placeholder': 'Escribe una descripcion sobre la habitacion',
                'id': 'nombreID',
                'class': 'special',
                'cols': '10',
            }
        )
    )

class RawClienteForm(forms.Form):
    nombres     = forms.CharField()
    apellidos   = forms.CharField()
    tarjeta     = forms.IntegerField()
    dni         = forms.IntegerField()
    habitacion  = forms.ModelChoiceField(queryset = Habitacion.objects.filter(estado = False))
    dias        = forms.IntegerField()
    servicios   = forms.IntegerField()

