from django import forms
from django.forms import ModelForm
from .models import Photos, Product

class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields=("title", "sale_price", "cost_per_unit", "notes")


class PhotoForm(ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Photos 
        fields = ('image',)