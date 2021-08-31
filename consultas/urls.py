from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('consultaticket', views.consultaticket, name='consultaticket'),
    path('consultadecredito', views.consultadecredito, name='consultadecredito'),
    path('mostrarticket', views.mostrarticket, name='mostrarticket'),
]