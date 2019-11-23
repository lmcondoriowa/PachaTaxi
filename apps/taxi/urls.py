from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListarViajesPorPasajeros,ListarViajesPorConductor, CrearViaje

urlpatterns = [
    #viajes
    path('listar_viajepp/', login_required(ListarViajesPorPasajeros.as_view()), name='listar_viajepp'),
    path('listar_viajepc/', login_required(ListarViajesPorConductor.as_view()), name='listar_viajepc'),
    path('crear_viaje/', CrearViaje.as_view(), name='crear_viaje'),
]