from django.urls import path
from .views import(
    HabitacionListView,
    HabitacionDetailView,
    ClienteListView,
    HabitacionCreateView,
    ClienteCreateView,
    ClienteSearchView,
    HabitacionDisponibleView,
    habitacionJsonView,
    clienteJsonView,
    ClienteDeleteView,
    ClienteDetailView,
    HabitacionUpdateView,
    )
app_name = 'hotel'

urlpatterns = [
    
    path('<int:myID>/', HabitacionDetailView.as_view(), name = 'habi-detail'),
    path('cliente/', ClienteListView.as_view(), name = 'cliente-list'),
    path('cliente/<int:myID>/', ClienteDetailView.as_view(), name = 'cliente-detail'),
    path('addHabitacion/', HabitacionCreateView.as_view(), name = 'habi-add'),

    # Son vistas que incluiremos en nuestra barra de navegacion.
    path('', HabitacionListView.as_view(), name = 'habitacion-list'),
    path('addCliente/', ClienteCreateView.as_view(), name = 'clie-adding'),
    path('searchCliente/', ClienteSearchView.as_view(), name = 'clie-search'),
    path('habDisponible/', HabitacionDisponibleView.as_view(), name = 'habi-dispo'),
    path('cliente/<int:myID>/delete', ClienteDeleteView.as_view(), name = 'clie-delete'),
    path('update/<int:myID>/', HabitacionUpdateView.as_view(), name = 'clie-update'),
    
    #Urls de json
    path('habiJSON/', habitacionJsonView.as_view(), name = 'habi-JSON'),
    path('searchCliente/cliJSON/', clienteJsonView.as_view(), name = 'cli-JSON'),
]

