from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Habitacion, Cliente
from .forms import RawHabitacionForm
from .forms import RawClienteForm
from django.views.generic.edit import UpdateView


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

class HabitacionUpdateView(View):
    def post(self, request, myID):
        habitacion = Habitacion.objects.get(id = myID)
        form = RawHabitacionForm(request.POST)
        if form.is_valid():
            dic = form.cleaned_data
            habitacion.tipo = dic["tipo"]
            habitacion.dias = dic["dias"]
            habitacion.servicios = dic["servicios"]
            habitacion.estado = dic["estado"]
            habitacion.mantenimiento = dic["mantenimiento"]
            habitacion.descripcion = dic["descripcion"]
            habitacion.save()
            return redirect('../')
        else:
            print("Errores")

    def get(self, request, myID):
        habitacion = Habitacion.objects.get(id = myID)
        form = RawHabitacionForm() # instance = habitacion
        context = {
            'forms': form,
        }
        return render(request, 'hotel/habitacionCreate.html', context)

class HabitacionDisponibleView(View):
    def get(self, request):
        obj = Habitacion.objects.filter(estado = False)
        context = {
            'object_list': obj,
        }

        return render(request, 'hotel/habitacionDisponible.html', context)

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
            # cleaned_data retorna un diccionario con 
            # los elementos enviados por el formulario
            dic = form.cleaned_data
            # creamos un objeto cliente
            cliente = Cliente()
            cliente.nombres     = dic["nombres"]
            cliente.apellidos   = dic["apellidos"]
            cliente.tarjeta     = dic["tarjeta"]
            cliente.dni         = dic["dni"]
            # -------------------------------------------
            habitacion          = dic["habitacion"]
            dias                = dic["dias"]
            servicios           = dic["servicios"]
            # modificamos el estado de la habitacion a ocupado
            habitacion.estado   = True
            habitacion.dias     = dias
            habitacion.servicios = servicios
            #--------------------------------------------
            habitacion.save()
            cliente.habitacion  = habitacion
        
            cliente.save()
            #Cliente.objects.create(**form.cleaned_data)
            #----------------------------------------
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

class ClienteDetailView(View):

    def get(self, request, myID):
        obj = Cliente.objects.get(id = myID)
        context = {
                'object': obj,
                }
        return render(request, 'hotel/clienteDetail.html', context)

class ClienteDeleteView(View):

    def post(self, request, myID):
        obj = Cliente.objects.get(id = myID)
        print("lo borro")
        habitacion = obj.habitacion
        habitacion.dias = 0
        habitacion.servicios = 0
        habitacion.estado = False
        habitacion.save()
        obj.delete()
        return redirect('../../')

    def get(self, request, myID):
        obj = Cliente.objects.get(id = myID)
        context = {
            'object': obj,
        }
        return render(request, 'hotel/clienteDelete.html', context)

class ClienteSearchView(View):

    def get(self, request):
        context = {}
        return render(request, 'hotel/clienteSearch.html', context)
        

class HabitacionDetailView(View):

    def get(self, request, myID):
        obj = Habitacion.objects.get(id = myID)
        context = {
                'object': obj,
                }
        return render(request, 'hotel/habitacion_detail.html', context)

#Vistas JSON 
class habitacionJsonView(View):
    def get(self, request, *args, **kwargs):
        queryset = Habitacion.objects.filter(estado=False)
        return JsonResponse(list(queryset.values()), safe= False)

class clienteJsonView(View):
    def get(self, request, *args, **kwargs):
        queryset = Cliente.objects.filter()
        return JsonResponse(list(queryset.values()), safe=False)
