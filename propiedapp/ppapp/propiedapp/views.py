from django.shortcuts import render, get_object_or_404
from .models import Propiedad

def detalle_propiedad(request, propiedad_id):
    propiedad = get_object_or_404(Propiedad, id=propiedad_id)
    return render(request, 'propiedapp/detalle_propiedad.html', {
        'propiedad': propiedad
    })