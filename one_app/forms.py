from django.forms import ModelForm
from .models import Products

class Mehsulelaveet(ModelForm):
    class Meta:
        model = Products
        fields = ['name','price','images','deyer','category']
