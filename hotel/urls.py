from django.urls import path
from .views import(
    HabitacionListView,
    HabitacionDetailView,
    ClienteListView,
    HabitacionCreateView,
    ClienteCreateView,
    ClienteSearchView,
    HabitacionDisponibleView,
    )
app_name = 'hotel'

urlpatterns = [
    
    path('<int:myID>/', HabitacionDetailView.as_view(), name = 'habi-detail'),
    path('cliente/', ClienteListView.as_view(), name = 'cliente-list'),
    path('addHabitacion/', HabitacionCreateView.as_view(), name = 'habi-add'),

    # Son vistas que incluiremos en nuestra barra de navegacion.
    path('', HabitacionListView.as_view(), name = 'habitacion-list'),
    path('addCliente/', ClienteCreateView.as_view(), name = 'clie-adding'),
    path('searchCliente/', ClienteSearchView.as_view(), name = 'clie-search'),
    path('habDisponible/', HabitacionDisponibleView.as_view(), name = 'habi-dispo'),
]
