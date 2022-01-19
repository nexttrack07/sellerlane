from django import forms
from django.forms import ModelForm
from .models import Photos, Product

def get_input_attrs(classes="", other={}):
    attrs = {
        'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md'
    }
    attrs['class'] = attrs['class'] + " " + classes

    return {**attrs, **other}

def get_textarea_attrs(classes=""):
    attrs = {
        'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
        'rows': 4
    }
    attrs['class'] = attrs['class'] + " " + classes

    return attrs
    
class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields=("title", "sale_price", "cost_per_unit", "notes")
        widgets = {
            'title': forms.TextInput(attrs=get_input_attrs()),
            'sale_price': forms.TextInput(attrs=get_input_attrs(other={ 'style': 'padding-left: 24px;', 'type': 'number'})),
            'cost_per_unit': forms.TextInput(attrs=get_input_attrs(other={ 'style': 'padding-left: 24px;', 'type': 'number'})),
            'notes': forms.Textarea(attrs=get_textarea_attrs()),
        }


class PhotoForm(ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Photos 
        fields = ('image',)