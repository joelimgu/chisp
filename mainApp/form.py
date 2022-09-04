from django import forms


class CustomNumberInput(forms.NumberInput):
    template_name = "mainApp/widgets/formWidgets/numberInput.html"


class TomSelect(forms.Select):
    template_name = "mainApp/widgets/formWidgets/tom-select.html"

    def __init__(self, create=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create = create

    def build_attrs(self, base_attrs, extra_attrs=None):
        attrs = super(TomSelect, self).build_attrs(base_attrs, extra_attrs)
        if "class" in attrs:
            attrs["class"] += " django-tom-select form-control"
        else:
            attrs["class"] = "django-tom-select form-control"
        return attrs

    def get_context(self, name, value, attrs):
        context = super(TomSelect, self).get_context(name, value, attrs)
        context["create"] = self.create
        return context

    class Media:
        js = ("mainApp/js/tom-select.complete.min.js", "mainApp/js/tom-select-django.js")
        css = {
            "all": ("mainApp/css/tom-select.bootstrap5.min.css",)
        }


class TomSelectMultiple(TomSelect):
    allow_multiple_selected = True


class TomSelectCreate(TomSelect):
    template_name = "mainApp/widgets/formWidgets/tom-select-create.html"

    def __init__(self, attrs=None, choices=(), form_url=None, data_url=None, data_kwargs=None, form_selector="form",
                 kwargs=None):
        super().__init__(attrs, choices)
        if kwargs is None:
            kwargs = {}
        self.kwargs = kwargs
        self.form_url = form_url
        self.data_kwargs = data_kwargs
        self.data_url = data_url
        self.form_selector = form_selector

    def get_context(self, name, value, attrs):
        context = super(TomSelectCreate, self).get_context(name, value, attrs)
        context["kwargs"] = self.kwargs
        context["form_url"] = self.form_url
        context["data_url"] = self.data_url
        context["data_kwargs"] = self.data_kwargs
        context["form_selector"] = self.form_selector
        return context

    class Media:
        js = ("mainApp/js/tom-select.complete.min.js", "mainApp/js/tom-select-django.js", "forms/modal-form.js")
        css = {
            "all": ("mainApp/css/tom-select.bootstrap5.min.css",)
        }


class TomSelectCreateMultiple(TomSelectCreate):
    allow_multiple_selected = True