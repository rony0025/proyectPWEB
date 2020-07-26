from django.contrib import admin
from .models import Habitacion
from .models import Cliente

# Register your models here.
admin.site.register(Habitacion)
admin.site.register(Cliente)
