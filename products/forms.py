from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']
        labels = {'name': 'Name of product', 'price': 'Price (format 0.00)'}