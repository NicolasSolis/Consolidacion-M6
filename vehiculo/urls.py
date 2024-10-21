from django.urls import path
from .views import add_vehiculo, view_vehiculo

urlpatterns = [
    path('add/', add_vehiculo, name='add_vehiculo'),
    path('listar/', view_vehiculo, name='view_vehiculo')
]