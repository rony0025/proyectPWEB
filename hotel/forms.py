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
    cliente     = forms.ModelChoiceField() # sleccione al cliente

