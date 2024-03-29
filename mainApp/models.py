from colorfield.fields import ColorField
from django.db import models

# Create your models here.
from django.db.models.functions import datetime
from django.urls import reverse


class Currency(models.Model):
    def __str__(self):
        return self.symbol

    symbol = models.CharField(max_length=7)
    name = models.CharField(max_length=255, unique=True)


def get_default_currency():
    return Currency.objects.get(name="euro")


class ElectricalComponent(models.Model):
    # ORDER BY 'last_update'
    class Meta:
        ordering = ['-last_update']

    def __str__(self):
        return self.reference

    def get_absolute_url(self):
        return reverse('component.view', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('component.delete_component', kwargs={'pk': self.pk})

    def get_edit_url(self):
        return reverse('component.edit_component', kwargs={'pk': self.pk})

    reference = models.CharField(max_length=255, null=False, unique=True)
    location = models.CharField(max_length=15, null=True)
    custom_description = models.CharField(max_length=1023)
    manufacturer_description = models.CharField(max_length=1023)
    recommended_stock = models.IntegerField(blank=True, null=False, default=0)
    current_stock = models.IntegerField(default=0)
    is_in_use_internally = models.BooleanField(default=False)
    estimated_price = models.FloatField(null=True, default=None)
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE, null=True, default=get_default_currency)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField("mainApp.Tag", related_name="electrical_components")
    store_link = models.CharField(max_length=1024, null=True, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    color = ColorField(default="#FFFFFF")

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('component.list_tags')

    def get_edit_url(self):
        return reverse('component.edit_tag', kwargs={'pk': self.pk})
