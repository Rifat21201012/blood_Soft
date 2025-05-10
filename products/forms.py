from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "blood_group",
            "gender",
            "phone_number",
            "age",
            "national_number",
            "present_address",
        ]


class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)


class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Search Blood Group', max_length=100)


class ProductSearchForm(forms.Form):
    search_query = forms.CharField(required=False, label='Search by Blood Group')
    location_query = forms.CharField(required=False, label='Search by Location')
