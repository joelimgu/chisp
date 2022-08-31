from django import forms


class CustomNumberInput(forms.NumberInput):
    template_name = "mainApp/widgets/formWidgets/numberInput.html"