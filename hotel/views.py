from django.shortcuts import render
from django.views import View
from .models import Habitacion, Cliente


# Create your views here.

# Vista para listar todas las habitaciones. 
class HabitacionListView(View):
    def get(self, request):
        obj = Habitacion.objects.all()

        context = {
                'object_list': obj,
                }
        return render(request, 'hotel/lsta_habitacion.html', context)
# Visa para listar los clientes

class ClienteListView(View):
    def get(self, request):
        obj = Cliente.objects.all()

        context = {
                    'object_list': obj,
                }
        return render(request, 'hotel/lsta_cliente.html', context)
class HabitacionDetailView(View):
    
    def get(self, request, myID):
        obj = Habitacion.objects.get(id = myID)
        context = {
            'object': obj,
            }
        return render(request, 'hotel/habitacion_detail.html', context)
