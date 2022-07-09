from django.contrib import admin

# Register your models here.
from mainApp.models import ElectricalComponent, Currency

admin.site.register(ElectricalComponent)
admin.site.register(Currency)
