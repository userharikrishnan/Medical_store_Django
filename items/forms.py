from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price']

class ProductSearchForm(forms.Form):
    query = forms.CharField(label='Search',)