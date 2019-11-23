from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Viaje, TipoUsuario, DestinoFavorito, Vehiculo
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import ViajeForm

# Create your views here.
class Home(TemplateView):
    template_name = 'taxi/local/index.html'

    def get_context_data(self, *args, **kwargs):
        viaje = Viaje.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['Viajes'] = viaje
        return context

#Pasajeros
'''@require_http_methods(["POST", "GET"])
def listar_viajepp2(request, user_id):
    viaje = Viaje.objects.get(pasajeroid=user_id)
    return render(request, 'taxi/viaje/listar_viaje.html', {
        'viajes': viaje
    })'''

class ListarViajesPorPasajeros(ListView):    
    model = Viaje
    template_name = 'taxi/viaje/listar_viaje.html'    
    context_object_name = 'viajes'

    def get_context_data(self, *args, **kwargs):
        viaje = Viaje.objects.filter(pasajero_id=self.request.user.id)
        context = super(ListarViajesPorPasajeros, self).get_context_data(*args, **kwargs)
        context['viajes'] = viaje
        return context

class ListarViajesPorConductor(ListView):    
    model = Viaje
    template_name = 'taxi/viaje/listar_viaje.html'    
    context_object_name = 'viajes'

    def get_context_data(self, *args, **kwargs):
        viaje = Viaje.objects.filter(conductor_id=self.request.user.id)
        context = super(ListarViajesPorConductor, self).get_context_data(*args, **kwargs)
        context['viajes'] = viaje
        return context

class CrearViaje(CreateView):
    model = Viaje
    form_class = ViajeForm
    template_name = 'taxi/viaje/crear_viaje.html'
    success_url = reverse_lazy('taxi:listar_viajepp')