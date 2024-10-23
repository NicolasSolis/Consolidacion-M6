from django.urls import path
from .views import add_vehiculo, view_vehiculo, view_registro, view_login, view_logout

urlpatterns = [
    path('add/', add_vehiculo, name='añadir'),
    path('listar/', view_vehiculo, name='listar'),
    path('registro/', view_registro, name='registro'),
    path('login/', view_login, name='login'),
    path('logout/', view_logout, name='logout'),
]