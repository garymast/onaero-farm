from django.shortcuts import render, get_object_or_404
from .models import Suburb

# Create your views here.

def all_suburbs(request):
    """ A view to show all suburbs within the delivery area """

    suburbs = Suburb.objects.all()
    suburbs = suburbs.order_by("suburb")
    context = {
        'suburbs': suburbs,
    }

    return render(request, 'delivery/delivery.html', context)

