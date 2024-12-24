from django.urls import path
from . import views

app_name = 'propiedapp'

urlpatterns = [
    path('', views.lista_propiedades, name='lista_propiedades'),
    path('propiedad/<int:propiedad_id>/', views.detalle_propiedad, name='detalle_propiedad'),
]