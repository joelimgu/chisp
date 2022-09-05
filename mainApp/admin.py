from django.contrib import admin

# Register your models here.
from mainApp.models import ElectricalComponent, Currency, Tag

admin.site.register(ElectricalComponent)
admin.site.register(Currency)
admin.site.register(Tag)
