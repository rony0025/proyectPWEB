from django.urls import path
from .views import(
    HabitacionListView,
    HabitacionDetailView,
    ClienteListView,
    HabitacionCreateView,
    ClienteCreateView
    )
app_name = 'hotel'

urlpatterns = [
    path('', HabitacionListView.as_view(), name = 'habitacion-list'),
    path('<int:myID>/', HabitacionDetailView.as_view(), name = 'habi-detail'),
    path('cliente/', ClienteListView.as_view(), name = 'cliente-list'),
    path('addHabitacion/', HabitacionCreateView.as_view(), name = 'habi-add'),
    path('addCliente/', ClienteCreateView.as_view(), name = 'clie-add'),
]
