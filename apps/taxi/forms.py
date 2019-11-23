from django import forms
from .models import Viaje


class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ['pasajero','origen','destino','fecha_registro','fecha_inicio','fecha_fin','conductor','puntaje','estado']
        labels = {
            'pasajero': 'Nombres del Pasajero',
            'origen': '',
            'destino': '',
            'fecha_registro': '',
            'fecha_inicio': '',
            'fecha_fin': '',
            'conductor': '',
            'puntaje': '',
            'estado': ''
        }
        widgets = {
            'pasajero': forms.TextInput(
                attrs={
                    'class': 'form-control',                    
                    'id': 'pasajero'
                }
            ),
            'origen': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'origen'
                }
            ),
            'destino': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'destino'
                }
            ),
            'fecha_registro': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'fecha_registro'
                }
            ),
            'fecha_inicio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'fecha_inicio'
                }
            ),
            'fecha_fin': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'fecha_fin'
                }
            ),
            'conductor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'conductor'
                }
            ),
            'puntaje': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'puntaje'
                }
            ),
            'estado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'estado'
                }
            )
        }