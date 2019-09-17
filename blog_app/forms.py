from django.forms import ModelForm
from .models import Blog

class Title(ModelForm):
    class Meta:
        model = Blog
        fields = ['title','short_content','full_content','author_id']