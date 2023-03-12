import traceback

from django.db.models import Q, F, Sum
from django.forms import ModelForm, ModelMultipleChoiceField
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView, TemplateView

from mainApp.form import CustomNumberInput, TomSelect, TomSelectCreate, TomSelectMultiple
from mainApp.models import ElectricalComponent, Tag


def index(request):
    return render(request, 'mainApp/index.html')


class ViewComponent(DetailView):
    model = ElectricalComponent

    def get_queryset(self):
        return super(ViewComponent, self).get_queryset()\
            .annotate(total=F("current_stock")*F("estimated_price"))


class UpdateComponent(UpdateView):
    model = ElectricalComponent
    fields = (
        'reference',
        'location',
        'custom_description',
        'manufacturer_description',
        'recommended_stock',
        'current_stock',
        'is_in_use_internally',
        'estimated_price',
        'currency',
        'tags',
        'store_link'
    )
    widgets = {
        "current_stock": CustomNumberInput(),
        "tags": TomSelectMultiple()
    }


class SearchComponent(ListView):
    template_name = "mainApp/electricalcomponent_list.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query is None:
            return []
        object_list = ElectricalComponent.objects.filter(
            Q(reference__icontains=query)
            | Q(custom_description=query)
            | Q(manufacturer_description__icontains=query)
            | Q(location__icontains=query)
            | Q(tags__name__icontains=query)
        ).distinct()
        return object_list

    paginate_by = 30  # also change in css
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
        'location',
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
            'location',
            'custom_description',
            'manufacturer_description',
            'recommended_stock',
            'current_stock',
            'is_in_use_internally',
            'estimated_price',
            'currency',
            'store_link',
            'tags'
        )
        widgets = {
            "current_stock": CustomNumberInput(),
            "tags": TomSelectMultiple()
        }


class DeleteComponent(DeleteView):
    model = ElectricalComponent
    template_name = "mainApp/electricalcomponent_delete.html"
    success_url = reverse_lazy("home")


class CreateComponent(CreateView):
    model = ElectricalComponent
    form_class = CreateComponentForm


class CreateTag(CreateView):
    model = Tag
    fields = ("name", "color")

    def get_success_url(self):
        return reverse("index")


class UpdateTag(UpdateView):
    model = Tag
    fields = ("name", "color")


class ListTag(ListView):
    template_name = 'mainApp/tag_list.html'
    paginate_by = 500
    model = Tag
    fields = ("name", "color")


class Statistics(TemplateView):
    template_name = 'mainApp/statistiques.html'

    def get_context_data(self, **kwargs):
        context = super(Statistics, self).get_context_data(**kwargs)
        context['total'] = ElectricalComponent.objects\
            .annotate(price=F('estimated_price')*F('current_stock')).aggregate(Sum('price'))
        context['nb_of_items'] = ElectricalComponent.objects.count()
        return context
