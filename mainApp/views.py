from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, ListView

from mainApp.models import ElectricalComponent


def index(request):
    return render(request, 'mainApp/index.html')


class ViewComponent(DetailView):
    model = ElectricalComponent


class SearchComponent(ListView):
    pass


class ComponentListView(ListView):
    paginate_by = 2
    model = ElectricalComponent

    fields = (
        'reference',
        'custom_description',
        'manufacturer_description',
        'recommended_stock',
        'current_stock',
        'is_in_use_internally',
        'estimated_price',
        'currency',
    )


class CreateComponent(CreateView):
    model = ElectricalComponent

    fields = (
        'reference',
        'custom_description',
        'manufacturer_description',
        'recommended_stock',
        'current_stock',
        'is_in_use_internally',
        'estimated_price',
        'currency',
    )
