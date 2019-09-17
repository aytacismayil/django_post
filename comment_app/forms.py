from django.forms import ModelForm
from .models import Comment

class Coment(ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name','email','comment','blog_id']