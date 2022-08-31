from django.db.models import Q
from django.forms import ModelForm
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from mainApp.form import CustomNumberInput
from mainApp.models import ElectricalComponent


def index(request):
    return render(request, 'mainApp/index.html')


class ViewComponent(DetailView):
    model = ElectricalComponent


class UpdateComponent(UpdateView):
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


class SearchComponent(ListView):
    template_name = "mainApp/electricalcomponent_list.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query is None:
            return []
        object_list = ElectricalComponent.objects.filter(
            Q(reference__icontains=query) | Q(manufacturer_description__icontains=query)
        )
        return object_list

    # def get(self, request, search_term):
    #     # search = self.request.GET.get('search_term')
    #     print(self.kwargs['search_term'])

    paginate_by = 50
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


class ComponentListView(ListView):
    paginate_by = 50
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

class CreateComponentForm(ModelForm):
    class Meta:
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
        widgets = {
            "current_stock": CustomNumberInput()
        }


class CreateComponent(CreateView):
    model = ElectricalComponent
    form_class = CreateComponentForm

