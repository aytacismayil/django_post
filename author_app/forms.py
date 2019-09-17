from django.forms import ModelForm
from .models import Author

class Ad(ModelForm):
    class Meta:
        model = Author
        fields = ['name','surname']