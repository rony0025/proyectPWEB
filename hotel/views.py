from django.shortcuts import render
from django.views import View
from .models import Habitacion, Cliente
from .forms import RawHabitacionForm
from .forms import RawClienteForm


# Create your views here.

# Vista para listar todas las habitaciones. 
class HabitacionListView(View):
    def get(self, request):
        obj = Habitacion.objects.all()

        context = {
                'object_list': obj,
                }
        return render(request, 'hotel/lsta_habitacion.html', context)

# Vista para crear una nueva habitacion
class HabitacionCreateView(View):
    def post(self, request):
        form = RawHabitacionForm()
        if request.method == 'POST':
            form = RawHabitacionForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                Habitacion.objects.create(**form.cleaned_data)

                form = RawHabitacionForm() #Limpiar el formulario
            else:
                print(form.errors)
        context = {
            'forms': form,
        }
        return render(request, 'hotel/habitacionCreate.html', context)

    def get(self,  request):
        form = RawHabitacionForm()
        context = {
            'forms': form,
        }
        return render(request, 'hotel/habitacionCreate.html', context)
        
# Visa para listar los clientes

class ClienteListView(View):
    def get(self, request):
        obj = Cliente.objects.all()

        context = {
                    'object_list': obj,
                }
        return render(request, 'hotel/lsta_cliente.html', context)

class ClienteCreateView(View):

    def post(self, request):
        form = RawClienteForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Cliente.objects.create(**form.cleaned_data)

            form = RawClienteForm() # Limpia el formulario
        else :
            print(form.errors)
        context = {
            'forms': form,
            }
        return render(request,'hotel/clienteCreate.html', context)

    def get(self, request):
        form = RawClienteForm()
        context ={
                'forms': form,
                }
        return render(request, 'hotel/clienteCreate.html', context)

class ClienteSearchView(View):

    def get(self, request):
        context = {}
        return  render(request, 'hotel/clienteSearch.html', context)

    def post(self, request, nombre):
        if request.method == 'POST':
            obje = Cliente.objects.get(nombres = nombre)
            context = {
                    'obj':obje,
                    }
            return render(request, 'hotel/clienteSearch.html', context)

class HabitacionDetailView(View):

    def get(self, request, myID):
        obj = Habitacion.objects.get(id = myID)
        context = {
                'object': obj,
                }
        return render(request, 'hotel/habitacion_detail.html', context)
